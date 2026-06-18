<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Efficient Shapley Performance Attribution for Least-Squares Regression

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the performance of a least-squares regression model, as judged by out-of-sample R^. Shapley values give a fair attribution of the performance of a model to its input features, taking into account interdependencies between features. Evaluating the Shapley values exactly requires solving a number of regression problems that is exponential in the number of features, so a Monte Carlo-type approximation is typically used. We focus on the special case of least-squares regression models, where several tricks can be used to compute and evaluate regression models efficiently. These tricks give a substantial speed up, allowing many more Monte Carlo samples to be evaluated, achieving better accuracy. We refer to our method as least-squares Shapley performance attribution (LS-SPA), and describe our open-source implementation.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider classic least-squares regression, with $p$ features, judged by an out-of-sample $R^{2}$ metric. A natural question is how much each of the $p$ features contributes to our $R^{2}$ metric; roughly speaking, how valuable is each feature to our least-squares predictor? Except for a special case described below in §2.4, this question seems difficult to answer, since the value of a feature depends on the other features.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our interest is in attributing the *overall performance* of a least-squares model to the features. A related task is attributing a *specific prediction* of a least-squares model to the features, which is a popular method for so-called explainable AI called SHAP, an acronym for Shapley additive explanations. That is a very different task, discussed in more detail below. In this paper, we consider only performance attribution, and not explaining a specific prediction from a model. We refer to this task as Shapley performance attribution to features.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This performance attribution problem was essentially solved in Lloyd Shapley's 1953 paper "A Value for $n$-person Games". He proposed a method to allocate the payoff in a cooperative game to the players, which came to be known as the Shapley values. The Shapley values provide a fair distribution of the total payoff in a game, taking into account the contributions of each player to the coalition. The Shapley values are provably the only attribution for which fairness, monotonicity, and full attribution (three key desiderata for attribution) all hold. We refer the reader to other papers for more discussion and justification of Shapley values for attributing regression model performance to its features.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We focus on efficiently computing (an approximation of) the Shapley values for least-squares regression problems, i.e., to attribute the overall $R^{2}$ to the $p$ features. We seek a number $S_{j}$ associated with feature $j$, where we interpret $S_{j}$ as the portion of the achieved $R^{2}$ metric that is attributed to feature $j$. Full attribution means ${\sum_{j = 1}^{p}S_{j}} = R^{2}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Shapley values rely on solving and evaluating around $2^{p}$ least-squares problems. This is impractical for $p$ larger than around 10, so Monte Carlo approximation is typically used to compute an approximation to the Shapley values. We propose a simple but effective quasi-Monte Carlo method that in practice gives better approximations of the Shapley values than Monte Carlo for the same number of least-square regression problems.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We do not introduce any new mathematical or computational methods. Instead, we collect well-known ideas and assemble them into an efficient method for computing the Shapley values for a least-squares regression problem, exploiting special properties of least-squares problems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Cooperative game theory", "weight": 1.0} -->

The Shapley value originated in cooperative game theory as a means of fairly splitting a coalition's reward between the individual players. The notion of a fair split is defined by four axioms, which Shapley proved resulted in a unique method for attribution. Since Shapley's seminal paper, numerous extensions, variations, and generalizations have been developed; see, for instance, \[ K0́7\].

<!-- chunk {"id": "body-0010", "role": "body", "section": "Cooperative game theory", "weight": 1.0} -->

Computing the Shapley value in general has a cost that increases exponentially in the number of players. Nonetheless, many games have structure that enables efficient exact computation of the Shapley values. Examples include weighted hypergraph games with fixed coalition sizes, determining airport landing costs, weighted voting games restricted by trees \[FAB^+^02\], cost allocation problems framed as extended tree games, sequencing games, games represented as marginal contribution networks, and determining certain notions of graph centrality \[MAS^+^13\]. On the other hand, computing the Shapley value in weighted majority games is #P-complete, as are elementary games, i.e., games whose value function is an indicator on a coalition.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Approximating Shapley values", "weight": 1.0} -->

Due to the computational complexity of computing exact Shapley values in general, various methods have been proposed for efficiently approximating Shapley values. Shapley initially described a Monte Carlo method for approximating Shapley values by sampling coalitions in 1960. Subsequent works have considered sampling permutations using simple Monte Carlo methods or with methods that ensure that each player appears in each position of a sampled permutation more uniformly \[vCHHL17, \].

<!-- chunk {"id": "body-0012", "role": "body", "section": "Approximating Shapley values", "weight": 1.0} -->

Beyond Monte Carlo approaches, other works have explored numerical integration schemes for approximating the Shapley values. The paper describes a multilinear extension of the characteristic function of an $n$-person game that allows for the computation of the Shapley value as a contour integral. This method has been further explored and.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Applications of Shapley values", "weight": 1.0} -->

