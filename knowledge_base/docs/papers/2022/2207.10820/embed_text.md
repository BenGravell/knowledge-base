## Introduction

Robust optimization (RO) and distributionally robust optimization (DRO) are popular tools for decision-making under uncertainty due to their high expressiveness and versatility. The main idea of RO is to define an uncertainty set and to minimize the worst-case cost across possible uncertainty realizations in that set. However, while RO often leads to tractable formulations, it can be overly-conservative. To reduce conservatism, DRO takes a probabilistic approach, by modeling the uncertainty as a random variable following a probability distribution known only to belong to an uncertainty set (also called ambiguity set) of distributions. In both RO and DRO, the choice of the uncertainty or ambiguity set can greatly influence the quality of the solution for both paradigms. Good-quality uncertainty sets can lead to excellent practical performance while ill chosen sets can lead to overly-conservative actions and intractable computations.

Traditional approaches design uncertainty sets based on theoretical assumptions on the uncertainty distributions. While these methods have been quite successful, they rely on a priori assumptions that are difficult to verify in practice. On the other hand, the last decade has seen an explosion in the availability of data. This change has brought a shift in focus from a priori assumptions on the probability distributions to data-driven methods in operations research and decision sciences. In RO and DRO, this new paradigm has fostered data-driven methods where uncertainty sets are shaped directly from data. In data-driven DRO, a popular choice of the ambiguity set is the ball of distributions whose Wasserstein distance to a nominal distribution is at most $\epsilon > 0$ Esfahani and Kuhn; Kuhn et al.; Gao; Gao and Kleywegt. When the reference distribution is an empirical distribution, the associated Wasserstein DRO can be formulated as a convex minimization problem where the number of constraints grows linearly with the number of datapoints. While less conservative than RO, data-driven DRO can lead to very large formulations that are intractable, especially in mixed-integer optimization (MIO).

A common idea to reduce the dimensionality of data-driven decision-making problems is to use clustering techniques from machine learning. While clustering has recently appeared in various works within the stochastic programming literature, the focus has been on the improvement of and comparisons to the sample average approximation (SAA) approach and not in a distributionally robust sense. In contrast, recent approaches in the DRO literature cluster data into partitions and either build moment-based uncertainty sets for each partition, or enrich Wasserstein DRO formulations with partition-specific information (e.g., relative weights) Esteban and Morales. While these approaches are promising, clustering is still used as a pre-processing heuristic on the data-sets in DRO, without a clear understanding of how it affects the conservatism of the optimal solutions. In particular, choosing the right clustering parameters to carefully balance computational tractability and out-of-sample performance is still an unsolved challenge.

### Our contributions

In this work, we present mean robust optimization (MRO), a data-driven method that, via machine learning clustering, bridges between RO and Wasserstein DRO.

We design the uncertainty set for RO as a ball around clustered data. Without clustering, our formulation corresponds to the finite convex reformulation in Wasserstein DRO. With just one cluster, our formulation corresponds to the classical RO approach. The number of clusters is a tunable parameter that provides a tradeoff between the worst-case objective value and computational efficiency, which includes both speed and memory usage.

We provide probabilistic guarantees of constraint satisfaction for our method, based on the quality of the clustering procedure.

We derive bounds on the effect of clustering in case of constraints with concave and maximum-of-concave dependency on the uncertainty. In addition, we show that, when constraints are linearly affected by the uncertainty, clustering does not affect the solution nor the probabilistic guarantees.

We show on various numerical examples that, thanks to our clustering procedure, our approach provides multiple orders of magnitude speedups over classical approaches while guaranteeing the same probability of constraint satisfaction. The code to reproduce our results is available at

### Related work

### Robust optimization

RO deals with decision-making problems where some of the parameters are subject to uncertainty. The idea is to restrict data perturbations to be within a deterministic uncertainty set, then optimize the worst-case performance across all realizations of this uncertainty. For a detailed overview of RO, we refer to the survey papers by Ben-Tal and Nemirovski Ben-Tal and Nemirovski and Bertsimas et al. Bertsimas et al., as well as the books by Ben-Tal et al. Ben-Tal et al. and Bertsimas and den Hertog Bertsimas and den Hertog. These approaches, while powerful, may be overly-conservative, and there have been approaches that provide a tradeoff between conservatism and constraint violation.

### Distributionally robust optimization

DRO minimizes the worst-case expected loss over a probabilistic ambiguity set characterized by certain known properties of the true data-generating distribution. Based on the type of ambiguity set considered existing literature on DRO can roughly be defined in two. Ambiguity sets of the first type contain all distributions that satisfy certain moment constraints. In many cases such ambiguity sets possess a tractable formulation, but have also been criticized for yielding overly conservative solutions. Ambiguity sets of the second type enjoy the interpretation of a ball of distributions around a nominal distribution, often the empirical distribution on the observed samples. Wasserstein uncertainty sets are one particular example and enjoy both a tractable primal as well as a tractable dual formulation. We refer to the work by Chen and Paschalidis Chen and Paschalidis for a thorough overview of DRO, and to the work by Zhen et al. Zhen et al. for a general theory on convex dual reformulations. When the ambiguity set is well chosen, DRO formulations enjoy strong out-of-sample statistical performance guarantees. As these statistical guarantees are typically not very sharp, in practice the radius of the uncertainty set is typically chosen through time consuming cross-validation. At the same time, DRO has the downside of being more computationally expensive than traditional robust approaches. We observe for instance that the number of constraints in Wasserstein DRO formulations scale linearly with the number of samples, which can become practically prohibitive especially when integer variables are involved. Our proposed method addresses this problem by reducing the number of constraints through clustering. While many works have recently emerged on the construction of DRO ambiguity sets through the partitioning of data Chen et al.; Esteban and Morales; Perakis et al., or the discretization of the underlying distribution Liu et al., there still exists a gap in the literature. In particular, theoretical bounds on the change in problem performance as affected by the number of clusters, as well as by the quality of the cluster assignment, remain largely unexplored. In this work, we fill the gap by providing such insights.

### Data-driven robust optimization

Data-driven optimization has been well-studied, with various techniques to learn the unknown data-generating distribution before formulating the uncertainty set. Bertsimas et al. Bertsimas et al. construct the ambiguity set as a confidence region for the unknown data-generating distribution $\mathbf{P}$ using several statistical hypothesis tests. By pairing a priori assumptions on $\mathbf{P}$ with different statistical tests, they obtain various data-driven uncertainty sets, each with its own geometric shape, computational properties, and modeling power. We, however, use machine learning in the form of clustering algorithms to preserve the geometric shape of the dataset, without explicitly learning and parametrizing the unknown distribution.

### Distributionally robust optimization as a robust program

Gao and Kleywegt Gao and Kleywegt consider a robust formulation of Wasserstein DRO similar to our mean robust optimization, but without the idea of dataset reduction. Given $N$ samples and a positive integer $K$, they introduce an approximation of Wasserstein DRO by defining a new ambiguity set as a subset of the standard Wasserstein DRO set, containing all distributions supported on $NK$ points with equal probability $1/{({NK})}$, as opposed to the standard set supported on $N$ points. In this work, however, we study how to reduce, instead of increase, the number of variables and constraints to make the Wasserstein DRO problem more tractable by linking it to robust optimization.

### Robust optimization as a distributionally robust optimization program

Xu et al. Xu et al. take inspiration from sample-based optimization problems to investigate probabilistic interpretations of RO. They generalize the ideas of Delage and Ye Delage and Ye, that the solution to a robust optimization problem is the solution to a special Distributionally Robust Stochastic Program (DRSP), where the distributional set contains all distributions whose support is contained in the uncertainty set. In a related vein, Bertsimas et al. Bertsimas et al. show that, under a particular construction of the uncertainty sets, multi-stage stochastic linear optimization can be interpreted as Wasserstein-$\infty$ DRO. We establish a similar equivalence between RO and DRO, focusing especially on Wasserstein-$p$ ambiguity sets for all $p$. We develop an easily interpretable construction of the primal constraints and uncertainty sets, and prove, in view of both the primal and dual problems, that $p = \infty$ is a limiting case of $p \geq 1$. This provides a natural extension of the equivalence proved .

### Probabilistic guarantees in robust and distributionally optimization

Bertsimas et al. Bertsimas et al. propose a disciplined methodology for deriving probabilistic guarantees for solutions of robust optimization problems with specific uncertainty sets and objective functions. They derive a posteriori guarantee to compensate for the conservatism of a priori uncertainty bounds. Esfahani and Kuhn Esfahani and Kuhn obtain finite-sample guarantees for Wasserstein DRO for selecting the radius $\epsilon$ of order $N^{- {1/{\max{\{ 2,m\}}}}}$, where $N$ is the number of samples and $m$ is the dimension of the problem data, while Gao Gao derives finite-sample guarantees for Wasserstein DRO for selecting $\epsilon$ of order $N^{- {1/2}}$ under specific assumptions. We provide theoretical results of a similar vein, with a slightly increased $\epsilon$ to compensate for information lost through clustering and achieve the same probabilistic guarantees. Our theoretical guarantees hold for Wasserstein-$p$ distance for all $p \geq 1$ and $p = \infty$, and are independent of the uncertain function to minimize. These bounds, however, following the literature, are theoretical in nature and not tight in practice, typically resulting in overly-conservative $\epsilon$. The final $\epsilon$ values are usually chosen through empirical empirication - in which case, our formulation, by being lower dimensional, is overall much faster to solve.

### Clustering in stochastic optimization

Clustering in stochastic optimization is closely related to the idea of scenario reduction. First introduced by Dupačová et al. Dupačová et al., scenario reduction seeks to approximate, with respect to a probability metric, an $N$-point distribution with a distribution with a smaller number of points. In particular, Rujeerapaiboon et al. Rujeerapaiboon et al. analyze the worst-case bounds on scenario reduction the approximation error with respect to the Wasserstein metric, for initial distributions constrained to a unit ball. They provide constant-factor approximation algorithms for $K$-medians and $K$-means clustering. Later, Bertsimas and Mundru Bertsimas and Mundru apply this idea to two-stage stochastic optimization problems, and provide an alternating-minimization method for finding optimal reduced scenarios under the modified objective. They also provide performance bounds on the stochastic optimization problem for different scenarios. Jacobson et al., Emelogu et al. Emelogu et al., Beraldi et al. Beraldi and Bruni, and Chen Chen apply a similar idea of clustering to reduce the sample/scenario size, then compare the results against the classical SAA approach where the sample size is not reduced. In MRO, we adapt and extend the scenario reduction approach to Wasserstein DRO, where upon fixing the reduced scenario points to ones found by the clustering algorithm, we allow for variation around these reduced points. We then provide performance bounds on the DRO problem depending on the number of clusters.

