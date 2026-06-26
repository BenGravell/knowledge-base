<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Improved Nonnegativity Testing in the Bernstein Basis via Geometric Means

Topics include Optimization and control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We develop a new kind of nonnegativity certificate for univariate polynomials on an interval. In many applications, nonnegative Bernstein coefficients are often used as a simple way of certifying polynomial nonnegativity. Our proposed condition is instead an explicit lower bound for each Bernstein coefficient in terms of the geometric mean of its adjacent coefficients, which is provably less restrictive than the usual test based on nonnegative coefficients. We generalize to matrix-valued polynomials of arbitrary degree, and we provide numerical experiments suggesting the practical benefits of this condition. The techniques for constructing this inexpensive certificate could potentially be applied to other semialgebraic feasibility problems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The cubic Bernstein polynomials (e.g.,) are Suppose we have a polynomial $p{(x)}$ such that We would like to find explicit conditions on the real numbers $p_{0},p_{1},p_{2},p_{3}$ (called Bernstein coefficients) that guarantee ${p{(x)}} \geq 0$ on $\lbrack 0,1\rbrack$. This task and its higher degree variants discussed in Section 4 are central questions in applied mathematics. Research on nonnegativity certificates of different kinds is a classical topic in real algebraic geometry, including well-known work by Sturm, Hilbert, Artin, and others; see e.g. and the references therein. More recently, concrete connections to applications in statistics, control, and optimization have heightened interest in finding computation-friendly nonnegativity certificates. Existing conditions that have been used in applications as nonnegativity certificates of on intervals can roughly be classified as follows: Exact characterizations: The Markov--Lukács Theorem (\[44, p.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

4\]) gives a necessary and sufficient condition for nonnegativity on an interval. It states that a polynomial $p$ is nonnegative on $\lbrack 0,1\rbrack$ if and only if there exist polynomials $s_{1}$ and $s_{2}$ such that In the cubic case, the polynomials $s_{1}$ and $s_{2}$ are linear, so writing this condition in the language of Bernstein polynomials along with a characterization of polynomials that are sums of squares (SOS) yields the second-order cone (SOCP) condition in Lemma 3. While this condition has fixed computational cost and is necessary and sufficient for a polynomial to be nonnegative on the interval, it is nontrivial to verify -- one has to search for the linear polynomials $s_{1}$ and $s_{2}$, typically via convex optimization.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Alternatively, an exact characterization can be given in terms of the discriminant of $p$. We elaborate on this approach in Section 3.3. As mentioned, conditions of this type on $p$ are typically more complicated to understand and to compute, particularly for higher degrees.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sufficient conditions: A simple, sufficient condition for nonnegativity of the polynomial $p$ is ${p_{0},p_{1},p_{2},p_{3}} \geq 0$. Because each of the Bernstein polynomials is nonnegative on the interval, a nonnegative combination of them is nonnegative too. This idea was mentioned by Bernstein in 1915, expanded in 1966, and further discussed more recently. The downside to this condition is that it is potentially conservative -- there are plenty of polynomials nonnegative on $\lbrack 0,1\rbrack$ that have at least one negative Bernstein coefficient.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We give names to the sets of polynomials that satisfy each of these conditions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Second order cones and Bernstein polynomials", "weight": 1.0} -->

The two main ingredients in our method are Bernstein polynomials and second order cones. We define both before presenting the second order cone condition for nonnegativity of a cubic Bernstein polynomial.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Subdivision method", "weight": 1.0} -->

The Bernstein coefficients are a key ingredient of the subdivision method to prove nonnegativity of a polynomial on the interval. The basic idea is to recursively bisect the domain, until a given termination criterion is satisfied. The subdivision method with nonnegativity criterion $S$ is described by the following algorithm.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Subdivision method", "weight": 1.0} -->

> Otherwise, subdivide $p$ into $p^{1}$ and $p^{2}$ (explained below). Repeat algorithm with $p^{1}$ and $p^{2}$ and wait until both calls terminate.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Subdivision method", "weight": 1.0} -->

