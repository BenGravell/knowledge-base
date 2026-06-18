<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-Driven Robust Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The last decade witnessed an explosion in the availability of data for operations research applications. Motivated by this growing availability, we propose a novel schema for utilizing data to design uncertainty sets for robust optimization using statistical hypothesis tests. The approach is flexible and widely applicable, and robust optimization problems built from our new sets are computationally tractable, both theoretically and practically. Furthermore, optimal solutions to these problems enjoy a strong, finite-sample probabilistic guarantee. \edit{We describe concrete procedures for choosing an appropriate set for a given application and applying our approach to multiple uncertain constraints. Computational evidence in portfolio management and queuing confirm that our data-driven sets significantly outperform traditional robust optimization techniques whenever data is available.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robust optimization is a popular approach to optimization under uncertainty. The key idea is to define an uncertainty set of possible realizations of the uncertain parameters and then optimize against worst-case realizations within this set. Computational experience suggests that with well-chosen sets, robust models yield tractable optimization problems whose solutions perform as well or better than other approaches. With poorly chosen sets, however, robust models may be overly-conservative or computationally intractable. Choosing a good set is crucial. Fortunately, there are several theoretically motivated and experimentally validated proposals for constructing good uncertainty sets. These proposals share a common paradigm; they combine a priori reasoning with mild assumptions on the uncertainty to motivate the construction of the set.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, the last decade witnessed an explosion in the availability of data. Massive amounts of data are now routinely collected in many industries. Retailers archive terabytes of transaction data. Suppliers track order patterns across their supply chains. Energy markets can access global weather data, historical demand profiles, and, in some cases, real-time power consumption information. These data have motivated a shift in thinking -- away from a priori reasoning and assumptions and towards a new data-centered paradigm. A natural question, then, is how should robust optimization techniques be tailored to this new paradigm?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a general schema for designing uncertainty sets for robust optimization from data. We consider uncertain constraints of the form ${f{(\overset{\sim}{\mathbf{u}},\mathbf{x})}} \leq 0$ where $\mathbf{x} \in {\mathbb{R}}^{k}$ is the optimization variable, and $\overset{\sim}{\mathbf{u}} \in {\mathbb{R}}^{d}$ is an uncertain parameter. We model this constraint by choosing a set $\mathcal{U}$ and forming the corresponding robust constraint

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We assume throughout that $f{(\mathbf{u},\mathbf{x})}$ is concave in $\mathbf{u}$ for any $\mathbf{x}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In many applications, robust formulations decompose into a series constraints of the form through an appropriate transformation of variables, including uncertain linear optimization and multistage adaptive optimization (see, e.g., Ben-Tal et al. ). In this sense, is a fundamental building block for more complex robust optimization models.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many approaches to constructing uncertainty sets for assume $\overset{\sim}{\mathbf{u}}$ is a random variable whose distribution ${\mathbb{P}}^{\ast}$ is not known except for some assumed structural features. For example, they may assume that ${\mathbb{P}}^{\ast}$ has independent components, while its marginal distributions are not known.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The robust constraint is *computationally tractable.*

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

(P2) ‣ 1 Introduction") ensures that a feasible solution to the robust constraint will also be feasible with probability $1 - \epsilon$ with respect to ${\mathbb{P}}^{\ast}$, despite not knowing ${\mathbb{P}}^{\ast}$ exactly. Existing proposals achieve (P2) ‣ 1 Introduction") by leveraging the a priori structural features of ${\mathbb{P}}^{\ast}$. Some of these approaches, e.g. only consider the special case when $f{(\mathbf{u},\mathbf{x})}$ is bi-affine, but one can generalize them to (2 ‣ 1 Introduction")) using techniques from Ben-Tal et al. (see also Sec. 2.1).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Like previous proposals, we also assume $\overset{\sim}{\mathbf{u}}$ is a random variable whose distribution ${\mathbb{P}}^{\ast}$ is not known exactly, and seek sets $\mathcal{U}_{\epsilon}$ that satisfy these properties. Unlike previous proposals -- and this is critical -- we assume that we have data $\mathcal{S} = {\{{\hat{\mathbf{u}}}^{1},\ldots,{\hat{\mathbf{u}}}^{N}\}}$ drawn i.i.d. according to ${\mathbb{P}}^{\ast}$. By combining these data with the a priori structural features of ${\mathbb{P}}^{\ast}$, we can design new sets that imply similar probabilistic guarantees, but which are much smaller with respect to subset containment than their traditional counterparts. Consequently, robust models built from our new sets yield less conservative solutions than traditional counterparts, while retaining their robustness properties.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The key to our schema is using the confidence region of a statistical hypothesis test to quantify what we learn about ${\mathbb{P}}^{\ast}$ from the data. Specifically, our constructions depend on three ingredients: the a priori assumptions on ${\mathbb{P}}^{\ast}$, the data, and a hypothesis test. By pairing different a priori assumptions and tests, we obtain distinct data-driven uncertainty sets, each with its own geometric shape, computational properties, and modeling power. These sets can capture a variety of features of ${\mathbb{P}}^{\ast}$, including skewness, heavy-tails and correlations.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In principle, there is a multitude of possible pairings of a priori assumptions and tests. We focus on pairings we believe are most relevant to applied robust modeling. Specifically, we consider a priori assumptions that are common in practice and tests that lead to tractable uncertainty sets. Our list is non-exhaustive; there may exist other pairings that yield effective sets.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

${\mathbb{P}}^{\ast}$ has known, finite discrete support (Sec. 4).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

${\mathbb{P}}^{\ast}$ may have continuous support, and the components of $\overset{\sim}{\mathbf{u}}$ are independent (Sec. 5).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

${\mathbb{P}}^{\ast}$ may have continuous support, but data are drawn from its marginal distributions asynchronously (Sec. 6). This situation models the case of missing values.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

${\mathbb{P}}^{\ast}$ may have continuous support, and data are drawn from its joint distribution (Sec. 7). This is the general case.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Table 1 summarizes the a priori structural assumptions, hypothesis tests, and resulting uncertainty sets that we propose. Each set is convex and admits a tractable, explicit description; see the referenced equations.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

Summary of data-driven uncertainty sets proposed in this paper. Assumptions on ℙ* Hypothesis Test \pbox20cmGeometric Description Eqs. Separation Discrete support χ2-test SOC Discrete support G-test Polyhedral* Independent marginals KS Test Polyhedral* line search Independent marginals K Test Polyhedral* line search Independent marginals CvM Test SOC* Independent marginals W Test SOC* Independent marginals AD Test EC Independent marginals Chen et al. SOC closed-form None Marginal Samples Box closed-form None Linear Convex Ordering Varies linear optimization None \pbox20cm Shawe-Taylor &amp; Cristianini SOC closed-form None Delage &amp; Ye LMI SOC, EC and LMI denote second-order cone representable sets, exponential cone representable sets, and linear matrix inequalities, respectively. The additional “*” notation indicates a set of of the above type with one additional, relative entropy constraint. K S, K, C v M, W, and A D denote the Kolmogorov-Smirnov, Kuiper, Cramer-von Mises, Watson and Anderson-Darling goodness of fit tests, respectively.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

In some cases, we can separate over the constraint for bi-affine f with a specialized algorithm. In these cases, the column “Separation” roughly describes this algorithm.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

For each of our sets, we provide an explicit, equivalent reformulation of. The complexity of optimizing over this reformulation depends both on the function $f{(\mathbf{u},\mathbf{x})}$ and the set $\mathcal{U}$. For each of our sets, we show that this reformulation is polynomial time tractable for a large class of functions $f$ including bi-affine functions, separable functions, conic-quadratic representable functions and certain sums of uncertain exponential functions. By exploiting special structure in some of our sets, we can provide specialized routines for directly separating over for bi-affine $f$. In these cases, the column "Separation" in Table 1 roughly describes these routines. Utilizing this separation routine within a cutting-plane method may offer performance superior to reformulation based-approaches (Bertsimas et al., Mutapcic and Boyd ).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

We are not the first to consider using hypothesis tests in data-driven optimization. Recently, Ben-Tal et al. proposed a class of data-driven uncertainty sets based on phi-divergences. (Phi divergences are closely related to some types of hypothesis tests.) They focus on the case where the uncertain parameter is a probability distribution with known, finite, discrete support. By contrast, we design uncertainty sets for general uncertain parameters with potentially continuous support such as future product demand, service times, and asset returns. Many existing robust optimization applications utilize similar general uncertain parameters. Consequently, retrofitting these applications with our new data-driven sets to yield data-driven variants is perhaps more straightforward than using sets for uncertain probabilities. From a methodological perspective, treating general uncertain parameters requires combining ideas from a variety of hypothesis tests (not just those based on phi-divergences of discrete distributions) with techniques from convex analysis and risk theory. (See Sec. 3.)

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

Other authors have also considered more specialized applications of hypothesis testing in data-driven optimization. Klabjan et al. proposes a distributionally robust dynamic program based on Pearson's $\chi^{2}$-test for a particular inventory problem. Goldfarb and Iyengar calibrate an uncertainty set for the mean and covariance of a distribution using linear regression and the $t$-test. It is not clear how to generalize these methods to other settings, e.g., distributions with continuous support in the first case or general parameter uncertainty in the second. By contrast, we offer a comprehensive study of the connection between hypothesis testing and uncertainty set design, addressing a number of cases with general machinery.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, our hypothesis testing perspective provides a unified view of many other data-driven methods from the literature. For example, Calafiore and El Ghaoui and Delage and Ye have proposed data-driven methods for chance-constrained and distributionally robust problems, respectively without using hypothesis testing. We show how these works can be reinterpreted through the lens of hypothesis testing. Leveraging this viewpoint enables us to apply state-of-the-art methods from statistics, such as the bootstrap, to refine these methods and improve their numerical performance. Moreover, applying our schema, we can design data-driven uncertainty sets for robust optimization based upon these methods. Although we focus on Calafiore and El Ghaoui and Delage and Ye in this paper, this strategy applies equally well to a host of other methods, such as the likelihood estimation approach of Wang et al.. In this sense, we believe hypothesis testing and uncertainty set design provide a common framework in which to compare and contrast different approaches.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we note that Campi and Garatti propose a very different data-driven method for robust optimization not based on hypothesis tests. In their approach, one replaces the uncertain constraint ${f{(\overset{\sim}{\mathbf{u}},\mathbf{x})}} \leq 0$ with $N$ sampled constraints over the data, ${f{({\hat{\mathbf{u}}}^{j},\mathbf{x})}} \leq 0$, for $j = {1,\ldots,N}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Introduction", "weight": 1.5} -->

For $f{(\mathbf{u},\mathbf{x})}$ convex in $\mathbf{x}$ with arbitrary dependence in $\mathbf{u}$, they provide a tight bound $N{(\epsilon)}$ such that if $N \geq {N{(\epsilon)}}$, then, with high probability with respect to the sampling, any $\mathbf{x}$ which is feasible in the $N$ sampled constraints satisfies ${{\mathbb{P}}^{\ast}{({{f{(\overset{\sim}{\mathbf{u}},\mathbf{x})}} \leq 0})}} \geq {1 - \epsilon}$. Various refinements of this base method have also been proposed yielding smaller bounds $N{(\epsilon)}$, including incorporating $\ell_{1}$-regularization and allowing $\mathbf{x}$ to violate a small fraction of the constraints.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Introduction", "weight": 1.5} -->

Compared to our approach, these methods are more generally applicable and provide a similar probabilistic guarantee. In the special case we treat where $f{(\overset{\sim}{\mathbf{u}},\mathbf{x})}$ is concave in $\mathbf{u}$, however, our proposed approach offers some advantages. First, because it leverages the concave structure of $f{(\mathbf{u},\mathbf{x})}$, our approach generally yields less conservative solutions (for the same $N$ and $\epsilon$) than Campi and Garatti. (See Sec. 3.) Second, for fixed $\epsilon > 0$, our approach is applicable even if $N < {N{(\epsilon)}}$, while theirs is not. This distinction is important when $\epsilon$ is very small and there may not exist enough data.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, as we will show, our approach reformulates as a series of (relatively) sparse convex constraints, while the Campi and Garatti approach will in general yield $N$ dense constraints which may be numerically challenging when $N$ is large. For these reasons, practitioners may prefer our proposed approach in certain applications.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a new, systematic schema for constructing uncertainty sets from data using statistical hypothesis tests. When the data are drawn i.i.d. from an unknown distribution ${\mathbb{P}}^{\ast}$, sets built from our schema imply a probabilistic guarantee for ${\mathbb{P}}^{\ast}$ at any desired level $\epsilon$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Introduction", "weight": 1.5} -->

We illustrate our schema by constructing a multitude of uncertainty sets. Each set is applicable under slightly different a priori assumptions on ${\mathbb{P}}^{\ast}$ as described in Table 1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Introduction", "weight": 1.5} -->

We prove that robust optimization problems over each of our sets are generally tractable. Specifically, for each set, we derive an explicit robust counterpart to and show that for a large class of functions $f{(\mathbf{u},\mathbf{x})}$ optimizing over this counterpart can be accomplished in polynomial time using off-the-shelf software.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Introduction", "weight": 1.5} -->

We unify several existing data-driven methods through the lens of hypothesis testing. Through this lens, we motivate the use of common numerical techniques from statistics such as bootstrapping and gaussian approximation to improve their performance. Moreover, we apply our schema to derive new uncertainty sets for inspired by the refined versions of these methods.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a new approach to modeling multiple uncertain constraints simultaneously with our sets by optimizing the parameters chosen for each individual constraint. We prove that this technique is tractable and yields solutions which will satisfy all the uncertain constraints simultaneously for any desired level $\epsilon$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide guidelines for practitioners on choosing an appropriate set and calibrating its parameters by leveraging techniques from model selection in machine learning.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Introduction", "weight": 1.5} -->

Through applications in queueing and portfolio allocation, we assess the relative strengths and weaknesses of our sets. Overall, we find that although all of our sets shrink in size as $N\rightarrow\infty$, they differ in their ability to represent features of ${\mathbb{P}}^{\ast}$. Consequently, they may perform very differently in a given application. In the above two settings, we find that our model selection technique frequently identifies a good set choice, and a robust optimization model built with this set performs as well or better than other robust data-driven approaches.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is structured as follows. Sec. 2 reviews background to keep the paper self-contained. Sec. 3 presents our schema for constructing uncertainty sets. Sec. 4-7 describe the various constructions in Table 1. Sec. 8 reinterprets several techniques in the literature through the lens of hypothesis testing and, subsequently, uses them to motivate new uncertainty sets. Sec. 9 and Sec. 10 discuss modeling multiple constraints and choosing the right set for an application, respectively. Sec. 11 presents numerical experiments, and Sec. 12 concludes. All proofs are in the electronic companion.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Tractability of Robust Nonlinear Constraints", "weight": 1.0} -->

Here, $f_{\ast}{(\mathbf{v},\mathbf{x})}$ denotes the partial concave-conjugate of $f{(\mathbf{u},\mathbf{x})}$ and $\delta^{\ast}{(\left. \mathbf{v} \middle| \mathcal{U} \right.)}$ denotes the support function of $\mathcal{U}$, defined respectively as

<!-- chunk {"id": "body-0038", "role": "body", "section": "Tractability of Robust Nonlinear Constraints", "weight": 1.0} -->

In what follows, we concentrate on proving we can separate over $\{{(\mathbf{v},t)}:{{\delta^{\ast}{(\left. \mathbf{v} \middle| \mathcal{U} \right.)}} \leq t}\}$ in polynomial time for each of our sets $\mathcal{U}$, usually by representing this set as a small number of convex inequalities suitable for off-the-shelf solvers. From, this representation will imply that is tractable for each of our sets whenever $f{(\mathbf{u},\mathbf{x})}$ is bi-affine.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Tractability of Robust Nonlinear Constraints", "weight": 1.0} -->

Consequently, by providing a representation of $\{{(\mathbf{v},t)}:{{\delta^{\ast}{(\left. \mathbf{v} \middle| \mathcal{U} \right.)}} \leq t}\}$ for each of our sets, we will also have proven that is tractable for each of these functions via. In other words, proving $\{{(\mathbf{v},t)}:{{\delta^{\ast}{(\left. \mathbf{v} \middle| \mathcal{U} \right.)}} \leq t}\}$ is tractable implies that is tractable not only for bi-affine functions, but for many other concave functions as well.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Tractability of Robust Nonlinear Constraints", "weight": 1.0} -->

For some sets, our formulation of $\{{(\mathbf{v},t)}:{{\delta^{\ast}{(\left. \mathbf{v} \middle| \mathcal{U} \right.)}} \leq t}\}$ will involve complex nonlinear constraints, such as exponential cone constraints (cf. Table 1). Although it is possible to optimize over these constraints directly, this approach may be numerically challenging. As mentioned, an alternative is to use cutting-plane or bundle methods as in Bertsimas et al., Mutapcic and Boyd. To this end, when appropriate, we provide specialized algorithms for separating over $\{{(\mathbf{v},t)}:{{\delta^{\ast}{(\left. \mathbf{v} \middle| \mathcal{U} \right.)}} \leq t}\}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Hypothesis Testing", "weight": 1.0} -->

We briefly review hypothesis testing as it relates to our set constructions. See Lehmann and Romano for a more complete treatment.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Hypothesis Testing", "weight": 1.0} -->

Given a null-hypothesis $H_{0}$ that makes a claim about an unknown distribution ${\mathbb{P}}^{\ast}$, a hypothesis test seeks to use data $\mathcal{S}$ drawn from ${\mathbb{P}}^{\ast}$ to either declare that $H_{0}$ is false, or, else, that there is insufficient evidence to determine its validity. For a given significance level $0 < \alpha < 1$, a typical test prescribes a statistic $T \equiv {T{(\mathcal{S},H_{0})}}$, depending on the data and $H_{0}$, and a threshold $\Gamma \equiv {\Gamma{(\alpha,\mathcal{S},H_{0})}}$, depending on $\alpha$, $\mathcal{S}$, and $H_{0}$. If $T > \Gamma$, we reject $H_{0}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Hypothesis Testing", "weight": 1.0} -->

Since $T$ depends on $\mathcal{S}$, it is random. The threshold $\Gamma$ is chosen so that the probability with respect to the sampling of *incorrectly* rejecting $H_{0}$ is at most $\alpha$. The appropriate $\alpha$ is often application specific, although values of $\alpha = {{1\%},{5\%}}$ and $10\%$ are common.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Hypothesis Testing", "weight": 1.0} -->

Here $\hat{\mu},\hat{\sigma}$ are the sample mean and sample standard deviation, respectively, and $t_{{N - 1},{1 - \alpha}}$ is the $1 - \alpha$ quantile of the Student $t$-distribution with $N - 1$ degrees of freedom. Under the a priori assumption that ${\mathbb{P}}^{\ast}$ is Gaussian, the test guarantees that we will incorrectly reject $H_{0}$ with probability at most $\alpha$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Hypothesis Testing", "weight": 1.0} -->

Many of the tests we consider are common in applied statistics, and tables for their thresholds are widely available. Several of our tests, however, are novel (e.g., the deviations test in Sec. 5.2.) In these cases, we propose using the *bootstrap* to approximate a threshold (cf. Algorithm 1). $N_{B}$ should be chosen to be fairly large; we take $N_{B} = 10^{4}$ in our experiments. The bootstrap is a well-studied and widely-used technique in statistics. Strictly speaking, hypothesis tests based on the bootstrap are only asymptotically valid for large $N$. (See the references for a precise statement.) Nonetheless, they are routinely used in applied statistics, even with $N$ as small as $100$, and a wealth of practical experience suggests they are extremely accurate. Consequently, we believe practitioners can safely use bootstrapped thresholds in the above tests.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Hypothesis Testing", "weight": 1.0} -->

𝒮j← Resample |𝒮| data points from 𝒮 with replacement
return ⌈NB (1−α)⌉-largest value of T1, …, TNB.
Algorithm 1 Bootstrapping a Threshold

<!-- chunk {"id": "body-0047", "role": "body", "section": "Hypothesis Testing", "weight": 1.0} -->

Finally, we introduce the confidence region of a test, which will play a critical role in our construction. Given data $\mathcal{S}$, the $1 - \alpha$ confidence region of a test is the set of null-hypotheses that would not be rejected for $\mathcal{S}$ at level $1 - \alpha$. For example, the $1 - \alpha$ confidence region of the $t$-test is $\left\{ {\mu \in {\mathbb{R}}}:{\left| \frac{\hat{\mu} - \mu}{\hat{\sigma}\sqrt{N}} \right| \leq t_{{N - 1},{1 - {\alpha/2}}}} \right\}.$ In what follows, however, we commit a slight abuse of nomenclature and instead use the term confidence region to refer to the set of all measures that are consistent with any a priori assumptions of the test and also satisfy a null-hypothesis that would not be rejected.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Hypothesis Testing", "weight": 1.0} -->

In the case of the $t$-test, the confidence region in the context of this paper is

<!-- chunk {"id": "body-0049", "role": "body", "section": "Hypothesis Testing", "weight": 1.0} -->

where $\Theta{({- \infty},\infty)}$ is the set of Borel probability measures on $\mathbb{R}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Hypothesis Testing", "weight": 1.0} -->

By construction, the probability (with respect to the sampling procedure) that ${\mathbb{P}}^{\ast}$ is a member of its confidence region is at least $1 - \alpha$ as long as all a priori assumptions are valid. This is a critical observation. Despite not knowing ${\mathbb{P}}^{\ast}$, we can use a hypothesis test to create a set of distributions from the data that contains ${\mathbb{P}}^{\ast}$ for any specified probability.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Geometric Characterization of the Probabilistic Guarantee", "weight": 1.0} -->

As a first step towards our schema, we provide a geometric characterization of (P2) ‣ 1 Introduction"). One might intuit that a set $\mathcal{U}$ implies a probabilistic guarantee at level $\epsilon$ only if ${{\mathbb{P}}^{\ast}{({\overset{\sim}{\mathbf{u}} \in \mathcal{U}})}} \geq {1 - \epsilon}$. As noted by other authors ), however, this intuition is false. Often, sets that are much smaller than the $1 - \epsilon$ support will still imply a probabilistic guarantee at level $\epsilon$, and such sets should be preferred because they are less conservative.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Geometric Characterization of the Probabilistic Guarantee", "weight": 1.0} -->

