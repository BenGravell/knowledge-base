<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-Driven Robust Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The last decade witnessed an explosion in the availability of data for operations research applications. Motivated by this growing availability, we propose a novel schema for utilizing data to design uncertainty sets for robust optimization using statistical hypothesis tests. The approach is flexible and widely applicable, and robust optimization problems built from our new sets are computationally tractable, both theoretically and practically. Furthermore, optimal solutions to these problems enjoy a strong, finite-sample probabilistic guarantee. \edit{We describe concrete procedures for choosing an appropriate set for a given application and applying our approach to multiple uncertain constraints. Computational evidence in portfolio management and queuing confirm that our data-driven sets significantly outperform traditional robust optimization techniques whenever data is available.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robust optimization is a popular approach to optimization under uncertainty. The key idea is to define an uncertainty set of possible realizations of the uncertain parameters and then optimize against worst-case realizations within this set. Computational experience suggests that with well-chosen sets, robust models yield tractable optimization problems whose solutions perform as well or better than other approaches. With poorly chosen sets, however, robust models may be overly-conservative or computationally intractable. Choosing a good set is crucial. Fortunately, there are several theoretically motivated and experimentally validated proposals for constructing good uncertainty sets [ben2000robust, bertsimas2004price, ben2009robust, bandi2012tractable]. These proposals share a common paradigm; they combine a priori reasoning with mild assumptions on the uncertainty to motivate the construction of the set.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, the last decade witnessed an explosion in the availability of data. Massive amounts of data are now routinely collected in many industries. Retailers archive terabytes of transaction data. Suppliers track order patterns across their supply chains. Energy markets can access global weather data, historical demand profiles, and, in some cases, real-time power consumption information. These data have motivated a shift in thinking away from a priori reasoning and assumptions and towards a new data-centered paradigm. A natural question, then, is how should robust optimization techniques be tailored to this new paradigm?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a general schema for designing uncertainty sets for robust optimization from data.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

\color{black}We consider uncertain constraints of the form $f({\mathbf{\tilde{u}}}, \mathbf{x}) \leq 0$ where $\mathbf{x} \in {\mathbb{R}}^k$ is the optimization variable, and ${\mathbf{\tilde{u}}} \in {\mathbb{R}}^d$ is an uncertain parameter. We model this constraint by choosing a set ${\mathcal{U}}$ and forming the corresponding robust constraint $$f(\mathbf{u}, \mathbf{x}) \leq 0 \ \ \forall \mathbf{u} \in {\mathcal{U}}.$$ We assume throughout that $f(\mathbf{u}, \mathbf{x})$ is concave in $\mathbf{u}$ for any $\mathbf{x}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In many applications, robust formulations decompose into a series constraints of the form [eq:NonlinearRobust] through an appropriate transformation of variables, including uncertain linear optimization and multistage adaptive optimization (see, e.g., [ben2009robust]). In this sense, [eq:NonlinearRobust] is a fundamental building block for more complex robust optimization models. [bertsimas2004price, ben2009robust, chen2010cvar] to constructing uncertainty sets for [eq:NonlinearRobust] assume ${\mathbf{\tilde{u}}}$ is a random variable whose distribution $\mathbb{P}^*$ is not known except for some assumed structural features. For example, they may assume that $\mathbb{P}^*$ has independent components, while its marginal distributions are not known.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

- The robust constraint [eq:NonlinearRobust] is computationally tractable.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

- The set ${\mathcal{U}}_\epsilon$ implies a probabilistic guarantee for $\mathbb{P}^*$ at level $\epsilon$, that is, for any $\mathbf{x}^* \in {\mathbb{R}}^k$ and for every function $f(\mathbf{u}, \mathbf{x})$ concave in $\mathbf{u}$ for all $\mathbf{x}$, we have the implication: $$\text{If } f(\mathbf{u}, \mathbf{x}^*) \leq 0 \ \ \forall \mathbf{u} \in {\mathcal{U}}_\epsilon, \text{ then } \mathbb{P}^*(f({\mathbf{\tilde{u}}}, \mathbf{x}^*) \leq 0) \geq 1-\epsilon.$$ [prop:guarantee] ensures that a feasible solution to the robust constraint will also be feasible with probability $1-\epsilon$ with respect to

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing proposals achieve [prop:guarantee] by leveraging the a priori structural features of $\mathbb{P}^*$. \textcolor{black}Some of these approaches, e.g. only consider the special case when $f(\mathbf{u}, \mathbf{x})$ is bi-affine, but one can generalize them to def:Guarantee using techniques from (see also Sec.sec:nonlinear).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Like previous proposals, we also assume ${\mathbf{\tilde{u}}}$ is a random variable whose distribution $\mathbb{P}^*$ is not known exactly, and seek sets ${\mathcal{U}}_\epsilon$ that satisfy these properties. Unlike previous proposals and this is critical we assume that we have data $\mathcal{S}=\{\hat{\mathbf{u}}^1, \ldots, \hat{\mathbf{u}}^N\}$ drawn i.i.d. according to $\mathbb{P}^*$. By combining these data with the a priori structural features of $\mathbb{P}^*$, we can design new sets that imply similar probabilistic guarantees, but which are much smaller with respect to subset containment than their traditional counterparts. Consequently, robust models built from our new sets yield less conservative solutions than traditional counterparts, while retaining their robustness properties.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The key to our schema is using the confidence region of a statistical hypothesis test to quantify what we learn about $\mathbb{P}^*$ from the data. Specifically, our constructions depend on three ingredients: the a priori assumptions on $\mathbb{P}^*$, the data, and a hypothesis test. By pairing different a priori assumptions and tests, we obtain distinct data-driven uncertainty sets, each with its own geometric shape, computational properties, and modeling power. These sets can capture a variety of features of $\mathbb{P}^*$, including skewness, heavy-tails and correlations.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In principle, there is a multitude of possible pairings of a priori assumptions and tests. We focus on pairings we believe are most relevant to applied robust modeling. Specifically, we consider a priori assumptions that are common in practice and tests that lead to tractable uncertainty sets. Our list is non-exhaustive; there may exist other pairings that yield effective sets.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

- $\mathbb{P}^*$ has known, finite discrete support (Sec.[sec:Discrete]). - $\mathbb{P}^*$ may have continuous support, and the components of ${\mathbf{\tilde{u}}}$ are independent (Sec.[sec:Independence]). - $\mathbb{P}^*$ may have continuous support, but data are drawn from its marginal distributions asynchronously (Sec.[sec:marginals]). This situation models the case of missing values. - $\mathbb{P}^*$ may have continuous support, and data are drawn from its joint distribution (Sec.[sec:Correlated]). This is the general case.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Table[tab:Results]summarizes the a priori structural assumptions, hypothesis tests, and resulting uncertainty sets that we propose. Each set is convex and admits a tractable, explicit description; see the referenced equations.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Summary of data-driven uncertainty sets proposed in this paper.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

| Assumptions on $\mathbb{P}^*$ | Hypothesis Test | 20cmGeometric Description | Eqs. | Separation | SOC, EC and LMI denote second-order cone representable sets, exponential cone representable sets, and linear matrix inequalities, respectively. The additional *" notation indicates a set of of the above type with one additional, relative entropy constraint. $KS$, $K$, $CvM$, $W$, and $AD$ denote the Kolmogorov-Smirnov, Kuiper, Cramer-von Mises, Watson and Anderson-Darling goodness of fit tests, respectively. In some cases, we can separate over the constraint eq:NonlinearRobust for bi-affine $f$ with a specialized algorithm. In these cases, the column Separation" roughly describes this algorithm.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

\textcolor{black}For each of our sets, we provide an explicit, equivalent reformulation of eq:NonlinearRobust. The complexity of optimizing over this reformulation depends both on the function $f(\mathbf{u}, \mathbf{x})$ and the set ${\mathcal{U}}$. For each of our sets, we show that this reformulation is polynomial time tractable for a large class of functions $f$ including bi-affine functions, separable functions, conic-quadratic representable functions and certain sums of uncertain exponential functions. By exploiting special structure in some of our sets, we can provide specialized routines for directly separating over eq:NonlinearRobust for bi-affine $f$. In these cases, the column Separation" in Tabletab:Results roughly describes these routines. Utilizing this separation routine within a cutting-plane method may offer performance superior to reformulation based-approaches.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

We are not the first to consider using hypothesis tests in data-driven optimization. Recently, proposed a class of data-driven uncertainty sets based on phi-divergences. (Phi divergences are closely related to some types of hypothesis tests.) They focus on the case where the uncertain parameter is a probability distribution with known, finite, discrete support. By contrast, we design uncertainty sets for general uncertain parameters with potentially continuous support such as future product demand, service times, and asset returns. Many existing robust optimization applications utilize similar general uncertain parameters. Consequently, retrofitting these applications with our new data-driven sets to yield data-driven variants is perhaps more straightforward than using sets for uncertain probabilities. From a methodological perspective, treating general uncertain parameters requires combining ideas from a variety of hypothesis tests (not just those based on phi-divergences of discrete distributions) with techniques from convex analysis and risk theory. (See Sec.sec:Schema.)

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

Other authors have also considered more specialized applications of hypothesis testing in data-driven optimization. proposes a distributionally robust dynamic program based on Pearson's $\chi^2$-test for a particular inventory problem. calibrate an uncertainty set for the mean and covariance of a distribution using linear regression and the $t$-test. It is not clear how to generalize these methods to other settings, e.g., distributions with continuous support in the first case or general parameter uncertainty in the second. By contrast, we offer a comprehensive study of the connection between hypothesis testing and uncertainty set design, addressing a number of cases with general machinery.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, our hypothesis testing perspective provides a unified view of many other data-driven methods from the literature. For example, and have proposed data-driven methods for chance-constrained and distributionally robust problems, respectively without using hypothesis testing. We show how these works can be reinterpreted through the lens of hypothesis testing. Leveraging this viewpoint enables us to apply state-of-the-art methods from statistics, such as the bootstrap, to refine these methods and improve their numerical performance. Moreover, applying our schema, we can design data-driven uncertainty sets for robust optimization based upon these methods. Although we focus on and in this paper, this strategy applies equally well to a host of other methods, such as the likelihood estimation approach of. In this sense, we believe hypothesis testing and uncertainty set design provide a common framework in which to compare and contrast different approaches.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we note that propose a very different data-driven method for robust optimization not based on hypothesis tests. In their approach, one replaces the uncertain constraint $f({\mathbf{\tilde{u}}}, \mathbf{x}) \leq 0$ with $N$ sampled constraints over the data, $f(\hat{\mathbf{u}}^j, \mathbf{x}) \leq 0$, for $j=1, \ldots, N$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

For $f(\mathbf{u}, \mathbf{x})$ convex in $\mathbf{x}$ with arbitrary dependence in $\mathbf{u}$, they provide a tight bound $N(\epsilon)$ such that if $N \geq N(\epsilon)$, then, with high probability with respect to the sampling, any $\mathbf{x}$ which is feasible in the $N$ sampled constraints satisfies $\mathbb{P}^*(f({\mathbf{\tilde{u}}}, \mathbf{x}) \leq 0) \geq 1-\epsilon$. Various refinements of this base method have also been proposed yielding smaller bounds $N(\epsilon)$, including incorporating $\ell_1$-regularization and allowing $\mathbf{x}$ to violate a small fraction of the constraints. Compared to our approach, these methods are more generally applicable and provide a similar probabilistic guarantee.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the special case we treat where $f({\mathbf{\tilde{u}}}, \mathbf{x})$ is concave in $\mathbf{u}$, however, our proposed approach offers some advantages. First, because it leverages the concave structure of $f(\mathbf{u}, \mathbf{x})$, our approach generally yields less conservative solutions (for the same $N$ and $\epsilon$) than. (See Sec.sec:Schema.) Second, for fixed $\epsilon > 0$, our approach is applicable even if $N < N(\epsilon)$, while theirs is not. This distinction is important when $\epsilon$ is very small and there may not exist enough data. Finally, as we will show, our approach reformulates eq:NonlinearRobust as a series of (relatively) sparse convex constraints, while the approach will in general yield $N$ dense constraints which may be numerically challenging when $N$ is large. For these reasons, practitioners may prefer our proposed approach in certain applications.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Introduction", "weight": 1.5} -->

- We propose a new, systematic schema for constructing uncertainty sets from data using statistical hypothesis tests. When the data are drawn i.i.d. from an unknown distribution $\mathbb{P}^*$, sets built from our schema imply a probabilistic guarantee for $\mathbb{P}^*$ at any desired level $\epsilon$. - We illustrate our schema by constructing a multitude of uncertainty sets. Each set is applicable under slightly different a priori assumptions on $\mathbb{P}^*$ as described in Table[tab:Results]. - \textcolor{black}We prove that robust optimization problems over each of our sets are generally tractable. Specifically, for each set, we derive an explicit robust counterpart to eq:NonlinearRobust and show that for a large class of functions $f(\mathbf{u}, \mathbf{x})$ optimizing over this counterpart can be accomplished in polynomial time using off-the-shelf software. - \textcolor{black}We unify several existing data-driven methods through the lens of hypothesis testing.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Introduction", "weight": 1.5} -->

Through this lens, we motivate the use of common numerical techniques from statistics such as bootstrapping and gaussian approximation to improve their performance. Moreover, we apply our schema to derive new uncertainty sets for eq:NonlinearRobust inspired by the refined versions of these methods. - \textcolor{black}We propose a new approach to modeling multiple uncertain constraints simultaneously with our sets by optimizing the parameters chosen for each individual constraint. We prove that this technique is tractable and yields solutions which will satisfy all the uncertain constraints simultaneously for any desired level $\epsilon$. - \textcolor{black}We provide guidelines for practitioners on choosing an appropriate set and calibrating its parameters by leveraging techniques from model selection in machine learning. - \textcolor{black}Through applications in queueing and portfolio allocation, we assess the relative strengths and weaknesses of our sets. Overall, we find that although all of our sets shrink in size as $N\rightarrow \infty$, they differ in their ability to represent features of $\mathbb{P}^*$. Consequently, they may perform very differently in a given application.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the above two settings, we find that our model selection technique frequently identifies a good set choice, and a robust optimization model built with this set performs as well or better than other robust data-driven approaches.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is structured as follows. Sec. [sec:Background] reviews background to keep the paper self-contained. Sec.[sec:Schema] presents our schema for constructing uncertainty sets. Sec.[sec:Discrete]-[sec:Correlated] describe the various constructions in Table[tab:Results]. \textcolor{black}Sec.sec:HypTestPerspective reinterprets several techniques in the literature through the lens of hypothesis testing and, subsequently, uses them to motivate new uncertainty sets. Sec.[sec:Multiple] and Sec.[sec:Choose] discuss modeling multiple constraints and choosing the right set for an application, respectively. Sec.[sec:computational] presents numerical experiments, and Sec.[sec:Conclusion]concludes. All proofs are in the electronic companion.