If the algorithm terminates, then $p \in \mathcal{P}$. Termination of the subdivision algorithm is guaranteed for positive polynomials when $S = {\mathcal{N}\mathcal{B}}$. As explained below, if the polynomial $p$ is written in the Bernstein basis, each of the steps can be efficiently computed.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Subdivision method", "weight": 1.0} -->

Step 1 of the subdivision method is to check an explicit nonnegativity condition (which we interchangeably call a "termination" or "nonnegativity" criterion). If $S = {\mathcal{N}\mathcal{B}}$, then we can efficiently check whether $p \in {\mathcal{N}\mathcal{B}}$ when the Bernstein coefficients are given.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Subdivision method", "weight": 1.0} -->

Step 2 of the subdivision method is to subdivide a polynomial. The idea of subdivision is to split the unit interval into two subintervals and give two polynomials that agree with the original on each half. Those new polynomials are rescaled to be defined on $\lbrack 0,1\rbrack$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Subdivision method", "weight": 1.0} -->

An illustration of this idea is given for the polynomial ${({1 - {2x}})}^{2}$ in Figure 1. Let ${p{(x)}} \in {{\mathbb{R}}_{d}{\lbrack x\rbrack}}$. Subdividing $p$ gives polynomials $p^{1}{(x)}$ and $p^{2}{(x)}$ such that When the Bernstein coefficients of a polynomial $p$ are known, De Casteljau's algorithm provides an efficient formula for computing the Bernstein coefficients of $p^{1}$ and $p^{2}$. For cubic polynomials, the Bernstein coefficients of $p^{1}$ and $p^{2}$ are In Section 6, we explore how the number of subdivision steps required by this method is impacted by using our new nonnegativity criterion versus using $\mathcal{N}\mathcal{B}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Subdivision method", "weight": 1.0} -->

While we consider just one variant of univariate subdivision, the general idea of subdivision is useful for a variety of problems in robustness analysis and computer-aided design.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The cubic case", "weight": 1.0} -->

We begin with the cubic case because it is the simplest setting in which our results are nontrivial. First we present the exact condition for nonnegativity alluded to in Section 1 and describe a strategy to use it to get new conditions on polynomials that imply nonnegativity. Then we employ this method to provide one based on geometric means in Section 3.1 and justify why it is natural in Section 3.2. Since in the cubic case the set of nonnegative polynomials can be understood via the discriminant, Section 3.3 contains an exact discriminantal condition, unrelated to our geometric mean one, in order to compare how much simpler ours is. We finish this section by showing how the geometric mean condition can also be used to construct an exact nonnegativity characterization.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The cubic case", "weight": 1.0} -->

The following lemma, written in the language of Bernstein polynomials and second order cones, gives an exact characterization of cubic nonnegativity and is the basis for how we develop our new conditions. lemnonnegativesocp\[Cubic nonnegativity and SOCP\] Let $p \in {{\mathbb{R}}_{3}{\lbrack x\rbrack}}$. The polynomial $p \in \mathcal{P}$ if and only if there exist ${c_{1},c_{2}} \in {\mathbb{R}}$ such that

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Lemma 3 above can be interpreted as a specialization to the cubic case of the usual SDP characterization of nonnegative polynomials, adapted to the interval; see e.g., \[5, Lemma 3.33\]. This is because SDPs of size $2 \times 2$ can be equivalently written as second-order cone programs.

<!-- chunk {"id": "body-0019", "role": "body", "section": "A new strategy", "weight": 1.0} -->

If we want to use Lemma 3 to prove that a given polynomial $p \in \mathcal{P}$ is nonnegative on the interval, we must find $c_{1}$ and $c_{2}$ that satisfy. Here are three possible strategies to find $c_{1}$ and $c_{2}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Convex optimization", "weight": 1.0} -->

