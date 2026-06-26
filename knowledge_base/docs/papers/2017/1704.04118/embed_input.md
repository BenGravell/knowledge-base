<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

From Data to Decisions: Distributionally Robust Optimization Is Optimal

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study stochastic programs where the decision-maker cannot observe the distribution of the exogenous uncertainties but has access to a finite set of independent samples from this distribution. In this setting, the goal is to find a procedure that transforms the data to an estimate of the expected cost function under the unknown data-generating distribution, i.e., a predictor, and an optimizer of the estimated cost function that serves as a near-optimal candidate decision, i.e., a prescriptor. As functions of the data, predictors and prescriptors constitute statistical estimators. We propose a meta-optimization problem to find the least conservative predictors and prescriptors subject to constraints on their out-of-sample disappointment. The out-of-sample disappointment quantifies the probability that the actual expected cost of the candidate decision under the unknown true distribution exceeds its predicted cost. Leveraging tools from large deviations theory, we prove that this meta-optimization problem admits a unique solution: The best predictor-prescriptor pair is obtained by solving a distributionally robust optimization problem over all distributions within a given relative entropy distance from the empirical distribution of the data.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study static decision problems under uncertainty, where the decision maker cannot observe the probability distribution of the uncertain problem parameters but has access to a finite number of independent samples from this distribution. Classical stochastic programming uses this data only indirectly. The data serves as the input for a statistical estimation problem that aims to infer the distribution of the uncertain problem parameters. The estimated distribution then serves as an input for an optimization problem that outputs a near-optimal decision as well as an estimate of the expected cost incurred by this decision. Thus, classical stochastic programming separates the decision-making process into an estimation phase and a subsequent optimization phase. The estimation method is typically selected with the goal to achieve maximum prediction accuracy but without tailoring it to the optimization problem at hand.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we develop a method of data-driven stochastic programming that avoids the artificial decoupling of estimation and optimization and that chooses an estimator that adapts to the underlying optimization problem. Specifically, we model data-driven solutions to a stochastic program through a predictor and its corresponding prescriptor. For any fixed feasible decision, the predictor maps the observable data to an estimate of the decision's expected cost. The prescriptor, on the other hand, computes a decision that minimizes the cost estimated by the predictor.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The set of all possible predictors and their induced prescriptors is vast. Indeed, there are countless possibilities to estimate the expected costs of a fixed decision from data, e.g., via the popular sample average approximation, by postulating a parametric model for the exogenous uncertainties and estimating its parameters via maximum likelihood estimation, or through kernel density estimation. Recently, it has become fashionable to construct conservative (pessimistic) estimates of the expected costs via methods of distributionally robust optimization. In this setting, the available data is used to generate an ambiguity set that represents a confidence region in the space of probability distributions and contains the unknown data-generating distribution with high probability. The expected cost of a fixed decision under the unknown true distribution is then estimated by the worst-case expectation over all distributions in the ambiguity set. Since the ambiguity set constitutes a confidence region for the unknown true distribution, the worst-case expectation represents an upper confidence bound on the true expected cost. The ambiguity set can be defined, for example, through confidence intervals for the distribution's moments.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Alternatively, the ambiguity set may contain all distributions that achieve a prescribed level of likelihood, that pass a statistical hypothesis test or that are sufficiently close to a reference distribution with respect to a probability metric such as the Prokhorov metric, the Wasserstein distance, the total variation distance or the $L^{1}$-norm. Ben-Tal et al. have shown that confidence sets for distributions can also be constructed using $\phi$-divergences such as the Pearson divergence, the Burg entropy or the Kullback-Leibler divergence. More recently, Bayraksan and Love provide a systematic classification of $\phi$-divergences and investigate the richness of the corresponding ambiguity sets.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given the numerous possibilities for constructing predictors from a given dataset, it is easy to lose oversight. In practice, predictors are often selected manually from within a small menu with the goal to meet certain statistical and/or computational requirements. However, there are typically many different predictors that exhibit the desired properties, and there always remains some doubt as to whether the chosen predictor is best suited for the particular decision problem at hand. In this paper we propose a principled approach to data-driven stochastic programming by solving a meta-optimization problem over a rich class of predictor-prescriptor-pairs including, among others, all examples reviewed above. This meta-optimization problem aims to find the least conservative (i.e., pointwise smallest) prescriptor whose out-of-sample disappointment decays at a prescribed exponential rate $r$ as the sample size tends to infinity---irrespective of the true data-generating distribution. The out-of-sample disappointment quantifies the probability that the actual expected cost of the prescriptor exceeds its predicted cost.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Put differently, it represents the probability that the predicted cost of a candidate decision is over-optimistic and leads to disappointment in out-of-sample tests. Thus, the proposed meta-optimization problem tries to identify the predictor-prescriptor-pairs that overestimate the expected out-of-sample costs by the least amount possible without risking disappointment under any thinkable data-generating distribution.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main results can be summarized as follows.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