Although they arose in the context of game theory, Shapley values have been applied across a variety of fields. In finance, Shapley values have been applied to attribute the performance of a portfolio to constituent assets and to allocate insurance risk. Elsewhere, Shapley values have been used to identify key individuals in social networks \[MRS^+^13, vCHHL17\], to identify which components of a user interface draw the most user engagement, to distribute rewards in multi-agent reinforcement learning, and to attribute the performance of a machine learning model to the individual training data points. We refer to and for a deeper review of applications of the Shapley value.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Explainable ML", "weight": 1.0} -->

Shapley attribution has recently found extensive use in machine learning in the context of model interpretability, in Shapley additive explanation (SHAP). SHAP uses approximate Shapley values to attribute a single prediction of a machine learning model across the input features. Although SHAP and Shapley performance attribution both involve prediction models and both use Shapley values, they otherwise have little relation. We refer to and for a more thorough review of SHAP.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Shapley values for statistics", "weight": 1.0} -->

In statistical learning, researchers often seek to assign a relative importance score to the features of a model. One approach is Shapley attribution. This method has been independently rediscovered numerous times and called numerous names \[ Grö06, Grö15\]. All of these works utilize Shapley attribution to decompose the $R^{2}$ of a regression model, though often without reference to Shapley. The paper decomposes the $R^{2}$ using a method similar to Shapley attribution but with different weights, and decomposes any goodness-of-fit metric of a regression model using a method shown to be equivalent to Shapley attribution.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Feature importance", "weight": 1.0} -->

While not directly related to the computation of Shapley values, the application of Shapley values to feature importance is a primary motivation behind their calculation in many contexts \[, MRS^+^13, vCHHL17\]. In statistics, the use of Shapley values for determining feature importance has been significantly explored, and papers further argue why the Shapley attribution is a particularly appropriate method for evaluating feature importance.

<!-- chunk {"id": "body-0017", "role": "body", "section": "This paper", "weight": 1.0} -->

We introduce an efficient method for (approximately) computing Shapley attribution of performance in least-squares regression problems, called least-squares Shapley performance attribution (LS-SPA). LS-SPA uses several computational tricks that exploit special properties of least-squares problems. The first is a reduction of the original train and test data to a compressed form in which the train and test data matrices are square. The second is to solve a set of $p$ least-squares problems, obtained as we add features one by one, with one QR factorization, in a time comparable to solving one least-squares problem. Finally, we propose using a quasi-Monte Carlo method, a variation of Monte Carlo sampling, to efficiently approximate the Shapley values. (This trick does not depend on any special properties of least-squares problems.)

<!-- chunk {"id": "body-0018", "role": "body", "section": "Outline", "weight": 1.0} -->

In §2 we present a mathematical overview of least-squares and Shapley values, setting our notation. We describe our method for efficiently estimating Shapley values for least-squares problems in §3. In §4, we describe some extensions and variations on our algorithm, and we conclude with numerical experiments in §5.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Least-squares Shapley performance values", "weight": 1.0} -->

In this section, we review the least-squares regression problem, set our notation, and define the Shapley values for the features.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Least-squares", "weight": 1.0} -->

We consider the least-squares regression problem

<!-- chunk {"id": "body-0021", "role": "body", "section": "Least-squares", "weight": 1.0} -->

with variable $\theta \in \text{R}^{p}$, the model parameter. Here $X \in \text{R}^{N \times p}$ is a given data or feature matrix and $y \in \text{R}^{N}$ is a given vector of responses or labels. The rows of $X$, denoted $x_{i}^{T}$ with $x_{i} \in \text{R}^{p}$, correspond to $N$ samples or observations, and each column of $X$ corresponds to a feature. We will assume that $X$ has rank $p$, which implies $N \geq p$, i.e., $X$ is square or tall. We denote the solution of the least-squares problem as

<!-- chunk {"id": "body-0022", "role": "body", "section": "Least-squares", "weight": 1.0} -->

The data $X$ and $y$ are the training data since they are used to find the model parameter $\theta^{\star}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Least-squares", "weight": 1.0} -->

While not technically needed, we will assume that the columns of $X$ and the vector $y$ are de-meaned, and our model does not have an intercept.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Out-of-sample $R^{2}$ metric", "weight": 1.0} -->

We evaluate the performance of a model parameter $\theta$ via out-of-sample validation. We have a second (test) data set of $M$ observations $X^{tst} \in \text{R}^{M \times p}$ and $y^{tst} \in \text{R}^{M}$, and evaluate the model on these data to obtain ${\hat{y}}^{tst} = {X^{tst}\theta}$. We assume that columns of $X^{tst}$ are demeaned according to the column means of $X$ and $y^{tst}$ is demeaned according to the mean of $y$. The prediction errors on the test set are given by ${\hat{y}}^{tst} - y^{tst}$. To evaluate the least-squares model with parameter $\theta$, we use the $R^{2}$ metric