Given $p$, one option is to solve the convex feasibility problem for some feasible $c_{1}$ and $c_{2}$. This is a foolproof way, in the sense that for every $p \in \mathcal{P}$, there always exist (generally nonunique) solutions $c_{i}$. The drawback of this strategy is the computational cost.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Constant guess, independent of $p$", "weight": 1.0} -->

On the other extreme, one could ignore $p$ and always try the same constants $c_{1}$ and $c_{2}$. Given any constants $c_{1}$ and $c_{2}$ there is a set of feasible $p$ to induced by any such choice; this set of feasible $p$ is a (possibly empty) convex subset of $\mathcal{P}$. Given $p$ and the fixed constant choices $c_{1}$ and $c_{2}$, checking feasibility of is as simple as verifying a few inequalities.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Constant guess, independent of $p$", "weight": 1.0} -->

In fact, this is the strategy used to construct $\mathcal{N}\mathcal{B}$. The set of polynomials that are feasible in when $c_{1} = c_{2} = 0$ is exactly the set $\mathcal{N}\mathcal{B}$. This also points out the main weakness of this strategy: there are plenty of polynomials in $\mathcal{P}$ that are not feasible in for $c_{1} = c_{2} = 0$. For example, consider $p = {{{({1 - x})}{({1 - {4x}})}^{2}} + x^{3}}$, whose Bernstein coefficients are $(1,{- 2},3,1)$, not all of which are nonnegative. On the other hand, the conditions in Lemma 3 hold for $c_{1} = {- 6}$ and $c_{2} = 0$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Explicit function of $p$", "weight": 1.0} -->

There is a clear compromise between the two strategies above. We propose instead a middle ground, where $c_{1}$ and $c_{2}$ are "simple," explicit functions of $p$. The decision variables depend on the data, but they are explicit, low-complexity computable functions.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Explicit function of $p$", "weight": 1.0} -->

What would be a good definition for $c_{1}$ and $c_{2}$ of this form? A "good choice" for $c_{1}$ and $c_{2}$ is one with the following informally stated properties: Non-inferiority: it should be no worse than fixing $c_{1} = c_{2} = 0$ and Maximality: it should be maximal in some sense.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Explicit function of $p$", "weight": 1.0} -->

Formal statements of these properties and additional intuition for our choices are presented in Section 3.2.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Explicit function of $p$", "weight": 1.0} -->

For the cubic case, we propose the choice While this is more complicated than $c_{1} = c_{2} = 0$, Section 3.2 provides additional motivation and an argument of why our proposal satisfies the desirata mentioned above. Substituting the values in into gives the conditions that define our new set.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Non-inferiority", "weight": 1.0} -->

The following theorem formalizes the claim that our choices of $c_{1}$ and $c_{2}$ are at least as good as $c_{1} = c_{2} = 0$. thmthmoneintwointhree ${\mathcal{N}\mathcal{B}} \subset {\mathcal{G}\mathcal{B}} \subset \mathcal{P}$

<!-- chunk {"id": "body-0028", "role": "body", "section": "Aside: an exact condition with the discriminant", "weight": 1.0} -->

One can also characterize strict positivity through the *discriminant* of a polynomial. As opposed to the second order cone constraints that require solving a convex optimization problem, this condition can be checked explicitly. The discriminant is defined as follows.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Example 1", "weight": 1.0} -->

The discriminant of the polynomial $\sum_{i = 0}^{3}{p_{i}b_{i}{(x)}}$ is (a) The two-dimensional slice p0 = p3 = 1. A point is shaded if b0(x) + p1b1(x) + p2b2(x) + b3(x) is a polynomial in 𝒫 or 𝒟≥.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Example 1", "weight": 1.0} -->

(b) The two-dimensional slice p0 = 1, p3 = 0. A point is shaded if b0(x) + p1b1(x) + p2b2(x) is a polynomial in 𝒫 or 𝒟≥.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 1", "weight": 1.0} -->

