<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Mean Robust Optimization

Topics include Robustness, Uncertainty, Clustering, Optimization, Control, Wasserstein distances, Robust optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robust optimization is a tractable and expressive technique for decision-making under uncertainty, but it can lead to overly conservative decisions when pessimistic assumptions are made on the uncertain parameters. Wasserstein distributionally robust optimization can reduce conservatism by being data-driven, but it often leads to very large problems with prohibitive solution times. We introduce mean robust optimization, a general framework that combines the best of both worlds by providing a trade-off between computational effort and conservatism. We propose uncertainty sets constructed based on clustered data rather than on observed data points directly thereby significantly reducing problem size. By varying the number of clusters, our method bridges between robust and Wasserstein distributionally robust optimization. We show finite-sample performance guarantees and explicitly control the potential additional pessimism introduced by any clustering procedure. In addition, we prove conditions for which, when the uncertainty enters linearly in the constraints, clustering does not affect the optimal solution. We illustrate the efficiency and performance preservation of our method on several numerical examples, obtaining multiple orders of magnitude speedups in solution time with little-to-no effect on the solution quality.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robust optimization (RO) and distributionally robust optimization (DRO) are popular tools for decision-making under uncertainty due to their high expressiveness and versatility. The main idea of RO is to define an uncertainty set and to minimize the worst-case cost across possible uncertainty realizations in that set. However, while RO often leads to tractable formulations, it can be overly-conservative. To reduce conservatism, DRO takes a probabilistic approach, by modeling the uncertainty as a random variable following a probability distribution known only to belong to an uncertainty set (also called ambiguity set) of distributions. In both RO and DRO, the choice of the uncertainty or ambiguity set can greatly influence the quality of the solution for both paradigms. Good-quality uncertainty sets can lead to excellent practical performance while ill chosen sets can lead to overly-conservative actions and intractable computations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Traditional approaches design uncertainty sets based on theoretical assumptions on the uncertainty distributions. While these methods have been quite successful, they rely on a priori assumptions that are difficult to verify in practice. On the other hand, the last decade has seen an explosion in the availability of data. This change has brought a shift in focus from a priori assumptions on the probability distributions to data-driven methods in operations research and decision sciences. In RO and DRO, this new paradigm has fostered data-driven methods where uncertainty sets are shaped directly from data. In data-driven DRO, a popular choice of the ambiguity set is the ball of distributions whose Wasserstein distance to a nominal distribution is at most $\epsilon > 0$ Esfahani and Kuhn; Kuhn et al.; Gao; Gao and Kleywegt. When the reference distribution is an empirical distribution, the associated Wasserstein DRO can be formulated as a convex minimization problem where the number of constraints grows linearly with the number of datapoints. While less conservative than RO, data-driven DRO can lead to very large formulations that are intractable, especially in mixed-integer optimization (MIO).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A common idea to reduce the dimensionality of data-driven decision-making problems is to use clustering techniques from machine learning. While clustering has recently appeared in various works within the stochastic programming literature, the focus has been on the improvement of and comparisons to the sample average approximation (SAA) approach and not in a distributionally robust sense. In contrast, recent approaches in the DRO literature cluster data into partitions and either build moment-based uncertainty sets for each partition, or enrich Wasserstein DRO formulations with partition-specific information (e.g., relative weights) Esteban and Morales. While these approaches are promising, clustering is still used as a pre-processing heuristic on the data-sets in DRO, without a clear understanding of how it affects the conservatism of the optimal solutions. In particular, choosing the right clustering parameters to carefully balance computational tractability and out-of-sample performance is still an unsolved challenge.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Our contributions", "weight": 1.0} -->

In this work, we present mean robust optimization (MRO), a data-driven method that, via machine learning clustering, bridges between RO and Wasserstein DRO.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We design the uncertainty set for RO as a ball around clustered data. Without clustering, our formulation corresponds to the finite convex reformulation in Wasserstein DRO. With just one cluster, our formulation corresponds to the classical RO approach. The number of clusters is a tunable parameter that provides a tradeoff between the worst-case objective value and computational efficiency, which includes both speed and memory usage.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We provide probabilistic guarantees of constraint satisfaction for our method, based on the quality of the clustering procedure.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We derive bounds on the effect of clustering in case of constraints with concave and maximum-of-concave dependency on the uncertainty. In addition, we show that, when constraints are linearly affected by the uncertainty, clustering does not affect the solution nor the probabilistic guarantees.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We show on various numerical examples that, thanks to our clustering procedure, our approach provides multiple orders of magnitude speedups over classical approaches while guaranteeing the same probability of constraint satisfaction. The code to reproduce our results is available at

<!-- chunk {"id": "body-0011", "role": "body", "section": "Robust optimization", "weight": 1.0} -->

RO deals with decision-making problems where some of the parameters are subject to uncertainty. The idea is to restrict data perturbations to be within a deterministic uncertainty set, then optimize the worst-case performance across all realizations of this uncertainty. For a detailed overview of RO, we refer to the survey papers by Ben-Tal and Nemirovski Ben-Tal and Nemirovski and Bertsimas et al. Bertsimas et al., as well as the books by Ben-Tal et al. Ben-Tal et al. and Bertsimas and den Hertog Bertsimas and den Hertog. These approaches, while powerful, may be overly-conservative, and there have been approaches that provide a tradeoff between conservatism and constraint violation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Distributionally robust optimization", "weight": 1.0} -->

DRO minimizes the worst-case expected loss over a probabilistic ambiguity set characterized by certain known properties of the true data-generating distribution. Based on the type of ambiguity set considered existing literature on DRO can roughly be defined in two. Ambiguity sets of the first type contain all distributions that satisfy certain moment constraints. In many cases such ambiguity sets possess a tractable formulation, but have also been criticized for yielding overly conservative solutions. Ambiguity sets of the second type enjoy the interpretation of a ball of distributions around a nominal distribution, often the empirical distribution on the observed samples. Wasserstein uncertainty sets are one particular example and enjoy both a tractable primal as well as a tractable dual formulation. We refer to the work by Chen and Paschalidis Chen and Paschalidis for a thorough overview of DRO, and to the work by Zhen et al. Zhen et al. for a general theory on convex dual reformulations. When the ambiguity set is well chosen, DRO formulations enjoy strong out-of-sample statistical performance guarantees. As these statistical guarantees are typically not very sharp, in practice the radius of the uncertainty set is typically chosen through time consuming cross-validation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Distributionally robust optimization", "weight": 1.0} -->

At the same time, DRO has the downside of being more computationally expensive than traditional robust approaches. We observe for instance that the number of constraints in Wasserstein DRO formulations scale linearly with the number of samples, which can become practically prohibitive especially when integer variables are involved. Our proposed method addresses this problem by reducing the number of constraints through clustering. While many works have recently emerged on the construction of DRO ambiguity sets through the partitioning of data Chen et al.; Esteban and Morales; Perakis et al., or the discretization of the underlying distribution Liu et al., there still exists a gap in the literature. In particular, theoretical bounds on the change in problem performance as affected by the number of clusters, as well as by the quality of the cluster assignment, remain largely unexplored. In this work, we fill the gap by providing such insights.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Data-driven robust optimization", "weight": 1.0} -->

Data-driven optimization has been well-studied, with various techniques to learn the unknown data-generating distribution before formulating the uncertainty set. Bertsimas et al. Bertsimas et al. construct the ambiguity set as a confidence region for the unknown data-generating distribution $\mathbf{P}$ using several statistical hypothesis tests. By pairing a priori assumptions on $\mathbf{P}$ with different statistical tests, they obtain various data-driven uncertainty sets, each with its own geometric shape, computational properties, and modeling power. We, however, use machine learning in the form of clustering algorithms to preserve the geometric shape of the dataset, without explicitly learning and parametrizing the unknown distribution.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Distributionally robust optimization as a robust program", "weight": 1.0} -->

Gao and Kleywegt Gao and Kleywegt consider a robust formulation of Wasserstein DRO similar to our mean robust optimization, but without the idea of dataset reduction. Given $N$ samples and a positive integer $K$, they introduce an approximation of Wasserstein DRO by defining a new ambiguity set as a subset of the standard Wasserstein DRO set, containing all distributions supported on $NK$ points with equal probability $1/{({NK})}$, as opposed to the standard set supported on $N$ points. In this work, however, we study how to reduce, instead of increase, the number of variables and constraints to make the Wasserstein DRO problem more tractable by linking it to robust optimization.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Robust optimization as a distributionally robust optimization program", "weight": 1.0} -->