<!-- chunk {"id": "body-0025", "role": "body", "section": "Out-of-sample $R^{2}$ metric", "weight": 1.0} -->

which is the fractional reduction in mean square test error compared to the baseline prediction $\hat{y} = 0$. Larger values of $R^{2}$ are better. It is at most one and can be negative.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Feature subsets", "weight": 1.0} -->

In later sections, we will be interested in the $R^{2}$ metric obtained with the least-squares model using only a subset $\mathcal{S} \subseteq {\{ 1,\ldots,p\}}$ of the features, i.e., using a parameter vector $\theta$ that satisfies $\theta_{j} = 0$ for $j \notin \mathcal{S}$. The associated least-squares problem is

<!-- chunk {"id": "body-0027", "role": "body", "section": "Feature subsets", "weight": 1.0} -->

We denote the associated parameter as $\theta_{\mathcal{S}}^{\star}$. From this we can find the $R^{2}$ metric, denoted $R_{\mathcal{S}}^{2}$, using. We use $R^{2}$ to denote the metric obtained using all features, i.e., $R_{\{ 1,\ldots,p\}}^{2}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Feature chains", "weight": 1.0} -->

A *feature chain* is an increasing sequence of $p$ subsets of features obtained by adding one feature at a time,

<!-- chunk {"id": "body-0029", "role": "body", "section": "Feature chains", "weight": 1.0} -->

Roughly speaking, $\pi$ gives the order in which we add features in the feature chain. We will set $\mathcal{S}_{0} = \varnothing$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Lifts associated with a feature chain", "weight": 1.0} -->

Consider feature $j$. It is the $l$th feature to be added in the feature chain given by $\pi$, where $l = {\pi^{- 1}{(j)}}$. We define the *lift* associated with feature $j$ in chain $\pi$ as

<!-- chunk {"id": "body-0031", "role": "body", "section": "Lifts associated with a feature chain", "weight": 1.0} -->

Roughly speaking, $L{(\pi)}_{j}$ is the increase in $R^{2}$ obtained when we add feature $j$ to the ones before it in the ordering $\pi$, i.e., features $\pi_{1},\ldots,\pi_{l - 1}$. The lift $L_{(}\pi)_{j}$ can be negative, which means that adding feature $j$ to the ones that come before it reduces the $R^{2}$ metric.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Lifts associated with a feature chain", "weight": 1.0} -->

We refer to the vector ${L{(\pi)}} \in \text{R}^{p}$ as the lift vector associated with the feature chain given by $\pi$. We observe that

<!-- chunk {"id": "body-0033", "role": "body", "section": "Lifts associated with a feature chain", "weight": 1.0} -->

the $R^{2}$ metric obtained using all features. The vector $L{(\pi)}$ gives an attribution of the values of each feature to the final $R^{2}$ obtained, assuming the features are added in the order $\pi$. In general, it depends on $\pi$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Shapley attributions", "weight": 1.0} -->

The vector of Shapley attributions for the features, denoted $S \in \text{R}^{p}$, is given by

<!-- chunk {"id": "body-0035", "role": "body", "section": "Shapley attributions", "weight": 1.0} -->

where $\mathcal{P}$ is the set of all $p!$ permutations of $\{ 1,\ldots,p\}$. We interpret $S_{j}$ as the average lift, or increase in $R^{2}$, obtained when adding feature $j$, over all feature chains. The average is over all feature chains, i.e., orderings of the features. In Appendix 2.5, we present a simple example of a Shapley attribution for a least-squares model with a small number of features.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Shapley attributions", "weight": 1.0} -->

For $p$ more than 10 or so, it is impractical to evaluate the lift vector for all $p!$ permutations. Instead, we estimate it as

<!-- chunk {"id": "body-0037", "role": "body", "section": "Shapley attributions", "weight": 1.0} -->

where $\Pi \subset \mathcal{P}$ is a subset of permutations with ${|\Pi|} = K \ll {p!}$. This is a Monte Carlo approximation of when $\Pi$ is a subset of permutations chosen uniformly at random from $\mathcal{S}$ with replacement. (We will describe a better choice in §3.5.)

<!-- chunk {"id": "body-0038", "role": "body", "section": "Uncorrelated features", "weight": 1.0} -->

We mention here one case in which the Shapley performance attribution for least-squares regression is easily found: When the empirical covariance of the features on both the train and test sets are diagonal, i.e.,

<!-- chunk {"id": "body-0039", "role": "body", "section": "Uncorrelated features", "weight": 1.0} -->