By leveraging Sanov's theorem from large deviations theory, we prove that the meta-optimization problem admits a unique optimal solution for any given stochastic program.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that the optimal data-driven predictor estimates the expected costs under the unknown true distribution by a worst-case expectation over all distributions within a given relative entropy distance from the empirical distribution of the data. This suggests that, among all possible data-driven solutions, a distributionally robust approach based on a relative entropy ambiguity set is optimal. This is perhaps surprising because the meta-optimization problem does not impose any structure on the predictors, which are generic functions of the data. In particular, there is no requirement forcing predictors to admit a distributionally robust interpretation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast to most of the existing work on data-driven distributionally robust optimization, our relative entropy ambiguity set does not play the role of a confidence region that contains the unknown data-generating distribution with a prescribed level of probability (see the discussions of below for exceptions). Instead, the radius of the relative entropy ambiguity set coincides with the desired exponential decay rate $r$ of the out-of-sample disappointment imposed by the meta-optimization problem.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We prove that the optimal (distributionally robust) predictor admits a dual representation as the optimal value of a one-dimensional convex optimization problem that can be solved highly efficiently. For continuously distributed problem parameters this representation seems to be new.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

To our best knowledge, we are the first to recognize the optimality of distributionally robust optimization in its ability to transform data to predictors and prescriptors. The optimal distributionally robust predictor identified in this paper can be evaluated by solving a tractable convex optimization problem. Under standard convexity assumptions about the feasible set and the cost function of the stochastic program, the corresponding optimal prescriptor can also be evaluated in polynomial time. Although perhaps desirable, the tractability and distributionally robust nature of the optimal predictor-prescriptor-pair are not dictated ex ante but emerge naturally.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Relative entropy ambiguity sets have already attracted considerable interest in distributionally robust optimization. Note, however, that the relative entropy constitutes an asymmetric distance measure between two distributions. The asymmetry implies, among others, that the first distribution must be absolutely continuous to the second one but not vice versa. Thus, ambiguity sets can be constructed in two different ways by designating the reference distribution either as the first or as the second argument of the relative entropy. All papers listed above favor the second option, and thus the emerging ambiguity sets contain only distributions that are absolutely continuous to the reference distribution. Maybe surprisingly, the optimal predictor resulting from our meta-optimization problem uses the reference distribution as the first argument of the relative entropy instead. Thus, the reference distribution is absolutely continuous to every distribution in the emerging ambiguity set. Relative entropy balls of this kind have previously been studied by Gupta, Lam and Bertsimas et al..

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Adopting a Bayesian perspective, Gupta determines the smallest ambiguity sets that contain the unknown data-generating distribution with a prescribed level of confidence as the sample size tends to infinity. Both Pearson divergence and relative entropy ambiguity sets with properly scaled radii are optimal in this setting. In the terminology of the present paper, Gupta thus restricts attention to the subclass of distributionally robust predictors and operates with an asymptotic notion of optimality. The meta-optimization problem proposed here entails a stronger notion of optimality, under which the distributionally robust predictor with relative entropy ambiguity set emerges as the unique optimizer. Lam also seeks distributionally robust predictors that trade conservatism for out-of-sample performance. He studies the probability that the estimated expected cost function dominates the actual expected cost function uniformly across all decisions, and he calls a predictor optimal if this probability is asymptotically equal to a prescribed confidence level. Using the empirical likelihood theorem of Owen, he shows that Pearson divergence and relative entropy ambiguity sets with properly scaled radii are optimal in this sense.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

This notion of optimality has again an asymptotic flavor in the sense that it refers to sequences of ambiguity sets that converge to a singleton, and it admits multiple optimizers.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper unfolds as follows. Section 2 provides a formal introduction to data-driven stochastic programming on finite state spaces and develops the meta-optimization problem for identifying the best predictor-prescriptor-pair. Section 3 reviews weak and strong large deviation principles, which are then used in Section 4 to determine the unique optimal solution of the meta-optimization problem. An extension to continuous state spaces is discussed in Section 5.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Data-driven stochastic programming", "weight": 1.0} -->