Xu et al. Xu et al. take inspiration from sample-based optimization problems to investigate probabilistic interpretations of RO. They generalize the ideas of Delage and Ye Delage and Ye, that the solution to a robust optimization problem is the solution to a special Distributionally Robust Stochastic Program (DRSP), where the distributional set contains all distributions whose support is contained in the uncertainty set. In a related vein, Bertsimas et al. Bertsimas et al. show that, under a particular construction of the uncertainty sets, multi-stage stochastic linear optimization can be interpreted as Wasserstein-$\infty$ DRO. We establish a similar equivalence between RO and DRO, focusing especially on Wasserstein-$p$ ambiguity sets for all $p$. We develop an easily interpretable construction of the primal constraints and uncertainty sets, and prove, in view of both the primal and dual problems, that $p = \infty$ is a limiting case of $p \geq 1$. This provides a natural extension of the equivalence proved.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Probabilistic guarantees in robust and distributionally optimization", "weight": 1.0} -->

Bertsimas et al. Bertsimas et al. propose a disciplined methodology for deriving probabilistic guarantees for solutions of robust optimization problems with specific uncertainty sets and objective functions. They derive a posteriori guarantee to compensate for the conservatism of a priori uncertainty bounds. Esfahani and Kuhn Esfahani and Kuhn obtain finite-sample guarantees for Wasserstein DRO for selecting the radius $\epsilon$ of order $N^{- {1/{\max{\{ 2,m\}}}}}$, where $N$ is the number of samples and $m$ is the dimension of the problem data, while Gao Gao derives finite-sample guarantees for Wasserstein DRO for selecting $\epsilon$ of order $N^{- {1/2}}$ under specific assumptions. We provide theoretical results of a similar vein, with a slightly increased $\epsilon$ to compensate for information lost through clustering and achieve the same probabilistic guarantees. Our theoretical guarantees hold for Wasserstein-$p$ distance for all $p \geq 1$ and $p = \infty$, and are independent of the uncertain function to minimize.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Probabilistic guarantees in robust and distributionally optimization", "weight": 1.0} -->

These bounds, however, following the literature, are theoretical in nature and not tight in practice, typically resulting in overly-conservative $\epsilon$. The final $\epsilon$ values are usually chosen through empirical empirication - in which case, our formulation, by being lower dimensional, is overall much faster to solve.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Clustering in stochastic optimization", "weight": 1.0} -->

Clustering in stochastic optimization is closely related to the idea of scenario reduction. First introduced by Dupačová et al. Dupačová et al., scenario reduction seeks to approximate, with respect to a probability metric, an $N$-point distribution with a distribution with a smaller number of points. In particular, Rujeerapaiboon et al. Rujeerapaiboon et al. analyze the worst-case bounds on scenario reduction the approximation error with respect to the Wasserstein metric, for initial distributions constrained to a unit ball. They provide constant-factor approximation algorithms for $K$-medians and $K$-means clustering. Later, Bertsimas and Mundru Bertsimas and Mundru apply this idea to two-stage stochastic optimization problems, and provide an alternating-minimization method for finding optimal reduced scenarios under the modified objective. They also provide performance bounds on the stochastic optimization problem for different scenarios.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Clustering in stochastic optimization", "weight": 1.0} -->

Jacobson et al., Emelogu et al. Emelogu et al., Beraldi et al. Beraldi and Bruni, and Chen Chen apply a similar idea of clustering to reduce the sample/scenario size, then compare the results against the classical SAA approach where the sample size is not reduced. In MRO, we adapt and extend the scenario reduction approach to Wasserstein DRO, where upon fixing the reduced scenario points to ones found by the clustering algorithm, we allow for variation around these reduced points. We then provide performance bounds on the DRO problem depending on the number of clusters.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Data compression in data-driven problems", "weight": 1.0} -->

Fabiani and Goulart Fabiani and Goulart compress data for robust control problems by minimizing the Wasserstein-1 distance between the original and compressed datasets, and observe a slight loss in performance in exchange for reduced computation time. While related, this is orthogonal to our approach of using machine learning clustering to reduce the dataset, where we include results and theoretical bounds for a more general set of robust optimization problems with Wasserstein-$p$ distance, and demonstrate conditions under which no performance loss is necessary.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Layout of the paper", "weight": 1.0} -->

In Section 2, we present our approach for concave uncertainty constraints, then extend the results to maximum-of-concave functions. In Section 3, we present connections to distributionally robust optimization, and give theoretical guarantees on constraint satisfaction. In Section 4, we analyze the effect on clustering on the worst-case value of the MRO solutions for both concave and maximum-of-concave constraints. In Section 5, we give guidelines for choosing hyperparameters. In Section 6, we provide computational verification of the speedups obtained through our methodology. In Section 7, we summarize our conclusions.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The problem", "weight": 1.0} -->

We consider an uncertain constraint of the form,

<!-- chunk {"id": "body-0024", "role": "body", "section": "The problem", "weight": 1.0} -->

where $x \in \mathcal{X} \subseteq \text{R}^{n}$ is the optimization variable and $\mathcal{X}$ is a compact set, $u \in \text{R}^{m}$ is an uncertain parameter, and $- {g{(u,x)}}$ is proper, convex, and lower-semicontinuous in $u$ for all $x$. Throughout this paper, we assume the support $S$ of $u$ to live within the domain of $g$ for the variable $u$, which we will refer to as $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}_{u}g$, i.e., $S \subseteq {\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}_{u}g}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The problem", "weight": 1.0} -->

We assume $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}_{u}g$ is independent of $x$, and that the following assumption holds.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

The domain $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}_{u}g$ is $\text{R}^{m}$. Otherwise, $g$ is either element-wise monotonically increasing in $u$ and only has a (potentially) lower-bounded domain, or element-wise monotonically decreasing in $u$ and only has a (potentially) upper-bounded domain.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

This assumption on the domain and monotonicity of $g$ is very common in practice as it is satisfied by linear and quadratic functions, as well as other common functions (e.g., $\log{(u)}$, and $1/{({1 + u})}$).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

In Section 2.4, we extend our results for $g$ being the maximum of of concave functions, each satisfying the aforementioned conditions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

The RO approach defines an uncertainty set $\mathcal{U} \subseteq \text{R}^{m}$ and forms the robust counterpart as

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

where the uncertainty set is chosen so that for any solution $x$, the above holds with a certain probability. We define this in terms of expectation,

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

where $\mathbf{P}$ is the unknown distribution of the uncertainty $u$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Risk measures", "weight": 1.0} -->

Expectation constraints of the form can represent popular risk measures, and can imply constraints commonly used in chance-constrained programming (CCP). In CCP, the probabilistic constraint considered is

<!-- chunk {"id": "body-0033", "role": "body", "section": "Risk measures", "weight": 1.0} -->

which corresponds to the value at risk being nonpositive, i.e.,

<!-- chunk {"id": "body-0034", "role": "body", "section": "Risk measures", "weight": 1.0} -->

Unfortunately, except in very special cases, the value at risk function is intractable. A tractable approximation of the value at risk is the conditional value at risk, defined as

<!-- chunk {"id": "body-0035", "role": "body", "section": "Risk measures", "weight": 1.0} -->

where ${(a)}_{+} = {\max{\{ a,0\}}}$. This expression can be modeled through our approach, by writing ${\operatorname{\mathbf{C}\mathbf{V}\mathbf{a}\mathbf{R}}{({g{(u,x)}},\alpha)}} = {\inf_{\tau}{\{{\text{E}{({\hat{g}{(u,x,\tau)}})}}\}}}$, where ${\hat{g}{(u,x,\tau)}} = {\tau + {{({1/\alpha})}{({{g{(u,x)}} - \tau})}_{+}}}$ is the maximum of concave functions, which we study in Sections 2.4, 6.4, and 6.5. It is well known from Uryasev and Rockafellar that the relationship between these probabilistic guarantees of constraint satisfaction is

<!-- chunk {"id": "body-0036", "role": "body", "section": "Risk measures", "weight": 1.0} -->

Therefore, our expectation constraint implies common chance constraints.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Finite-sample guarantees", "weight": 1.0} -->

In data-driven optimization, while $\mathbf{P}$ is unknown, it is partially observable through a finite set of $N$ independent samples of the random vector $u$. We denote the training dataset of these samples by $\mathcal{D}_{N} = {\{ d_{i}\}}_{i \leq N} \subseteq S$, and note that this dataset is governed by $\mathbf{P}^{N}$, the product distribution supported on $S^{N}$. A data-driven solution of a robust optimization problem is a feasible decision ${\hat{x}}_{N} \in \text{R}^{n}$ found using the data-driven uncertainty set $\mathcal{U}$, which in turn is constructed by the training dataset $\mathcal{D}_{N}$. Specifically, the feasible decision and data-driven uncertainty set $\mathcal{U}$ we construct must imply the probabilistic guarantee