with $\Lambda$ and $\overset{\sim}{\Lambda}$ diagonal. In this case, we have $\theta_{j}^{\star} = {\Lambda_{jj}^{- 1}{({X^{T}y})}_{j}}$, for any subset $\mathcal{S}$ that contains $j$. The test error is also additive, i.e., the sum of contributions from each feature. It follows that the lift vectors do not depend on $\pi$, so $S = {L{(\pi)}}$ for any $\pi$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Uncorrelated features", "weight": 1.0} -->

When these assumptions almost hold, i.e., the features are not too correlated on the train and test sets, the method we propose exhibits very fast convergence.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Toy example", "weight": 1.0} -->

To illustrate the ideas above we present a simple example. We use a synthetic dataset with $p = 3$ features, $N = 50$ training examples, and $M = 50$ test examples. We generate feature matrices $X$ and $X^{\text{tst}}$ by taking, respectively, $N$ and $M$ independent samples from a multivariate normal distribution with mean zero and covariance

<!-- chunk {"id": "body-0042", "role": "body", "section": "Toy example", "weight": 1.0} -->

Table 1 shows the out-of-sample $R^{2}$ for each of the $8$ subsets of features. Table 2 shows the lift associated with each of $6$ feature orderings. We display the same data as a lattice in figure 1. In this figure, vertices are labeled with subsets of the features and subscripted with the associated $R^{2}$. The edges, oriented to point to the subset to which one feature was added, are labeled with the lift for adding that feature to the subset. Every path from $\varnothing$ to $\{ 1,2,3\}$ corresponds to an ordering of the features, with the lifts along the path giving the associated lift vector.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Toy example", "weight": 1.0} -->

The $R^{2}$ using all features is $0.92$, and the Shapley values are

<!-- chunk {"id": "body-0044", "role": "body", "section": "Toy example", "weight": 1.0} -->

Roughly speaking, most of our performance comes from feature 1, followed closely by feature 2, with feature 3 negatively affecting performance. Indeed, we can see that the performance using only features 1 and 2 is the same (to two decimal places) as the performance using all three.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Efficient computation", "weight": 1.0} -->

In this section, we explain LS-SPA, our method for efficiently computing $\hat{S}$, an approximation of $S$. The method can be broken into two parts. The first is a method to efficiently compute $L{(\pi)}$, the lift associated with a specific feature ordering $\pi$. The second is a method for choosing the set of permutations $\Pi$ that gives a better approximation than basic Monte Carlo sampling.

<!-- chunk {"id": "body-0046", "role": "body", "section": "The naïve method", "weight": 1.0} -->

The naïve method for computing $\hat{S}$ is to solve a chain of $p$ least-squares problems $K$ times, and evaluate them on a test set. Solving a least-squares problem with $k$ (nonzero) coefficients has a cost $O{({Nk^{2}})}$ flops. (It can be done, for example, via the QR factorization.) Evaluating its performance costs $O{({Mk})}$. Assuming $M$ is no more than $Nk$ in order, this second term is negligible. Summing $O{({Nk^{2}})}$ from $k = 1$ to $p$ gives $O{({Np^{3}})}$. This is done for $K$ permutations so the naïve method requires

<!-- chunk {"id": "body-0047", "role": "body", "section": "The naïve method", "weight": 1.0} -->

flops. This naïve method can be parallelized: All of the least-squares problems can be solved in parallel.

<!-- chunk {"id": "body-0048", "role": "body", "section": "The naïve method", "weight": 1.0} -->

We will describe a method to carry out this computation far more efficiently. The computation tricks we describe below are all individually well known; we are merely assembling them into an efficient method.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Initial reduction of training and test data sets", "weight": 1.0} -->

We can carry out an initial reduction of the original train and test data matrices, so each has $p$ rows instead of $N$ and $M$ respectively. Let $X = {QR}$ denote the QR factorization of $X$, with $Q \in \text{R}^{N \times p}$ and $R \in \text{R}^{p \times p}$. Simple algebra shows that

<!-- chunk {"id": "body-0050", "role": "body", "section": "Initial reduction of training and test data sets", "weight": 1.0} -->

Computing the least-squares solutions for a chain now costs $O{(p^{4})}$, whereas in the naïve method, the cost was $O{({Np^{3}})}$ per chain. The cost of computing least-squares solutions for $K$ chains is then

<!-- chunk {"id": "body-0051", "role": "body", "section": "Initial reduction of training and test data sets", "weight": 1.0} -->

compared to $O{({KNp^{3}})}$ for the naïve method. When $N$ or $K$ is large (which is typical), the cost savings is substantial.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Initial reduction of training and test data sets", "weight": 1.0} -->