Stochastic programming is a powerful modeling paradigm for taking informed decisions in an uncertain environment. A generic single-stage stochastic program can be represented as Here, the goal is to minimize the expected value of a cost function ${\gamma{(x,\xi)}} \in \Re$, which depends both on a decision variable $x \in X$ and a random parameter $\xi \in \Xi$ governed by a probability distribution ${\mathbb{P}}^{\star}$. We will assume that the cost $\gamma{(x,\xi)}$ is continuous in $x$ for every fixed $\xi \in \Xi$, the feasible set $X \subseteq \Re^{n}$ is compact, and $\Xi = {\{ 1,\ldots,d\}}$ is finite. Thus, $\xi$ has $d$ distinct scenarios that are represented---without loss of generality---by the integers $1,\ldots,d$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Data-driven stochastic programming", "weight": 1.0} -->

We will relax this requirement in Section 5, where $\Xi$ will be modeled as an arbitrary compact subset of $\Re^{d}$. A wide spectrum of decision problems can be cast as instances of. Shapiro et al. point out, for example, that can be viewed as the first stage of a two-stage stochastic program, where the cost function $\gamma{(x,\xi)}$ embodies the optimal value of a subordinate second-stage problem. Alternatively, problem may also be interpreted as a generic learning problem in the spirit of statistical learning theory.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Data-driven stochastic programming", "weight": 1.0} -->

In the following, we distinguish the prediction problem, which merely aims to predict the expected cost associated with a fixed decision $x$, and the prescription problem, which seeks to identify a decision $x^{\star}$ that minimizes the expected cost across all $x \in X$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Data-driven stochastic programming", "weight": 1.0} -->

Any attempt to solve the prescription problem seems futile unless there is a procedure for solving the corresponding prediction problem. The generic prediction problem is closely related to what Le Maître and Knio call an uncertainty quantification problem and is therefore of prime interest in its own right. Throughout the rest of the paper, we thus analyze prediction and prescription problems on equal footing.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Data-driven stochastic programming", "weight": 1.0} -->

In the what follows we formalize the notion of a data-driven solution to the prescription and prediction problems, respectively. Furthermore, we introduce the basic assumptions as well as the notation used throughout the remainder of the paper.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Data-driven predictors and prescriptors", "weight": 1.0} -->

If the distribution ${\mathbb{P}}^{\star}$ of $\xi$ is unobservable and must be estimated from a training dataset consisting of finitely many independent samples from ${\mathbb{P}}^{\star}$, we lack essential information to evaluate the expected cost of any fixed decision and to solve the stochastic program. The standard approach to overcome this deficiency is to approximate ${\mathbb{P}}^{\star}$ with a parametric or non-parametric estimate $\hat{\mathbb{P}}$ inferred from the samples and to minimize the expected cost under $\hat{\mathbb{P}}$ instead of the true expected cost under ${\mathbb{P}}^{\star}$. However, if we calibrate a stochastic program to a training data set and evaluate its optimal decision on a test data set, then the resulting test performance is often disappointing---even if the two datasets are sampled independently from ${\mathbb{P}}^{\star}$. This phenomenon has been observed in many different contexts.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Data-driven predictors and prescriptors", "weight": 1.0} -->

It is particularly pronounced in finance, where Michaud refers to it as the 'error maximization effect' of portfolio optimization, and in statistics or machine learning, where it is known as 'overfitting'. In decision analysis, Smith and Winkler refer to it as the 'optimizer's curse'. Thus, when working with data instead of exact probability distributions, one should safeguard against solutions that display promising in-sample performance but lead to out-of-sample disappointment.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Data-driven predictors and prescriptors", "weight": 1.0} -->

Any ${\mathbb{P}} \in \mathcal{P}$ encodes a possible probabilistic model for the data process. Thus, by slight abuse of terminology, we will henceforth refer to the distributions ${\mathbb{P}} \in \mathcal{P}$ as models and to $\mathcal{P}$ as the model class. Evidently, the true model ${\mathbb{P}}^{\star}$ is an (albeit unknown) element of $\mathcal{P}$. Next, we introduce model-based predictors and prescriptors corresponding to the stochastic program, where the true unknown distribution ${\mathbb{P}}^{\star}$ is replaced with a hypothetical model ${\mathbb{P}} \in \mathcal{P}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example 2.4 (Sample average predictor)", "weight": 1.0} -->