### Data compression in data-driven problems

Fabiani and Goulart Fabiani and Goulart compress data for robust control problems by minimizing the Wasserstein-1 distance between the original and compressed datasets, and observe a slight loss in performance in exchange for reduced computation time. While related, this is orthogonal to our approach of using machine learning clustering to reduce the dataset, where we include results and theoretical bounds for a more general set of robust optimization problems with Wasserstein-$p$ distance, and demonstrate conditions under which no performance loss is necessary.

### Layout of the paper

In Section 2, we present our approach for concave uncertainty constraints, then extend the results to maximum-of-concave functions. In Section 3, we present connections to distributionally robust optimization, and give theoretical guarantees on constraint satisfaction. In Section 4, we analyze the effect on clustering on the worst-case value of the MRO solutions for both concave and maximum-of-concave constraints. In Section 5, we give guidelines for choosing hyperparameters. In Section 6, we provide computational verification of the speedups obtained through our methodology. In Section 7, we summarize our conclusions.

## Mean robust optimization

### The problem

We consider an uncertain constraint of the form, where $x \in \mathcal{X} \subseteq \text{R}^{n}$ is the optimization variable and $\mathcal{X}$ is a compact set, $u \in \text{R}^{m}$ is an uncertain parameter, and $- {g{(u,x)}}$ is proper, convex, and lower-semicontinuous in $u$ for all $x$. Throughout this paper, we assume the support $S$ of $u$ to live within the domain of $g$ for the variable $u$, which we will refer to as $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}_{u}g$, i.e., $S \subseteq {\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}_{u}g}$. We assume $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}_{u}g$ is independent of $x$, and that the following assumption holds.

### Assumption 2.1

The domain $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}_{u}g$ is $\text{R}^{m}$. Otherwise, $g$ is either element-wise monotonically increasing in $u$ and only has a (potentially) lower-bounded domain, or element-wise monotonically decreasing in $u$ and only has a (potentially) upper-bounded domain.

This assumption on the domain and monotonicity of $g$ is very common in practice as it is satisfied by linear and quadratic functions, as well as other common functions (e.g., $\log{(u)}$, and $1/{({1 + u})}$).

In Section 2.4, we extend our results for $g$ being the maximum of of concave functions, each satisfying the aforementioned conditions.

The RO approach defines an uncertainty set $\mathcal{U} \subseteq \text{R}^{m}$ and forms the robust counterpart as where the uncertainty set is chosen so that for any solution $x$, the above holds with a certain probability. We define this in terms of expectation, where $\mathbf{P}$ is the unknown distribution of the uncertainty $u$.

### Risk measures

Expectation constraints of the form can represent popular risk measures, and can imply constraints commonly used in chance-constrained programming (CCP). In CCP, the probabilistic constraint considered is which corresponds to the value at risk being nonpositive, i.e., Unfortunately, except in very special cases, the value at risk function is intractable. A tractable approximation of the value at risk is the conditional value at risk, defined as where ${(a)}_{+} = {\max{\{ a,0\}}}$. This expression can be modeled through our approach, by writing ${\operatorname{\mathbf{C}\mathbf{V}\mathbf{a}\mathbf{R}}{({g{(u,x)}},\alpha)}} = {\inf_{\tau}{\{{\text{E}{({\hat{g}{(u,x,\tau)}})}}\}}}$, where ${\hat{g}{(u,x,\tau)}} = {\tau + {{({1/\alpha})}{({{g{(u,x)}} - \tau})}_{+}}}$ is the maximum of concave functions, which we study in Sections 2.4, 6.4, and 6.5. It is well known from Uryasev and Rockafellar that the relationship between these probabilistic guarantees of constraint satisfaction is Therefore, our expectation constraint implies common chance constraints.

### Finite-sample guarantees

In data-driven optimization, while $\mathbf{P}$ is unknown, it is partially observable through a finite set of $N$ independent samples of the random vector $u$. We denote the training dataset of these samples by $\mathcal{D}_{N} = {\{ d_{i}\}}_{i \leq N} \subseteq S$, and note that this dataset is governed by $\mathbf{P}^{N}$, the product distribution supported on $S^{N}$. A data-driven solution of a robust optimization problem is a feasible decision ${\hat{x}}_{N} \in \text{R}^{n}$ found using the data-driven uncertainty set $\mathcal{U}$, which in turn is constructed by the training dataset $\mathcal{D}_{N}$. Specifically, the feasible decision and data-driven uncertainty set $\mathcal{U}$ we construct must imply the probabilistic guarantee where $\beta > 0$ is the specified probability of constraint violation. From now, when we refer to probabilistic guarantees of constraint satisfaction, it will be a reference to.

### Our approach

To meet the probabilistic guarantees outlined above, we propose to construct ${\hat{x}}_{N}$ to satisfy particular constraints, with respect to a particular uncertainty set.

### Case $p \geq 1$

In the case where $p \geq 1$, the set we consider takes the form where we partition $\mathcal{D}_{N}$ into $K$ disjoint subsets $C_{k}$, and ${\overline{d}}_{k}$ is the centroid of the $k$th subset, for $k = {1,\ldots,K}$. The weight $w_{k} > 0$ of each subset is equivalent to the proportion of points in the subset, i.e., $w_{k} = {{|C_{k}|}/N}$. We choose $p$ to be an integer exponent, and $\epsilon$ will be chosen depending on the other parameters to ensure satisfaction of the probability guarantee. When $p = 2$ and $S = \text{R}^{m}$, the set can be visualized as an ellipsoid in $\mathbf{R}^{Km}$ with the center formed by stacking together all ${\overline{d}}_{k}$ into a single vector of dimension $\mathbf{R}^{Km}$. When we additionally have $K = N$ or $K = 1$, this ellipsoid becomes a ball of dimension $\text{R}^{Nm}$ or $\text{R}^{m}$ respectively, as shown in Figure 1.

Figure 1: Visualizing the uncertainty set 𝒰 (N, ϵ) and 𝒰 (1, ϵ) as high dimension balls when p = 2.

### Case $p = \infty$

In the case where $p = \infty$, the set we consider takes a more specific form, where the constraints for individual $v_{k}$ become decoupled. See Figure 2 for an example when $K = 3$ and $K = 1$. This decoupling follows the result for the Wasserstein type $p = \infty$ metric, as our uncertainty set is analogous to the set of all distributions within Wasserstein-$\infty$ distance of $\overline{d}$. We note that, if any of the decoupled constraints are violated, then ${\lim_{p\rightarrow\infty}{\sum_{k = 1}^{K}{w_{k}{\|{v_{k} - {\overline{d}}_{k}}\|}^{p}}}} \geq \epsilon^{p}$, and the summation constraint will be violated.

Figure 2: Visualizing the decoupled uncertainty set 𝒰 (K, ϵ) with p = ∞.

For both cases, $p \geq 1$ and $p = \infty$, when $K = 1$, we have a simple uncertainty set: a ball of radius $\epsilon$ around the empirical mean of the entire dataset, ${{\mathcal{U}{(1,\epsilon)}} = \left\{ {v \in S}\mid{{\|{v - \overline{d}}\|} \leq \epsilon} \right\}}.$ This is equivalent to the uncertainty set of traditional RO, as it is of the same dimension $m$ as the uncertain parameter. When $K = N$ and $w_{k} = {1/N}$, both cases closely resemble the ambiguity sets of Wasserstein-$p$ DRO.

Having defined the uncertainty set, we now introduce constraints of the form where $g$ is defined in the original constraint. The weights $w_{k}$ correspond to the ones defined in the uncertainty set. Putting everything together, ${\hat{x}}_{N}$ is the solution to the robust optimization problem where $f$ is the objective function. We call this problem the mean robust optimization (MRO) problem.

### Data-driven procedure

Given the problem data, we formulate the uncertainty set from clustered data using machine learning, with the choice of $K$ and $\epsilon$ chosen experimentally. Then, we solve the MRO problem to arrive at a data-driven solution ${\hat{x}}_{N}$ which satisfies the probabilistic guarantee, see Figure 3.

Figure 3: Mean robust optimization procedure.

### Solving the robust problem

We now outline two ways to solve the MRO problem, using a direct convex reformulation and using a cutting plane algorithm. The reformulation and cutting plane procedure follow usual techniques for RO problems in existing literature, with adaptations made for the MRO setup, as well as a reformulation derived for the case $p = \infty$. We include simple examples and pseudocode for completeness.

### Direct convex reformulation for $p \geq 1$

In the case where $p \geq 1$, the MRO can be rewritten as the optimization problem which, by dualizing the inner maximization problem, has the following reformulation: with variables $\lambda \in \text{R}$, $s_{k} \in \text{R}$, $z_{k} \in \text{R}^{m}$, and $y_{k} \in \text{R}^{m}$. Here, ${{\lbrack{- g}\rbrack}^{\ast}{(z,x)}} = {{\sup_{u \in {\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}_{u}g}}{z^{T}u}} - {\lbrack{- {g{(u,x)}}}\rbrack}}$ is the conjugate of $- g$, ${\sigma_{S}{(z)}} = {\sup_{u \in S}{z^{T}u}}$ is the support function of $S \subseteq \mathbf{R}^{m}$, $\parallel \cdot \parallel_{\ast}$ is the dual norm of $\parallel \cdot \parallel$, and ${\phi{(q)}} = {{({q - 1})}^{({q - 1})}/q^{q}}$ for $q > 1$. Note that $q$ satisfies ${{1/p} + {1/q}} = 1$, i.e., $q = {p/{({p - 1})}}$. When $p = 1$ and $q = \infty$, we note the formulation. The support function $\sigma_{S}$ is also the conjugate of $\chi_{S}$, which is defined ${\chi_{S}{(u)}} = 0$ if $u \in S$, and $\infty$ otherwise. The proof of the derivation and strong duality of the constraint is delayed to Appendix A.1 ‣ Appendix A Appendices ‣ Mean Robust Optimization"). Since the dual of the constraint becomes a minimization problem, any feasible solution that with objective less than or equal to $0$ will satisfy the constraint, so we can remove the minimization to arrive at the above form. While traditionally we take the supremum instead of maximizing, here the supremum is always achieved as we assume $g$ to be upper-semicontinuous. For specific examples of the conjugate forms of different $g$, see Bertsimas and den Hertog and Beck.