We note in passing that many existing data-driven approaches for robust optimization, e.g., Campi and Garatti, do not leverage this dependence. Consequently, although these approaches are general purpose, they may yield overly conservative uncertainty sets.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Geometric Characterization of the Probabilistic Guarantee", "weight": 1.0} -->

In order to tightly characterize (P2) ‣ 1 Introduction"), we introduce the Value at Risk. For any $\mathbf{v} \in {\mathbb{R}}^{d}$ and measure $\mathbb{P}$, the Value at Risk at level $\epsilon$ with respect to $\mathbf{v}$ is

<!-- chunk {"id": "body-0054", "role": "body", "section": "Geometric Characterization of the Probabilistic Guarantee", "weight": 1.0} -->

Value at Risk is positively homogenous (in $\mathbf{v}$), but typically non-convex. (Recall a function $g{(\mathbf{v})}$ is positively homogenous if ${g{({\lambda\mathbf{v}})}} = {\lambdag{(\mathbf{v})}}$ for all $\lambda > 0$.) The critical result underlying our method is, then,

<!-- chunk {"id": "body-0055", "role": "body", "section": "Our Schema", "weight": 1.0} -->

The principal challenge in applying Theorem 3.1 to designing uncertainty sets is that ${\mathbb{P}}^{\ast}$ is not known. Recall, however, that the confidence region $\mathcal{P}$ of a hypothesis test, will contain ${\mathbb{P}}^{\ast}$ with probability at least $1 - \alpha$. This motivates the following schema: Fix $0 < \alpha < 1$ and $0 < \epsilon < 1$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Our Schema", "weight": 1.0} -->