The model-based predictor $c$ introduced in Definition 2.1 ‣ 2.1 Data-driven predictors and prescriptors ‣ 2 Data-driven stochastic programming") constitutes a simple data-driven predictor $\hat{c} = c$, that is, $c{(x,{\hat{\mathbb{P}}}_{T})}$ can readily be used as a naïve approximation for $c{(x,{\mathbb{P}}^{\star})}$. Note that the model-based predictor $c$ is indeed continuous as desired. By the definition of the empirical estimator, this naïve predictor approximates $c{(x,{\mathbb{P}}^{\star})}$ with which is readily recognized as the popular sample average approximation.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Optimizing over all data-driven predictors and prescriptors", "weight": 1.0} -->

The estimates $\hat{c}{(x,{\hat{\mathbb{P}}}_{T})}$ and $\hat{x}{({\hat{\mathbb{P}}}_{T})}$ inherit the randomness from the empirical estimator ${\hat{\mathbb{P}}}_{T}$, which is constructed from the (random) samples ${\{\xi_{t}\}}_{t = 1}^{T}$. Note that the prediction and prescription problems are naturally interpreted as instances of statistical estimation problems. Indeed, data-driven prediction aims to estimate the expected cost $c{(x,{\mathbb{P}}^{\star})}$ from data.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Optimizing over all data-driven predictors and prescriptors", "weight": 1.0} -->

Standard statistical estimation theory would typically endeavor to find a data-driven predictor $\hat{c}$ that (approximately) minimizes the mean squared error over some appropriately chosen class of predictors $\hat{c}$, where the expectation is taken with respect to the distribution ${({\mathbb{P}}^{\star})}^{\infty}$ governing the sample path and the empirical estimator. The mean squared error penalizes the mismatch between the actual cost $c{(x,{\mathbb{P}}^{\star})}$ and its estimator $\hat{c}{(x,{\hat{\mathbb{P}}}_{T})}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Optimizing over all data-driven predictors and prescriptors", "weight": 1.0} -->

Events in which we are left disappointed (${c{(x,{\mathbb{P}}^{\star})}} > {\hat{c}{(x,{\hat{\mathbb{P}}}_{T})}}$) are not treated differently from positive surprises (${c{(x,{\mathbb{P}}^{\star})}} < {\hat{c}{(x,{\hat{\mathbb{P}}}_{T})}}$). In a decision-making context where the goal is to minimize costs, however, disappointments (underestimated costs) are more harmful than positive surprises (overestimated costs). While statisticians strive for accuracy by minimizing a symmetric estimation error, decision makers endeavor to limit the one-sided prediction disappointment.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 2.6 (Large out-of-sample disappointment)", "weight": 1.0} -->

As the sample size $T$ tends to infinity, the central limit theorem implies that converges in law to a normal distribution with mean $0$ and variance ${\mathbb{E}}_{\mathbb{P}}{\lbrack{({\xi - {{\mathbb{E}}_{\mathbb{P}}{\lbrack\xi\rbrack}}})}^{2}\rbrack}$. Thus, which means that the out-of-sample prediction disappointment remains large for all sample sizes. The sample average predictor hence violates the asymptotic guarantee (3 ‣ 2.2 Optimizing over all data-driven predictors and prescriptors ‣ 2 Data-driven stochastic programming")) and the stronger finite sample guarantee (4 ‣ 2.2 Optimizing over all data-driven predictors and prescriptors ‣ 2 Data-driven stochastic programming")). Note that by adding any positive constant to the sample average predictor, we recover a predictor with exponentially decaying out-of-sample disappointment.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example 2.6 (Large out-of-sample disappointment)", "weight": 1.0} -->

In the following we call a predictor $\hat{c}$ conservative if ${\hat{c}{(x,{\mathbb{P}}')}} > {c{(x,{\mathbb{P}}')}}$ for all decisions $x \in X$ and estimator realizations ${\mathbb{P}}' \in \mathcal{P}$. The above discussion shows that if we require the out-of-sample disappointment to decay asymptotically, we must focus on conservative predictors. Basic results from large deviations theory further ensure that the out-of-sample disappointment of any conservative predictor necessarily decays at an exponential rate.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example 2.6 (Large out-of-sample disappointment)", "weight": 1.0} -->