The same trick can be used to efficiently evaluate the $R^{2}$ metrics. We carry out one QR factorization of the test matrix at a cost of $O{({Mp^{2}})}$, after which we can evaluate the metric with $O{({pk})}$ flops, where $k = {|\mathcal{S}|}$. To evaluate the metrics for a chain is then $O{(p^{2})}$ flops, compared to $O{({Mp})}$ for the naïve method. To compute $\hat{S}$ for $K$ chains has cost

<!-- chunk {"id": "body-0053", "role": "body", "section": "Initial reduction of training and test data sets", "weight": 1.0} -->

which is negligible compared to the cost of solving the least-squares problems.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Initial reduction of training and test data sets", "weight": 1.0} -->

Using this initial reduction trick, we obtain a complexity of $O{({{Np^{2}} + {Kp^{4}}})}$, compared to $O{({KNp^{3}})}$ for the naïve method. This simple trick has been known since at least the 1960s.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Efficiently computing lift vectors", "weight": 1.0} -->

In this section, we show how the cost of computing regression models and evaluating them for one chain can be reduced from $O{(p^{4})}$ to $O{(p^{3})}$, using a well-known property of the QR factorization.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Efficiently computing lift vectors", "weight": 1.0} -->

To evaluate a chain defined by $\pi$, we can permute the features to the standard ordering, and then permute back once we have evaluated the $R^{2}$ values. So without loss of generality, we can consider the case $\pi = {(1,2,\ldots,p)}$. Our task is to compute least-squares parameters $\theta_{j}^{\star}$, $j = {1,\ldots,p}$, where $\theta_{j}^{\star} = 0$ for $j > k$. We collect these parameter vectors into one $p \times p$ upper triangular matrix $\Theta^{\star}$, with columns $\theta_{1}^{\star},\ldots,\theta_{p}^{\star}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Efficiently computing lift vectors", "weight": 1.0} -->

Let $\overset{\sim}{X} \in \text{R}^{p \times p}$ be the reduced data matrix with its columns permuted, and $\overset{\sim}{y} = {Q^{T}y}$ the reduced righthand side, so our problem is to find $\Theta^{\star}$, the solution of the matrix least-squares problem

<!-- chunk {"id": "body-0058", "role": "body", "section": "Efficiently computing lift vectors", "weight": 1.0} -->

with variable $\Theta \in \text{R}^{p \times p}$. Here $\parallel \cdot \parallel_{F}^{2}$ is the Frobenius norm squared, i.e., the sum of the entries. The matrix $\overset{\sim}{Y}$ is given by $\overset{\sim}{Y} = {\overset{\sim}{y}\mathbf{1}^{T}}$, where $\mathbf{1}$ is the vector with all entries one, i.e., $\overset{\sim}{Y}$ is the matrix with all columns $\overset{\sim}{y}$. (The $p$ different least-squares problems are uncoupled, but it is convenient to represent them as one matrix least-squares problem.)

<!-- chunk {"id": "body-0059", "role": "body", "section": "Efficiently computing lift vectors", "weight": 1.0} -->

Let ${\overset{\sim}{Q}\overset{\sim}{R}} = \overset{\sim}{X}$ denote the QR decomposition of $\overset{\sim}{X}$. Substituting $\overset{\sim}{Q}\overset{\sim}{R}$ for $\overset{\sim}{X}$ above, and multiplying the argument of the Frobenius norm the orthogonal matrix ${\overset{\sim}{Q}}^{T}$, the problem above can be written as

<!-- chunk {"id": "body-0060", "role": "body", "section": "Efficiently computing lift vectors", "weight": 1.0} -->

with variable $\Theta \in \text{R}^{p \times p}$. The solution has the simple form

<!-- chunk {"id": "body-0061", "role": "body", "section": "Efficiently computing lift vectors", "weight": 1.0} -->

where ${\mathbf{t}\mathbf{r}\mathbf{i}\mathbf{u}}{( \cdot )}$ gives the upper triangular part of its argument, i.e., sets the strictly lower triangular entries to zero. Note that the righthand side is upper triangular since upper triangularity is preserved under inversion and matrix multiplication. This result is equivalent to application of the Frish--Waugh--Lovell theorem from econometrics and is also well known in statistics.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Complexity", "weight": 1.0} -->

Computing the QR factorization of $\overset{\sim}{X}$ costs $O{(p^{3})}$. We can form ${{\overset{\sim}{Q}}^{T}\overset{\sim}{Y}} = {{\overset{\sim}{Q}}^{T}\overset{\sim}{y}\mathbf{1}}$ in $O{(p^{2})}$, which is negligible. We can compute $\Theta^{\star}$ using in $O{(p^{3})}$ flops. In other words: We can find the parameter vectors for a whole chain in $O{(p^{3})}$, the same cost as solving a single least-squares problem with $p$ variables and $p$ equations. We evidently save a factor of $p$, compared to the naïve method of solving $p$ least-squares problems, which has cost $O{(p^{4})}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Complexity", "weight": 1.0} -->