<!-- chunk {"id": "body-0038", "role": "body", "section": "Finite-sample guarantees", "weight": 1.0} -->

where $\beta > 0$ is the specified probability of constraint violation. From now, when we refer to probabilistic guarantees of constraint satisfaction, it will be a reference to.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Our approach", "weight": 1.0} -->

To meet the probabilistic guarantees outlined above, we propose to construct ${\hat{x}}_{N}$ to satisfy particular constraints, with respect to a particular uncertainty set.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Case $p \\geq 1$", "weight": 1.0} -->

In the case where $p \geq 1$, the set we consider takes the form

<!-- chunk {"id": "body-0041", "role": "body", "section": "Case $p \\geq 1$", "weight": 1.0} -->

where we partition $\mathcal{D}_{N}$ into $K$ disjoint subsets $C_{k}$, and ${\overline{d}}_{k}$ is the centroid of the $k$th subset, for $k = {1,\ldots,K}$. The weight $w_{k} > 0$ of each subset is equivalent to the proportion of points in the subset, i.e., $w_{k} = {{|C_{k}|}/N}$. We choose $p$ to be an integer exponent, and $\epsilon$ will be chosen depending on the other parameters to ensure satisfaction of the probability guarantee. When $p = 2$ and $S = \text{R}^{m}$, the set can be visualized as an ellipsoid in $\mathbf{R}^{Km}$ with the center formed by stacking together all ${\overline{d}}_{k}$ into a single vector of dimension $\mathbf{R}^{Km}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Case $p \\geq 1$", "weight": 1.0} -->

When we additionally have $K = N$ or $K = 1$, this ellipsoid becomes a ball of dimension $\text{R}^{Nm}$ or $\text{R}^{m}$ respectively, as shown in Figure 1.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Case $p = \\infty$", "weight": 1.0} -->

In the case where $p = \infty$, the set we consider takes a more specific form,

<!-- chunk {"id": "body-0044", "role": "body", "section": "Case $p = \\infty$", "weight": 1.0} -->

where the constraints for individual $v_{k}$ become decoupled. See Figure 2 for an example when $K = 3$ and $K = 1$. This decoupling follows the result for the Wasserstein type $p = \infty$ metric, as our uncertainty set is analogous to the set of all distributions within Wasserstein-$\infty$ distance of $\overline{d}$. We note that, if any of the decoupled constraints are violated, then ${\lim_{p\rightarrow\infty}{\sum_{k = 1}^{K}{w_{k}{\|{v_{k} - {\overline{d}}_{k}}\|}^{p}}}} \geq \epsilon^{p}$, and the summation constraint will be violated.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Case $p = \\infty$", "weight": 1.0} -->

For both cases, $p \geq 1$ and $p = \infty$, when $K = 1$, we have a simple uncertainty set: a ball of radius $\epsilon$ around the empirical mean of the entire dataset, ${{\mathcal{U}{(1,\epsilon)}} = \left\{ {v \in S}\mid{{\|{v - \overline{d}}\|} \leq \epsilon} \right\}}.$ This is equivalent to the uncertainty set of traditional RO, as it is of the same dimension $m$ as the uncertain parameter. When $K = N$ and $w_{k} = {1/N}$, both cases closely resemble the ambiguity sets of Wasserstein-$p$ DRO.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Case $p = \\infty$", "weight": 1.0} -->

Having defined the uncertainty set, we now introduce constraints of the form

<!-- chunk {"id": "body-0047", "role": "body", "section": "Case $p = \\infty$", "weight": 1.0} -->

where $g$ is defined in the original constraint. The weights $w_{k}$ correspond to the ones defined in the uncertainty set. Putting everything together, ${\hat{x}}_{N}$ is the solution to the robust optimization problem

<!-- chunk {"id": "body-0048", "role": "body", "section": "Case $p = \\infty$", "weight": 1.0} -->

where $f$ is the objective function. We call this problem the mean robust optimization (MRO) problem.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Data-driven procedure", "weight": 1.0} -->

Given the problem data, we formulate the uncertainty set from clustered data using machine learning, with the choice of $K$ and $\epsilon$ chosen experimentally. Then, we solve the MRO problem to arrive at a data-driven solution ${\hat{x}}_{N}$ which satisfies the probabilistic guarantee, see Figure 3.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Solving the robust problem", "weight": 1.0} -->

We now outline two ways to solve the MRO problem, using a direct convex reformulation and using a cutting plane algorithm. The reformulation and cutting plane procedure follow usual techniques for RO problems in existing literature, with adaptations made for the MRO setup, as well as a reformulation derived for the case $p = \infty$. We include simple examples and pseudocode for completeness.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Direct convex reformulation for $p \\geq 1$", "weight": 1.0} -->

In the case where $p \geq 1$, the MRO can be rewritten as the optimization problem

<!-- chunk {"id": "body-0052", "role": "body", "section": "Direct convex reformulation for $p \\geq 1$", "weight": 1.0} -->

Note that $q$ satisfies ${{1/p} + {1/q}} = 1$, i.e., $q = {p/{({p - 1})}}$. When $p = 1$ and $q = \infty$, we note the formulation. The support function $\sigma_{S}$ is also the conjugate of $\chi_{S}$, which is defined ${\chi_{S}{(u)}} = 0$ if $u \in S$, and $\infty$ otherwise. The proof of the derivation and strong duality of the constraint is delayed to Appendix A.1 ‣ Appendix A Appendices ‣ Mean Robust Optimization"). Since the dual of the constraint becomes a minimization problem, any feasible solution that with objective less than or equal to $0$ will satisfy the constraint, so we can remove the minimization to arrive at the above form. While traditionally we take the supremum instead of maximizing, here the supremum is always achieved as we assume $g$ to be upper-semicontinuous.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Direct convex reformulation for $p \\geq 1$", "weight": 1.0} -->

For specific examples of the conjugate forms of different $g$, see Bertsimas and den Hertog and Beck.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Direct convex reformulation for $p \\geq 1$", "weight": 1.0} -->

When $K$ is set to be $N$, $w_{k}$ is $1/N$, and this is of an analogous form to the convex reduction of the worst case problem for Wasserstein DRO, which we will introduce in Section 3.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Direct convex reformulation for $p \\geq 1$", "weight": 1.0} -->

We note the special case when $p = 1$. We observe from that

<!-- chunk {"id": "body-0056", "role": "body", "section": "Direct convex reformulation for $p \\geq 1$", "weight": 1.0} -->

Therefore, the above formulation becomes

<!-- chunk {"id": "body-0057", "role": "body", "section": "Example with affine constraints", "weight": 1.0} -->

Consider a single affine constraint of the form

<!-- chunk {"id": "body-0058", "role": "body", "section": "Example with affine constraints", "weight": 1.0} -->

where the number of variables or constraints does not depend on $K$. Since vector $\sum_{k = 1}^{K}{w_{k}{\overline{d}}_{k}}$ is the average of the datapoints in $\mathcal{D}_{N}$ for any $K \in {\{ 1,\ldots,N\}}$, this formulation corresponds to always choosing $K = 1$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Direct convex reformulation for $p = \\infty$", "weight": 1.0} -->

In the case where $p = \infty$, the MRO can be rewritten as the optimization problem

<!-- chunk {"id": "body-0060", "role": "body", "section": "Direct convex reformulation for $p = \\infty$", "weight": 1.0} -->

which has a reformulation where the constraint above is dualized,

<!-- chunk {"id": "body-0061", "role": "body", "section": "Direct convex reformulation for $p = \\infty$", "weight": 1.0} -->

with new variables $s_{k} \in \text{R}$, $z_{k} \in \text{R}^{m}$, and $y_{k} \in \text{R}^{m}$. The proof is delayed to Appendix A.2 ‣ Appendix A Appendices ‣ Mean Robust Optimization").

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 2.1 (Case $p = \\infty$ is the limit of case $p \\geq 1$)", "weight": 1.0} -->

In terms of the primal problem, is the limiting case of as $p\rightarrow\infty$. In terms of the reformulated problem with dualized constraints, problem is the limiting case of as $p\rightarrow\infty$. The proofs are delayed to Appendix A.5 and Appendix A.6 respectively. These proofs extend the ideas stated.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Example with affine constraints", "weight": 1.0} -->

Consider again the case of affine constraint as in with support set $S = \text{R}^{m}$, now with $p = \infty$. Following a similar derivation as, we substitute the conjugate function ${\lbrack{- g}\rbrack}^{\ast}$ in problem, we can obtain