Specifically, asymptotic guarantees of the type (3 ‣ 2.2 Optimizing over all data-driven predictors and prescriptors ‣ 2 Data-driven stochastic programming")) hold whenever the empirical distribution ${\hat{\mathbb{P}}}_{T}$ satisfies a weak large deviation principle, while finite sample guarantees of the type (4 ‣ 2.2 Optimizing over all data-driven predictors and prescriptors ‣ 2 Data-driven stochastic programming")) hold when ${\hat{\mathbb{P}}}_{T}$ satisfies a strong large deviation principle. As will be shown in Section 3, the empirical distribution does satisfy weak and strong large deviation principles. One predictor that fails to be conservative is the sample average predictor.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Example 2.6 (Large out-of-sample disappointment)", "weight": 1.0} -->

For ease of exposition, we henceforth denote by $\mathcal{C}$ the set of all data-driven predictors, that is, all continuous functions that map $X \times \mathcal{P}$ to the reals. Moreover, we introduce a partial order $\preceq_{\mathcal{C}}$ on $\mathcal{C}$ defined through for any ${{\hat{c}}_{1},{\hat{c}}_{2}} \in \mathcal{C}$. Thus, ${\hat{c}}_{1} \preceq_{\mathcal{C}}{\hat{c}}_{2}$ means that ${\hat{c}}_{1}$ is (weakly) less conservative than ${\hat{c}}_{2}$. The problem of finding the least conservative predictor among all data-driven predictors whose out-of-sample disappointment decays at rate at least $r > 0$ can thus be formalized as the following vector optimization problem.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 2.6 (Large out-of-sample disappointment)", "weight": 1.0} -->

We are now ready to construct a meta-optimization problem akin to, which enables us to identify the best prescriptor. To this end, we henceforth denote by $\mathcal{X}$ the set of all data-driven predictor-prescriptor-pairs $(\hat{c},\hat{x})$, where $\hat{c} \in \mathcal{C}$, and $\hat{x}$ is a prescriptor induced by $\hat{c}$ as per Definition 2.3 ‣ 2.1 Data-driven predictors and prescriptors ‣ 2 Data-driven stochastic programming").

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 2.6 (Large out-of-sample disappointment)", "weight": 1.0} -->

Moreover, we equip $\mathcal{X}$ with a partial order $\preceq_{\mathcal{X}}$, which is defined through Note that ${\hat{c}}_{1} \preceq_{\mathcal{C}}{\hat{c}}_{2}$ actually implies ${({\hat{c}}_{1},{\hat{x}}_{1})} \preceq_{\mathcal{X}}{({\hat{c}}_{2},{\hat{x}}_{2})}$ but not vice versa. The problem of finding the least conservative predictor-prescriptor-pair whose out-of-sample prescription disappointment decays at rate at least $r > 0$ can now be formalized as the following vector optimization problem.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example 2.6 (Large out-of-sample disappointment)", "weight": 1.0} -->

Generic vector optimization problems typically only admit weak solutions. In Section 4 we will show, however, that as well as admit (unique) strong solutions in closed form. In fact, we will show that these closed-form solutions have a natural interpretation as the solutions of convex distributionally robust optimization problems.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 2.7 (Out-of-sample and in-sample performance)", "weight": 1.0} -->

The natural performance measure to quantify the goodness of a data-driven prescriptor $\hat{x}$ is its out-of-sample performance $c{({\hat{x}{({\hat{\mathbb{P}}}_{T})}},{\mathbb{P}}^{\star})}$ under the true model ${\mathbb{P}}^{\star}$. As ${\mathbb{P}}^{\star}$ is unknown, however, the out-of-sample performance cannot be optimized directly. A naïve remedy would be to formulate a meta-optimization problem that minimizes the worst-case (or some average) of the out-of-sample performance of $\hat{x}$ across all models ${\mathbb{P}} \in \mathcal{P}$. The approach proposed here optimizes the out-of-sample performance implicitly.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 2.7 (Out-of-sample and in-sample performance)", "weight": 1.0} -->