It is easily verified that the cost of evaluating the $p$ least-squares parameters on the test data is also $O{(p^{3})}$, so the cost of evaluating the lifts for the chain is $O{(p^{3})}$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Summary", "weight": 1.0} -->

which can be compared to the complexity of the naïve method, $O{({KNp^{3}})}$. The speedup over the naïve method is at least the minimum of $N$ and $Kp$, neither of which is typically small. We note that LS-SPA can also be parallelized, by computing the lifts for each $\pi \in \Pi$ in parallel.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Quasi-Monte Carlo approximation", "weight": 1.0} -->

Here we explain an improvement over the simple Monte Carlo method. (This improvement has nothing to do with the problems being least-squares and is applicable in other cases.) We will use quasi-Monte Carlo (QMC) sampling instead of randomly sampling permutations to obtain $\Pi$. One proposed method (which we call *permutohedron QMC*) is given. It maps a Sobol' sequence in ${\lbrack 0,1\rbrack}^{p - 2}$ onto the permutohedron for $p$-element permutations by mapping to the $({p - 1})$-sphere, then embedding the $({p - 1})$-sphere into $\text{R}^{p}$ via an area-preserving transform and rounding points to the nearest permutohedron vertex.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Quasi-Monte Carlo approximation", "weight": 1.0} -->

We propose another method (which we call *argsort QMC*), which is to take a Sobol' sequence on ${\lbrack 0,1\rbrack}^{p} \subset \text{R}^{p}$, and choose the permutations as the argsort (permutation that gives the sorted ordering) of each point in the sequence. We have found empirically that this method does as well or better than permutohedron sampling for this problem, and is computationally simpler.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Error", "weight": 1.0} -->

We define the error in the estimate of the $j$th Shapley attribution to be

<!-- chunk {"id": "body-0068", "role": "body", "section": "Error", "weight": 1.0} -->

where $S \in \text{R}^{p}$ is the true vector of Shapley attributions and $\hat{S} \in \text{R}^{p}$ is the estimated vector of Shapley attributions as described in §2.3. We also define the overall error in the Shapley estimate to be

<!-- chunk {"id": "body-0069", "role": "body", "section": "Risk estimation", "weight": 1.0} -->

If a permutation $\pi$ is sampled from the uniform distribution on $\mathcal{P}$, then the expected value of $L{(\pi)}$ is $S$. Let $\Sigma$ denote the covariance of $L{(\pi)}$. The central limit theorem guarantees that $\sqrt{K}{({\hat{S} - S})}$ converges in distribution to $\mathcal{N}{(0,\Sigma)}$ as $K\rightarrow\infty$. We can thus estimate the $q$th quantile values of and over the distribution of $\hat{S}$ for $K$ samples via Monte Carlo.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Risk estimation", "weight": 1.0} -->

and the estimated overall error as

<!-- chunk {"id": "body-0071", "role": "body", "section": "Batching", "weight": 1.0} -->

We can efficiently compute a batched version of the risk estimate on the fly for use as a stopping criterion. For any subset $\Pi$ of permutations, define the sample mean

<!-- chunk {"id": "body-0072", "role": "body", "section": "Batching", "weight": 1.0} -->

and the biased sample covariance

<!-- chunk {"id": "body-0073", "role": "body", "section": "Batching", "weight": 1.0} -->

We set a batch size $B$, a maximum number of batches $K/B$, and a risk tolerance $\epsilon > 0$. Instead of computing $\Pi$, $\hat{S}$, and the risk estimate all at once, we compute them iteratively via batches $\Pi^{},\ldots,\Pi^{({K/B})}$, each of size $B$. Initialize the estimated Shapley values ${\hat{S}}^{} = 0$ and the estimated biased sample covariance ${\hat{\Sigma}}_{b}^{} = 0$. In iteration $j$, we can compute ${\hat{S}}^{(j)}$ using the update rule

<!-- chunk {"id": "body-0074", "role": "body", "section": "Batching", "weight": 1.0} -->

which holds since $\Pi^{},\ldots,\Pi^{({K/B})}$ are equally sized. We can also compute ${\hat{\Sigma}}_{b}^{(j)}$ using the update rule provided,

<!-- chunk {"id": "body-0075", "role": "body", "section": "Batching", "weight": 1.0} -->

Note that batching in this manner can result in terminating early when $\hat{S}$ is computed on a number of permutations that is not a power of $2$. This can destroy the balance properties expected of QMC, but in practice, we have found this does not matter.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Batching", "weight": 1.0} -->

The central limit theorem is based on random samples, which is not the case for QMC methods. As a result, risk estimates when $\hat{S}$ is computed via a QMC method to sample permutations do not come with the theoretical guarantees that random samples have. We have observed empirically that estimates using QMC are still good estimates of the actual errors.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Algorithm summary", "weight": 1.0} -->