Polynomials with repeated roots provide an intuitive connection between the discriminant and the set of nonnegative polynomials. On the one hand, the discriminant of $p$ vanishes precisely when $p$ has repeated roots, as can be seen directly from the definition. On the other hand, the boundary of the set of polynomials nonnegative on $\mathbb{R}$ consists of polynomials with repeated roots. This connection via polynomials with repeated roots suggests that changes in nonnegativity can be characterized by changes in sign of the discriminant.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example 1", "weight": 1.0} -->

There is a caveat for using this intuition for nonnegativity on the interval: it matters whether the repeated root is actually *on* the interval -- it could be outside, or it could even be complex-valued. In those cases the discriminant would vanish, but $p$ may not on the boundary of $\mathcal{P}$. This concern is addressed by ensuring additional conditions, not just sign conditions on $D{(p)}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example 1", "weight": 1.0} -->

Theorem 4 carefully formalizes the connection but requires the definition of a few sets. The interior of the set $\mathcal{P}$, which we denote $\mathcal{P}^{\circ}$, is the set of strictly positive cubic polynomials on the closed interval $\lbrack 0,1\rbrack$. Similarly, $\mathcal{N}\mathcal{B}^{\circ}$ is the set of cubic polynomials with strictly positive Bernstein coefficients. Let $\mathcal{D}^{>}$ be the set of cubic polynomials $p$ such that ${p_{0},p_{3}} > 0$ and ${- {D{(p)}}} > 0$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Example 1", "weight": 1.0} -->

It is evident from Figure 3(a) ‣ Figure 4 ‣ 3.3 Aside: an exact condition with the discriminant ‣ 3 The cubic case ‣ Improved Nonnegativity Testing in the Bernstein Basis via Geometric Means") that $\mathcal{D}^{>}$ is not all of $\mathcal{P}^{\circ}$ (because $\mathcal{P}^{\circ}$ includes $\mathcal{N}\mathcal{B}^{\circ}$). All that is needed is to include $\mathcal{N}\mathcal{B}^{\circ}$: thmexactcubic $\mathcal{P}^{\circ} = {\mathcal{D}^{>} \cup {\mathcal{N}\mathcal{B}^{\circ}}}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 1", "weight": 1.0} -->

On the other hand, $\mathcal{P} \neq {\mathcal{D}^{\geq} \cup {\mathcal{N}\mathcal{B}}}$.^33^3It is easy to overlook these subtle complications on the boundary, but doing so could lead to imprecise results such as Proposition 2 of. If the discriminant of $p$ vanishes when $p \notin {\mathcal{N}\mathcal{B}}$, it is not possible to characterize the sign of $p$ solely based on this information. We can see this in Figure 3(b) ‣ Figure 4 ‣ 3.3 Aside: an exact condition with the discriminant ‣ 3 The cubic case ‣ Improved Nonnegativity Testing in the Bernstein Basis via Geometric Means"). The negative horizontal axis has vanishing discriminant but does not contain nonnegative polynomials. The left hand side of the parabola consists of nonnegative polynomials. To be completely explicit, we provide two polynomials, one from each of these sets, marked with a dot.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 1", "weight": 1.0} -->

These examples show that both $\mathcal{P}$ and its complement have a nonempty intersection with $\mathcal{D}^{\geq}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example 3", "weight": 1.0} -->

Let $s = {{{({1 - x})}^{3} - {6x{({1 - x})}^{2}}} + {3x^{2}{({1 - x})}}} = {{({1 - x})}{({1 - {4x}})}^{2}}$. Not all the Bernstein coefficients are positive and the discriminant of $s$ is zero. Nevertheless, the factored form demonstrates nonnegativity of $s$ on the interval.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example 3", "weight": 1.0} -->

While the exact condition discussed in this section has an explicit form, it only characterizes strictly positive polynomials.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Example 3", "weight": 1.0} -->

A traditional proof of Theorem 4 would involve a somewhat tedious enumeration of cases. Instead of that route, we take a more modern computational approach and use a quantifier elimination program to "derive" the theorem. See Appendix D for a demonstration.