Indeed, the meta-optimization problem represents $\hat{x}$ as a minimizer of some predictor $\hat{c}$, where $\hat{c}{({\hat{x}{({\hat{\mathbb{P}}}_{T})}},{\hat{\mathbb{P}}}_{T})}$ should be interpreted as the in-sample performance of $\hat{x}$. Instead of minimizing the out-of-sample performance of $\hat{x}$, problem minimizes the in-sample performance of $\hat{x}$ but ensures through the constraints on the disappointment that the out-of-sample performance is smaller than the in-sample performance with increasingly high confidence as the sample size grows. In this sense, problem minimizes a tight upper bound on the out-of-sample performance of $\hat{x}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Large deviation principles", "weight": 1.0} -->

Large deviations theory provides bounds on the exact exponential rate at which the probabilities of atypical estimator realizations decay under a model $\mathbb{P}$ as the sample size $T$ tends to infinity. These bounds are expressed in terms of the relative entropy of ${\hat{\mathbb{P}}}_{T}$ with respect to $\mathbb{P}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Distributionally robust predictors and prescriptors are optimal", "weight": 1.0} -->

Armed with the fundamental results of large deviations theory, we now endeavor to identify the least conservative data-driven predictors and prescriptors whose out-of-sample disappointment decays at a rate no less than some prescribed threshold $r > 0$ under any model ${\mathbb{P}} \in \mathcal{P}$, that is, we aim to solve the vector optimization problems and.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Distributionally robust predictors", "weight": 1.0} -->

The relative entropy lends itself to constructing a data-driven predictor in the sense of Definition 2.3 ‣ 2.1 Data-driven predictors and prescriptors ‣ 2 Data-driven stochastic programming"). We will show below that this predictor is strongly optimal.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 4.4 (Sample average predictor)", "weight": 1.0} -->

For $r = 0$ the distributionally robust predictor ${\hat{c}}_{r}$ collapses to the sample average predictor of Example 2.4 ‣ 2.1 Data-driven predictors and prescriptors ‣ 2 Data-driven stochastic programming").

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 4.4 (Sample average predictor)", "weight": 1.0} -->

Indeed, because of the strict positivity of the relative entropy ${I{({\mathbb{P}}',{\mathbb{P}})}} > 0$ for ${\mathbb{P}}' \neq {\mathbb{P}}$, see Proposition 3.2 ‣ 3 Large deviation principles")(i), we have that As shown in Example 2.6 ‣ 2.2 Optimizing over all data-driven predictors and prescriptors ‣ 2 Data-driven stochastic programming"), the sample average predictor fails to offer asymptotic or finite sample guarantees of the form (3 ‣ 2.2 Optimizing over all data-driven predictors and prescriptors ‣ 2 Data-driven stochastic programming")) and (4 ‣ 2.2 Optimizing over all data-driven predictors and prescriptors ‣ 2 Data-driven stochastic programming")), respectively.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 4.5 (Alternative distributionally robust predictors)", "weight": 1.0} -->

The relative entropy can also be used to construct a reverse distributionally robust predictor ${\check{c}}_{r} \in \mathcal{C}$ defined through In contrast to ${\hat{c}}_{r}$, the reverse distributionally robust predictor ${\check{c}}_{r}$ fixes the second argument of the relative entropy and maximizes over the first argument. Note that ${\check{c}}_{r}$ can be viewed as the entropic value-at-risk of the uncertain cost $\gamma{(x,\xi)}$; see. Another predictor related to $\hat{c}$ is the restricted distributionally robust predictor ${\overline{c}}_{r} \in \mathcal{C}$ defined through where ${\mathbb{P}} \ll {\mathbb{P}}'$ expresses the requirement that $\mathbb{P}$ must be absolutely continuous with respect to ${\mathbb{P}}'$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 4.5 (Alternative distributionally robust predictors)", "weight": 1.0} -->

The predictors ${\hat{c}}_{r}$ and ${\check{c}}_{r}$ differ because the relative entropy fails to be symmetric. We emphasize that the reverse predictor ${\check{c}}_{r}$ has appeared often in the literature on distributionally robust optimization, see, e.g.,. The predictors ${\hat{c}}_{r}$ and ${\overline{c}}_{r}$ differ, too, because of the additional constraint ${\mathbb{P}} \ll {\mathbb{P}}'$, which is significant when not all outcomes in $\Xi$ have been observed. The statistical properties of the predictor ${\overline{c}}_{r}$ have been analyzed by Lam and more recently by Duchi et al. from the perspective of the empirical likelihood theory introduced by Owen.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 4.5 (Alternative distributionally robust predictors)", "weight": 1.0} -->

The predictor ${\hat{c}}_{r}$ suggested here has not yet been studied extensively even though---as we will demonstrate below---it displays attractive theoretical properties that are not shared by either ${\check{c}}_{r}$ or ${\overline{c}}_{r}$. The difference between ${\hat{c}}_{r}$ and ${\check{c}}_{r}$ or ${\overline{c}}_{r}$ is significant. Indeed, both ${\check{c}}_{r}$ and ${\overline{c}}_{r}$ hedge only against models $\mathbb{P}$ that are absolutely continuous with respect to the (observed realization of the) empirical distribution ${\mathbb{P}}'$. While it is clear that the empirical distribution must be absolutely continuous with respect to the data-generating distribution, however, the converse implication is generally false. Indeed, an outcome can have positive probability even if it does not show up in a given finite time series.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 4.5 (Alternative distributionally robust predictors)", "weight": 1.0} -->

By taking the worst case only over models that are absolutely continuous with respect to ${\mathbb{P}}'$, both predictors ${\check{c}}_{r}$ and ${\overline{c}}_{r}$ potentially ignore many models that could have generated the observed data.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 4.5 (Alternative distributionally robust predictors)", "weight": 1.0} -->

We first establish that ${\hat{c}}_{r}$ indeed belongs to the set $\mathcal{C}$ of all data-driven predictors, that is, the family of continuous functions mapping $X \times \mathcal{P}$ to the reals.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Distributionally robust prescriptors", "weight": 1.0} -->

The distributionally robust predictor ${\hat{c}}_{r}$ of Definition 4.1 ‣ 4.1 Distributionally robust predictors ‣ 4 Distributionally robust predictors and prescriptors are optimal") induces a corresponding prescriptor.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 4.23 (Optimal hypothesis testing)", "weight": 1.0} -->