<!-- chunk {"id": "body-0064", "role": "body", "section": "Example with affine constraints", "weight": 1.0} -->

where the number of constraints and variables does not depend on $K$. Similairy to problem, the term $\sum_{k = 1}^{K}{w_{k}{\overline{d}}_{k}}$ is the average of the datapoints in $\mathcal{D}_{N}$ for any $K \in {\{ 1,\ldots,N\}}$. Therefore, the choice of $K$ does not affect this formulation. This can be viewed as the robust counterpart when the uncertainty set is a norm ball of radius $\epsilon$ centered at ${({1/N})}{\sum_{i = 1}^{N}d_{i}}$

<!-- chunk {"id": "body-0065", "role": "body", "section": "Example with affine constraints", "weight": 1.0} -->

Note that, if $\overline{d} = 0$ the constraint can be simplified even further, obtaining ${{a^{T}x} + {\epsilon{\|{P^{T}x}\|}_{\ast}}} \leq b$, which corresponds to the robust counterpart in RO with norm uncertainty sets,.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 2.2", "weight": 1.0} -->

When $g$ is affine and $S = \text{R}^{m}$, for any $\epsilon$ and norm, the convex reformulations for $p = 1$ and $p = \infty$ are identical. The proof appears in Appendix A.7.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Cutting plane algorithm", "weight": 1.0} -->

The second approach to solve problem (MRO) is to use a cutting plane procedure, in which we consider the minimization problem where $x$ is the variable and $S$ a finite set of values for the uncertainty,

<!-- chunk {"id": "body-0068", "role": "body", "section": "Cutting plane algorithm", "weight": 1.0} -->

and the maximization problem over $u$ with $x^{k}$ fixed,

<!-- chunk {"id": "body-0069", "role": "body", "section": "Cutting plane algorithm", "weight": 1.0} -->

The procedure works as follows. We first solve with a set $\hat{S} = {\{\overline{u}\}}$, where $\overline{u}$ is nominal value of the uncertainty, obtaining $x^{k}$. Then, we solve, obtaining $u^{k}$. If ${\overline{g}{(u^{k},x^{k})}} > 0$, then we add $u^{k}$ to the set $\hat{S}$. Otherwise, we terminate. This procedure is summarized in Algorithm 1. As demonstrated by Bertimas et al. Bertsimas et al., the cutting plane and convex reformulation methods are comparable in terms of performance, thus both are viable.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Cutting plane algorithm", "weight": 1.0} -->

1:given $\hat{S} = {\{\overline{u}\}}$
3: xk← solve minimization problem over x
4: uk← solve maximization problem over u
Algorithm 1 Cutting plane algorithm to solve (MRO)

<!-- chunk {"id": "body-0071", "role": "body", "section": "Maximum-of-concave constraint function", "weight": 1.0} -->

We now consider a more general maximum-of-concave function

<!-- chunk {"id": "body-0072", "role": "body", "section": "Maximum-of-concave constraint function", "weight": 1.0} -->

with each $- g_{j}$ being proper, convex, and lower-semicontinuous in $u$ for all $x$. When we take $J = 1$, we arrive back at the formulations given in Section 2. Note that any problem with multiple uncertain constraints ${{{g_{j}{(u,x)}},j} = 1},{\ldots,J}$, where we assume the usual conditions on $g_{j}$, can be combined to create a joint constraint of this maximum-of-concave form. As mentioned in Section 2.1, this can also be used to model $\operatorname{\mathbf{C}\mathbf{V}\mathbf{a}\mathbf{R}}$ constraints, which has a maximum-of-concave analytical form.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Problem parametrization", "weight": 1.0} -->

We now consider constraints of the form

<!-- chunk {"id": "body-0074", "role": "body", "section": "Problem parametrization", "weight": 1.0} -->

where $\alpha \in \Gamma$, with $\Gamma = \left. \{\alpha \middle| {{{\sum_{j = 1}^{J}\alpha_{jk}} = w_{k}},{\alpha_{jk} \geq {{0{\forall k}},j}}}\} \right.$. For each constituent function $g_{j}$, the uncertainty set contains a set of vectors $(v_{j1},\ldots,v_{jK})$, and a set of parameters $(\alpha_{j1},\ldots,\alpha_{jK})$ to denote the fraction of mass assigned to that function for each $k$. The total amount of mass assigned for each cluster, $\sum_{j = 1}^{J}\alpha_{jk}$, is the weight of the cluster, $w_{k}$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Problem parametrization", "weight": 1.0} -->

We use a summation over weighted pieces $g_{j}$ instead of a maximum over $g_{j}$, as this is a generalization of the maximum, and has a more natural dual reformulation. We take inspiration, where $\alpha$ arises from the extremal distribution for Wasserstein DRO. Note that the intuitive maximization over $g_{j}$'s is analogous to setting $\alpha_{jk} = w_{k}$ for a specific $j$ for each $k$, and $\alpha_{jk} = 0$ otherwise.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Problem parametrization", "weight": 1.0} -->

The uncertainty set is given as follows.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Case $p \\geq 1$", "weight": 1.0} -->

In the case where $p \geq 1$, we have

<!-- chunk {"id": "body-0078", "role": "body", "section": "Case $p \\geq 1$", "weight": 1.0} -->

Note that the single concave case given previously follows when we take $J = 1$. All parameters are defined as in the single concave case.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Case $p = \\infty$", "weight": 1.0} -->

In the case where $p = \infty$, the set we consider becomes

<!-- chunk {"id": "body-0080", "role": "body", "section": "Case $p = \\infty$", "weight": 1.0} -->

where we once again introduce weight parameters $\alpha$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Case $p = \\infty$", "weight": 1.0} -->

Following these changes, ${\hat{x}}_{N}$ is again the solution to the robust optimization problem (MRO), defined now with the generalized uncertainty set and constraint.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Solving the robust problem", "weight": 1.0} -->

We give the direct reformulation approach for solving the generalized problem for $p \geq 1$. The case $p = \infty$ is delayed to Appendix A.4. We write the MRO problem as the optimization problem

<!-- chunk {"id": "body-0083", "role": "body", "section": "Solving the robust problem", "weight": 1.0} -->

with variables $\lambda \in \text{R}$, $s_{k} \in \text{R}$, $z_{jk} \in \text{R}^{m}$, and $y_{jk} \in \text{R}^{m}$. The proof is delayed to Appendix A.3 ‣ Appendix A Appendices ‣ Mean Robust Optimization"). Again, while traditionally we take the supremum instead of maximizing, here the supremum is always achieved as we assume $g_{j}$ to be upper-semicontinuous for all $j$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Solving the robust problem", "weight": 1.0} -->

In addition, when $K$ is set to be $N$, and $w_{k}$'s are $1/N$, this is also of an analogous form to the convex reduction of the worst case problem for Wasserstein DRO, given in Section 3.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Links to Wasserstein distributionally robust optimization", "weight": 1.0} -->

Distributionally robust optimization (DRO) solves the problem

<!-- chunk {"id": "body-0086", "role": "body", "section": "Links to Wasserstein distributionally robust optimization", "weight": 1.0} -->

where the ambiguity set $\mathcal{P}_{N}$ contains, with high confidence, all distributions that could have generated the training samples $\mathcal{D}^{N}$, such that the probabilistic guarantee is satisfied. Wasserstein DRO constructs $\mathcal{P}_{N}$ as a ball of radius $\epsilon$ with respect to the Wasserstein metric around the empirical distribution ${\hat{\mathbf{P}}}^{N} = {\sum_{i = 1}^{N}{\delta_{d_{i}}/N}}$, where $\delta_{d_{i}}$ denotes the Dirac distribution concentrating unit mass at $d_{i} \in \mathbf{R}^{m}$. Specifically, we write

<!-- chunk {"id": "body-0087", "role": "body", "section": "Links to Wasserstein distributionally robust optimization", "weight": 1.0} -->

where $\mathcal{M}{(S)}$ is the set of probability distributions supported on $S$ satisfying a light-tailed assumption (more details in section 3.1), and

<!-- chunk {"id": "body-0088", "role": "body", "section": "Links to Wasserstein distributionally robust optimization", "weight": 1.0} -->

Here, $p$ is any integer greater than 1, and $\Pi$ is any joint distribution of $u$ and $u^{\prime}$ with marginals $\mathbf{Q}$ and $\mathbf{Q}^{\prime}$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Links to Wasserstein distributionally robust optimization", "weight": 1.0} -->

When $K = N$, the constraint of the DRO problem is equivalent to the constraint of (MRO). In particular, for case $p \geq 1$, the expression