Let $\mathcal{P}{(\mathcal{S},\alpha,\epsilon)}$ be the confidence region of a hypothesis test at level $\alpha$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Our Schema", "weight": 1.0} -->

Identify the closed, convex set $\mathcal{U}{(\mathcal{S},\epsilon,\alpha)}$ such that ${g{(\mathbf{v},\mathcal{S},\epsilon,\alpha)}} = {\delta^{\ast}{(\left. \mathbf{v} \middle| {\mathcal{U}{(\mathcal{S},\epsilon,\alpha)}} \right.)}}$.^22^endnote: ^2^The existence of such a set in Step 3 by the bijection between closed, positively homogenous convex functions and closed convex sets in convex analysis (see Bertsekas et al. ).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

We note in passing that ${\delta^{\ast}{(\left. \mathbf{v} \middle| {\mathcal{U}{(\mathcal{S},\epsilon,\alpha)}} \right.)}} \leq t$ is a safe-approximation to the ambiguous chance constraint ${\sup_{{\mathbb{P}} \in {\mathcal{P}{(\mathcal{S},\alpha,\epsilon)}}}{{\mathbb{P}}{({{\mathbf{v}^{T}\overset{\sim}{\mathbf{u}}} \leq t})}}} \geq {1 - \epsilon}$ as defined in Ben-Tal et al.. Ambiguous chance-constraints are closely related to sets which imply a probabilistic guarantee. We refer the reader to Ben-Tal et al. for more details.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

Theorem 3.2 ensures that with probability at least $1 - \alpha$ with respect to the sampling, a robust feasible solution $\mathbf{x}$ will satisfy a *single* uncertain constraint ${f{(\overset{\sim}{\mathbf{u}},\mathbf{x})}} \leq 0$ with probability at least $1 - \epsilon$. Often, however, we face $m > 1$ uncertain constraints ${f_{j}{(\overset{\sim}{\mathbf{u}},\mathbf{x})}} \leq 0$, $j = {1,\ldots,m}$, and seek $\mathbf{x}$ that will simultaneously satisfy these constraints, i.e.,