Bertsimas et al. propose to construct predictors and prescriptors from statistical hypothesis tests. A hypothesis test uses i.i.d. samples $\xi_{1},\ldots,\xi_{T}$ drawn from the unknown true distribution ${\mathbb{P}}^{\star}$ to decide whether the null hypothesis ${\mathbb{P}}^{\star} = {\mathbb{P}}$ is false for a fixed model ${\mathbb{P}} \in \mathcal{P}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 4.23 (Optimal hypothesis testing)", "weight": 1.0} -->

Specifically, the null hypothesis is rejected (it is declared that ${\mathbb{P}}^{\star} \neq {\mathbb{P}}$) if the empirical distribution ${\hat{\mathbb{P}}}_{T}$ associated with the observed sample path falls outside of a (measurable) acceptance region ${A_{T}{({\mathbb{P}})}} \subseteq \mathcal{P}$, which depends on the conjectured model $\mathbb{P}$ and the sample size $T$. Otherwise, it is deemed that there is insufficient data to reject the null hypothesis.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 4.23 (Optimal hypothesis testing)", "weight": 1.0} -->

Bertsimas et al. associate with each hypothesis test a predictor which evaluates the worst-case expected cost across all models ${\mathbb{P}} \in \mathcal{P}$ that pass the hypothesis test in view of the realization ${\mathbb{P}}' \in \mathcal{P}_{T} = {\mathcal{P} \cap {\{ 0,{1/T},\ldots,{{({T - 1})}/T},1\}}^{d}}$ of the empirical distribution ${\hat{\mathbb{P}}}_{T}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 4.23 (Optimal hypothesis testing)", "weight": 1.0} -->

The quality of a hypothesis test is usually measured by its type I error ${\mathbb{P}}^{\infty}{({{\hat{\mathbb{P}}}_{T} \notin {A_{T}{({\mathbb{P}})}}})}$, that is, the probability of falsely rejecting the null hypothesis, as well as its type II error ${\mathbb{Q}}^{\infty}{({{\hat{\mathbb{P}}}_{T} \in {A_{T}{({\mathbb{P}})}}})}$, that is, the probability of falsely accepting the null hypothesis if the data follows a distribution ${\mathbb{Q}} \neq {\mathbb{P}}$. A particularly popular test is the likelihood ratio test, which uses the acceptance region Zeitouni et al. prove that the likelihood ratio test is optimal in the following sense.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 4.23 (Optimal hypothesis testing)", "weight": 1.0} -->