<!-- chunk {"id": "body-0040", "role": "body", "section": "An exact condition with $\\mathcal{G}\\mathcal{B}$", "weight": 1.0} -->

One can also use $\mathcal{G}\mathcal{B}$ to provide an exact characterization of nonnegativity. Recall that we have the strict containment ${\mathcal{G}\mathcal{B}} \subset \mathcal{P}$. Perhaps surprisingly, any element in $\mathcal{P}$ is actually the sum of two elements in the smaller set $\mathcal{G}\mathcal{B}$, i.e., The following proposition shows how to construct $\mathcal{P}$ from two convex subsets of $\mathcal{G}\mathcal{B}$ and yields as a corollary.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Arbitrary degree", "weight": 1.0} -->

Now we extend the definitions of $\mathcal{N}\mathcal{B}$, $\mathcal{P}$, and eventually $\mathcal{G}\mathcal{B}$ to arbitrary degree.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 4", "weight": 1.0} -->

Just as in the cubic case, we can produce sufficient conditions for nonnegativity as follows. Fix an explicit formula for $c_{i}$ in Lemma 21. If a polynomial satisfies those fixed constraints then $p \in \mathcal{P}_{d}$. Setting $c_{i} = 0$ in this procedure gives the defining conditions of $\mathcal{N}\mathcal{B}_{d}$. We propose the choice which gives rise to the condition below. Define $p_{i} = 0$ if $i < 0$ or $i > d$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Polynomial matrices", "weight": 1.0} -->

The same problems and approaches we considered for scalar polynomials generalize to matrix-valued polynomials, or polynomial matrices. A (symmetric) polynomial matrix $P{(x)}$ is given by where ${P_{0},\ldots,P_{d}} \in S^{n}$; that is, the coefficients are symmetric matrices of the same dimensions. Because $P{(x)}$ is symmetric, it has real eigenvalues for every $x$. Before, we were concerned with nonnegativity of polynomials. The analogous property for polynomial matrices is positive semidefiniteness. We want conditions on the $P_{i}$ that guarantee that ${P{(x)}} \succeq 0$ for all $0 \leq x \leq 1$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Polynomial matrices", "weight": 1.0} -->

The approaches from the scalar case can be extended to the polynomial matrix case.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Fact 1 (Theorem 3.4 of )", "weight": 1.0} -->

The geometric mean $A\# B$ is the largest (in the Loewner order) $X \in S^{n}$ such that holds.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Fact 1 (Theorem 3.4 of )", "weight": 1.0} -->

With the correct notions of positive projection and geometric mean in place, we can now define $\mathcal{G}\mathcal{B}_{d}^{n}$ as a natural generalization of $\mathcal{G}\mathcal{B}_{d}$. Let $\mathbf{0}_{n}$ be the $n \times n$ zero matrix. Let $P_{i} = \mathbf{0}_{n}$ if $i < 0$ or $i > d$. We choose which appropriately generalizes and.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

For every application that membership in $\mathcal{N}\mathcal{B}$ is used as a sufficient condition for nonnegativity, it could be worth considering how testing membership in $\mathcal{G}\mathcal{B}$ instead may provide a benefit. Our examples deal with certifying a lower bound $\delta$ on a polynomial $p$, or proving $p - \delta$ is nonnegative. We compare how well $\mathcal{N}\mathcal{B}$ and $\mathcal{G}\mathcal{B}$ work as termination criteria for the subdivision method.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

Recall the subdivision method described in Section 2.2. The computation required by De Casteljau's algorithm in Step 2 exceeds the cost of checking $p \in S$ in Step 1 when $S = {\mathcal{N}\mathcal{B}}$ or $\mathcal{G}\mathcal{B}$, so saving on the number of subdivisions can provide a significant advantage. We therefore count the number of subdivisions required when using the two different nonnegativity criteria.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Varying root locations", "weight": 1.0} -->