<!-- chunk {"id": "body-0060", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

for some given $\overline{\epsilon}$. In this case, one approach is to replace each uncertain constraint with a corresponding robust constraint

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

where $\mathcal{U}{(\mathcal{S},\epsilon_{j},\alpha)}$ is constructed via our schema at level $\epsilon_{j} = {\epsilon/m}$. By the union bound and Theorem 3.2, with probability at least $1 - \alpha$ with respect to the sampling, any $\mathbf{x}$ which satisfies will satisfy.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

The choice $\epsilon_{j} = {\epsilon/m}$ is somewhat arbitrary. We would prefer to treat the $\epsilon_{j}$ as decision variables and optimize over them, i.e., replace the $m$ uncertain constraints by

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

Unfortunately, we cannot use Theorem 3.2 to claim that with probability at least $1 - \alpha$ with respect to the sampling, any feasible to solution to will satisfy. Indeed, in general, this implication will hold with probability much less than $1 - \alpha$. The issue is that Theorem 3.2 requires selecting $\epsilon$ independently of $\mathcal{S}$, whereas the optimal $\epsilon_{j}$'s in *will* depend on $\mathcal{S}$, creating an in-sample bias. Consequently, we next extend Theorem 3.2 to lift this requirement.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

Given a family of sets indexed by $\epsilon$, $\{{\mathcal{U}{(\epsilon)}}:{0 < \epsilon < 1}\}$, we say this family *simultaneously* implies a probabilistic guarantee for ${\mathbb{P}}^{\ast}$ if, for all $0 < \epsilon < 1$, each $\mathcal{U}{(\epsilon)}$ implies a probabilistic guarantee for ${\mathbb{P}}^{\ast}$ at level $\epsilon$. Then,

<!-- chunk {"id": "body-0065", "role": "body", "section": "Uncertainty Sets Built from Discrete Distributions", "weight": 1.0} -->

The confidence regions for Pearson's $\chi^{2}$ test and the $G$ test are, respectively,

<!-- chunk {"id": "body-0066", "role": "body", "section": "Uncertainty Sets Built from Discrete Distributions", "weight": 1.0} -->

Conditional Value at Risk is well-known to be a convex upper bound to Value at Risk for a fixed $\mathbb{P}$. We can compute a bound in Step 2 by considering the worst-case Conditional Value at Risk over the above confidence regions, yielding

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 4.3", "weight": 1.0} -->

Theorem 4.1 exemplifies the distinction drawn in the introduction between uncertainty sets for discrete probability distributions -- such as $\mathcal{P}^{\chi^{2}}$ or $\mathcal{P}^{G}$ which have been proposed in Ben-Tal et al. -- and uncertainty sets for general uncertain parameters like $\mathcal{U}_{\epsilon}^{\chi^{2}}$ and $\mathcal{U}_{\epsilon}^{G}$. The relationship between these two types of sets is explicit in eqs. and because we have known, finite support. For continuous support and our other sets, the relationship is implicit and must be understood through worst-case value-at-risk in Step 2 of our schema.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 4.4", "weight": 1.0} -->

When considering $\{{(\mathbf{v},t)}:{{\delta^{\ast}{(\left. \mathbf{v} \middle| \mathcal{U}_{\epsilon}^{\chi^{2}} \right.)}} \leq t}\}$ or $\{{(\mathbf{v},t)}:{{\delta^{\ast}{(\left. \mathbf{v} \middle| \mathcal{U}_{\epsilon}^{G} \right.)}} \leq t}\}$, we may drop the minimum in the formulation or. Thus, these sets are second-order-cone representable and exponential-cone representable, respectively. Although theoretically tractable, the exponential cone can be numerically challenging.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 4.4", "weight": 1.0} -->

Because of these numerical issues, modeling with $\mathcal{U}_{\epsilon}^{\chi^{2}}$ is perhaps preferable to modeling with $\mathcal{U}_{\epsilon}^{G}$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Remark 4.6", "weight": 1.0} -->

Fig. 1 also enables us to contrast our approach to that of Campi and Garatti. Namely, suppose that $f{(\mathbf{u},\mathbf{x})}$ is linear in $\mathbf{u}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 4.6", "weight": 1.0} -->

As $N\rightarrow\infty$, $\mathcal{A}\rightarrow{\text{supp}{({\mathbb{P}}^{\ast})}}$ almost surely. In other words, as $N\rightarrow\infty$, the method of Campi and Garatti in this case is equivalent to using the entire support as an uncertainty set, which is much larger than $\mathcal{U}^{\text{CVaR}_{\epsilon}^{{\mathbb{P}}^{\ast}}}$ above. Similar examples can be constructed with continuous distributions or the method of Calafiore and Monastero. In each case, the critical observation is that these methods do not explicitly leverage the concave (or, in this case, linear) structure of $f{(\mathbf{u},\mathbf{x})}$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Independent Marginal Distributions", "weight": 1.0} -->

We next consider the case where ${\mathbb{P}}^{\ast}$ may have continuous support, but the marginal distributions ${\mathbb{P}}_{i}^{\ast}$ are known to be independent. Our strategy is to build up a multivariate test by combining univariate tests for each marginal distribution.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Uncertainty Sets Built from the Kolmogorov-Smirnov Test", "weight": 1.0} -->

Given a univariate measure ${\mathbb{P}}_{0,i}$, the Kolmogorov-Smirnov (KS) goodness-of fit test applied to marginal $i$ considers the null-hypothesis $H_{0}:{{\mathbb{P}}_{i}^{\ast} = {\mathbb{P}}_{0,i}}$. It rejects this hypothesis if

<!-- chunk {"id": "body-0074", "role": "body", "section": "Uncertainty Sets Built from the Kolmogorov-Smirnov Test", "weight": 1.0} -->

The confidence region of the above test for the $i$-th marginal distribution is

<!-- chunk {"id": "body-0075", "role": "body", "section": "Uncertainty Sets Built from the Kolmogorov-Smirnov Test", "weight": 1.0} -->

("I" in $\mathcal{P}^{I}$ is to emphasize independence). We use this confidence region in Step 1 of our schema.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Uncertainty Sets Built from the Kolmogorov-Smirnov Test", "weight": 1.0} -->

When the marginals are independent, Nemirovski and Shapiro proved

<!-- chunk {"id": "body-0077", "role": "body", "section": "Uncertainty Sets Built from the Kolmogorov-Smirnov Test", "weight": 1.0} -->

We use the worst-case value of this bound over $\mathcal{P}^{I}$ in Step 2 of our schema. By passing the supremum through the infimum and logarithm, we obtain

<!-- chunk {"id": "body-0078", "role": "body", "section": "Uncertainty Sets Built from the Kolmogorov-Smirnov Test", "weight": 1.0} -->

Despite the infinite dimensionality, we can solve in the inner-most supremum explicitly by leveraging the simple geometry of $\mathcal{P}_{i}^{KS}$. Intuitively, the worst-case distribution will either be the lefthand boundary or the righthand boundary of the region in Fig. 1 depending on the sign of $v_{i}$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Uncertainty Sets Built from the Kolmogorov-Smirnov Test", "weight": 1.0} -->

Both ${{\mathbf{q}^{L}{(\Gamma)}},{\mathbf{q}^{R}{(\Gamma)}}} \in \Delta_{N + 2}$ so that each vector can be interpreted as a discrete probability distribution on the points ${\hat{u}}_{i}^{},\ldots,{\hat{u}}_{i}^{({N + 1})}$. One can check that the distributions corresponding to these vectors are precisely the lefthand side and righthand side of the grey region in Fig. 1. Then, we have

<!-- chunk {"id": "body-0080", "role": "body", "section": "Remark 5.2", "weight": 1.0} -->

Because $\mathbf{q}^{L}{(\Gamma)}$ (resp. $\mathbf{q}^{R}{(\Gamma)}$) is decreasing (resp. increasing) in its components, the lefthand branch of the innermost maximum in will be attained when $v_{i} \leq 0$ and the righthand branch is attained otherwise. Thus, for fixed $\mathbf{v}$, the optimization problem in $\lambda$ is convex and differentiable and can be efficiently solved with a line search.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Remark 5.3", "weight": 1.0} -->

When representing ${\{{(\mathbf{v},t)}:\delta^{\ast}{(\mathbf{v}|\mathcal{U}^{I})} \leq t)}\}$, we can drop the infimum. Thus, this set is exponential cone representable, which, again, may be numerically challenging. Using the above line search, however, we can separate over this set: Given ${\mathbf{v} \in {\mathbb{R}}^{d}},{t \in {\mathbb{R}}}$ such that ${\delta^{\ast}{(\left. \mathbf{v} \middle| \mathcal{U}^{I} \right.)}} > t$, solve by line search, and let $\lambda^{\ast}$ be an optimal solution. Define

<!-- chunk {"id": "body-0082", "role": "body", "section": "Remark 5.4", "weight": 1.0} -->

The KS test is one of many goodness-of-fit tests based on the empirical distribution function (EDF), including the Kuiper (K), Cramer von-Mises (CvM), Watson (W) and Andersen-Darling (AD) tests. We can define analogues of $\mathcal{U}_{\epsilon}^{I}$ for each of these tests, each having slightly different shape. Separating over $\{{(\mathbf{v},t)}:{{\delta^{\ast}{(\left. \mathbf{v} \middle| \mathcal{U} \right.)}} \leq t}\}$ is polynomial time tractable for each these sets, but we no longer have a simple algorithm for generating violated cuts. Thus, these sets are considerably less attractive from a computational point of view. Fortunately, through simulation studies with a variety of different distributions, we have found that the version of $\mathcal{U}_{\epsilon}^{I}$ based on the KS test generally performs as well as or better than the other EDF tests.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Remark 5.4", "weight": 1.0} -->

Consequently, we recommend using the sets $\mathcal{U}_{\epsilon}^{I}$ as described. For completeness, we present the constructions for the analogous tests in Appendix 18.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Uncertainty Sets Motivated by Forward and Backward Deviations", "weight": 1.0} -->

In Chen et al., the authors propose an uncertainty set based on the forward and backward deviations of a distribution. They focus on a non-data-driven setting, where the mean and support of ${\mathbb{P}}^{\ast}$ are known a priori, and show how to upper bound these deviations to calibrate their set. In a setting where one has data *and a priori knows the mean of* ${\mathbb{P}}^{\ast}$ *precisely*, they propose a method based on sample average approximation to estimate these deviations. Unfortunately, the precise statistical behavior of these estimators is not known, so it is not clear that this set calibrated from data implies a probabilistic guarantee with high probability with respect to the sampling.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Uncertainty Sets Motivated by Forward and Backward Deviations", "weight": 1.0} -->