Algorithm 3.1 Least-squares Shapley attribution (LS-SPA)

<!-- chunk {"id": "body-0078", "role": "body", "section": "Algorithm summary", "weight": 1.0} -->

We note that the Cholesky reduction described in §4.4 may be used instead of the QR reduction described in §3.2 step 1. Furthermore, as described in §3.6, the algorithm may be performed in batches, allowing for early termination via a stopping criterion based on the overall error estimate $\hat{\sigma}$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Implementation", "weight": 1.0} -->

We have written two Python implementations of algorithm 3.7. The computational results we present in §5 are derived from a JAX-based \[BFH^+^23\] implementation of algorithm 3.7 and some of the extensions discussed in §4. The JAX implementation, along with our numerical experiments, is available at

<!-- chunk {"id": "body-0080", "role": "body", "section": "Implementation", "weight": 1.0} -->

We also provide a more user-friendly, NumPy-based \[HMvdW^+^20\] library implementing algorithm 3.7 at

<!-- chunk {"id": "body-0081", "role": "body", "section": "Extensions and variations", "weight": 1.0} -->

In this section, we describe some extensions to the basic problem and method described above.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Cross validation metric", "weight": 1.0} -->

In the discussion above we used simple out-of-sample validation, but we can also use other more sophisticated validation methods, such as $M$-fold cross validation \[, Ch. 17\]. Here the original data are split into $M$ different 'folds'. For $m = {1,\ldots,M}$ we fit a model using as training data all folds except $m$ and validate it on fold $m$. We use the average validation mean-square error to obtain the $R^{2}$ score. The methods above apply immediately to this situation.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Ridge regularization", "weight": 1.0} -->

In ridge regression, we choose the parameter $\theta$ by solving the $\ell_{2}$-regularized least-squares problem

<!-- chunk {"id": "body-0084", "role": "body", "section": "Ridge regularization", "weight": 1.0} -->

where $\theta \in \text{R}^{p}$ is the optimization variable, $X \in \text{R}^{N \times p}$ and $y \in \text{R}^{N}$ are data, and $\lambda$ is a positive regularization hyperparameter. Observe that can be reformulated as

<!-- chunk {"id": "body-0085", "role": "body", "section": "Ridge regularization", "weight": 1.0} -->

This reformulation transforms the regularized problem into a least-squares problem in the form of. As such, we can now perform LS-SPA on the regularized problem.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Hyper-parameter selection", "weight": 1.0} -->

To choose the value of the hyper-parameter $\lambda$, we consider a set of candidate values $\lambda_{1},\ldots,\lambda_{L}$. We solve the regularized least-squares regression problem for each one and evaluate the resulting parameter $\lambda$ using out-of-sample or cross-validation. We then choose $\lambda$ as the one among our choices that achieves the lower mean-square test error. We use this value to compute the $R^{2}$ metric.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Very large data", "weight": 1.0} -->

If $X$ is too large to fit into memory such that performing the initial QR factorization cannot be done, one alternative is to compute the Cholesky factorization of the covariance matrix of $\lbrack{Xy}\rbrack$, i.e., the matrix

<!-- chunk {"id": "body-0088", "role": "body", "section": "Very large data", "weight": 1.0} -->

The covariance matrix $\hat{\Sigma}$ is $p \times p$ and can be computed via block matrix multiplication by blocking $\lbrack{Xy}\rbrack$ vertically, making it possible to distribute the computation across multiple devices or compute iteratively on one device. The upper-triangular factor $\overset{\sim}{R}$ in the Cholesky factorization ${{\overset{\sim}{R}}^{T}\overset{\sim}{R}} = \hat{\Sigma}$ can then be blocked as

<!-- chunk {"id": "body-0089", "role": "body", "section": "Very large data", "weight": 1.0} -->

where ${QR} = X$ is the QR factorization of $X$. We can thus extract $R$, $Q^{T}y$, and ${\|{y - {Q{({Q^{T}y})}}}\|}_{2}$ from $\overset{\sim}{R}$ to compute the reduction for use in LS-SPA. This alternative approach costs $O{({Np^{2}})}$ flops for the computation of $\hat{\Sigma}$ and $O{(p^{3})}$ flops for the computation of $\overset{\sim}{R}$, giving a total cost of $O{({Np^{2}})}$, the same as the QR method. However, Cholesky factorization is less stable than QR and will fail for poorly conditioned $\hat{\Sigma}$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Non-quadratic regularizers", "weight": 1.0} -->

We consider the case where the quadratic loss is paired with a non-quadratic but convex regularizer. This means we choose the model parameter $\theta$ by solving