When $K$ is set to be $N$, $w_{k}$ is $1/N$, and this is of an analogous form to the convex reduction of the worst case problem for Wasserstein DRO, which we will introduce in Section 3.

We note the special case when $p = 1$. We observe from that Therefore, the above formulation becomes

### Example with affine constraints

Consider a single affine constraint of the form where $a \in \text{R}^{n}$, $P \in \text{R}^{n \times m}$, and $b \in \text{R}$. In other words, ${g{(u,x)}} = {{{({a + {Pu}})}^{T}x} - b}$, and the support set is $S = \text{R}^{m}$. Note that, in this case, $y_{k}$ must be $0$ for the support function $\sigma_{S}{(y_{k})}$ to be finite. We compute the conjugate as To substitute $\sigma_{S}{(y_{k})}$ and ${\lbrack{- g}\rbrack}^{\ast}{({z_{k} - y_{k}},x)}$ into, we note that $y_{k} = 0$ and $z_{k} = {- {P^{T}x}}$, i.e., $z_{k}$ is independent from $k$. By combining the $K$ constraints, we arrive at the form where the number of variables or constraints does not depend on $K$. Since vector $\sum_{k = 1}^{K}{w_{k}{\overline{d}}_{k}}$ is the average of the datapoints in $\mathcal{D}_{N}$ for any $K \in {\{ 1,\ldots,N\}}$, this formulation corresponds to always choosing $K = 1$.

### Direct convex reformulation for $p = \infty$

In the case where $p = \infty$, the MRO can be rewritten as the optimization problem which has a reformulation where the constraint above is dualized, with new variables $s_{k} \in \text{R}$, $z_{k} \in \text{R}^{m}$, and $y_{k} \in \text{R}^{m}$. The proof is delayed to Appendix A.2 ‣ Appendix A Appendices ‣ Mean Robust Optimization").

### Remark 2.1 (Case $p = \infty$ is the limit of case $p \geq 1$)

In terms of the primal problem, is the limiting case of as $p\rightarrow\infty$. In terms of the reformulated problem with dualized constraints, problem is the limiting case of as $p\rightarrow\infty$. The proofs are delayed to Appendix A.5 and Appendix A.6 respectively. These proofs extend the ideas stated .

### Example with affine constraints

Consider again the case of affine constraint as in with support set $S = \text{R}^{m}$, now with $p = \infty$. Following a similar derivation as, we substitute the conjugate function ${\lbrack{- g}\rbrack}^{\ast}$ in problem, we can obtain where the number of constraints and variables does not depend on $K$. Similairy to problem, the term $\sum_{k = 1}^{K}{w_{k}{\overline{d}}_{k}}$ is the average of the datapoints in $\mathcal{D}_{N}$ for any $K \in {\{ 1,\ldots,N\}}$. Therefore, the choice of $K$ does not affect this formulation. This can be viewed as the robust counterpart when the uncertainty set is a norm ball of radius $\epsilon$ centered at ${({1/N})}{\sum_{i = 1}^{N}d_{i}}$ Note that, if $\overline{d} = 0$ the constraint can be simplified even further, obtaining ${{a^{T}x} + {\epsilon{\|{P^{T}x}\|}_{\ast}}} \leq b$, which corresponds to the robust counterpart in RO with norm uncertainty sets,.

### Remark 2.2

When $g$ is affine and $S = \text{R}^{m}$, for any $\epsilon$ and norm, the convex reformulations for $p = 1$ and $p = \infty$ are identical. The proof appears in Appendix A.7.

### Cutting plane algorithm

The second approach to solve problem (MRO) is to use a cutting plane procedure, in which we consider the minimization problem where $x$ is the variable and $S$ a finite set of values for the uncertainty, and the maximization problem over $u$ with $x^{k}$ fixed, The procedure works as follows. We first solve with a set $\hat{S} = {\{\overline{u}\}}$, where $\overline{u}$ is nominal value of the uncertainty, obtaining $x^{k}$. Then, we solve, obtaining $u^{k}$. If ${\overline{g}{(u^{k},x^{k})}} > 0$, then we add $u^{k}$ to the set $\hat{S}$. Otherwise, we terminate. This procedure is summarized in Algorithm 1. As demonstrated by Bertimas et al. Bertsimas et al., the cutting plane and convex reformulation methods are comparable in terms of performance, thus both are viable.

1:given $\hat{S} = {\{\overline{u}\}}$ 3: xk← solve minimization problem over x 4: uk← solve maximization problem over u Algorithm 1 Cutting plane algorithm to solve (MRO)

### Maximum-of-concave constraint function

We now consider a more general maximum-of-concave function with each $- g_{j}$ being proper, convex, and lower-semicontinuous in $u$ for all $x$. When we take $J = 1$, we arrive back at the formulations given in Section 2. Note that any problem with multiple uncertain constraints ${{{g_{j}{(u,x)}},j} = 1},{\ldots,J}$, where we assume the usual conditions on $g_{j}$, can be combined to create a joint constraint of this maximum-of-concave form. As mentioned in Section 2.1, this can also be used to model $\operatorname{\mathbf{C}\mathbf{V}\mathbf{a}\mathbf{R}}$ constraints, which has a maximum-of-concave analytical form.

### Problem parametrization

We now consider constraints of the form where $\alpha \in \Gamma$, with $\Gamma = \left. \{\alpha \middle| {{{\sum_{j = 1}^{J}\alpha_{jk}} = w_{k}},{\alpha_{jk} \geq {{0{\forall k}},j}}}\} \right.$. For each constituent function $g_{j}$, the uncertainty set contains a set of vectors $(v_{j1},\ldots,v_{jK})$, and a set of parameters $(\alpha_{j1},\ldots,\alpha_{jK})$ to denote the fraction of mass assigned to that function for each $k$. The total amount of mass assigned for each cluster, $\sum_{j = 1}^{J}\alpha_{jk}$, is the weight of the cluster, $w_{k}$.

We use a summation over weighted pieces $g_{j}$ instead of a maximum over $g_{j}$, as this is a generalization of the maximum, and has a more natural dual reformulation. We take inspiration , where $\alpha$ arises from the extremal distribution for Wasserstein DRO. Note that the intuitive maximization over $g_{j}$'s is analogous to setting $\alpha_{jk} = w_{k}$ for a specific $j$ for each $k$, and $\alpha_{jk} = 0$ otherwise.

The uncertainty set is given as follows.

### Case $p \geq 1$

In the case where $p \geq 1$, we have Note that the single concave case given previously follows when we take $J = 1$. All parameters are defined as in the single concave case.

### Case $p = \infty$

In the case where $p = \infty$, the set we consider becomes where we once again introduce weight parameters $\alpha$.

Following these changes, ${\hat{x}}_{N}$ is again the solution to the robust optimization problem (MRO), defined now with the generalized uncertainty set and constraint.

### Solving the robust problem

We give the direct reformulation approach for solving the generalized problem for $p \geq 1$. The case $p = \infty$ is delayed to Appendix A.4. We write the MRO problem as the optimization problem and, by dualizing the inner maximization problem, arrive at the reformulation: with variables $\lambda \in \text{R}$, $s_{k} \in \text{R}$, $z_{jk} \in \text{R}^{m}$, and $y_{jk} \in \text{R}^{m}$. The proof is delayed to Appendix A.3 ‣ Appendix A Appendices ‣ Mean Robust Optimization"). Again, while traditionally we take the supremum instead of maximizing, here the supremum is always achieved as we assume $g_{j}$ to be upper-semicontinuous for all $j$.

In addition, when $K$ is set to be $N$, and $w_{k}$'s are $1/N$, this is also of an analogous form to the convex reduction of the worst case problem for Wasserstein DRO, given in Section 3.

## Links to Wasserstein distributionally robust optimization

Distributionally robust optimization (DRO) solves the problem where the ambiguity set $\mathcal{P}_{N}$ contains, with high confidence, all distributions that could have generated the training samples $\mathcal{D}^{N}$, such that the probabilistic guarantee is satisfied. Wasserstein DRO constructs $\mathcal{P}_{N}$ as a ball of radius $\epsilon$ with respect to the Wasserstein metric around the empirical distribution ${\hat{\mathbf{P}}}^{N} = {\sum_{i = 1}^{N}{\delta_{d_{i}}/N}}$, where $\delta_{d_{i}}$ denotes the Dirac distribution concentrating unit mass at $d_{i} \in \mathbf{R}^{m}$. Specifically, we write where $\mathcal{M}{(S)}$ is the set of probability distributions supported on $S$ satisfying a light-tailed assumption (more details in section 3.1), and Here, $p$ is any integer greater than 1, and $\Pi$ is any joint distribution of $u$ and $u'$ with marginals $\mathbf{Q}$ and $\mathbf{Q}'$.

When $K = N$, the constraint of the DRO problem is equivalent to the constraint of (MRO). In particular, for case $p \geq 1$, the expression is equivalent to the dual of the constraint of, when $K = N$, and $w_{k} = {1/N}$. This is noted. We give a proof of strong duality in Appendix A.8 ‣ Appendix A Appendices ‣ Mean Robust Optimization"). This is the dual of the generalized max-of-concave form, which is equivalent to the dual of the single concave form when $J = 1$. By the same logic, in the case where $p = \infty$, the expression is equivalent to the dual of the constraint of. Given the above reductions, we can rewrite the Wasserstein DRO problem in the same form as, the MRO problem.

Our approach can then be viewed as a form of Wasserstein DRO, with the difference that, when $K < N$, we deal with the clustered and averaged dataset. We form $\mathcal{P}_{N}$ as a ball around the empirical distribution ${\hat{\mathbf{P}}}^{K}$ of the centroids of our clustered data where $w_{k}$ is the proportion of data in cluster $k$. This formulation allows for the reduction of the sample size while preserving key properties of the sample, which translates directly to a reduction in the number of constraints and variables, while maintaining high quality solutions.

### Satisfying the probabilistic guarantees

As we have noted the parallels between MRO and Wasserstein DRO, we now show that the conditions for satisfying the probabilistic guarantees are also analogous.