<!-- chunk {"id": "body-0090", "role": "body", "section": "Links to Wasserstein distributionally robust optimization", "weight": 1.0} -->

is equivalent to the dual of the constraint of, when $K = N$, and $w_{k} = {1/N}$. This is noted. We give a proof of strong duality in Appendix A.8 ‣ Appendix A Appendices ‣ Mean Robust Optimization"). This is the dual of the generalized max-of-concave form, which is equivalent to the dual of the single concave form when $J = 1$. By the same logic, in the case where $p = \infty$, the expression is equivalent to the dual of the constraint of. Given the above reductions, we can rewrite the Wasserstein DRO problem in the same form as, the MRO problem.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Links to Wasserstein distributionally robust optimization", "weight": 1.0} -->

Our approach can then be viewed as a form of Wasserstein DRO, with the difference that, when $K < N$, we deal with the clustered and averaged dataset. We form $\mathcal{P}_{N}$ as a ball around the empirical distribution ${\hat{\mathbf{P}}}^{K}$ of the centroids of our clustered data

<!-- chunk {"id": "body-0092", "role": "body", "section": "Links to Wasserstein distributionally robust optimization", "weight": 1.0} -->

where $w_{k}$ is the proportion of data in cluster $k$. This formulation allows for the reduction of the sample size while preserving key properties of the sample, which translates directly to a reduction in the number of constraints and variables, while maintaining high quality solutions.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Satisfying the probabilistic guarantees", "weight": 1.0} -->

As we have noted the parallels between MRO and Wasserstein DRO, we now show that the conditions for satisfying the probabilistic guarantees are also analogous.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Case $p = \\infty$", "weight": 1.0} -->

When $p = \infty$, Bertsimas et al. note that the light-tailed assumption is no longer sufficient. Wasserstein DRO satisfies under stronger assumptions, as given in the following theorem.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Worst-case value of the uncertain constraint", "weight": 1.0} -->

The MRO approach is closely centered around the concept of clustering to reduce sample size while maintaining sample diversity. We wish to cluster points that are close together, such that the objective is only minimally affected. With this goal, we then cluster data-points such that the average distance of the points in each cluster to their data-center is minimized,

<!-- chunk {"id": "body-0096", "role": "body", "section": "Worst-case value of the uncertain constraint", "weight": 1.0} -->

where ${\overline{d}}_{k}$ is the mean of the points in cluster $C_{k}$. A well-known algorithm is $K$-means, where we create $K$ clusters by iteratively solving a least-squares problem. Note that once the clusters have been selected, and we assume it to be optimal (i.e. attain $D{(K)}$), then for the case $p = 2$, we have ${\eta_{N}{(K)}} = {D{(K)}}$ from Theorem 3.3. ‣ Case 𝑝=∞. ‣ 3.1 Satisfying the probabilistic guarantees ‣ 3 Links to Wasserstein distributionally robust optimization ‣ Mean Robust Optimization").

<!-- chunk {"id": "body-0097", "role": "body", "section": "Worst-case value of the uncertain constraint", "weight": 1.0} -->

In this section, we then show the effects of clustering on the worst-case value of the constraint function in (MRO). We prove two sets of results, corresponding to $g$ given as a single concave function, and as a more general maximum-of-concave function. For the latter, we also include the special case of the maximum-of-affine function.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Single concave function", "weight": 1.0} -->

For the simplest case of a single concave function, we prove that when the support is large enough,

<!-- chunk {"id": "body-0099", "role": "body", "section": "Single concave function", "weight": 1.0} -->

If $g$ is affine in $u$, MRO does not increase the worst-case value, regardless of $K$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Single concave function", "weight": 1.0} -->

If $g$ is concave in $u$ and satisfies certain smoothness conditions, MRO has a higher worst-case value than Wasserstein DRO and the increase is inversely related to the number of clusters $K$. In other words, the smaller the $K$, the higher the worst-case value.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Quantifying the clustering effect", "weight": 1.0} -->

To quantify the effect of clustering, we calculate the difference between the following formulations of the worst-case value of the constraint in (MRO)

<!-- chunk {"id": "body-0102", "role": "body", "section": "Quantifying the clustering effect", "weight": 1.0} -->

where (MRO-N) is the formulation of the constraint without clustering, akin to traditional Wasserstein DRO, (MRO-N\*) is the same, except we drop the support constraint, and (MRO-K) is the formulation with $K$ clusters. From here, when we mention that the support affects the worst-case constraint value, we refer to situations where at least one of the constraints $v_{i} \in S$ for $i = {1,\ldots,N}$ is binding. Formally, the definition is ${{\overline{g}}^{N}{(x)}} \neq {{\overline{g}}^{N \ast}{(x)}}$ for any $x$ feasible for the DRO problem. We note a sufficient but not necessary condition for the support to not affect the worst-case constraint value: the situation in which the support doesn't affect the uncertainty set, which is defined as

<!-- chunk {"id": "body-0103", "role": "body", "section": "Quantifying the clustering effect", "weight": 1.0} -->

If the support satisfies this condition, then we can conclude that ${{\overline{g}}^{N}{(x)}} = {{\overline{g}}^{N \ast}{(x)}}$ for any $x$ feasible for the DRO problem, and obtain improved bounds below. While the condition depends on the location of the datapoints, it is acceptable to have this dependency, as this is a condition we can check given data to potentially improve the following bounds, without having to solve the MRO problem.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Quantifying the clustering effect", "weight": 1.0} -->

With these definitions, we can construct solutions for (MRO-N), (MRO-K), and (MRO-N\*) to prove the following relations.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

While $\Delta$ could be constructed to be arbitrarily bad, in practice, we expect our relevant range of $\epsilon$ to be small enough such that the difference is insignificant. We can then approximate $\Delta \approx 0$ and simply use the upper bound ${({L/2})}D{(K)}$, as this bound is often not tight. See Sections 6.5 and 6.1 for examples.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Uncertain objective", "weight": 1.0} -->

When the uncertainty is in the objective, Theorem 4.1 quantifies the difference in optimal values.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Uncertain constraints", "weight": 1.0} -->

When the uncertainty is in the constraints, the difference between ${\overline{g}}^{K}{(x)}$ and ${\overline{g}}^{K}{(x)}$ no longer directly reflects the difference in optimal values. Instead, clustering creates a restriction on the feasible set for $x$ as follows. For the same $\hat{x}$, ${\overline{g}}^{K}{(\hat{x})}$ takes a greater value than ${\overline{g}}^{N}{(\hat{x})}$. Since both of them are constrained to be nonpositive from (MRO), the feasible region with $K$ clusters is smaller.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Affine dependence on uncertainty", "weight": 1.0} -->

As a special case, when $g$ is affine in $u$, $L = 0$, so we observe the following corollary.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Maximum-of-concave functions", "weight": 1.0} -->

We now consider the more general case of a maximum-of-concave constraint function, ${g{(u,x)}} = {{\max_{j \leq J}g_{j}}{(u,x)}}$, subject to a polyhedral support, $S = {\{ u\mid{{Hu} \leq h}\}}$. We define the new primal problems

<!-- chunk {"id": "body-0110", "role": "body", "section": "Maximum-of-concave functions", "weight": 1.0} -->

We also make use of the dual versions of the optimization problems, defined as follows.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Maximum-of-concave functions", "weight": 1.0} -->

where we have $K$ clusters. Given these definitions, we obtain bounds on the worst-case value of the constraint function for $K$ clusters.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Uncertain objective", "weight": 1.0} -->

When the uncertainty is in the objective, Theorem 4.2 and Corollary 4.2.1 quantifies the possible difference in optimal values between the MRO problem with $K$ and $N$ clusters. We again define $\Delta = {\max_{x}\left( {{{\overline{g}}^{N \ast}{(x)}} - {{\overline{g}}^{N}{(x)}}} \right)}$, subject to $x$ being feasible for problem (MRO). Note, however, that this is only needed for the upper bound. The lower bound holds without needing to consider ${\overline{g}}^{N \ast}{(x)}$; we need not consider the effect of the support set on the problem.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Uncertain constraints", "weight": 1.0} -->

When the uncertainty is in the constraints, the difference between ${\overline{g}}^{N}{(x)}$ and ${\overline{g}}^{K}{(x)}$ as given in Theorem 4.2 no longer directly reflect the difference in optimal values. Instead, clustering affects the feasible set for $x$ as follows. In the case ${{\overline{g}}^{N}{(x)}} \geq {{\overline{g}}^{K}{(x)}}$, for any $\hat{x}$, ${\overline{g}}^{K}{(\hat{x})}$ can be at most $\delta{(K,z,\gamma)}$ lower in value than ${\overline{g}}^{N}{(\hat{x})}$. Since both values are constrained to be nonpositive from (MRO), the feasible region of the MRO problem with $K$ clusters may be less restricted than that of $N$ clusters.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Uncertain constraints", "weight": 1.0} -->