In this section, we use our schema to generalize the set of Chen et al. to a data-driven setting where *neither the mean of the distribution nor its support are known.* Our set differs in shape and size from their proposal, and, our construction, unlike their original proposal, will simultaneously imply a probabilistic guarantee for ${\mathbb{P}}^{\ast}$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Uncertainty Sets Motivated by Forward and Backward Deviations", "weight": 1.0} -->

We begin by specifying an appropriate multivariate hypothesis test based on combining univariate tests. Specifically, for a known (univariate) distribution ${\mathbb{P}}_{i}$ define its forward and backward deviations by

<!-- chunk {"id": "body-0087", "role": "body", "section": "Uncertainty Sets Motivated by Forward and Backward Deviations", "weight": 1.0} -->

We can test these hypotheses (separately) using $|{{\hat{\mu}}_{i} - \mu_{0,i}}|$, $\sigma_{fi}{({\hat{\mathbb{P}}}_{i})}$ and $\sigma_{bi}{({\hat{\mathbb{P}}}_{i})}$, respectively, as test statistics. Since these are not common hypothesis tests in applied statistics, there are no tables for their thresholds. Instead, we compute approximate thresholds $t_{i}$, ${\overline{\sigma}}_{fi}$ and ${\overline{\sigma}}_{bi}$ at the $\alpha/2$, $\alpha/4$ and $\alpha/4$ significance level, respectively, using the bootstrap procedure in Algorithm 1.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Uncertainty Sets Motivated by Forward and Backward Deviations", "weight": 1.0} -->

By the union bound, the univariate test which rejects if any of these thresholds is exceeded is a valid test at level $\alpha$ for the three hypotheses above to hold simultaneously. The confidence region of this test is

<!-- chunk {"id": "body-0089", "role": "body", "section": "Uncertainty Sets Motivated by Forward and Backward Deviations", "weight": 1.0} -->

Next, consider the multivariate null-hypothesis that all three null-hypotheses in hold simultaneously for all $i = {1,\ldots,d}$. As in Sec. 5, the test which rejects if the above univariate test rejects at level $\alpha^{\prime} = {1 - \sqrt[d]{1 - \alpha}}$ for any $i$ is a valid test. Its confidence region is ${\mathcal{P}^{FB} = {\{{\mathbb{P}}:{{{\mathbb{P}}_{i} \in {\mathcal{P}_{i}^{FB}i} = 1},{\ldots,d}}\}}}.$ We will use this confidence region in Step 1 of our schema.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Uncertainty Sets Motivated by Forward and Backward Deviations", "weight": 1.0} -->

When the mean and deviations for $\mathbb{P}$ are known and the marginals are independent, Chen et al. prove

<!-- chunk {"id": "body-0091", "role": "body", "section": "Remark 5.6", "weight": 1.0} -->

Then, ${\mathbf{u}^{T}\mathbf{v}} \leq t$ is a violated constraint. The correctness of this procedure follows from the proof of Theorem 5.5.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Remark 5.7", "weight": 1.0} -->

so that with $\mathcal{U}_{\epsilon}^{FB} \cap \mathcal{U}_{0}$ will be tractable whenever $\{{(\mathbf{v},t)}:{{\delta^{\ast}{(\left. \mathbf{v} \middle| \mathcal{U}_{0} \right.)}} \leq t}\}$ is tractable, examples of which include when $\mathcal{U}_{0}$ is a norm-ball, ellipse, or polyhedron (see Ben-Tal et al. ).

<!-- chunk {"id": "body-0093", "role": "body", "section": "Comparing $\\mathcal{U}_{\\epsilon}^{I}$ and $\\mathcal{U}_{\\epsilon}^{FB}$", "weight": 1.0} -->

In the absence of any data, knowing only $\text{supp}{({\mathbb{P}}^{\ast})}$ and that ${\mathbb{P}}^{\ast}$ has independent components, the smallest uncertainty which implies a probabilistic guarantee is the unit square (dotted line). With $N = 100$ data points from this distribution (blue circles), however, we can construct both $\mathcal{U}_{\epsilon}^{I}$ (dashed black line) and $\mathcal{U}_{\epsilon}^{FB}$ (solid black line) with $\epsilon = \alpha = {10\%}$, as shown. We also plot the limiting shape of these two sets as $N\rightarrow\infty$ (corresponding grey lines).

<!-- chunk {"id": "body-0094", "role": "body", "section": "Comparing $\\mathcal{U}_{\\epsilon}^{I}$ and $\\mathcal{U}_{\\epsilon}^{FB}$", "weight": 1.0} -->

Several features are evident from the plots. First, both sets are able to learn that ${\mathbb{P}}^{\ast}$ is symmetric in its first coordinate (the sets display vertical symmetry) and that ${\mathbb{P}}^{\ast}$ is skewed downwards in its second coordinate (the sets taper more sharply towards the top). Both sets *learn* these features from the data. Second, although $\mathcal{U}_{\epsilon}^{I}$ is a strict subset of $\text{supp}{({\mathbb{P}}^{\ast})}$, $\mathcal{U}_{\epsilon}^{FB}$ is not (see also Remark 5.7).

<!-- chunk {"id": "body-0095", "role": "body", "section": "Comparing $\\mathcal{U}_{\\epsilon}^{I}$ and $\\mathcal{U}_{\\epsilon}^{FB}$", "weight": 1.0} -->

Finally, neither set is a subset of the other, and, although for $N = 100$, $\mathcal{U}_{\epsilon}^{FB} \cap {\text{supp}{({\mathbb{P}}^{\ast})}}$ has smaller volume than $\mathcal{U}_{\epsilon}^{I}$, the reverse holds for larger $N$. Consequently, it is not clear which set to prefer in a given application, and the best choice likely depends on $N$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Uncertainty Sets Built from Marginal Samples", "weight": 1.0} -->

In this section, we observe samples from the marginal distributions of ${\mathbb{P}}^{\ast}$ separately, but do not assume these marginals are independent. This happens, e.g., when samples are drawn asynchronously, or when there are many missing values. In these cases, it is impossible to learn the joint distribution of ${\mathbb{P}}^{\ast}$ from the data. To streamline the exposition, we assume that we observe exactly $N$ samples of each marginal distribution. The results generalize to the case of different numbers of samples at the expense of more notation.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Uncertainty Sets Built from Marginal Samples", "weight": 1.0} -->

and let $s = {N + 1}$ if the corresponding set is empty. Then, the test which rejects if $q_{i,0} > {\hat{u}}_{i}^{(s)}$ is valid at level ${\alpha/2}d$. David and Nagaraja also prove that $\frac{s}{N} \downarrow {(1 - \epsilon/d}$).

<!-- chunk {"id": "body-0098", "role": "body", "section": "Uncertainty Sets Built from Marginal Samples", "weight": 1.0} -->

Here "M" is to emphasize "marginals." We use this confidence region in Step 1 of our schema.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Uncertainty Sets Built from Marginal Samples", "weight": 1.0} -->

When the marginals of $\mathbb{P}$ are known, Embrechts et al. proves

<!-- chunk {"id": "body-0100", "role": "body", "section": "Remark 6.2", "weight": 1.0} -->

Notice that the family $\{\mathcal{U}_{\epsilon}^{M}:{0 < \epsilon < 1}\}$, may *not* simultaneously imply a probabilistic guarantee for ${\mathbb{P}}^{\ast}$ because the confidence region $\mathcal{P}^{M}$ depends on $\epsilon$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Remark 6.3", "weight": 1.0} -->

The set $\{{(\mathbf{v},t)}:{{\delta^{\ast}{(\left. \mathbf{v} \middle| \mathcal{U}^{M} \right.)}} \leq t}\}$ is a simple box, representable by linear inequalities. We can separate over this set in closed form via.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Uncertainty Sets for Potentially Non-independent Components", "weight": 1.0} -->

In this section, we assume we observe samples drawn from the joint distribution of ${\mathbb{P}}^{\ast}$ which may have unbounded support. We consider a goodness-of-fit hypothesis test based on linear-convex ordering proposed in Bertsimas et al.. Specifically, given some multivariate ${\mathbb{P}}_{0}$, consider the null-hypothesis $H_{0}:{{\mathbb{P}}^{\ast} = {\mathbb{P}}_{0}}$.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Uncertainty Sets for Potentially Non-independent Components", "weight": 1.0} -->

for appropriate thresholds $\Gamma_{LCX},\Gamma_{\sigma}$ is a valid test at level $\alpha$. The authors provide an explicit bootstrap algorithm to compute $\Gamma_{LCX},\Gamma_{\sigma}$.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Uncertainty Sets for Potentially Non-independent Components", "weight": 1.0} -->

The confidence region of this test is

<!-- chunk {"id": "body-0105", "role": "body", "section": "Uncertainty Sets for Potentially Non-independent Components", "weight": 1.0} -->

We will use this confidence region in Step 1 of our schema.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Uncertainty Sets for Potentially Non-independent Components", "weight": 1.0} -->

Combining techniques from semi-infinite optimization with our schema (see electronic companion for proof), we obtain