### Case $p \geq 1$

Wasserstain DRO satisfies if the data-generating distribution, supported on a convex and closed set $S$, satisfies a light-tailed assumption: there exists an exponent $a > 0$ and $t > 0$ such that ${A = {\text{E}^{\mathbf{P}}{({\exp{({t{\| u\|}^{a}})}})}} = {\int_{S}{{\exp{({t{\| u\|}^{a}})}}\mathbf{P}{({du})}}} < \infty}.$ We refer to the following theorem.

### Theorem 3.1 (Measure concentration )

If the light-tailed assumption holds, we have where $\phi$ is an exponentially decaying function of $N$.

Theorem (3.1). ‣ Case 𝑝≥1. ‣ 3.1 Satisfying the probabilistic guarantees ‣ 3 Links to Wasserstein distributionally robust optimization ‣ Mean Robust Optimization")) estimates the probability that the unknown data-generating distribution $\mathbf{P}$ lies outside the Wasserstein ball $\mathbf{B}_{\epsilon}^{p}{({\hat{\mathbf{P}}}^{N})}$, which is our ambiguity set. Thus, we can estimate the smallest radius $\epsilon$ such that the Wasserstein ball contains the true distribution with probability $1 - \beta$, for some target $\beta \in {}$. We equate the right-hand-side to $\beta$, and solve for $\epsilon_{N}{(\beta)}$ that provides us the desired guarantees for Wasserstein DRO.

### Case $p = \infty$

When $p = \infty$, Bertsimas et al. note that the light-tailed assumption is no longer sufficient. Wasserstein DRO satisfies under stronger assumptions, as given in the following theorem.

### Theorem 3.2 (Measure concentration, $\mathbf{p} = \infty$ )

Let the support $S \subset \text{R}^{m}$ of the data-generating distribution be a bounded, connected, open set with Lipschitz boundary. Let $\mathbf{P}$ be a probability measure on $S$ with density $\rho:{S\rightarrow{(0,\infty)}}$, such that there exists $\lambda \geq 1$ for which ${{1/\lambda} \leq {\rho{(x)}} \leq \lambda},{{\forall x} \in S}$. Then, where $\phi$ is an exponentially decaying function of $N$.

We can again equate the right-hand-side to $\beta$ and find $\epsilon_{N}{(\beta)}$. We extend this result to the clustered set in MRO.

### Theorem 3.3 (MRO finite sample guarantee)

Assume the light-tailed assumption holds when $p \geq 1$, and the corresponding assumptions hold when $p = \infty$. If $\beta \in {}$, $\eta_{N}{(K)}$ is the average $p$-th powered distance of data-points in $\mathcal{D}_{N}$ from their assigned cluster centers, and ${\hat{x}}_{N}$ is the optimal solution to (MRO) with uncertainty set $\mathcal{U}{(K,{{\epsilon_{N}{(\beta)}} + {\eta_{N}{(K)}^{1/p}}})}$, then the finite sample guarantee holds.

### Proof

Compared with Wasserstein DRO, MRO has to account for the additional difference between the two empirical distributions ${\hat{\mathbf{P}}}^{N}$ and ${\hat{\mathbf{P}}}^{K}$. We can write If we introduce a new parameter, $\eta_{N}{(K)}$, defined as the average $p$-powered distance with respect to the norm used in the Wasserstein metric, of all data-points in $\mathcal{D}_{N}$ from their assigned cluster centers ${\overline{d}}_{k}$, we notice that where we have replaced the integral with a finite sum, as the distributions are discrete. Therefore, by Theorems 3.1). ‣ Case 𝑝≥1. ‣ 3.1 Satisfying the probabilistic guarantees ‣ 3 Links to Wasserstein distributionally robust optimization ‣ Mean Robust Optimization"), 3.2). ‣ Case 𝑝=∞. ‣ 3.1 Satisfying the probabilistic guarantees ‣ 3 Links to Wasserstein distributionally robust optimization ‣ Mean Robust Optimization") and the triangle inequality for the Wasserstein metric Clement and Desch, with probability at least $1 - \beta$. We thus have which implies the uncertainty set $\mathcal{U}{(K,{{\epsilon_{N}{(\beta)}} + {\eta_{N}{(K)}^{1/p}}})}$ contains all possible realizations of uncertainty with probability $1 - \beta$, so the finite sample guarantee holds. ∎

## Worst-case value of the uncertain constraint

The MRO approach is closely centered around the concept of clustering to reduce sample size while maintaining sample diversity. We wish to cluster points that are close together, such that the objective is only minimally affected. With this goal, we then cluster data-points such that the average distance of the points in each cluster to their data-center is minimized, where ${\overline{d}}_{k}$ is the mean of the points in cluster $C_{k}$. A well-known algorithm is $K$-means, where we create $K$ clusters by iteratively solving a least-squares problem. Note that once the clusters have been selected, and we assume it to be optimal (i.e. attain $D{(K)}$), then for the case $p = 2$, we have ${\eta_{N}{(K)}} = {D{(K)}}$ from Theorem 3.3. ‣ Case 𝑝=∞. ‣ 3.1 Satisfying the probabilistic guarantees ‣ 3 Links to Wasserstein distributionally robust optimization ‣ Mean Robust Optimization").

In this section, we then show the effects of clustering on the worst-case value of the constraint function in (MRO). We prove two sets of results, corresponding to $g$ given as a single concave function, and as a more general maximum-of-concave function. For the latter, we also include the special case of the maximum-of-affine function.

### Single concave function

For the simplest case of a single concave function, we prove that when the support is large enough, If $g$ is affine in $u$, MRO does not increase the worst-case value, regardless of $K$.

If $g$ is concave in $u$ and satisfies certain smoothness conditions, MRO has a higher worst-case value than Wasserstein DRO and the increase is inversely related to the number of clusters $K$. In other words, the smaller the $K$, the higher the worst-case value.

### Quantifying the clustering effect

To quantify the effect of clustering, we calculate the difference between the following formulations of the worst-case value of the constraint in (MRO) | | ${{\overline{g}}^{N}{(x)}} = \underset{v_{1}\ldotsv_{N}}{\text{maximize}}$ | $\frac{1}{N}{\sum\limits_{i = 1}^{N}{g{(v_{i},x)}}}$ | | (MRO-N) | | | subject to | ${\frac{1}{N}{\sum\limits_{i = 1}^{N}{\|{v_{i} - d_{i}}\|}^{p}}} \leq \epsilon^{p}$ | | | | | ${{\overline{g}}^{K}{(x)}} = \underset{u_{1}\ldotsu_{K}}{\text{maximize}}$ | $\sum\limits_{k = 1}^{K}{\frac{|C_{k}|}{N}g{(u_{k},x)}}$ | | (MRO-K) | | | subject to | ${\sum\limits_{k = 1}^{K}{\frac{|C_{k}|}{N}{\|{u_{k} - {\overline{d}}_{k}}\|}^{p}}} \leq \epsilon^{p}$ | | | | | ${{\overline{g}}^{N \ast}{(x)}} = \underset{v_{1}\ldotsv_{N}}{\text{maximize}}$ | $\frac{1}{N}{\sum\limits_{i = 1}^{N}{g{(v_{i},x)}}}$ | | (MRO-N\*) | | | subject to | ${{\frac{1}{N}{\sum\limits_{i = 1}^{N}{\|{v_{i} - d_{i}}\|}^{p}}} \leq \epsilon^{p}},$ | | | where (MRO-N) is the formulation of the constraint without clustering, akin to traditional Wasserstein DRO, (MRO-N\*) is the same, except we drop the support constraint, and (MRO-K) is the formulation with $K$ clusters. From here, when we mention that the support affects the worst-case constraint value, we refer to situations where at least one of the constraints $v_{i} \in S$ for $i = {1,\ldots,N}$ is binding. Formally, the definition is ${{\overline{g}}^{N}{(x)}} \neq {{\overline{g}}^{N \ast}{(x)}}$ for any $x$ feasible for the DRO problem. We note a sufficient but not necessary condition for the support to not affect the worst-case constraint value: the situation in which the support doesn't affect the uncertainty set, which is defined as If the support satisfies this condition, then we can conclude that ${{\overline{g}}^{N}{(x)}} = {{\overline{g}}^{N \ast}{(x)}}$ for any $x$ feasible for the DRO problem, and obtain improved bounds below. While the condition depends on the location of the datapoints, it is acceptable to have this dependency, as this is a condition we can check given data to potentially improve the following bounds, without having to solve the MRO problem.

With these definitions, we can construct solutions for (MRO-N), (MRO-K), and (MRO-N\*) to prove the following relations.

### Theorem 4.1

With the same $x$ and $\epsilon$, and for any integer $p \geq 1$, we always have Suppose that Assumption 2.1 holds, and $- g$ satisfies an $L$-smooth condition on its domain with respect to the $\ell_{2}$-norm and for a given $x$, Then, with the same $x$ and $\epsilon$, and for any integer $p \geq 1$, we always have The proof is delayed to Appendix A.9. The results also hold for $p = \infty$, as we have shown in Remark 2.1. ‣ 2.3.2 Direct convex reformulation for 𝑝=∞ ‣ 2.3 Solving the robust problem ‣ 2 Mean robust optimization ‣ Mean Robust Optimization") that the case $p = \infty$ is the limit of the case $p \geq 1$, and these results hold under the limit.

Let $\Delta$ be the maximum difference in constraint value resultant from relaxing the support constraint on the MRO uncertainty sets, i.e., $\Delta = {\max_{x \in \mathcal{X}}\left( {{{\overline{g}}^{N \ast}{(x)}} - {{\overline{g}}^{N}{(x)}}} \right)}$, subject to $x$ being feasible for problem (MRO). As we assume Assumption 2.1 to hold, combined with the smoothness of $g$, we note that when solving for ${\overline{g}}^{N \ast}{(x)}$, the chosen $v_{i}$ values without the support constraint will still remain in the domain $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}_{u}$ of $g$. Refer to a similar argument in Appendix A.9 (ii) for details. The function ${{\overline{g}}^{N \ast}{(x)}} - {{\overline{g}}^{N}{(x)}}$ is then continuous in $x$ and everywhere defined for $x \in \mathcal{X}$, thus maximizing with respect to $\mathcal{X}$, a compact set, the value $\Delta$ is finite. Then, we observe that ${{{\overline{g}}^{K}{(x)}} - {{\overline{g}}^{N}{(x)}}} \leq {\Delta + {{({L/2})}D{(K)}}}$ for all such $x$, so the smaller the $D{(K)}$, (i.e., higher-quality clustering procedure), the smaller the increase in the worst-case constraint value. In addition, the value $\Delta$ is independent of $K$, as we calculate it with only ${\overline{g}}^{N \ast}{(x)}$ and ${\overline{g}}^{N}{(x)}$.