This indirectly allows MRO with $K$ clusters to obtain a smaller optimal value. On the other hand, in the case ${{\overline{g}}^{N}{(\hat{x})}} \leq {{\overline{g}}^{K}{(\hat{x})}}$, ${\overline{g}}^{K}{(\hat{x})}$ can be at most ${{\max_{j \leq J}{({L_{j}/2})}}D{(K)}} + \Delta$ higher in value than ${\overline{g}}^{N}{(\hat{x})}$. Since both values are constrained to be nonpositive, the feasible region of the MRO problem with $K$ clusters may be more restricted than that of $N$ clusters. This indirectly lets MRO with $K$ clusters to obtain a larger optimal value.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Choosing $K$", "weight": 1.0} -->

When the uncertain constraint is affine and $S$ does not affect the worst-case constraint value, the number of clusters $K$ does not affect the final solution, so it is always best to choose $K = 1$. We trivially cluster by averaging all data-points without using any clustering algorithm. When $S$ affects the worst-case constraint value, there is a difference of at most $\Delta$ between setting $K = 1$ and $K = N$, which can often be approximated $\approx 0$ for small $\epsilon$. Therefore, setting $K = 1$ remains the recommendation. When the constraint is concave, we choose $K$ to obtain a reasonable upper bound on ${\overline{g}}^{K}{(x)}$, as described in Theorem 4.1. This upper bound depends linearly on $D{(K)}$, the clustering value, so by choosing the elbow of the plot of $D{(K)}$, we choose a cluster number that, while being a reasonably low value, best conforms to the shape of the underlying distribution.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Choosing $K$", "weight": 1.0} -->

When the constraint is maximum-of-concave, the bounds given in Theorem 4.2 also depends on $D{(K)}$. Notice that the value $\delta{(K,z,\gamma)}$ in the lower bound is also a weighted transformation of $D{(K)}$. The elbow method has been commonly used in machine learning problems pertaining the choice of hyper-parameters, especially for $K$-means, and can be traced back to Thorndike Thorndike in 1953. Note that, by directly returning $D{(K)}$ and examining the elbow as an initial step, this procedure can be completed in the clustering step without having to solve the downstream optimization problem. To further improve the choice of $K$, or if the elbow is unclear, cross-validation may be used for low $K$ values or $K$ values around the elbow. No matter if the uncertainty lies in the objective or the constraints, this bound will inform us of the potential difference between choosing different $K$.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Choosing $\\epsilon$", "weight": 1.0} -->

While we have outlined theoretical results in Theorem 3.3. ‣ Case 𝑝=∞. ‣ 3.1 Satisfying the probabilistic guarantees ‣ 3 Links to Wasserstein distributionally robust optimization ‣ Mean Robust Optimization") for choosing $\epsilon$, in practice, we experimentally select $\epsilon$ through cross validation to arrive at the desired guarantee. Therefore, while the theoretical bounds suggest to choose a larger $\epsilon$ when we cluster, this may not be the case experimentally. In fact, for concave $g$, we may even choose a smaller $\epsilon$, due to the increase in the level of conservatism for small $K$. On the other hand, for maximum-of-concave $g$, we do need to choose larger $\epsilon$, as smaller $K$ leads to less conservative solutions.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Choosing $\\epsilon$", "weight": 1.0} -->

However, for both cases, we show a powerful result in the upcoming numerical examples: although for the same $\epsilon$, MRO with $K$ clusters differs in conservatism from Wasserstein DRO ($N$ clusters), there are cases where we can tune $\epsilon$ such that MRO and DRO provide almost identical tradeoffs between objective values and probabilitic guarantees, such that no loss in performance results from choosing a smaller cluster number $K$.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Data with outliers", "weight": 1.0} -->

When the provided dataset contains outliers, one might imagine that the centoids created by the clustering algorithm will be biased towards the outliers. While this is true, the weights of the outliers will not increase through clustering, thus the effect of outliers on these clustered Wasserstein balls is not worse than their effect on the original Wasserstein balls, which include the Wasserstein ball around the outlier point. In fact, by clustering the outlier point with other points, MRO offers protection against the outlier. We demonstrate this in on the numerical experiment in Section 6.6, where we compare three methods: MRO, MRO with outlier removal, and MRO with the outlier considered as its own cluster.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

We now illustrate the computational performance and robustness of the proposed method on various numerical examples. All the code to reproduce our experiments is available, in Python, at

<!-- chunk {"id": "body-0121", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

We run the experiments on the Princeton Institute for Computational Science and Engineering (PICSciE) facility with 20 parallel 2.4 GHz Skylake cores. We solve all optimization problems with MOSEK optimizer with default settings.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

All numerical examples are solved through direct reformulations if not stated otherwise. The calculated in-sample objective value and out-of-sample expected values, as well as the out-of-sample probability of constraint violation, are averaged over 50 independent runs of each experiment. For each run, we generate evaluation data of the same size $N$ as the training dataset.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

For numerical examples with an uncertain objective, the probability of constraint violation is measured as the probability the average out-of-sample value is above the in-sample value. For numerical examples with an uncertain constraint, the probablity of constraint violation is measured as the probability the average constraint value is above zero.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

In Sections 6.1, 6.2, and 6.3, we demonstrate the performance of MRO when the uncertain constraint is concave. In Section 6.4, 6.5, and 6.6, we demonstrate the performance of MRO for maximum-of-affine uncertainty.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Capital budgeting", "weight": 1.0} -->

We consider the capital budgeting problem, where we select a portfolio of investment projects maximizing the total net present value (NPV) of the portfolio, while the weighted sum of the projects is less than a total budget $\theta$. The NPV for all projects is ${\eta{(u)}} \in \text{R}^{n}$, where for each project $j$, $\eta_{j}{(u)}$ is the sum of discounted cash flows $F_{jt}$ over the years $t = {0,\ldots,T}$, i.e., ${\eta_{j}{(u)}} = {\sum_{t = 0}^{T}{F_{jt}/{({1 + u_{j}})}^{t}}}$. Here, $u_{j}$ is the discount rate of project $j$. We formulate the uncertain function to be minimized as

<!-- chunk {"id": "body-0126", "role": "body", "section": "Capital budgeting", "weight": 1.0} -->

where $x = {(x_{1},\ldots,x_{n})} \in {\{ 0,1\}}^{n}$ is the indicator for selecting each project. The discount rate $u_{j}$ is subject to uncertainty, as it depends on several factors, such as the interest rate of the country where project $j$ is located and the level of return the decision-maker wants to compensate the risk. The function $g$ is concave and monotonically increasing in $u$, and we can define a domain $u \geq 0$ so that Assumption 2.1 and Theorem 4.1 applies. The robust problem can be written as

<!-- chunk {"id": "body-0127", "role": "body", "section": "Capital budgeting", "weight": 1.0} -->

where $h$ is the vector of project weights. We refer to and arrive at the convex reformulation for $p = 2$

<!-- chunk {"id": "body-0128", "role": "body", "section": "Capital budgeting", "weight": 1.0} -->

We have variables $x_{j} \in \text{R}$, $z_{k} \in \text{R}^{n}$, $Y_{k} \in \text{R}^{n \times T}$, $\delta_{k} \in \text{R}^{n \times T}$, $\tau \in \text{R}$, $\gamma_{k} \in \text{R}^{2n}$, $s_{k} \in \text{R}$, for $j = {1,\ldots,n}$, $k = {1,\ldots,K}$, and $t = {1,\ldots,T}$. The derivation of reformulation is in Appendix A.11 ‣ Appendix A Appendices ‣ Mean Robust Optimization"). Note that there are variables with total dimension $KnT$, which grows swiftly when any of the parameters are large.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Capital budgeting", "weight": 1.0} -->

For each cluster $k$, we introduce $nT$ new variables for $y$ and $\delta$, as well as $nT$ new power cone constraints, which greatly increases the compuational complexity of the problem.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Choosing $K$", "weight": 1.0} -->

Plotting the clustering value $D{(K)}$ over $K$, we note that the elbow occurs around $K = 2$, which suggests using cross-validation for $K$ values around 2.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Results", "weight": 1.0} -->