<!-- chunk {"id": "body-0091", "role": "body", "section": "Non-quadratic regularizers", "weight": 1.0} -->

with variable $\theta \in \text{R}^{p}$, data $X \in \text{R}^{N \times p}$ and $y \in \text{R}^{N}$, and convex but non-quadratic regularizer $r:{\text{R}^{p}\rightarrow{\text{R} \cup {\{\infty\}}}}$. Here $\lambda$ is the regularization hyper-parameter. Simple examples include the nonnegative indicator function, so the problem above is a non-negative least-squares problem. Another example is ${r{(\theta)}} = {\|\theta\|}_{1}$, which gives the lasso problem.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Non-quadratic regularizers", "weight": 1.0} -->

While our formula for $\theta$ given in §3.2 no longer holds, we can still reduce the complexity of the computation with the initial reduction. Thus when we find $\theta$ we solve a smaller convex optimization problem with a square data matrix.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Experiment descriptions", "weight": 1.0} -->

We describe two numerical experiments, one medium size and one large, that demonstrate the relationship between the runtime of the LS-SPA and the accuracy of the approximated Shapley attribution. The code for the experiments can be found in

<!-- chunk {"id": "body-0094", "role": "body", "section": "Medium size experiment", "weight": 1.0} -->

The medium size experiment uses a data set with $p = 100$ features, and $N = M = 10^{5}$ data points for the train and test data sets. It is meant to show how the error in the estimate of the Shapley attributions evolves with an increasing number of feature chains. All three methods of feature chain sampling (MC, permutohedron QMC, and argsort QMC) were tested in the medium size experiment. The quantile used for risk estimation is $q = 0.95$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Large experiment", "weight": 1.0} -->

The large experiment uses a data set with $p = 1000$ features and $N = M = 10^{6}$ data points for the train and test data sets. It is meant to demonstrate that LS-SPA scales to large problems. The large experiment uses argsort QMC only. The quantile used for risk estimation is $q = 0.95$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Computation platforms", "weight": 1.0} -->

The medium size experiment was done with an 8-core AMD Ryzen 9 5900HX at 3.3 GHz with 32 GB RAM and an NVIDIA GeForce RTX 3080 Mobile with 16 GB RAM. The large experiment was done with two 20-core Intel Xeon E5-2698 v4 CPUs at 2.2 GHz with 512 GB RAM and eight NVIDIA Tesla V100 GPUs, each of which has 16 GB RAM. Note that in both experiments, all numerical computations were done on GPU. Furthermore, in the large experiment, all eight GPUs were utilized to perform the Cholesky reduction described in §4.4, but all remaining computations were done on only one GPU.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Data generation", "weight": 1.0} -->

For both experiments, we solved instances of on randomly generated train and test data, $(X^{trn},y^{trn})$ and $(X^{tst},y^{tst})$, respectively. To generate the data, we first randomly generate a feature covariance matrix $\Sigma = {{FF^{T}} + I}$, where $F \in \text{R}^{p \times {({p/20})}}$ is generated by sampling its entries independently from a $\mathcal{N}{}$ distribution. We then let $C$ be the correlation matrix of $\Sigma$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Data generation", "weight": 1.0} -->

Next, the true vector of feature coefficients $\theta$ was generated by randomly selecting $\lfloor{{({p + 1})}/10}\rfloor$ entries to be $2$ and the remaining entries to be $0$.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Medium size experiment", "weight": 1.0} -->

We used each of MC, permutohedron QMC, and argsort QMC to sample $D = 2^{13}$ feature chains, done in $2^{5}$ batches of size $2^{8}$, to illustrate the progress we keep track of the running sample mean. LS-SPA took around 3.2 seconds to compute $2^{13}$ samples, including compilation time. To get the "ground-truth" Shapley values, we ran argsort QMC with $D = 2^{28}$ feature chains. The errors for each method as a function of the number of feature chains completed are shown in figure 2. Note that the condition number of $C$ was $248.0$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Medium size experiment", "weight": 1.0} -->

In figure 3, we also plot the "ground-truth" error against the error estimate, which was computed using the risk estimation procedure described in §3.6, at each step of the algorithm using argsort QMC to sample feature chains.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Large experiment", "weight": 1.0} -->

We used argsort QMC to sample $2^{4}$ batches each with $2^{9}$ permutations. We use the Cholesky reduction presented in §4.4. The correlation matrix $C$ has condition number $4.3 \times 10^{5}$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Large experiment", "weight": 1.0} -->

The algorithm took 3.5 seconds to complete the initial reduction. LS-SPA ran for 14.6 seconds to reach an error estimate of $8.4 \times 10^{- 3}$, and ran for 113.3 seconds to complete all $2^{13}$ permutations, for a total time of 116.8 seconds to complete, reaching an error estimate of $2.0 \times 10^{- 3}$.