### Remark 4.1

While $\Delta$ could be constructed to be arbitrarily bad, in practice, we expect our relevant range of $\epsilon$ to be small enough such that the difference is insignificant. We can then approximate $\Delta \approx 0$ and simply use the upper bound ${({L/2})}D{(K)}$, as this bound is often not tight. See Sections 6.5 and 6.1 for examples.

### Uncertain objective

When the uncertainty is in the objective, Theorem 4.1 quantifies the difference in optimal values.

### Corollary 4.1.1

Consider the problem where $g$ is itself the objective function we would like to minimize and $X \subseteq \text{R}^{n}$ represents the constraints, which are deterministic. Then, ${({L/2})}D{(K)}$ + $\Delta$ upper bounds the difference in optimal values of the MRO problem with $K$ and $N$ clusters.

### Uncertain constraints

When the uncertainty is in the constraints, the difference between ${\overline{g}}^{K}{(x)}$ and ${\overline{g}}^{K}{(x)}$ no longer directly reflects the difference in optimal values. Instead, clustering creates a restriction on the feasible set for $x$ as follows. For the same $\hat{x}$, ${\overline{g}}^{K}{(\hat{x})}$ takes a greater value than ${\overline{g}}^{N}{(\hat{x})}$. Since both of them are constrained to be nonpositive from (MRO), the feasible region with $K$ clusters is smaller.

### Affine dependence on uncertainty

As a special case, when $g$ is affine in $u$, $L = 0$, so we observe the following corollary.

### Corollary 4.1.2 (Clustering with affine dependence on the uncertainty)

If $g{(u,x)}$ is affine in $u$ and the worst-case constraint value is not affected by the support constraint, then clustering makes no difference to the optimal value and optimal solution to (MRO).

### Proof

In view of the primal problem and constraints, from Theorem 4.1, if $g{(u,x)}$ is affine in $u$ and the support does not affect the uncertainty set, ${{\overline{g}}^{N}{(x)}} = {{\overline{g}}^{K}{(x)}}$. So for some fixed $\hat{x}$ we have ${{{\overline{g}}^{K}{(\hat{x})}} \leq 0}\Leftrightarrow{{{\overline{g}}^{N}{(\hat{x})}} \leq 0}$. Therefore, The feasible region of (MRO) is identical for $K = N$ and $K < N$, and the optimal solutions will be identical so long as the optimal solution to (MRO) is unique. In view of the dual problem and constraints, if $g{(u,x)}$ is affine in $u$ following, we observe from that the only term dependent on $K$ is ${({P^{T}x})}^{T}{\sum_{k = 1}^{K}{w_{k}{\overline{d}}_{k}}}$, which is equivalent for all $K$. ∎

### Maximum-of-concave functions

We now consider the more general case of a maximum-of-concave constraint function, ${g{(u,x)}} = {{\max_{j \leq J}g_{j}}{(u,x)}}$, subject to a polyhedral support, $S = {\{ u\mid{{Hu} \leq h}\}}$. We define the new primal problems We also make use of the dual versions of the optimization problems, defined as follows. where no clustering occurs, and | | ${{\overline{g}}^{K}{(x)}} = \underset{\lambda\geq{0,z_{jk},y_{jk},s_{k}}}{\text{minimize}}$ | $\sum\limits_{k}^{K}{{({{|C_{k}|}/N})}s_{k}}$ | | (MRO-K-Dual) | | | subject to | ${{{{\lbrack{- g_{j}}\rbrack}^{\ast}{({z_{jk} - {H^{T}\gamma_{jk}}})}} + {\gamma_{jk}^{T}{({h - {H{\overline{d}}_{k}}})}}} - {z_{jk}^{T}{\overline{d}}_{k}}} + {\lambda\epsilon^{p}}$ | | | | | | ${{{+ {\phi{(q)}\lambda\left\| {z_{jk}/\lambda} \right\|_{\ast}^{q}}} \leq s_{k}},{{k = {1,\ldots,K}},{j = {1,\ldots,J}}}},$ | | | where we have $K$ clusters. Given these definitions, we obtain bounds on the worst-case value of the constraint function for $K$ clusters.

### Theorem 4.2

When $g$ is the maximum of concave functions with domain ${\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}_{u}g} = \text{R}^{m}$ and polyhedral support $S = {\{ u\mid{{Hu} \leq h}\}}$, and where each $- g_{j}$ satisfies an $L$-smooth condition on its domain with respect to the $\ell_{2}$-norm at a given $x$, we have, for the same $x$ and $\epsilon$, where ${\delta{(K,z,\gamma)}} = {{({1/N})}{\sum_{k = 1}^{K}{\sum_{i \in C_{k}}{\max_{j \leq J}{({{({{- z_{jk}} - {H^{T}\gamma_{jk}}})}^{T}{({d_{i} - {\overline{d}}_{k}})}})}}}}}$, and $z$, $\gamma$ are the dual variable from (MRO-K). The constants $L_{j}$ are the $L$-smoothness constants for the concave functions $g_{j}$.

The proof is delayed to Appendix A.10. We note that due to the nonconvex and nonconcave nature of maximum-of-concave functions, we can no longer directly fix the relationship between ${\overline{g}}^{N}{(x)}$ and ${\overline{g}}^{K}{(x)}$. Instead, we need to define the lower bound with the extra term $\delta{(K,z,\gamma)}$. However, in the special case where $g$ is a maximum-of-affine function, which is convex, we know ${\overline{g}}^{N \ast}{(x)}$ to be an upper bound on ${\overline{g}}^{K}{(x)}$.

### Corollary 4.2.1

When $g$ is the maximum of affine functions with domain $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}_{u} = \text{R}^{m}$ and polyhedral support $S = {\{ u\mid{{Hu} \leq h}\}}$, for the same $x$ and $\epsilon$, This follows from the fact that $L_{j} = 0$ for all affine functions $g_{j}$.

### Uncertain objective

When the uncertainty is in the objective, Theorem 4.2 and Corollary 4.2.1 quantifies the possible difference in optimal values between the MRO problem with $K$ and $N$ clusters. We again define $\Delta = {\max_{x}\left( {{{\overline{g}}^{N \ast}{(x)}} - {{\overline{g}}^{N}{(x)}}} \right)}$, subject to $x$ being feasible for problem (MRO). Note, however, that this is only needed for the upper bound. The lower bound holds without needing to consider ${\overline{g}}^{N \ast}{(x)}$; we need not consider the effect of the support set on the problem.

### Corollary 4.2.2

Consider the problem where $g$ is itself the objective function we would like to minimize and $X \subseteq \text{R}^{n}$ represents the constraints, which are deterministic. Then, $\delta{(K,z,\gamma)}$ upper bounds the possible decrease in optimal values of the MRO problem with $K$ clusters compared with that of $N$ clusters. Similarly, ${{\max_{j \leq J}{({L_{j}/2})}}D{(K)}} + \Delta$ upper bounds the possible increase in optimal values.

### Uncertain constraints

When the uncertainty is in the constraints, the difference between ${\overline{g}}^{N}{(x)}$ and ${\overline{g}}^{K}{(x)}$ as given in Theorem 4.2 no longer directly reflect the difference in optimal values. Instead, clustering affects the feasible set for $x$ as follows. In the case ${{\overline{g}}^{N}{(x)}} \geq {{\overline{g}}^{K}{(x)}}$, for any $\hat{x}$, ${\overline{g}}^{K}{(\hat{x})}$ can be at most $\delta{(K,z,\gamma)}$ lower in value than ${\overline{g}}^{N}{(\hat{x})}$. Since both values are constrained to be nonpositive from (MRO), the feasible region of the MRO problem with $K$ clusters may be less restricted than that of $N$ clusters. This indirectly allows MRO with $K$ clusters to obtain a smaller optimal value. On the other hand, in the case ${{\overline{g}}^{N}{(\hat{x})}} \leq {{\overline{g}}^{K}{(\hat{x})}}$, ${\overline{g}}^{K}{(\hat{x})}$ can be at most ${{\max_{j \leq J}{({L_{j}/2})}}D{(K)}} + \Delta$ higher in value than ${\overline{g}}^{N}{(\hat{x})}$. Since both values are constrained to be nonpositive, the feasible region of the MRO problem with $K$ clusters may be more restricted than that of $N$ clusters. This indirectly lets MRO with $K$ clusters to obtain a larger optimal value.

## Parameter selection and outliers

### Choosing $K$

When the uncertain constraint is affine and $S$ does not affect the worst-case constraint value, the number of clusters $K$ does not affect the final solution, so it is always best to choose $K = 1$. We trivially cluster by averaging all data-points without using any clustering algorithm. When $S$ affects the worst-case constraint value, there is a difference of at most $\Delta$ between setting $K = 1$ and $K = N$, which can often be approximated $\approx 0$ for small $\epsilon$. Therefore, setting $K = 1$ remains the recommendation. When the constraint is concave, we choose $K$ to obtain a reasonable upper bound on ${\overline{g}}^{K}{(x)}$, as described in Theorem 4.1. This upper bound depends linearly on $D{(K)}$, the clustering value, so by choosing the elbow of the plot of $D{(K)}$, we choose a cluster number that, while being a reasonably low value, best conforms to the shape of the underlying distribution. When the constraint is maximum-of-concave, the bounds given in Theorem 4.2 also depends on $D{(K)}$. Notice that the value $\delta{(K,z,\gamma)}$ in the lower bound is also a weighted transformation of $D{(K)}$. The elbow method has been commonly used in machine learning problems pertaining the choice of hyper-parameters, especially for $K$-means, and can be traced back to Thorndike Thorndike in 1953. Note that, by directly returning $D{(K)}$ and examining the elbow as an initial step, this procedure can be completed in the clustering step without having to solve the downstream optimization problem. To further improve the choice of $K$, or if the elbow is unclear, cross-validation may be used for low $K$ values or $K$ values around the elbow. No matter if the uncertainty lies in the objective or the constraints, this bound will inform us of the potential difference between choosing different $K$.