We observe in Figure 5 that using two clusters is enough to achieve performance almost identical to that of using 120 clusters. Although from the left image, we see that $K = 2$ slightly upper bounds $K = 120$, from the right, their tradeoffs between the objective value and relevant constraint violation probability ($\beta \leq 0.2$) are largely the same, so we can always tune $\epsilon$ to achieve the same performance and guarantees. Notice that the results for $K = 120$ and $K = 120^{\ast}$ are near identical for small $\epsilon$, where $K = 120^{\ast}$ is the formulation without the support constraint. Therefore, while ${\overline{g}}^{N \ast}{(x)}$ slightly upper bounds ${\overline{g}}^{N}{(x)}$, we can approximate their difference $\Delta \approx 0$ for small enough $\epsilon$, for which the upper bound ${({L/2})}D{(K)}$ thus hold.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Results", "weight": 1.0} -->

In fact in this example, even for larger $\epsilon$ where we observe $\Delta > 0$, the actual difference between ${\overline{g}}^{K}$ and ${\overline{g}}^{N}$ is bounded by ${({L/2})}D{(K)}$. In Figure 6, we see that the elbow of the upper bound is at $K = 2$, and the true difference follows the same trend, matching the suggestion from Figure 4. Therefore, setting $K = 2$ is the optimal decision, with a time reduction of 2 orders of magnitude, and a complexity reduction from 26626 variables and 12000 power cones to 666 variables and 200 power cones.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Quadratic concave uncertainty", "weight": 1.0} -->

We refer to the example from Ben-Tal et al. with concave uncertainty of the form

<!-- chunk {"id": "body-0134", "role": "body", "section": "Quadratic concave uncertainty", "weight": 1.0} -->

where ${h_{i}{(u)}} = {- {{({1/2})}u^{T}A_{i}u}}$, each $A_{i} \in \text{R}^{m \times m}$ a symmetric positive definite matrix, $u \in \text{R}^{m}$, and $x \in \text{R}_{+}^{n}$. For simplicity, we also require that $x$ sums to 1, $p = 2$, and the support of the uncertainty $S = \text{R}^{m}$. Assuming the uncertainty is in the objective, such that the uncertain constraint is created using epigraph form, we solve the problem

<!-- chunk {"id": "body-0135", "role": "body", "section": "Choosing $K$", "weight": 1.0} -->

Plotting the clustering value $D{(K)}$ over $K$, we note that the elbow occurs at $K = 5$, which suggests a choice of $K = 5$.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Results", "weight": 1.0} -->

We observe on the left of Figure 8 that using 5 clusters is enough to achieve performance almost identical to that of using 90 clusters. Indeed, in Figure 9, the elbow of the upper bound (dotted lines) on the difference in objective values is at $K = 5$, and the true difference follows the same trend, corroborating with Figure 7. Furthermore, on the left plot of Figure 9, we note for $K \geq 5$, the tradeoff between the objective value and constraint violation is the same, so we can tune $\epsilon$ to achieve the same performance and guarantees. In fact, for this particular example, using a smaller $K$ such as 1 or 2 may allow us to tune $\epsilon$ to achieve an even better tradeoff. However, this result cannot be guaranteed in general, so the recommended action is still to choose $K = 5$.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Robust log-sum-exp optimization", "weight": 1.0} -->

We also consider uncertainty from Bertimas and den Hertog of the form

<!-- chunk {"id": "body-0138", "role": "body", "section": "Robust log-sum-exp optimization", "weight": 1.0} -->

concave in $u$ and convex in $x$. This function $g$ is monotonically increasing in $u$, and we can define a domain $u \geq 0.01$ so that Assumption 2.1 and Theorem 4.1 apply. Assuming the simple case where the uncertainty is in the objective, we add some further restrictions on $x$ and use a cutting plane procedure to solve, for $p = 2$,

<!-- chunk {"id": "body-0139", "role": "body", "section": "Choosing $K$", "weight": 1.0} -->

Plotting the clustering value $D{(K)}$ over $K$, we note that the elbow occurs at $K = 3$, which suggests using cross-validation for $K$ values around 3.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Results", "weight": 1.0} -->

We observe on the left of Figure 11 that while setting $K$ to smaller values increases the objective value, setting $K = 3$, the number of modes of the underlying distribution, already offers near identical performance to that of setting $K = 90$. On the left of Figure 12, we see that $K = 3$ is at the elbow of upper bound and actual difference, corroborating with Figure 10. Furthermore, we note that setting $K = 3$ and above give identical tradeoff curves, therefore, choosing $K = 3$ is the time-efficient solution.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Sparse portfolio optimization", "weight": 1.0} -->

We consider a market that forbids short-selling and has $m$ assets as. Daily returns of these assets are given by the random vector $d = {(d_{1},\ldots,d_{m})} \in \text{R}^{m}$. The percentage weights (of the total capital) invested in each asset are given by the decision vector $x = {(x_{1},\ldots,x_{n})} \in \text{R}^{n}$. We restrict our selection to at most $\theta$ assets. The underlying data-generating distribution $\mathbf{P}$ is unknown, but we have observed a historical dataset $\mathcal{D}_{N}$. Our objective is to minimize the CVaR with respect to variable $x$,

<!-- chunk {"id": "body-0142", "role": "body", "section": "Sparse portfolio optimization", "weight": 1.0} -->

which represents the average of the $\alpha$ largest portfolio losses that occur. In other words, the $\operatorname{\mathbf{C}\mathbf{V}\mathbf{a}\mathbf{R}}$ term seeks to ensure that the expected magnitude of portfolio losses, when they occur, is low.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Sparse portfolio optimization", "weight": 1.0} -->

From this, we obtain $g$ as the maximum of affine functions,

<!-- chunk {"id": "body-0144", "role": "body", "section": "Sparse portfolio optimization", "weight": 1.0} -->

Using the formulation with $p = \infty$, we can write a convex reformulation of the form

<!-- chunk {"id": "body-0145", "role": "body", "section": "Problem setup", "weight": 1.0} -->

We take stock data from the past 10 years of S&P500, and generate synthetic data from their fitted general Pareto distributions. We choose a generalized Pareto fit over a normal distribution as it better models the heavy tails of the returns. See the Github repository for the code, which uses the "Rsafd" R package Carmona. We let $\alpha = {20\%}$, $m = 50$ stocks, and generate a dataset size of $N = 1000$. Our portfolio can include at most $\theta = 5$ stocks.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Choosing $K$", "weight": 1.0} -->

Plotting the clustering value $D{(K)}$ over $K$, we note that the elbow occurs at $K = 5$, which suggests using cross-validation for $K$ values around 5.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Results", "weight": 1.0} -->

In Figure 14, while setting $K$ to smaller values lead to a decrease in the optimal value across $\epsilon$, we note that for $K = 5$ and above, we can already achieve a tradeoff curve between the optimal value and probability of constraint satisfaction that is similar to that of $K = 1000$, and setting $K = 10$ brings it slightly closer. In Figures 13 and 15, in the plots of $D{(K)}$ and of the upper bound on the difference, we also note that the elbow is around $K = 5$. We thus recommend choosing $K$ through cross validation around 5, as tuning $\epsilon$ for these small $K$ gives 1 - 3 orders of magnitude time reduction.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Facility location", "weight": 1.0} -->

We examine the classic facility location problem. Consider a set of $n$ potential facilities, and $m$ customers. Variable $x \in {\{ 0,1\}}^{n}$ describes whether or not we construct each facility $i$ for $i = {1,\ldots,n}$, with cost $c_{i}$. In addition, we would like to satisfy the uncertain demand $u \in \text{R}^{m}$ at minimal cost. We define variable $X \in \mathbf{R}^{n \times m}$ where $X_{ij}$ corresponding to the portion of the demand of customer $j$ shipped from facility $i$ with corresponding cost $C_{ij}$. Furthermore, $r \in \text{R}^{n}$ represents the production capacity for each facility, and $u \in \text{R}^{m}$ represents the uncertain demand from each customer. For each customer $j$, $X_{j}$ represents the proportion of goods shipped from any facility to that customer, which sums to $1$.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Facility location", "weight": 1.0} -->

For each facility $i$, ${(X^{T})}_{i}$ represents the proportion of goods shipped to any customer. Putting this all together, we obtain multiple affine uncertain capacity constraints,

<!-- chunk {"id": "body-0150", "role": "body", "section": "Facility location", "weight": 1.0} -->

which we combine to create a single maximum-of-affine constraint,

<!-- chunk {"id": "body-0151", "role": "body", "section": "Facility location", "weight": 1.0} -->

Now, to ensure a high probability of constraint satisfaction, we use the $\operatorname{\mathbf{C}\mathbf{V}\mathbf{a}\mathbf{R}}$ reformulation,