<!-- chunk {"id": "body-0107", "role": "body", "section": "Remark 7.2", "weight": 1.0} -->

As the intersection of convex constraints, $\mathcal{U}_{\epsilon}^{LCX}$ is convex.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Remark 7.3", "weight": 1.0} -->

It is possible to separate over (31b) efficiently. Specifically, fix ${\mathbf{u},\mathbf{r}} \in {\mathbb{R}}^{d}$ and $1 \leq z \leq {1/\epsilon}$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Remark 7.3", "weight": 1.0} -->

corresponding to the potential signs of ${\mathbf{a}^{T}\mathbf{r}} - {b{({z - 1})}}$ and ${\mathbf{a}^{T}\mathbf{u}} - b$ at the worst-case value. (The fourth case, where both terms are negative is trivial since $\Gamma_{LCX} > 0$.) Each of these optimization problems can be written as linear optimizations. If ${\max{(\xi_{1},\xi_{2},\xi_{3})}} \leq \Gamma_{LCX}$, then $\mathbf{u},\mathbf{r}$ and $z$ are feasible in (31b). Otherwise, the optimal $\mathbf{a},b$ in the maximizing subproblem yields a violated cut.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Remark 7.4", "weight": 1.0} -->

The representation of $\delta^{\ast}{(\left. \mathbf{v} \middle| \mathcal{U}^{LCX} \right.)}$ is not particularly convenient. Nonetheless, we can separate over $\{{(\mathbf{v},t)}:{{\delta^{\ast}{(\left. \mathbf{v} \middle| \mathcal{U}^{LCX} \right.)}} \leq t}\}$ in polynomial time by using the above separation routine with the ellipsoid algorithm to solve $\max_{\mathbf{u} \in \mathcal{U}^{LCX}}{\mathbf{v}^{T}\mathbf{u}}$. Alternatively, combining the above separation routine with the dual-simplex algorithm yields a practically efficient algorithm for large-scale instances

<!-- chunk {"id": "body-0111", "role": "body", "section": "Hypothesis Testing: A Unifying Perspective", "weight": 1.0} -->

Several data-driven methods in the literature create families of measures $\mathcal{P}{(\mathcal{S})}$ that contain ${\mathbb{P}}^{\ast}$ with high probability. These methods do not explicitly reference hypothesis testing. In this section, we provide a hypothesis testing interpretation of two such methods. Leveraging this new perspective, we show how standard techniques for hypothesis testing, such as the bootstrap, can be used to improve upon these methods. Finally, we illustrate how our schema can be applied to these improved family of measures to generate new uncertainty sets. To the best of our knowledge, generating uncertainty sets for is a new application of both.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Hypothesis Testing: A Unifying Perspective", "weight": 1.0} -->

The key idea in both cases is to recast $\mathcal{P}{(\mathcal{S})}$ as the confidence region of a hypothesis test. This correspondence is not unique to these methods. There is a one-to-one correspondence between families of measures which contain ${\mathbb{P}}^{\ast}$ with probability at least $1 - \alpha$ with respect to the sampling and the confidence regions of hypothesis tests. This correspondence is sometimes called the "duality between confidence regions and hypothesis testing" in the statistical literature. It implies that any data-driven method predicated on a family of measures that contain ${\mathbb{P}}^{\ast}$ with probability $1 - \alpha$ can be interpreted in the light of hypothesis testing.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Hypothesis Testing: A Unifying Perspective", "weight": 1.0} -->

This observation is interesting for two reasons. First, it provides a unified framework to compare distinct methods in the literature and ties them to the well-established theory of hypothesis testing in statistics. Secondly, there is a wealth of practical experience with hypothesis testing. In particular, we know empirically which tests are best suited to various applications and which tests perform well even when the underlying assumptions on ${\mathbb{P}}^{\ast}$ that motivated the test may be violated. In the next section, we leverage some of this practical experience with hypothesis testing to strengthen these methods, and then derive uncertainty sets corresponding to these hypothesis tests to facilitate comparison between the approaches.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Uncertainty Set Motivated by Cristianini and Shawe-Taylor, 2003", "weight": 1.0} -->

Let $\parallel \cdot \parallel_{F}$ denote the Frobenius norm of matrices. As part of a particular machine learning application, Shawe-Taylor and Cristianini prove

<!-- chunk {"id": "body-0115", "role": "body", "section": "Remark 8.5", "weight": 1.0} -->

Like $\mathcal{U}_{\epsilon}^{FB}$, there is no guarantee that $\mathcal{U}_{\epsilon}^{CS} \subseteq {\text{supp}{({\mathbb{P}}^{\ast})}}$. Consequently, when a priori knowledge of the support is available, we can refine this set as in Remark 5.7.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Remark 8.5", "weight": 1.0} -->

To emphasize the benefits of bootstrapping when constructing uncertainty sets, Fig. 6 in the electronic companion illustrates the set $\mathcal{U}_{\epsilon}^{CS}$ for the example considered in Fig. 2 with thresholds computed with and without the bootstrap.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Uncertainty Set Motivated by Delage and Ye, 2010", "weight": 1.0} -->

Delage and Ye propose a data-driven approach for solving distributionally robust optimization problems. Their method relies on a slightly more general version of the following:^33^endnote: ^3^Specifically, since $R$ is typically unknown, the authors describe an estimation procedure for $R$ and prove a modified version of the Theorem 8.6 ‣ 8.2 Uncertainty Set Motivated by Delage and Ye, 2010 ‣ 8 Hypothesis Testing: A Unifying Perspective") using this estimate and different constants. We treat the simpler case where $R$ is known here. Extensions to the other case are straightforward.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Remark 8.9", "weight": 1.0} -->

The set $\{{(\mathbf{v},t)}:{{\delta^{\ast}{(\left. \mathbf{v} \middle| \mathcal{U}^{DY} \right.)}} \leq t}\}$ is representable as a linear matrix inequality. At time of writing, solvers for linear matrix inequalities are not as developed as those for second order cone programs. Consequently, one may prefer $\mathcal{U}_{\epsilon}^{CS}$ to $\mathcal{U}_{\epsilon}^{DY}$ in practice for its simplicity.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Comparing $\\mathcal{U}_{\\epsilon}^{M}$, $\\mathcal{U}_{\\epsilon}^{LCX}$, $\\mathcal{U}_{\\epsilon}^{CS}$ and $\\mathcal{U}_{\\epsilon}^{DY}$", "weight": 1.0} -->

One of the benefits of deriving uncertainty sets corresponding to the methods of Shawe-Taylor and Cristianini and Delage and Ye is that it facilitates comparisons between these methods and our own proposals. In Fig. 3, we illustrate the sets $\mathcal{U}_{\epsilon}^{M}$, $\mathcal{U}_{\epsilon}^{LCX}$, $\mathcal{U}_{\epsilon}^{CS}$ and $\mathcal{U}_{\epsilon}^{DY}$ for the same numerical example from Fig. 2. Because $\mathcal{U}^{M}$ does not leverage the joint distribution ${\mathbb{P}}^{\ast}$, it does not learn that its marginals are independent. Consequently, $\mathcal{U}^{M}$ has pointed corners permitting extreme values of both coordinates simultaneously. The remaining sets do learn the marginal independence from the data and, hence, have rounded corners.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Comparing $\\mathcal{U}_{\\epsilon}^{M}$, $\\mathcal{U}_{\\epsilon}^{LCX}$, $\\mathcal{U}_{\\epsilon}^{CS}$ and $\\mathcal{U}_{\\epsilon}^{DY}$", "weight": 1.0} -->

Finally, $\mathcal{U}^{LCX}$ is contained within $\text{supp}{({\mathbb{P}}^{\ast})}$ and displays symmetry in the first coordinate and skewness in the second. In this example it is also the smallest set (in terms of volume). All sets shrink as $N$ increases.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Refining $\\mathcal{U}_{\\epsilon}^{FB}$", "weight": 1.0} -->

Another common approach to hypothesis testing in applied statistics is to use tests designed for Gaussian data that are "robust to departures from normality." The best known example of this approach is the $t$-test from Sec. 2.2, for which there is a great deal of experimental evidence to suggest that the test is still approximately valid when the underlying data is non-Gaussian. Moreover, certain nonparametric tests of the mean for non-Gaussian data are asymptotically equivalent to the $t$-test, so that the $t$-test, itself, is asymptotically valid for non-Gaussian data. Consequently, the $t$-test is routinely used in practice, even when the Gaussian assumption may be invalid.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Refining $\\mathcal{U}_{\\epsilon}^{FB}$", "weight": 1.0} -->

We next use the $t$-test in combination with bootstrapping to refine $\mathcal{U}_{\epsilon}^{FB}$. We replace $m_{fi},m_{bi}$ in Eq., with the upper and lower thresholds of a $t$-test at level $\alpha^{\prime}/2$. We expect these new thresholds to correctly bound the true mean $\mu_{i}$ with probability approximately $1 - {\alpha^{\prime}/2}$ with respect to the data. We then use the bootstrap to calculate bounds on the forward and backward deviations ${\overline{\sigma}}_{fi},{\overline{\sigma}}_{bi}$.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Refining $\\mathcal{U}_{\\epsilon}^{FB}$", "weight": 1.0} -->