### Choosing $\epsilon$

While we have outlined theoretical results in Theorem 3.3. ‣ Case 𝑝=∞. ‣ 3.1 Satisfying the probabilistic guarantees ‣ 3 Links to Wasserstein distributionally robust optimization ‣ Mean Robust Optimization") for choosing $\epsilon$, in practice, we experimentally select $\epsilon$ through cross validation to arrive at the desired guarantee. Therefore, while the theoretical bounds suggest to choose a larger $\epsilon$ when we cluster, this may not be the case experimentally. In fact, for concave $g$, we may even choose a smaller $\epsilon$, due to the increase in the level of conservatism for small $K$. On the other hand, for maximum-of-concave $g$, we do need to choose larger $\epsilon$, as smaller $K$ leads to less conservative solutions. However, for both cases, we show a powerful result in the upcoming numerical examples: although for the same $\epsilon$, MRO with $K$ clusters differs in conservatism from Wasserstein DRO ($N$ clusters), there are cases where we can tune $\epsilon$ such that MRO and DRO provide almost identical tradeoffs between objective values and probabilitic guarantees, such that no loss in performance results from choosing a smaller cluster number $K$.

### Data with outliers

When the provided dataset contains outliers, one might imagine that the centoids created by the clustering algorithm will be biased towards the outliers. While this is true, the weights of the outliers will not increase through clustering, thus the effect of outliers on these clustered Wasserstein balls is not worse than their effect on the original Wasserstein balls, which include the Wasserstein ball around the outlier point. In fact, by clustering the outlier point with other points, MRO offers protection against the outlier. We demonstrate this in on the numerical experiment in Section 6.6, where we compare three methods: MRO, MRO with outlier removal, and MRO with the outlier considered as its own cluster.

## Numerical examples

We now illustrate the computational performance and robustness of the proposed method on various numerical examples. All the code to reproduce our experiments is available, in Python, at We run the experiments on the Princeton Institute for Computational Science and Engineering (PICSciE) facility with 20 parallel 2.4 GHz Skylake cores. We solve all optimization problems with MOSEK optimizer with default settings.

All numerical examples are solved through direct reformulations if not stated otherwise. The calculated in-sample objective value and out-of-sample expected values, as well as the out-of-sample probability of constraint violation, are averaged over 50 independent runs of each experiment. For each run, we generate evaluation data of the same size $N$ as the training dataset.

For numerical examples with an uncertain objective, the probability of constraint violation is measured as the probability the average out-of-sample value is above the in-sample value. For numerical examples with an uncertain constraint, the probablity of constraint violation is measured as the probability the average constraint value is above zero.

In Sections 6.1, 6.2, and 6.3, we demonstrate the performance of MRO when the uncertain constraint is concave. In Section 6.4, 6.5, and 6.6, we demonstrate the performance of MRO for maximum-of-affine uncertainty.

### Capital budgeting

We consider the capital budgeting problem, where we select a portfolio of investment projects maximizing the total net present value (NPV) of the portfolio, while the weighted sum of the projects is less than a total budget $\theta$. The NPV for all projects is ${\eta{(u)}} \in \text{R}^{n}$, where for each project $j$, $\eta_{j}{(u)}$ is the sum of discounted cash flows $F_{jt}$ over the years $t = {0,\ldots,T}$, i.e., ${\eta_{j}{(u)}} = {\sum_{t = 0}^{T}{F_{jt}/{({1 + u_{j}})}^{t}}}$. Here, $u_{j}$ is the discount rate of project $j$. We formulate the uncertain function to be minimized as where $x = {(x_{1},\ldots,x_{n})} \in {\{ 0,1\}}^{n}$ is the indicator for selecting each project. The discount rate $u_{j}$ is subject to uncertainty, as it depends on several factors, such as the interest rate of the country where project $j$ is located and the level of return the decision-maker wants to compensate the risk. The function $g$ is concave and monotonically increasing in $u$, and we can define a domain $u \geq 0$ so that Assumption 2.1 and Theorem 4.1 applies. The robust problem can be written as where $h$ is the vector of project weights. We refer to and arrive at the convex reformulation for $p = 2$ where $a \in \text{R}^{T}$ with $a_{t} = {t^{1/{({t + 1})}} + t^{- {t/{({t + 1})}}}}$ for $t = {1,\ldots,T}$, and ${(x,y,z)} \in \mathcal{K}^{\alpha}$ is a power cone constraint given as ${x^{\alpha}y^{1 - \alpha}} \geq {|z|}$. The vector $F_{0}$ indicates the first column of $F$, and matrix $C$ and vector $b$ encode the support of $u$, which we take to be $\{{u \in \text{R}^{m}}\mid{0 \leq u \leq \mathbf{1}}\}$, where $m = n$. We have variables $x_{j} \in \text{R}$, $z_{k} \in \text{R}^{n}$, $Y_{k} \in \text{R}^{n \times T}$, $\delta_{k} \in \text{R}^{n \times T}$, $\tau \in \text{R}$, $\gamma_{k} \in \text{R}^{2n}$, $s_{k} \in \text{R}$, for $j = {1,\ldots,n}$, $k = {1,\ldots,K}$, and $t = {1,\ldots,T}$. The derivation of reformulation is in Appendix A.11 ‣ Appendix A Appendices ‣ Mean Robust Optimization"). Note that there are variables with total dimension $KnT$, which grows swiftly when any of the parameters are large. For each cluster $k$, we introduce $nT$ new variables for $y$ and $\delta$, as well as $nT$ new power cone constraints, which greatly increases the compuational complexity of the problem.

### Problem setup

We set $n = 20$, $N = 120$, $T = 5$. We generate $F_{jt}$ from a uniform distribution on $\lbrack 0.1,{0.5 + {0.004t}}\rbrack$ for $j = {1,\ldots,n}$, $t = {0,\ldots,T}$. For all $j$, $h_{j}$ is generated from a uniform distribution on $\lbrack 1,{3 - {0.5j}}\rbrack$, and the total budget $\theta$ is set to be 12. We generate uncertain data from two slightly different uniform distributions, to simulate two different sets of predictions on the discount rates. The first half is generated on $\lbrack{0.005j},{0.02j}\rbrack$, and the other half on $\lbrack{0.01j},{0.025j}\rbrack$, for all $j$. We calculate an upper bound on the $L$-smooth parameter, $L = {\|{\nabla^{2}{\sum_{j = 1}^{n}{\sum_{t = 0}^{T}{F_{jt}{({\hat{x}}_{N})}_{j}{({1 + u_{j}})}^{- t}}}}}\|}_{2,2} \leq {\|{\sum_{j = 1}^{n}{\sum_{t = 0}^{T}{t{({t + 1})}F_{jt}{({\hat{x}}_{N})}_{j}}}}\|}_{2,2}$ for each data-driven solution ${\hat{x}}_{N}$.

### Choosing $K$

Plotting the clustering value $D{(K)}$ over $K$, we note that the elbow occurs around $K = 2$, which suggests using cross-validation for $K$ values around 2.

Figure 4: Capital budgeting. D (K) vs. K. Dotted red line: K = 2.

Figure 5: Capital budgeting. Left: in-sample objective values and out-of-sample expected values vs. ϵ for different K. Solid lines are the in-sample objective value, dotted lines are the out-of-sample expected value. Right: objective value vs. β for different K; each point represents the solution for the ϵ achieving the smallest objective value. K = 120* is the formulation without the support constraint.

Figure 6: Capital budgeting. Left: the difference in the value of the uncertain objective between using K and N clusters, calculated as ${{\overline{g}}^{K}{(x)}} - {{\overline{g}}^{N}{(x)}}$, compared with the theoretical upper bound (L/2) D (K) from Corollary 4.1.1. Solid lines are the difference, dotted lines are the upper bounds. Right: solve time.

### Results

We observe in Figure 5 that using two clusters is enough to achieve performance almost identical to that of using 120 clusters. Although from the left image, we see that $K = 2$ slightly upper bounds $K = 120$, from the right, their tradeoffs between the objective value and relevant constraint violation probability ($\beta \leq 0.2$) are largely the same, so we can always tune $\epsilon$ to achieve the same performance and guarantees. Notice that the results for $K = 120$ and $K = 120^{\ast}$ are near identical for small $\epsilon$, where $K = 120^{\ast}$ is the formulation without the support constraint. Therefore, while ${\overline{g}}^{N \ast}{(x)}$ slightly upper bounds ${\overline{g}}^{N}{(x)}$, we can approximate their difference $\Delta \approx 0$ for small enough $\epsilon$, for which the upper bound ${({L/2})}D{(K)}$ thus hold. In fact in this example, even for larger $\epsilon$ where we observe $\Delta > 0$, the actual difference between ${\overline{g}}^{K}$ and ${\overline{g}}^{N}$ is bounded by ${({L/2})}D{(K)}$. In Figure 6, we see that the elbow of the upper bound is at $K = 2$, and the true difference follows the same trend, matching the suggestion from Figure 4. Therefore, setting $K = 2$ is the optimal decision, with a time reduction of 2 orders of magnitude, and a complexity reduction from 26626 variables and 12000 power cones to 666 variables and 200 power cones.

### Quadratic concave uncertainty

We refer to the example from Ben-Tal et al. with concave uncertainty of the form where ${h_{i}{(u)}} = {- {{({1/2})}u^{T}A_{i}u}}$, each $A_{i} \in \text{R}^{m \times m}$ a symmetric positive definite matrix, $u \in \text{R}^{m}$, and $x \in \text{R}_{+}^{n}$. For simplicity, we also require that $x$ sums to 1, $p = 2$, and the support of the uncertainty $S = \text{R}^{m}$. Assuming the uncertainty is in the objective, such that the uncertain constraint is created using epigraph form, we solve the problem The $A_{i}^{- 1}$ terms come from taking the conjugate of $g$, and the derivation can be found. We have variables $x \in \text{R}^{n}$, $z_{k} \in \text{R}^{m}$, $Y_{k} \in \text{R}^{m \times n}$, $\tau \in \text{R}$, $s_{k} \in \text{R}$, for $k = {1,\ldots,K}$. We let ${(Y_{k})}_{i}$ indicate the $i$th column of $Y_{k}$.

### Problem setup