<!-- chunk {"id": "body-0152", "role": "body", "section": "Facility location", "weight": 1.0} -->

where we add the auxiliary variable $\tau$. We assume a polyhedral support $S = {\{ u\mid{{Hu} \leq b}\}}$ for the demand, and solve the problem, for $p = \infty$,

<!-- chunk {"id": "body-0153", "role": "body", "section": "Problem setup", "weight": 1.0} -->

To generate data, we set $n = 5$ facilities, $m = 25$ customers, and $N = 50$ data samples. For the $\operatorname{\mathbf{C}\mathbf{V}\mathbf{a}\mathbf{R}}$ reformulation, we set $\alpha = {20\%}$. We set costs $c = {(46.68,58.81,30,42.09,35.87)}$, and generate the two coordinates of each customer's location from a uniform distribution on $\lbrack 0,15\rbrack$. We then calculate $C$ as the $\ell_{2}$ distance between each pair of customers. We set production capacities $r = {}$.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Problem setup", "weight": 1.0} -->

We assume the demand $d$ is supported between 1 and 6, which we write as ${Hu} \leq b$, where $H = {\lbrack{- {II}}\rbrack}^{T}$ and $b$ is the concatenation of two vectors: a vector of $- 1$'s of length $m$, and a vector of $6$'s of length $m$. We generate demands as the combination of two normal distributions. Half of the data is generated from the normal distribution with mean $\mu_{1} = 3$ and variance $\sigma_{1} = 0.9$, the second half has mean $\mu_{1} = 4$ and variance $\sigma_{1} = 0.8$. We then project the demands onto $$.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Problem setup", "weight": 1.0} -->

For the upper bound $\delta{(K,z,\gamma)}$ on ${{\overline{g}}^{N}{(x)}} - {{\overline{g}}^{K}{(x)}}$ from Corollary 4.2.1, we have ${(1/N)}\sum_{k = 1}^{K}\sum_{i \in C_{k}}\max{(\max_{j \leq J}{({(X{\lbrack i\rbrack} - H^{T}\gamma_{jk})},0)}^{T}{(d_{i} - {\overline{d}}_{k})})}$. Note that this upper bounds the difference in constraint values, and only indirectly affects the objective values through restrictions on the feasible region. Therefore, it is not an upper bound on the difference in objective value, merely a rough estimate.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Problem setup", "weight": 1.0} -->

We cannot directly compare this upper bound against the change in constraint values, as at the optimal chonsen $x,X$ for each $K$, which differ due to differences in the feasible regions, the constraint value will always be near 0 for optimality. We thus compare it against the change in objective values.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Choosing $K$", "weight": 1.0} -->

Plotting the clustering value $D{(K)}$ over $K$, we note that the elbow occurs at $K = 2$, which suggests using cross-validation for $K$ values around 2.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Results", "weight": 1.0} -->

As expected of maximum-of-affine $g$, we note in Figure 17 that setting $K$ to smaller values lead to a decrease in the optimal value across different $\epsilon$ values. While $K = 1$ yields poor performance in terms of the probability of constraint violation, we observe that $K = 2$ already yields a tradeoff between the objective and probability of constraint violation close to that of $K = 50$. Through cross-validation with different $K$, we select $K = 5$, which provides a tradeoff curve closer to optimality. As this problem has uncertainty in the constraints and not the objective, the bounds given in Corollary 4.2.1 do not directly reflect the difference in the objective values. However, they do give a reference value and inform us of the general trend of the difference. In this case, they still upper bound the actual difference, as shown in Figure 17. We note that the bounds we use do not depend on ${\overline{g}}^{N \ast}{(x)}$, so it is irrelevant whether or not the support has an affect on the worst-case constraint value.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Results", "weight": 1.0} -->

Overall, choosing $K = 5$ leads to a time reduction of an order of magnitude while achieving near-optimal performance.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Newsvendor problem", "weight": 1.0} -->

We consider a 2-item newsvendor problem where, at the beginning of each day, the vendor orders $x \in \text{R}^{2}$ products at price $h = {}$. These products will be sold at the prices $c = {(5,6.5)}$, until either the uncertain demand $u$ or inventory $x$ is exhausted.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Newsvendor problem", "weight": 1.0} -->

from which we obtain the maximum-of-affine uncertain function $g$ to minimize,

<!-- chunk {"id": "body-0162", "role": "body", "section": "Newsvendor problem", "weight": 1.0} -->

For this problem, we consider the effects of outliers on the performance of MRO. Therefore, we consider the data to have an outlier at $$, the worst-case value of the support set. In Figure 19, we show a set of generated data along with this outlier point.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Newsvendor problem", "weight": 1.0} -->

We consider three ways to solve the problem, decribed as follows.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Newsvendor problem", "weight": 1.0} -->

MRO, where we directly apply MRO to the dataset with the outlier.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Newsvendor problem", "weight": 1.0} -->

ROB-MRO, where we perform preliminary analysis on the dataset to remove the outlier point, then apply MRO to the cleaned dataset.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Newsvendor problem", "weight": 1.0} -->

AUG-MRO, where we perform the clustering step on data without the outlier, then define an augmented distribution supported on $K + 1$ points, where the extra point is the outlier point, with weight $1/N$. The weights of the other clusters are ajusted accordingly.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Problem setup", "weight": 1.0} -->

To generate data, we set $N = 100$ data samples. We assume demand is supported between 0 and 40, which we write as ${Cu} \leq b$, where $C = {\lbrack{- {II}}\rbrack}^{T}$ and $b = {}$. We allow non-integer demand to allow for more variance in the data. We generate the demand from a log-normal distribution, where the underlying normal distribution has parameters

<!-- chunk {"id": "body-0168", "role": "body", "section": "Choosing $K$", "weight": 1.0} -->

Plotting the clustering value $D{(K)}$ over $K$, for the dataset both with and without the outlier, we note an elbow at around $K = 5$, though not very prominent. The recommendation is setting $K$ around 5, to be fine tuned through cross-validation.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Results", "weight": 1.0} -->

In Figure 21, we compare the in and out-of-sample objective values of the three methods, and note their similar performance. While setting $K = 1$ yields suboptimal results, we note that for $K = 5$ and above, we can achieve similar performance as setting $K = 100$. To examine the effect of the outlier more closely, in Figures 22 and 23, we compare, for $K = 10$ and $K = 100$, the objectives and tradeoff curves for the three methods. We note that, when the outlier is averaged with other datapoints, the final in-sample objective may be improved, as the centroid moves closer to the non-outlier points. We observe this in Figure 22, where MRO, in which the outlier may be clustered with other points, offers a lower in-sample objective than AUG-MRO, in which the outlier is considered its own cluster. MRO has in fact offered protection against the outlier. Lastly, as expected, ROB-MRO, where the outlier point is removed, yields the best in-sample results.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Results", "weight": 1.0} -->

Regardless of the method, we note that the final out-of-sample tradeoff curves are near-identical. Comparing Figures 22 and 23, we note that the difference between MRO and ROB-MRO for $K = 10$ is not larger than the difference for $K = N = 100$, which shows that, while removing outliers before solving the problem may be helpful, the effect of outliers will not be worse for MRO compared to classic Wasserstein DRO.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Results", "weight": 1.0} -->

We note in Figure 24 that the upper bound on ${{\overline{g}}^{N}{(x)}} - {{\overline{g}}^{K}{(x)}}$, given in Corollary 4.2.1, holds for MRO. We again note that bounds we observe do not depend on ${\overline{g}}^{N \ast}{(x)}$, so it is irrelevant whether or not the support has an affect on the worst-case constraint value. Regardless, we see that the support only minimally affects the worst-case constraint value, at only at higher values of $\epsilon$. Overall, choosing $K = 5$, we obtain an order of magnitude computational speed-up.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have presented mean robust optimization (MRO), a new data-driven methodology for decision-making under uncertainty that bridges robust and distributionally robust optimization while preserving rigorous probabilistic guarantees. By clustering the dataset before performing MRO, we solve an efficient and computationally tractable formulation with limited performance degradation. In particular, we showed that when the constraints are affine in the uncertainty, clustering does not affect the optimal value of the objective. When the constraint is concave or maximum-of-concave in the uncertainty, we directly quantified the change in worst-case constraint value that is caused by clustering. For problems with objective uncertainty, this directly bounds the change in the optimal value caused by clustering. We demonstrated this result through a set of numerical examples, where we observed the possibility of tuning the size of the uncertainty set such that using a small number of clusters achieves near-identical performance of traditional DRO, with much higher computational efficiency. In the final example, we also demonstrated that MRO offers protection against outliers compared to Wasserstein DRO.