We stress not all tests designed for Gaussian data are robust to departures from normality. Applying Gaussian tests that lack this robustness will likely yield poor performance. Consequently, some care must be taken when choosing an appropriate test.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Optimizing over Multiple Constraints", "weight": 1.0} -->

In this section, we propose an approach for solving. The key observation is

<!-- chunk {"id": "body-0125", "role": "body", "section": "Choosing the \"Right\" Set and Tuning $\\alpha$, $\\epsilon$", "weight": 1.0} -->

Often several of our data-driven sets may be consistent with the a priori knowledge of ${\mathbb{P}}^{\ast}$. Choosing an appropriate set from amongst our proposals is a non-trivial task that depends on the application and the data. One may be tempted to use the intersection of all eligible sets. We caution that the intersection of two sets which imply a probabilistic guarantee at level $\epsilon$ need not imply a probabilistic guarantee at level $\epsilon$. Similarly, one may be tempted to solve the robust optimization model for each eligible set separately and select the set and solution with best objective value. We caution that a set chosen in this way will suffer from an in-sample bias. Specifically, the probability with respect to the sampling that this set does not imply a probabilistic guarantee at level $\epsilon$ may be much larger than $\alpha$.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Choosing the \"Right\" Set and Tuning $\\alpha$, $\\epsilon$", "weight": 1.0} -->

Drawing an analogy to model selection in machine learning, we propose a different approach to set selection. Specifically, split the data into two parts, a training set and a hold-out set. Use the training set to construct each potential uncertainty set, in turn, and solve the robust optimization problem. Test each of the corresponding solutions out-of-sample on the hold-out set, and select the best solution and corresponding uncertainty set. Since the two halves of the data are independent, it follows that with probability at least $1 - \alpha$ with respect to the sampling, the set so selected will correctly imply a probabilistic guarantee at level $\epsilon$.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Choosing the \"Right\" Set and Tuning $\\alpha$, $\\epsilon$", "weight": 1.0} -->

The drawback of this approach is that only half the data is used to calibrate the uncertainty set. When $N$ is only moderately large, this may be impractical. In these cases, $k$-fold cross-validation can be used to select a set. (See Hastie et al. for a review of cross-validation.) Unlike the above procedure, we cannot prove that the set chosen by $k$-fold cross-validation satisfies the appropriate guarantee. Nevertheless, experience in model selection suggests that this procedure frequently identifies a good model, and, thus, we expect it will identify a good set. We use $5$-fold cross-validation in our numerical experiments.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Choosing the \"Right\" Set and Tuning $\\alpha$, $\\epsilon$", "weight": 1.0} -->

In applications where there is not a natural choice for $\alpha$ or $\epsilon$, we suggest tuning these parameters in an entirely analogous way. Namely, we propose selecting a grid of potential values for $\alpha$ and/or $\epsilon$ and then selecting the best value either using a hold-out set or cross-validation. Since the optimal value likely depends on the choice of uncertainty set, we suggest choosing them jointly.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Applications", "weight": 1.0} -->

We demonstrate how our new sets may be used in two applications: portfolio management and queueing theory. Our goals are to, first, illustrate their application and, second, to compare them to one another.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Applications", "weight": 1.0} -->

In these two applications, our data-driven sets outperform traditional, non-data driven uncertainty sets, and, moreover, robust models built with our sets perform as well or better than other data-driven approaches.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Applications", "weight": 1.0} -->

Although our data-driven sets all shrink as $N\rightarrow\infty$, they learn different features of ${\mathbb{P}}^{\ast}$, such as correlation structure and skewness. Consequently, different sets may be better suited to different applications, and the right choice of set may depend on $N$. Cross-validation and other model selection techniques effectively identify the best set.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Applications", "weight": 1.0} -->

Optimizing the $\epsilon_{j}$'s in the case of multiple constraints can significantly improve performance.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Portfolio Management", "weight": 1.0} -->

Portfolio management has been well-studied in the robust optimization literature.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Portfolio Management", "weight": 1.0} -->

which seeks the portfolio $\mathbf{x}$ with maximal worst-case return over the set $\mathcal{U}$. If $\mathcal{U}$ implies a probabilistic guarantee for ${\mathbb{P}}^{\ast}$ at level $\epsilon$, then the optimal value $z^{\ast}$ of this optimization is a conservative bound on the $\epsilon$-worst case return for the optimal solution $\mathbf{x}^{\ast}$.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Portfolio Management", "weight": 1.0} -->

We consider a synthetic market with $d = 10$ assets. Returns are generated according to the following model from Natarajan et al.:

<!-- chunk {"id": "body-0136", "role": "body", "section": "Portfolio Management", "weight": 1.0} -->

In this model, all assets have the same mean return (0%), the same standard deviation ($1.00\%$), but have different skew and support. Higher indexed assets are highly skewed; they have a small probability of achieving a very negative return. Returns for different assets are independent. We simulate $N = 500$ returns to use as data.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Portfolio Management", "weight": 1.0} -->

We will utilize our sets $\mathcal{U}_{\epsilon}^{M}$ and $\mathcal{U}_{\epsilon}^{LCX}$ in this application. We do not consider the sets $\mathcal{U}_{\epsilon}^{I}$ or $\mathcal{U}_{\epsilon}^{FB}$ since we do not know a priori that the returns are independent. To contrast to the methods of and we also construct the sets $\mathcal{U}_{\epsilon}^{CS}$ and $\mathcal{U}_{\epsilon}^{DY}$. Recall from Remarks 8.3 and 8.8 that robust linear constraints over these sets are equivalent to ambiguous chance-constraints in the original methods, but with improved thresholds. As discussed in Remark 8.5, we also construct $\mathcal{U}_{\epsilon}^{CS} \cap {\text{supp}{({\mathbb{P}}^{\ast})}}$ for comparison.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Portfolio Management", "weight": 1.0} -->

We use $\alpha = \epsilon = {10\%}$ in all of our sets. Finally, we will also compare to the method of Calafiore and Monastero (denoted "CM" in our plots), which is not an uncertainty set based method. We calibrate this method to also provide a bound on the $10\%$ worst-case return that holds with at least $90\%$ with respect to the sampling so as to provide a fair comparison.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Portfolio Management", "weight": 1.0} -->

We first consider the problem of selecting an appropriate set via $5$-fold cross-validation. The top left panel in Fig. 4 shows the out-of-sample 10% worst-case return for each of the $5$ runs (blue dots), as well as the average performance on the $5$ runs for each set (black square). Sets $\mathcal{U}_{\epsilon}^{M}$, $\mathcal{U}_{\epsilon}^{CS} \cap {\text{supp}{({\mathbb{P}}^{\ast})}}$ and $\mathcal{U}_{\epsilon}^{DY}$ yield identical portfolios (investing everything in the first asset) so we only include $\mathcal{U}^{M}$ in our graphs. The average performance is also shown in Table 1 under column CV (for "cross-validation.") The optimal objective value of for each of our sets (trained with the entire data set) is shown in column $z_{In}$.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Portfolio Management", "weight": 1.0} -->

Based on the top left panel of Fig. 4, it is clear that $\mathcal{U}_{\epsilon}^{LCX}$ and $\mathcal{U}_{\epsilon}^{CS}$ significantly outperform the remaining sets. They seem to perform similarly to the CM method. Consequently, we would choose one of these two sets in practice.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Portfolio Management", "weight": 1.0} -->

We can assess the quality of this choice by using the ground-truth model to calculate the true 10% worst-case return for each of the portfolios. These are shown in Table 1 under column $z_{Out}$. Indeed, these sets perform better than the alternatives, and, as expected, the cross-validation estimates are reasonably close to the true out-of-sample performance. By contrast, the in-sample objective value $z_{In}$ is a loose bound. We caution against using this in-sample value to select the best set.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Portfolio Management", "weight": 1.0} -->

Interestingly, we point out that while $\mathcal{U}_{\epsilon}^{CS} \cap {\text{supp}{({\mathbb{P}}^{\ast})}}$ is potentially smaller (with respect to subset containment) than $\mathcal{U}_{\epsilon}^{CS}$, it performs much worse out-of-sample (it performs identically to $\mathcal{U}_{\epsilon}^{M}$). This experiment highlights the fact that size calculations alone cannot predict performance. Cross-validation or similar techniques are required.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Portfolio Management", "weight": 1.0} -->

One might ask if these results are specific to the particular draw of $500$ data points we use. We repeat the above procedure $100$ times. The resulting distribution of 10% worst-case return is shown in the top right panel of Fig. 4 and the average of these runs is shown Table 1 under column $z_{Avg}$. As might have been guessed from the cross-validation results, $\mathcal{U}_{\epsilon}^{CS}$ delivers more stable and better performance than either $\mathcal{U}_{\epsilon}^{LCX}$ or CM. $\mathcal{U}_{\epsilon}^{LCX}$ slightly outperforms CM, and its distribution is shifted right.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Portfolio Management", "weight": 1.0} -->