We set ${n = m = 10},{N = 90}$, and generate synthetic uncertainty as a multi-modal normal distribution with 5 modes, where $\mu_{i} = {\gamma_{j}0.03i}$ for all $i = {1,\ldots,n}$ for mode $j$, with mode scales $\gamma = {}$. The variance is $\sigma_{i} = {0.02^{2} + {({0.025i})}^{2}}$ for all modes. We generate $A_{i}$ as random positive semi-definite matrices for all $i = {1,\ldots,n}$. For the upper bound, we calulate $L = {\|{\sum_{i = 1}^{n}{A_{i}{({\hat{x}}_{N})}_{i}}}\|}_{2,2}$ for each data-driven solution ${\hat{x}}_{N}$.

### Choosing $K$

Plotting the clustering value $D{(K)}$ over $K$, we note that the elbow occurs at $K = 5$, which suggests a choice of $K = 5$.

Figure 7: Quadratic concave uncertainty. D (K) vs. K. Dotted red line: K = 5.

Figure 8: Quadratic concave uncertainty. Left: in-sample objective values and out-of-sample expected values of g vs. ϵ for different K. Solid lines are the in-sample objective value, dotted lines are the out-of-sample expected value. Right: objective value vs. β for different K; each point represents the solution for the ϵ achieving the smallest objective value.

Figure 9: Quadratic concave uncertainty. Left: the difference in the value of the uncertain objective between using K and N clusters, calculated as ${{\overline{g}}^{K}{(x)}} - {{\overline{g}}^{N}{(x)}}$, compared with the theoretical upper bound (L/2) D (K) from Corollary (4.1.1). Solid lines are the difference, dotted lines are the upper bounds. Right: solve time.

### Results

We observe on the left of Figure 8 that using 5 clusters is enough to achieve performance almost identical to that of using 90 clusters. Indeed, in Figure 9, the elbow of the upper bound (dotted lines) on the difference in objective values is at $K = 5$, and the true difference follows the same trend, corroborating with Figure 7. Furthermore, on the left plot of Figure 9, we note for $K \geq 5$, the tradeoff between the objective value and constraint violation is the same, so we can tune $\epsilon$ to achieve the same performance and guarantees. In fact, for this particular example, using a smaller $K$ such as 1 or 2 may allow us to tune $\epsilon$ to achieve an even better tradeoff. However, this result cannot be guaranteed in general, so the recommended action is still to choose $K = 5$.

### Robust log-sum-exp optimization

We also consider uncertainty from Bertimas and den Hertog of the form concave in $u$ and convex in $x$. This function $g$ is monotonically increasing in $u$, and we can define a domain $u \geq 0.01$ so that Assumption 2.1 and Theorem 4.1 apply. Assuming the simple case where the uncertainty is in the objective, we add some further restrictions on $x$ and use a cutting plane procedure to solve, for $p = 2$,

### Problem setup

We set ${n = 30},{N = 90}$, and observe synthetic data from 3 sets of uniform distributions, scaled respectively by $\gamma = {}$. Specifically, for each set $j$, each $d_{i}$ is generated uniformly on the intervals $0.01{\lbrack{\gamma_{j}i},{\gamma_{j}{({i + 1})}}\rbrack}$ for $i = {1,\ldots,n}$. For the upper bound, we calculate $L = \parallel \nabla^{2}g \parallel_{2,2} \leq \exp{({\hat{x}}_{N})}^{T}\exp{({\hat{x}}_{N})}\min{(d_{k}^{T}\exp{({\hat{x}}_{N})})}^{- 2}$, for each data-driven solution ${\hat{x}}_{N}$.

### Choosing $K$

Plotting the clustering value $D{(K)}$ over $K$, we note that the elbow occurs at $K = 3$, which suggests using cross-validation for $K$ values around 3.

Figure 10: Log-sum-exp uncertainty. D (K) vs. K. Dotted red line: K = 3.

Figure 11: Log-sum-exp uncertainty. Left: in-sample objective values and out-of-sample expected values vs. ϵ for different K. Solid lines are the in-sample objective value, dotted lines are the out-of-sample expected value. Right: objective value vs. β for different K.

Figure 12: Log-sum-exp uncertainty. Left: the difference in the value of the uncertain objective between using K and N clusters. Solid lines are the difference, the dotted line is the upper bound. Right: solve time.

### Results

We observe on the left of Figure 11 that while setting $K$ to smaller values increases the objective value, setting $K = 3$, the number of modes of the underlying distribution, already offers near identical performance to that of setting $K = 90$. On the left of Figure 12, we see that $K = 3$ is at the elbow of upper bound and actual difference, corroborating with Figure 10. Furthermore, we note that setting $K = 3$ and above give identical tradeoff curves, therefore, choosing $K = 3$ is the time-efficient solution.

### Sparse portfolio optimization

We consider a market that forbids short-selling and has $m$ assets as. Daily returns of these assets are given by the random vector $d = {(d_{1},\ldots,d_{m})} \in \text{R}^{m}$. The percentage weights (of the total capital) invested in each asset are given by the decision vector $x = {(x_{1},\ldots,x_{n})} \in \text{R}^{n}$. We restrict our selection to at most $\theta$ assets. The underlying data-generating distribution $\mathbf{P}$ is unknown, but we have observed a historical dataset $\mathcal{D}_{N}$. Our objective is to minimize the CVaR with respect to variable $x$, which represents the average of the $\alpha$ largest portfolio losses that occur. In other words, the $\operatorname{\mathbf{C}\mathbf{V}\mathbf{a}\mathbf{R}}$ term seeks to ensure that the expected magnitude of portfolio losses, when they occur, is low. The objective has an analytical form with an extra variable $\tau$ given as: From this, we obtain $g$ as the maximum of affine functions, Using the formulation with $p = \infty$, we can write a convex reformulation of the form with variables $x \in \text{R}^{m}$, $z \in \text{R}^{m}$, $y \in \text{R}$, $\tau \in \text{R}$, $s_{k} \in \text{R}$. The variables $z$ are introduced to replace the cardinality constraint using big-$M$ formulation.

### Problem setup

We take stock data from the past 10 years of S&P500, and generate synthetic data from their fitted general Pareto distributions. We choose a generalized Pareto fit over a normal distribution as it better models the heavy tails of the returns. See the Github repository for the code, which uses the "Rsafd" R package Carmona. We let $\alpha = {20\%}$, $m = 50$ stocks, and generate a dataset size of $N = 1000$. Our portfolio can include at most $\theta = 5$ stocks. For the upper bound $\delta{(K,z,\gamma)}$ on ${{\overline{g}}^{N}{(x)}} - {{\overline{g}}^{K}{(x)}}$, we note the special structure of this problem, where one of the affine pieces is independent of $u$, to arrive at a bound ${\delta{(K,z,\gamma)}} = {\max_{k}{\{{\max_{i}{\{{{{({{\overline{d}}_{k} - d_{i}})}^{T}x}/\alpha}\}}}\}}}$.

### Choosing $K$

Plotting the clustering value $D{(K)}$ over $K$, we note that the elbow occurs at $K = 5$, which suggests using cross-validation for $K$ values around 5.

Figure 13: Sparse portfolio. D (K) vs. K. Dotted red line: K = 5.

### Results

In Figure 14, while setting $K$ to smaller values lead to a decrease in the optimal value across $\epsilon$, we note that for $K = 5$ and above, we can already achieve a tradeoff curve between the optimal value and probability of constraint satisfaction that is similar to that of $K = 1000$, and setting $K = 10$ brings it slightly closer. In Figures 13 and 15, in the plots of $D{(K)}$ and of the upper bound on the difference, we also note that the elbow is around $K = 5$. We thus recommend choosing $K$ through cross validation around 5, as tuning $\epsilon$ for these small $K$ gives 1 - 3 orders of magnitude time reduction.

Figure 14: Sparse portfolio. Left: in-sample objective values and out-of-sample expected values vs ϵ for different K. Solid lines are the in-sample objective value, dotted lines are the out-of-sample expected value. Right: objective value vs β for different K; each point represents the solution for the ϵ achieving the smallest objective value.

Figure 15: Sparse portfolio. Left: the difference in the value of the uncertain objective between using N and K clusters, calculated as ${{\overline{g}}^{N}{(x)}} - {{\overline{g}}^{K}{(x)}}$, compared with the theoretical upper bound δ (K, z, γ) from Corollary 4.2.1. Solid lines are the difference, dotted lines are the upper bounds. Right: solve time for K ≥ 5.

### Facility location

We examine the classic facility location problem. Consider a set of $n$ potential facilities, and $m$ customers. Variable $x \in {\{ 0,1\}}^{n}$ describes whether or not we construct each facility $i$ for $i = {1,\ldots,n}$, with cost $c_{i}$. In addition, we would like to satisfy the uncertain demand $u \in \text{R}^{m}$ at minimal cost. We define variable $X \in \mathbf{R}^{n \times m}$ where $X_{ij}$ corresponding to the portion of the demand of customer $j$ shipped from facility $i$ with corresponding cost $C_{ij}$. Furthermore, $r \in \text{R}^{n}$ represents the production capacity for each facility, and $u \in \text{R}^{m}$ represents the uncertain demand from each customer. For each customer $j$, $X_{j}$ represents the proportion of goods shipped from any facility to that customer, which sums to $1$. For each facility $i$, ${(X^{T})}_{i}$ represents the proportion of goods shipped to any customer. Putting this all together, we obtain multiple affine uncertain capacity constraints, which we combine to create a single maximum-of-affine constraint, Now, to ensure a high probability of constraint satisfaction, we use the $\operatorname{\mathbf{C}\mathbf{V}\mathbf{a}\mathbf{R}}$ reformulation, where we add the auxiliary variable $\tau$. We assume a polyhedral support $S = {\{ u\mid{{Hu} \leq b}\}}$ for the demand, and solve the problem, for $p = \infty$, We have variables $x \in {\{ 0,1\}}^{n}$, $X \in \text{R}^{n \times m}$, $s_{k} \in \text{R}$, $\tau \in \text{R}$, $\lambda_{k} \in \text{R}$, $\gamma_{ik} \in \text{R}^{m}$, for $i = {1,\ldots,n}$ and $k = {1,\ldots,K}$. The $\gamma$ variables arise from enforcing the support constraints.

### Problem setup