The acceptance region of the likelihood ratio test thus simplifies to where the equality holds because ${\inf_{{\mathbb{Q}} \neq {\mathbb{P}}}{I{({\mathbb{P}}',{\mathbb{Q}})}}} = 0$. Hence, the distributionally robust predictor ${\hat{c}}_{r}$ that is strongly optimal in the meta-optimization problem coincides with the hypothesis test-based predictor (22 ‣ Proof 4.18 ‣ 4.2 Distributionally robust prescriptors ‣ 4 Distributionally robust predictors and prescriptors are optimal")) corresponding to the likelihood ratio test.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Extension to continuous state spaces", "weight": 1.0} -->

Assume now that the realizations of the random parameter $\xi$ may range over an arbitrary compact set $\Xi \subseteq \Re^{d}$ that is not necessarily finite. In analogy to the discrete case, we denote by $\mathcal{P}$ the family of all Borel probability distributions supported on $\Xi$. Note that $\mathcal{P}$ is now a convex subset of an infinite-dimensional space, which significantly complicates the problem of finding optimal predictors and prescriptors. We equip $\mathcal{P}$ with the standard topology of weak convergence of distributions, recalling that the weak topology is metrized by the Prokhorov metric. Consequently, we equip $X \times \mathcal{P}$ with the product of the standard Euclidean topology on $X$ and the weak topology on $\mathcal{P}$. In the remainder of this section we analyze to what extent---and under what additional conditions---the results for finite state spaces carry over to the more general continuous case. As this analysis requires more subtle mathematical techniques, we relegate all proofs to Appendix 6.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Extension to continuous state spaces", "weight": 1.0} -->

We first note that the definitions of model-based predictors and prescriptors require no changes. In order to evaluate the expectation in the definition of the model-based predictor ${c{(x,{\mathbb{P}})}} = {\int_{\Xi}{\gamma{(x,\xi)}{d{\mathbb{P}}}{(\xi)}}}$, however, we now need to evaluate an integral with respect to $\mathbb{P}$ instead of a finite sum. Throughout this section we assume that the cost function $\gamma{(x,\xi)}$ is jointly continuous in $x$ and $\xi$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Case 2b", "weight": 1.0} -->

Assume now that ${{\mathbb{P}}_{0}{({\Xi^{\star}{(x)}})}} = 0$. In this case we can prove as in Case 2a. The only differences are that $\mathbb{U}$ may now be any distribution on $\Xi^{\star}{(x)}$ and that the continuity of $I{({\mathbb{P}}_{0}',{{\mathbb{P}}{(\lambda)}})}$ in $\lambda \in {\lbrack 0,1)}$ can now be shown more directly by noting that All other arguments remain unaffected.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Case 2b", "weight": 1.0} -->

Now that the implication has been established, we demonstrate that the probability of the event ${\hat{\mathbb{P}}}_{T} \in {\mathcal{D}{(x,{\mathbb{P}}_{0})}}$ decays at a rate of at least $r$. To this end, we first note that the weak disappointment set $\overline{\mathcal{D}}{(x,{\mathbb{P}}_{0})}$ includes the strict disappointment set $\mathcal{D}{(x,{\mathbb{P}}_{0})}$ and is closed because of the continuity of ${\hat{c}}_{r}$ established in Proposition 5.4 ‣ 5 Extension to continuous state spaces").

<!-- chunk {"id": "body-0060", "role": "body", "section": "Case 2b", "weight": 1.0} -->

The weak LDP upper bound (24a ‣ 5 Extension to continuous state spaces")) then implies that where the second inequality holds because $\overline{\mathcal{D}}{(x,{\mathbb{P}}_{0})}$ is closed and contains $\mathcal{D}{(x,{\mathbb{P}}_{0})}$, while the third inequality follows. Thus, the probability of the event ${\hat{\mathbb{P}}}_{T} \in {\mathcal{D}{(x,{\mathbb{P}}_{0})}}$ decays indeed at a rate of at least $r$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Case 2b", "weight": 1.0} -->

As the choice of $x \in X$ and ${\mathbb{P}}_{0} \in \mathcal{P}$ was arbitrary, and as Cases 1 and 2 are exhaustive, ${\hat{c}}_{r}$ is feasible.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Case 2b", "weight": 1.0} -->

In order to show that ${\hat{c}}_{r}$ is strongly optimal in when $\epsilon > 0$, we can repeat the proof of Theorem 4.10 ‣ 4.1 Distributionally robust predictors ‣ 4 Distributionally robust predictors and prescriptors are optimal") almost verbatim with obvious minor modifications (most notably, there is no need to construct ${\mathbb{P}}_{2}$). $\square$