The first experiment considers the quadratic polynomials ${({x - t})}^{2}$, written in the cubic Bernstein basis. The rationale of using such a simple model is to gain a fundamental understanding of how the locations of roots affect the subdivision method. Generically, polynomials are locally quadratic near local minima, thus by studying subdivisions of quadratics one can hope to learn about the behavior of higher degree polynomials with several local minima.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Varying root locations", "weight": 1.0} -->

Given a small fixed value of $\delta > 0$, in Figure 5 we report the number of subdivisions required to prove ${({x - t})}^{2} \geq {- \delta}$. The fractal pattern is related to the binary expansion of the root $t$. Both methods do better when a subdivision occurs near the minimizer. For example, ${({x - \frac{1}{2}})}^{2}$ only takes one subdivision because when we subdivide $\lbrack 0,1\rbrack$, the first subdivision split is at $x = \frac{1}{2}$. When $\mathcal{N}\mathcal{B}$ is the termination criterion, a small change in the location of the minimizer may have a big effect on the number of subdivisions required. On the other hand, $\mathcal{G}\mathcal{B}$ is less sensitive to the exact location of the minimizer.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Varying root locations", "weight": 1.0} -->

We can observe from Figure 5 that the number of subdivisions required with $\mathcal{G}\mathcal{B}$ is never bigger than the number required with $\mathcal{N}\mathcal{B}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Varying root locations", "weight": 1.0} -->

The same phenomenon is presented in a different way in Figure 6. We show the percentage of roots $t$ on $\lbrack 0,1\rbrack$ for which fewer than ${1,2,3,4,5},$ and 6 subdivisions are required with each of the nonnegativity criteria to prove ${({x - t})}^{2} \geq {- \delta}$ for a small $\delta > 0$. We see that a nontrivial portion of the ensemble requires just a couple subdivisions when we check nonnegativity with $\mathcal{G}\mathcal{B}$, whereas checking with $\mathcal{N}\mathcal{B}$ frequently requires the maximum number of subdivisions.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Varying matrix size", "weight": 1.0} -->

The second experiment compares different termination criteria in the subdivision method for matrix-valued polynomials of varying sizes whose eigenvalues approach 0 for many $x$. In this case, the subdivisions $P^{1}{(x)}$ and $P^{2}{(x)}$ are defined so that For each $n$, we sample 100 $n \times n$ matrices of the form where the entries of $T$ are independently and identically distributed Gaussian random variables and all $\rho{(x)}$ are random cubic polynomials nonnegative on the interval. The random congruence transformation means that is still always positive semidefinite but implies the eigenvalues are not polynomials in $x$. An example of the eigenvalues for one such $10 \times 10$ matrix are given in Figure 7.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Varying matrix size", "weight": 1.0} -->

We run the subdivision algorithm on the matrix polynomials to prove ${P{(x)}} \succeq {- {\delta I}}$ using $\mathcal{N}\mathcal{B}$ and $\mathcal{G}\mathcal{B}$ as nonnegativity criteria. For each matrix we compute the difference in the number of subdivisions required with each criteria. The average and standard deviations across all 100 matrices are plotted in Figure 8. As the matrices get larger, the average number of subdivisions saved with $\mathcal{G}\mathcal{B}$ increases.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We developed novel simple and explicit conditions to certify nonnegativity of Bernstein polynomials. The new tests better balance the tradeoffs between exact but expensive conditions, and the commonly used test based on nonnegative Bernstein coefficients. The method is based on making explicit choices for the decision variables in the SDP/SOCP characterizations of nonnegativity, bypassing the need to solve them numerically.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion", "weight": 1.5} -->

There are several related open areas for potential further work. An open question is whether there are other reasonable low-complexity choices for the decision variables (that may violate the hypotheses of Proposition 3.2 or that may not satisfy the conditions of Theorem 3.2). Generalizing the basic idea of Proposition 3.2 to higher degrees and the polynomial matrix case is also future work. Finally, it would be interesting to do a more comprehensive evaluation of how well these techniques perform in different applied settings.