To generate data, we set $n = 5$ facilities, $m = 25$ customers, and $N = 50$ data samples. For the $\operatorname{\mathbf{C}\mathbf{V}\mathbf{a}\mathbf{R}}$ reformulation, we set $\alpha = {20\%}$. We set costs $c = {(46.68,58.81,30,42.09,35.87)}$, and generate the two coordinates of each customer's location from a uniform distribution on $\lbrack 0,15\rbrack$. We then calculate $C$ as the $\ell_{2}$ distance between each pair of customers. We set production capacities $r = {}$. We assume the demand $d$ is supported between 1 and 6, which we write as ${Hu} \leq b$, where $H = {\lbrack{- {II}}\rbrack}^{T}$ and $b$ is the concatenation of two vectors: a vector of $- 1$'s of length $m$, and a vector of $6$'s of length $m$. We generate demands as the combination of two normal distributions. Half of the data is generated from the normal distribution with mean $\mu_{1} = 3$ and variance $\sigma_{1} = 0.9$, the second half has mean $\mu_{1} = 4$ and variance $\sigma_{1} = 0.8$. We then project the demands onto $$. For the upper bound $\delta{(K,z,\gamma)}$ on ${{\overline{g}}^{N}{(x)}} - {{\overline{g}}^{K}{(x)}}$ from Corollary 4.2.1, we have ${(1/N)}\sum_{k = 1}^{K}\sum_{i \in C_{k}}\max{(\max_{j \leq J}{({(X{\lbrack i\rbrack} - H^{T}\gamma_{jk})},0)}^{T}{(d_{i} - {\overline{d}}_{k})})}$. Note that this upper bounds the difference in constraint values, and only indirectly affects the objective values through restrictions on the feasible region. Therefore, it is not an upper bound on the difference in objective value, merely a rough estimate. We cannot directly compare this upper bound against the change in constraint values, as at the optimal chonsen $x,X$ for each $K$, which differ due to differences in the feasible regions, the constraint value will always be near 0 for optimality. We thus compare it against the change in objective values.

### Choosing $K$

Plotting the clustering value $D{(K)}$ over $K$, we note that the elbow occurs at $K = 2$, which suggests using cross-validation for $K$ values around 2.

Figure 16: Facility location. D (K) vs. K. Dotted red line: K = 2.

### Results

As expected of maximum-of-affine $g$, we note in Figure 17 that setting $K$ to smaller values lead to a decrease in the optimal value across different $\epsilon$ values. While $K = 1$ yields poor performance in terms of the probability of constraint violation, we observe that $K = 2$ already yields a tradeoff between the objective and probability of constraint violation close to that of $K = 50$. Through cross-validation with different $K$, we select $K = 5$, which provides a tradeoff curve closer to optimality. As this problem has uncertainty in the constraints and not the objective, the bounds given in Corollary 4.2.1 do not directly reflect the difference in the objective values. However, they do give a reference value and inform us of the general trend of the difference. In this case, they still upper bound the actual difference, as shown in Figure 17. We note that the bounds we use do not depend on ${\overline{g}}^{N \ast}{(x)}$, so it is irrelevant whether or not the support has an affect on the worst-case constraint value. Overall, choosing $K = 5$ leads to a time reduction of an order of magnitude while achieving near-optimal performance.

Figure 17: Facility location. Left: in-sample objective values vs ϵ for different K. Right: objective value vs β for different K; each point represents the solution for the ϵ achieving the smallest objective value.

Figure 18: Facility location. Left: the difference in the value of the uncertain objective between using N and K clusters, calculated as Obj(N) - Obj(K), compared with the theoretical upper bound δ (K, z, γ) on the worst-case constraint value ${{\overline{g}}^{N}{(x)}} - {{\overline{g}}^{K}{(x)}}$, from Corollary 4.2.1. Solid lines are the difference, dotted lines are the upper bounds. Right: solve time.

### Newsvendor problem

We consider a 2-item newsvendor problem where, at the beginning of each day, the vendor orders $x \in \text{R}^{2}$ products at price $h = {}$. These products will be sold at the prices $c = {(5,6.5)}$, until either the uncertain demand $u$ or inventory $x$ is exhausted. The objective function to minimize is the sum of the ordering cost minus the revenue: from which we obtain the maximum-of-affine uncertain function $g$ to minimize, We assume a polyhedral support $S = {\{ u\mid{{Cu} \leq b}\}}$, and solve, with $p = 1$, We have variables $x \in \text{R}^{n}$,$s_{k} \in \text{R}$, $\lambda \in \text{R}$, $\gamma_{jk} \in \text{R}^{m}$, for $j = {1,\ldots,4}$ and $k = {1,\ldots,K}$. The $\gamma$ variables arise from enforcing the support. We denote $e_{1} = {}$ and $e_{2} = {}$.

For this problem, we consider the effects of outliers on the performance of MRO. Therefore, we consider the data to have an outlier at $$, the worst-case value of the support set. In Figure 19, we show a set of generated data along with this outlier point.

Figure 19: Newsvendor. Datapoints and the outlier .

We consider three ways to solve the problem, decribed as follows.

MRO, where we directly apply MRO to the dataset with the outlier.

ROB-MRO, where we perform preliminary analysis on the dataset to remove the outlier point, then apply MRO to the cleaned dataset.

AUG-MRO, where we perform the clustering step on data without the outlier, then define an augmented distribution supported on $K + 1$ points, where the extra point is the outlier point, with weight $1/N$. The weights of the other clusters are ajusted accordingly.

### Problem setup

To generate data, we set $N = 100$ data samples. We assume demand is supported between 0 and 40, which we write as ${Cu} \leq b$, where $C = {\lbrack{- {II}}\rbrack}^{T}$ and $b = {}$. We allow non-integer demand to allow for more variance in the data. We generate the demand from a log-normal distribution, where the underlying normal distribution has parameters and take the minimum between the generated values and 40. For the upper bound $\delta{(K,z,\gamma)}$ on ${{\overline{g}}^{N}{(x)}} - {{\overline{g}}^{K}{(x)}}$ from Corollary 4.2.1, we have ${({1/N})}{\sum_{k = 1}^{K}{\sum_{i \in C_{k}}{\max_{j \leq 4}{({{({{- {\overset{\sim}{c}}_{j}} - {C^{T}\gamma_{jk}}})}^{T}{({d_{i} - {\overline{d}}_{k}})}})}}}}$, where ${{\overset{\sim}{c}}_{1} = 0},{{{\overset{\sim}{c}}_{2} = {c_{1}e_{1}}},{{{\overset{\sim}{c}}_{3} = {c_{2}e_{2}}},{{\overset{\sim}{c}}_{4} = c}}}$.

### Choosing $K$

Plotting the clustering value $D{(K)}$ over $K$, for the dataset both with and without the outlier, we note an elbow at around $K = 5$, though not very prominent. The recommendation is setting $K$ around 5, to be fine tuned through cross-validation.

Figure 20: Newsvendor. D (K) vs. K. Dotted red line: K = 5.

### Results

In Figure 21, we compare the in and out-of-sample objective values of the three methods, and note their similar performance. While setting $K = 1$ yields suboptimal results, we note that for $K = 5$ and above, we can achieve similar performance as setting $K = 100$. To examine the effect of the outlier more closely, in Figures 22 and 23, we compare, for $K = 10$ and $K = 100$, the objectives and tradeoff curves for the three methods. We note that, when the outlier is averaged with other datapoints, the final in-sample objective may be improved, as the centroid moves closer to the non-outlier points. We observe this in Figure 22, where MRO, in which the outlier may be clustered with other points, offers a lower in-sample objective than AUG-MRO, in which the outlier is considered its own cluster. MRO has in fact offered protection against the outlier. Lastly, as expected, ROB-MRO, where the outlier point is removed, yields the best in-sample results. Regardless of the method, we note that the final out-of-sample tradeoff curves are near-identical. Comparing Figures 22 and 23, we note that the difference between MRO and ROB-MRO for $K = 10$ is not larger than the difference for $K = N = 100$, which shows that, while removing outliers before solving the problem may be helpful, the effect of outliers will not be worse for MRO compared to classic Wasserstein DRO.

We note in Figure 24 that the upper bound on ${{\overline{g}}^{N}{(x)}} - {{\overline{g}}^{K}{(x)}}$, given in Corollary 4.2.1, holds for MRO. We again note that bounds we observe do not depend on ${\overline{g}}^{N \ast}{(x)}$, so it is irrelevant whether or not the support has an affect on the worst-case constraint value. Regardless, we see that the support only minimally affects the worst-case constraint value, at only at higher values of $\epsilon$. Overall, choosing $K = 5$, we obtain an order of magnitude computational speed-up.

## Conclusions

We have presented mean robust optimization (MRO), a new data-driven methodology for decision-making under uncertainty that bridges robust and distributionally robust optimization while preserving rigorous probabilistic guarantees. By clustering the dataset before performing MRO, we solve an efficient and computationally tractable formulation with limited performance degradation. In particular, we showed that when the constraints are affine in the uncertainty, clustering does not affect the optimal value of the objective. When the constraint is concave or maximum-of-concave in the uncertainty, we directly quantified the change in worst-case constraint value that is caused by clustering. For problems with objective uncertainty, this directly bounds the change in the optimal value caused by clustering. We demonstrated this result through a set of numerical examples, where we observed the possibility of tuning the size of the uncertainty set such that using a small number of clusters achieves near-identical performance of traditional DRO, with much higher computational efficiency. In the final example, we also demonstrated that MRO offers protection against outliers compared to Wasserstein DRO.

Figure 21: Newsvendor. Left: in-sample objective values vs ϵ for different K. Right: objective value vs β for different K; each point represents the solution for the ϵ achieving the smallest objective value. K = 100* is the formulation without the support constraint. Top: MRO. Middle: ROB-MRO. Bottom: AUG-MRO.

Figure 22: Newsvendor. Left: in-sample objective values vs ϵ for K = 10. Right: objective value vs β for K = 10.

Figure 23: Newsvendor. Left: in-sample objective values vs ϵ for K = 100. Right: objective value vs β for K = 100.

Figure 24: Newsvendor. Left: the difference in the value of the uncertain objective between using N and K clusters, calculated as ${{\overline{g}}^{N}{(x)}} - {{\overline{g}}^{K}{(x)}}$, compared with the theoretical upper bound δ (K, z, γ) from Corollary 4.2.1. Solid lines are the difference, dotted lines are the upper bounds. Right: solve time.