We next look at the distribution of actual holdings between these methods. We show the average holding across these $100$ runs as well as $10\%$ and $90\%$ quantiles for each asset in the bottom left panel of Fig. 4. Since $\mathcal{U}_{\epsilon}^{M}$ does not use the joint distribution, it sees no benefit to diversification. Portfolios built from $\mathcal{U}_{\epsilon}^{M}$ consistently holds all their wealth in the first asset over all the runs, hence, omitted from graphs. The set $\mathcal{U}_{\epsilon}^{CS}$ depends only on the first two moments of the data, and, consequently, cannot distinguish between the assets. It holds a very stable portfolio of approximately the same amount in each asset. By contrast, $\mathcal{U}^{LCX}$ is able to learn the asymmetry in the distributions, and holds slightly less of the higher indexed (toxic) assets. CM is similar to $\mathcal{U}^{LCX}$, but demonstrates more variability in the holdings.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Portfolio Management", "weight": 1.0} -->

We point out that the performance of each method depends slightly on $N$. We repeat the above experiments with $N = 2000$. Results are summarized in Table 1. The bottom right panel of Fig. 4 shows the distribution of the $10\%$ worst-case return. (Additional plots are also available in Appendix 16.) Both $\mathcal{U}^{LCX}$ and CM perform noticeably better with the extra data, but $\mathcal{U}^{LCX}$ now noticeably outperforms CM and its distribution is shifted significantly to the right.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Queueing Analysis", "weight": 1.0} -->

One of the strengths of our approach is the ability to retrofit existing robust optimization models by replacing their uncertainty sets with our proposed sets, thereby creating new data-driven models that satisfy strong guarantees. In this section, we illustrate this idea with a robust queueing model as in Bertsimas et al. and Bandi et al.. Bandi et al. use robust optimization to generate *approximations* to a performance metric of a queuing network. We will combine their method with our new sets to generate *probabilistic upper bounds* to these metrics. For concreteness, we focus on the waiting time in a G/G/1 queue. Extending our analysis to more complex queueing networks can likely be accomplished similarly. We stress that we do not claim that our new bounds are the best possible -- indeed there exist extremely accurate, specialized techniques for the G/G/1 queue -- but, rather, that the retrofitting procedure is general purpose and yields reasonably good results. These features suggest that a host of other robust optimization applications in information theory, supply-chain management and revenue management might benefit from this retrofitting.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Queueing Analysis", "weight": 1.0} -->

From Lindley's recursion, the waiting time of the $n^{\text{th}}$ customer is

<!-- chunk {"id": "body-0148", "role": "body", "section": "Queueing Analysis", "weight": 1.0} -->

Motivated by Bandi et al., we consider a worst-case realization of a Lindley recursion

<!-- chunk {"id": "body-0149", "role": "body", "section": "Queueing Analysis", "weight": 1.0} -->

Taking $\mathcal{U} = \mathcal{U}_{\overline{\epsilon}/n}^{FB}$ and applying Theorem 5.5 to the inner-most optimization yields

<!-- chunk {"id": "body-0150", "role": "body", "section": "Queueing Analysis", "weight": 1.0} -->

Relaxing the integrality on $j$, this optimization can be solved closed-form yielding

<!-- chunk {"id": "body-0151", "role": "body", "section": "Queueing Analysis", "weight": 1.0} -->

From, with probability at least $1 - \alpha$ with respect to the sampling, each of the inner-most optimizations upper bound their corresponding random quantity with probability $1 - {\overline{\epsilon}/n}$ with respect to ${\mathbb{P}}^{\ast}$. Thus, by union bound, ${{\mathbb{P}}^{\ast}{({{\overset{\sim}{W}}_{n} \leq W_{n}^{1,{FB}}})}} \geq {1 - \overline{\epsilon}}$.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Queueing Analysis", "weight": 1.0} -->

On the other hand, since $\{\mathcal{U}_{\epsilon}^{FB}:{0 < \epsilon < 1}\}$ simultaneously implies a probabilistic guarantee, we can also optimize the choice of $\epsilon_{j}$, yielding

<!-- chunk {"id": "body-0153", "role": "body", "section": "Queueing Analysis", "weight": 1.0} -->

From the KKT conditions, the constraint will be tight for all $j$, so that $W_{n}^{2,{FB}}$ satisfies

<!-- chunk {"id": "body-0154", "role": "body", "section": "Queueing Analysis", "weight": 1.0} -->

We can further refine our bound by truncating the recursion at customer $\min{(n,n^{(k)})}$ where, with high probability, $\overset{\sim}{n} \leq n^{(k)}$. A formal derivation of the resulting bound, which we denote $W_{n}^{3,{FB}}$, can be found in Appendix 17. Therein we also prove that with probability at least $1 - \alpha$ with respect to the sampling, ${{\mathbb{P}}^{\ast}{({{\overset{\sim}{W}}_{n} \leq W_{n}^{3,{FB}}})}} \geq {1 - \overline{\epsilon}}$.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Queueing Analysis", "weight": 1.0} -->

Finally, our choice of $\mathcal{U}_{\epsilon}^{FB}$ was somewhat arbitrary. Similar analysis can be performed for many of our sets. To illustrate, Appendix 17 also contains corresponding bounds for the set $\mathcal{U}_{\epsilon}^{CS}$.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Queueing Analysis", "weight": 1.0} -->

We illustrate these ideas numerically. Let service times follow a Pareto distribution with parameter $1.1$ truncated at $15$, and the interarrival times follow an exponential distribution with rate $3.05$ truncated at 15.25. The resulting truncated distributions have means of approximately $3.029$ and $3.372$, respectively, yielding an approximate 90% utilization.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Queueing Analysis", "weight": 1.0} -->

As a first experiment, we bound the median waiting time ($\epsilon = {50\%}$) for the $n = 10$ customer, using each of our bounds with differing amounts of data. We repeat this procedure $100$ times to study the variability of our bounds with respect to the data. The left panel of Fig. 5 shows the average value of the bound and error bars for the 10% and 90% quantiles. As can be seen, all of the bounds improve as we add more data. Moreover, optimizing the $\epsilon_{j}$'s (the difference between $W_{n}^{{FB},1}$ and $W_{n}^{{FB},2}$ is significant.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Queueing Analysis", "weight": 1.0} -->

For comparison purposes, we include a sample analogue of Kingman's bound on the $1 - \epsilon$ quantile of the waiting time, namely,

<!-- chunk {"id": "body-0159", "role": "body", "section": "Queueing Analysis", "weight": 1.0} -->

where ${\hat{\mu}}_{t},{\hat{\sigma}}_{t}^{2}$ are the sample mean and sample variance of the arrivals, ${\hat{\mu}}_{x},{\hat{\sigma}}_{x}^{2}$ are the sample mean and sample variance of the service times, and we have applied Markov's inequality. Unfortunately, this bound is extremely unstable, even for large $N$. The dotted line in the left-panel of Fig. 5 is the average value over the $100$ runs of this bound for $N = {10,000}$ data points (the error-bars do not fit on graph.) Sample statistics for this bound and our bounds can also be seen in Table 2. As shown, our bounds are both significantly better (with less data), and exhibit less variability.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Queueing Analysis", "weight": 1.0} -->

As a second experiment, we use our bounds to calculate a probabilistic upper bound on the entire CDF of ${\overset{\sim}{W}}_{n}$ for $n = 10$ with $N = {1,000}$, $\alpha = {20\%}$. Results can be seen in the right panel of Fig. 5. We have included the empirical CDF of the waiting time and the sampled version of the Kingman bound comparison. As seen, our bounds significantly improve upon the sampled Kingman bound, and the benefit of optimizing the $\epsilon_{j}$'s is again, significant. We remark that the ability to simultaneously bound the entire CDF for any $n$, whether transient or steady-state, is an important strength of this type of analysis.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Conclusions", "weight": 1.0} -->

The prevalence of high quality data is reshaping operations research. Indeed, a new data-centered paradigm is emerging. In this work, we took a first step towards adapting traditional robust optimization techniques to this new paradigm. Specifically, we proposed a novel schema for designing uncertainty sets for robust optimization from data using hypothesis tests. Sets designed using our schema imply a probabilistic guarantee and are typically much smaller than corresponding data poor variants. Models built from these sets are thus less conservative than conventional robust approaches, yet retain the same robustness guarantees.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Endnotes", "weight": 1.0} -->

Recall that for any non-empty convex set $\mathcal{U}$, ${ri{(\mathcal{U})}} \equiv {\{{\mathbf{u} \in \mathcal{U}}:{{{\forall\mathbf{z}} \in \mathcal{U}},{{\exists\lambda} > {{1\text{~s.t.~}\lambda\mathbf{u}} + {{({1 - \lambda})}\mathbf{z}}} \in \mathcal{U}}}\}}$ (cf. Bertsekas et al. ). 2. 2 The existence of such a set in Step 3 by the bijection between closed, positively homogenous convex functions and closed convex sets in convex analysis (see Bertsekas et al. ). 3. 3 Specifically, since $R$ is typically unknown, the authors describe an estimation procedure for $R$ and prove a modified version of the Theorem 8.6 using this estimate and different constants. We treat the simpler case where $R$ is known here.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Endnotes", "weight": 1.0} -->

Extensions to the other case are straightforward.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Endnotes", "weight": 1.0} -->

Part of this work was supported by the National Science Foundation Graduate Research Fellowship under Grant No. 1122374. We would also like to thank two anonymous reviewers and the Associate Editor for their insightful and constructive comments. They greatly helped to improve the quality of the paper.
