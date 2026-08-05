<!-- arxiv-full-text:v1 {"arxiv_id": "2309.10675", "source": "arxiv-html"} -->

## Introduction

The cubic Bernstein polynomials (e.g.,) are Suppose we have a polynomial $p{(x)}$ such that We would like to find explicit conditions on the real numbers $p_{0},p_{1},p_{2},p_{3}$ (called Bernstein coefficients) that guarantee ${p{(x)}} \geq 0$ on $\lbrack 0,1\rbrack$. This task and its higher degree variants discussed in Section 4 are central questions in applied mathematics. Research on nonnegativity certificates of different kinds is a classical topic in real algebraic geometry, including well-known work by Sturm, Hilbert, Artin, and others; see e.g. and the references therein. More recently, concrete connections to applications in statistics, control, and optimization have heightened interest in finding computation-friendly nonnegativity certificates. Existing conditions that have been used in applications as nonnegativity certificates of on intervals can roughly be classified as follows: Exact characterizations: The Markov--Lukács Theorem (\[44, p. 4\]) gives a necessary and sufficient condition for nonnegativity on an interval. It states that a polynomial $p$ is nonnegative on $\lbrack 0,1\rbrack$ if and only if there exist polynomials $s_{1}$ and $s_{2}$ such that In the cubic case, the polynomials $s_{1}$ and $s_{2}$ are linear, so writing this condition in the language of Bernstein polynomials along with a characterization of polynomials that are sums of squares (SOS) yields the second-order cone (SOCP) condition in Lemma 3. While this condition has fixed computational cost and is necessary and sufficient for a polynomial to be nonnegative on the interval, it is nontrivial to verify -- one has to search for the linear polynomials $s_{1}$ and $s_{2}$, typically via convex optimization.

Alternatively, an exact characterization can be given in terms of the discriminant of $p$. We elaborate on this approach in Section 3.3. As mentioned , conditions of this type on $p$ are typically more complicated to understand and to compute, particularly for higher degrees.

Sufficient conditions: A simple, sufficient condition for nonnegativity of the polynomial $p$ is ${p_{0},p_{1},p_{2},p_{3}} \geq 0$. Because each of the Bernstein polynomials is nonnegative on the interval, a nonnegative combination of them is nonnegative too. This idea was mentioned by Bernstein in 1915, expanded in 1966 , and further discussed more recently . The downside to this condition is that it is potentially conservative -- there are plenty of polynomials nonnegative on $\lbrack 0,1\rbrack$ that have at least one negative Bernstein coefficient.

We give names to the sets of polynomials that satisfy each of these conditions.

### Definition 1

$\mathcal{P}$ ("Positive") is the set of cubic polynomials such that ${p{(x)}} \geq 0$ on $\lbrack 0,1\rbrack$.

### Definition 2

$\mathcal{N}\mathcal{B}$ ("Nonnegative Bernstein") is the set of cubic polynomials whose Bernstein coefficients are all nonnegative.

These conditions reflect two extremes in the tradeoff space between cost and quality of approximation. On the one hand, $\mathcal{P}$ is the full set, but testing membership is nontrivial. On the other hand, $\mathcal{N}\mathcal{B}$ is a smaller set for which checking membership is easy. The purpose of this paper is to introduce a set that lies in between $\mathcal{N}\mathcal{B}$ and $\mathcal{P}$, a set that better trades off accuracy for computational cost. In doing so, we highlight a technique for generating new sufficient conditions for nonnegativity based on making an explicit data-dependent choice of feasible solutions in the SOS characterizations.

In the cubic case, these conditions become the explicit set of inequalities ${p_{0},p_{3}} \geq 0$ and These inequalities imply nonnegativity of $p$ on the interval without requiring solving a program with additional decision variables. This new condition, and its higher degree generalizations, more gracefully balance the tradeoffs between efficiency and approximation power. We show how these fast-to-check, explicit conditions naturally generalize to arbitrary degree (Section 4) and polynomial matrices (Section 5); see Definition 37 and Theorem 14. Finally, we illustrate how using them in the right context may have practical benefits.

### Related work

There is a long history of work related to nonnegativity certificates. Some of the oldest results are due to Descartes, Sylvester, Sturm, Budan and Fourier (see, for instance, ). In the multivariate case, Hilbert's 1888 paper on sums of squares again revitalized the area. Ever since, there has been consistent work on characterizing large classes of nonnegative polynomials. Due the intrinsic computational difficulty of the problem, to varying extents all these methods trade off conservativeness for computational ease.

Bernstein's original 1915 work provided a sufficient condition for nonnegativity on the unit interval. This condition is exceptionally easy to test, and within about fifty years a higher dimensional version was adopted for applications in the context of computer aided design. The higher dimension version is the familiar Bézier curve, which is a parametric curve such that each coordinate is a univariate Bernstein polynomial. Bernstein's sufficient condition in one dimension is exactly the defining condition of $\mathcal{N}\mathcal{B}$; it can be generalized to the containment of a Bézier curve in the polytope defined by the convex hull of the Bernstein coefficient vectors. This condition is tractable enough that it has been used in applications ranging from geometric constraints systems to problems of robust stability.

On the other hand, sum of squares nonnegativity certificates were not too practical until the development of further connections to tractable optimization problems. Sum of squares polynomials became useful for applications when Shor, Nesterov, Parrilo and Lasserre used convex optimization and semidefinite programming to algorithmically check this property. Sum of squares techniques allow a more precise tuning of the computational costs -- the more conservative one wants to be, the more expensive the method becomes. Further work built on this, by restricting to subsets of the set of sum of squares for which checking membership is more tractable. One proposal is to look for easier-to-check certificates; e.g., instead of requiring the associated Gram matrix to be positive semidefinite, one can use the stronger condition of diagonal dominance or scaled diagonal dominance.

Other classes of nonnegativity certificates have also been explored, with an eye towards potential computational benefits. A thread of work that goes back to Reznick, uses a decomposition of a polynomial as a sum whose terms are nonnegative due to the AM-GM inequality. This idea, combined with relative entropy optimization has been used to generate a variety of new nonnegativity conditions including those presented . In general, these sets are incomparable with the set of sum of squares, so they exemplify another compromise between conservativeness and computational ease. These approaches have a similar flavor to our proposal; however, checking the membership condition of the existing methods still requires the solution of some program, so they are generally more expensive than checking Bernstein's condition. Because our conditions are explicit, and do not require solving any optimization programs, they sit closer to the cheaper, less explored end of the tradeoff spectrum.

## Preliminaries

### Notation

We use ${\mathbb{R}}_{d}{\lbrack x\rbrack}$ to denote the vector space of univariate polynomials of degree less than or equal to $d$. Given a set $S$, let $S^{\circ}$ be the interior of the set $S$.

While the paper begins with a focus on univariate polynomials, we eventually generalize our results to polynomial matrices in Section 5. In that case, the analogue of being pointwise nonnegative is to be pointwise positive semidefinite. Let $\mathcal{P}_{d}^{n}$ denote the set of symmetric $n \times n$ univariate polynomial matrices of degree $d$ with nonnegative eigenvalues on the unit interval. For example, $\mathcal{P}_{3}^{1}$ is the set of cubic polynomials nonnegative on $\lbrack 0,1\rbrack$. We use the same subscript/superscript convention for other sets such as in $\mathcal{N}\mathcal{B}_{3}^{1}$. If we drop the dimension superscript or the degree subscript it should be implied from context.

If $x \in {\mathbb{R}}$, let $x_{+} = {\max{(0,x)}}$. Let ${X,Y} \in S^{n}$ be $n \times n$ symmetric matrices. Let $X_{+}$ be the orthogonal projection of $X$ onto the positive semidefinite cone. We write $X \succeq Y$ if $X - Y$ is positive semidefinite and $X \succ Y$ if $X - Y$ is positive definite. If $X$ is positive semidefinite, then $X^{\frac{1}{2}}$ is its matrix square root, which is the unique positive semidefinite matrix $Z$ such that $Z^{2} = X$. Both the projection and the square root can be computed with eigenvalue decompositions; a review of the algorithms are given in Appendix A.

### Second order cones and Bernstein polynomials

The two main ingredients in our method are Bernstein polynomials and second order cones. We define both before presenting the second order cone condition for nonnegativity of a cubic Bernstein polynomial.

### Definition 3

The three-dimensional *rotated second order cone* $\mathcal{Q} \subset {\mathbb{R}}^{3}$ is the set This is a closed convex cone. The point ${(x_{0},x_{1};x_{2})} \in \mathcal{Q}$ if and only if the matrix is positive semidefinite. The second order cone is self-dual; i.e., $\mathcal{Q}$ is the set of points whose inner product with every point in $\mathcal{Q}$ is nonnegative. In particular, if ${(x_{0},x_{1};x_{2})} \in \mathcal{Q}$ and ${(y_{0},y_{1};y_{2})} \in \mathcal{Q}$, then ${{x_{0}y_{0}} + {x_{1}y_{1}} + {x_{2}y_{2}}} \geq 0$. See for more background on $\mathcal{Q}$.

### Definition 4

Let $0 \leq i \leq d$. The $i$th degree $d$ *Bernstein polynomial* is The degree $d$ of $b_{i}$ will be made clear from context.

There are two well-known properties of Bernstein polynomials we use: They form a basis: ${\{ b_{i}\}}_{i = 0}^{d}$ is a basis of ${\mathbb{R}}_{d}{\lbrack x\rbrack}$.

The basis is nonnegative: For every $d$, $0 \leq i \leq d$, and $0 \leq x \leq 1$, ${b_{i}{(x)}} \geq 0$.

Even though the second property is stated for the unit interval, Bernstein polynomials are useful in a more general context. If the interval of interest is not $\lbrack 0,1\rbrack$ but rather $\lbrack r,s\rbrack$, change $b_{i}{(x)}$ to $b_{i}{(\frac{x - r}{s - r})}$. This change of variables allows us to restrict our attention to the $\lbrack 0,1\rbrack$ case without loss of generality.

The following lemma is an algebraic identity relating consecutive Bernstein polynomials. The identity provides a connection between Bernstein polynomials and the second order cone $\mathcal{Q}$.

Then for $1 \leq i \leq {d - 1}$, In particular, for every $0 \leq x \leq 1$,

### Proof

Therefore, the quadratic inequality required by holds with equality -- geometrically, these points all lie on the boundary of $\mathcal{Q}$. ∎

### Definition 5

Let $p \in {{\mathbb{R}}_{d}{\lbrack x\rbrack}}$. The *Bernstein coefficients* of $p$ are the unique real numbers ${\{ p_{i}\}}_{i = 0}^{d}$ such that We write $p_{i}$ to refer to the Bernstein coefficients of a polynomial $p$.

### Subdivision method

The Bernstein coefficients are a key ingredient of the subdivision method to prove nonnegativity of a polynomial on the interval. The basic idea is to recursively bisect the domain, until a given termination criterion is satisfied. The subdivision method with nonnegativity criterion $S$ is described by the following algorithm.

> Check if $p \in S$. If yes, terminate.

> Otherwise, subdivide $p$ into $p^{1}$ and $p^{2}$ (explained below). Repeat algorithm with $p^{1}$ and $p^{2}$ and wait until both calls terminate.

If the algorithm terminates, then $p \in \mathcal{P}$. Termination of the subdivision algorithm is guaranteed for positive polynomials when $S = {\mathcal{N}\mathcal{B}}$. As explained below, if the polynomial $p$ is written in the Bernstein basis, each of the steps can be efficiently computed.

Step 1 of the subdivision method is to check an explicit nonnegativity condition (which we interchangeably call a "termination" or "nonnegativity" criterion). If $S = {\mathcal{N}\mathcal{B}}$, then we can efficiently check whether $p \in {\mathcal{N}\mathcal{B}}$ when the Bernstein coefficients are given.

Step 2 of the subdivision method is to subdivide a polynomial. The idea of subdivision is to split the unit interval into two subintervals and give two polynomials that agree with the original on each half. Those new polynomials are rescaled to be defined on $\lbrack 0,1\rbrack$.

Figure 1: Subdivision of (1 − 2x)2 into the polynomials shown in Figures 0(b) and 0(c) as described .

An illustration of this idea is given for the polynomial ${({1 - {2x}})}^{2}$ in Figure 1. Let ${p{(x)}} \in {{\mathbb{R}}_{d}{\lbrack x\rbrack}}$. Subdividing $p$ gives polynomials $p^{1}{(x)}$ and $p^{2}{(x)}$ such that When the Bernstein coefficients of a polynomial $p$ are known, De Casteljau's algorithm provides an efficient formula for computing the Bernstein coefficients of $p^{1}$ and $p^{2}$. For cubic polynomials, the Bernstein coefficients of $p^{1}$ and $p^{2}$ are In Section 6, we explore how the number of subdivision steps required by this method is impacted by using our new nonnegativity criterion versus using $\mathcal{N}\mathcal{B}$. While we consider just one variant of univariate subdivision, the general idea of subdivision is useful for a variety of problems in robustness analysis and computer-aided design.

## The cubic case

We begin with the cubic case because it is the simplest setting in which our results are nontrivial. First we present the exact condition for nonnegativity alluded to in Section 1 and describe a strategy to use it to get new conditions on polynomials that imply nonnegativity. Then we employ this method to provide one based on geometric means in Section 3.1 and justify why it is natural in Section 3.2. Since in the cubic case the set of nonnegative polynomials can be understood via the discriminant, Section 3.3 contains an exact discriminantal condition, unrelated to our geometric mean one, in order to compare how much simpler ours is. We finish this section by showing how the geometric mean condition can also be used to construct an exact nonnegativity characterization.

The following lemma, written in the language of Bernstein polynomials and second order cones, gives an exact characterization of cubic nonnegativity and is the basis for how we develop our new conditions. lemnonnegativesocp\[Cubic nonnegativity and SOCP\] Let $p \in {{\mathbb{R}}_{3}{\lbrack x\rbrack}}$. The polynomial $p \in \mathcal{P}$ if and only if there exist ${c_{1},c_{2}} \in {\mathbb{R}}$ such that

### Proof

First we prove sufficiency: If the second order cone conditions hold for $p$, then $p \in \mathcal{P}$. In this proof, we write $b_{i}$ to mean $b_{i}{(x)}$ for any fixed $0 \leq x \leq 1$. Plugging $n = 3$ into Lemma 4, we get ${(b_{0},b_{2};{\sqrt{\frac{2}{3}}b_{1}})} \in \mathcal{Q}$ and ${(b_{1},b_{3};{\sqrt{\frac{2}{3}}b_{2}})} \in \mathcal{Q}$. Applying self duality of the second order cone, we get Adding these, we get ${{p_{0}b_{0}} + {p_{1}b_{1}} + {p_{2}b_{2}} + {p_{3}b_{3}}} \geq 0$ as desired. That proves sufficiency.

Next we prove necessity. If $p \geq 0$ on $\lbrack 0,1\rbrack$, then by the Markov--Lukács Theorem (\[44, p. 4\]), ${p{(x)}} = {{xq_{1}^{2}{(x)}} + {{({1 - x})}q_{2}^{2}{(x)}}}$ where $q_{1}{(x)}$ and $q_{2}{(x)}$ are linear functions. A basis of linear functions is given by $\{ x,{1 - x}\}$, so there exist ${M_{1},M_{2}} \succeq 0$ such that The affine constraints on the coefficients give $M_{1} = \begin{pmatrix} \end{pmatrix}$ and $M_{2} = \begin{pmatrix} \end{pmatrix}$ for some ${c_{1},c_{2}} \in {\mathbb{R}}$. Multiplying $M_{1}$ by $\begin{pmatrix} \end{pmatrix}$ on both sides and $M_{2}$ by $\begin{pmatrix} \end{pmatrix}$ on both sides gives two matrices that are positive semidefinite if and only if is satisfied. ∎

### Remark 1

Lemma 3 above can be interpreted as a specialization to the cubic case of the usual SDP characterization of nonnegative polynomials, adapted to the interval; see e.g., \[5, Lemma 3.33\]. This is because SDPs of size $2 \times 2$ can be equivalently written as second-order cone programs.

### A new strategy

If we want to use Lemma 3 to prove that a given polynomial $p \in \mathcal{P}$ is nonnegative on the interval, we must find $c_{1}$ and $c_{2}$ that satisfy. Here are three possible strategies to find $c_{1}$ and $c_{2}$.

### Convex optimization

Given $p$, one option is to solve the convex feasibility problem for some feasible $c_{1}$ and $c_{2}$. This is a foolproof way, in the sense that for every $p \in \mathcal{P}$, there always exist (generally nonunique) solutions $c_{i}$. The drawback of this strategy is the computational cost.

### Constant guess, independent of $p$

On the other extreme, one could ignore $p$ and always try the same constants $c_{1}$ and $c_{2}$. Given any constants $c_{1}$ and $c_{2}$ there is a set of feasible $p$ to induced by any such choice; this set of feasible $p$ is a (possibly empty) convex subset of $\mathcal{P}$. Given $p$ and the fixed constant choices $c_{1}$ and $c_{2}$, checking feasibility of is as simple as verifying a few inequalities.

In fact, this is the strategy used to construct $\mathcal{N}\mathcal{B}$. The set of polynomials that are feasible in when $c_{1} = c_{2} = 0$ is exactly the set $\mathcal{N}\mathcal{B}$. This also points out the main weakness of this strategy: there are plenty of polynomials in $\mathcal{P}$ that are not feasible in for $c_{1} = c_{2} = 0$. For example, consider $p = {{{({1 - x})}{({1 - {4x}})}^{2}} + x^{3}}$, whose Bernstein coefficients are $(1,{- 2},3,1)$, not all of which are nonnegative. On the other hand, the conditions in Lemma 3 hold for $c_{1} = {- 6}$ and $c_{2} = 0$.

### Explicit function of $p$

There is a clear compromise between the two strategies above. We propose instead a middle ground, where $c_{1}$ and $c_{2}$ are "simple," explicit functions of $p$. The decision variables depend on the data, but they are explicit, low-complexity computable functions.

What would be a good definition for $c_{1}$ and $c_{2}$ of this form? A "good choice" for $c_{1}$ and $c_{2}$ is one with the following informally stated properties: Non-inferiority: it should be no worse than fixing $c_{1} = c_{2} = 0$ and Maximality: it should be maximal in some sense.

Formal statements of these properties and additional intuition for our choices are presented in Section 3.2.

For the cubic case, we propose the choice While this is more complicated than $c_{1} = c_{2} = 0$, Section 3.2 provides additional motivation and an argument of why our proposal satisfies the desirata mentioned above. Substituting the values in into gives the conditions that define our new set.

### Definition 6

The set $\mathcal{G}\mathcal{B}$ ("Geometric Bernstein") is Each Bernstein coefficient is bounded below by a multiple of the geometric mean of its neighboring Bernstein coefficients, which motivates the name of the set. A visual comparison of $\mathcal{G}\mathcal{B}$ to $\mathcal{N}\mathcal{B}$ and $\mathcal{P}$ is given in Figure 2.

Figure 2: Membership in 𝒩ℬ, 𝒢ℬ, and 𝒫 for a two dimensional slice (p0 = p3 = 1) of all cubic polynomials. The axes of the graphs are p1 and p2. A point is shaded depending on whether b0(x) + p1b1(x) + p2b2(x) + b3(x) is in 𝒩ℬ, 𝒢ℬ, or 𝒫. The inclusions 𝒩ℬ ⊂ 𝒢ℬ ⊂ 𝒫 are evident, and for this slice each inclusion is strict. We see that the set 𝒢ℬ is not convex.

### Why this definition?

### Non-inferiority

The following theorem formalizes the claim that our choices of $c_{1}$ and $c_{2}$ are at least as good as $c_{1} = c_{2} = 0$. thmthmoneintwointhree ${\mathcal{N}\mathcal{B}} \subset {\mathcal{G}\mathcal{B}} \subset \mathcal{P}$

### Proof of Theorem 3.2

The containment ${\mathcal{N}\mathcal{B}} \subset {\mathcal{G}\mathcal{B}}$ is simple: If all $p_{i} \geq 0$, the left hand side of all inequalities in are nonnegative and the right hand sides are nonpositive. Therefore $p \in {\mathcal{G}\mathcal{B}}$.

Next, we show that ${\mathcal{G}\mathcal{B}} \subset \mathcal{P}$. Let $p \in {\mathcal{G}\mathcal{B}}$. We claim setting $c_{1}$ and $c_{2}$ as in satisfies. The constraint ${(p_{0},{p_{2} - \frac{c_{2}}{3}};\frac{c_{1}}{\sqrt{6}})} \in \mathcal{Q}$ is a combination of three inequalities: $p_{0} \geq 0$: This is required by membership in $\mathcal{G}\mathcal{B}$. ${2p_{0}{({p_{2} - \frac{c_{2}}{3}})}} \geq \frac{c_{1}^{2}}{6}$: First consider the case $p_{2} \geq 0$. We always have $c_{2} \leq 0$, so ${2p_{0}{({p_{2} - \frac{c_{2}}{3}})}} \geq {2p_{0}p_{2}} = \frac{c_{1}^{2}}{6}$. In the other case $p_{2} < 0$ and so $c_{1} = 0$. In that case the first two inequalities prove the product is nonnegative.

Therefore this second order cone condition is satisfied. The argument that the other second order cone condition holds is analogous.∎ A less precise, but more insightful, "picture proof" that ${\mathcal{N}\mathcal{B}} \subset {\mathcal{G}\mathcal{B}}$ is given in Figure 3, which also motivates the choice of $c_{1}$ and $c_{2}$. The feasible region of each second order cone condition is the shaded region inside of each parabola. We want a point $(c_{1},c_{2})$ inside the intersection of these two regions. The set $\mathcal{N}\mathcal{B}$ results from picking the origin. The $\star$ will always be in the intersection whenever the origin is.

The intuition for why $\mathcal{G}\mathcal{B}$ strictly contains $\mathcal{N}\mathcal{B}$ is the following. If $p_{1} < 0$, the horizontal parabola moves left. Then we would choose $c_{2} = 0$, but picking a negative $c_{1}$ may still be in the intersection even if the origin is not.

Figure 3: The feasibility region of (c1, c2) for Lemma 3 when pi > 0. Re-arrange the conditions given by the second order cone problem to get $c_{2} \leq \frac{{12p_{0}p_{2}} - c_{1}^{2}}{4p_{0}}$ and $c_{1} \leq \frac{{12p_{1}p_{3}} - c_{2}^{2}}{4p_{3}}$. The region of feasibility for c1 and c2 is the intersection of the shaded regions bounded by the parabolas. When $c_{1} = {- {2\sqrt{3p_{0}p_{2}}}}$, then as long as c2 ≤ 0, the point will be in the feasible region of the vertical parabola. Similar reasoning follows for the horizontal parabola. The choice made for 𝒢ℬ is marked with a star, as opposed to the choice used for 𝒩ℬ.

### Maximality

Now that we have established our choice of $c_{1}$ and $c_{2}$ is "better" than $c_{1} = c_{2} = 0$, we formalize the sense in which our choice is maximal. In general, $c_{1}$ and $c_{2}$ could be functions of all of the Bernstein coefficients; i.e., $c_{1} = {g{(p_{0},p_{1},p_{2},p_{3})}}$ and $c_{2} = {h{(p_{0},p_{1},p_{2},p_{3})}}$.^11^1For instance, if $g$ and $h$ were defined as giving the analytic center \[13, §8.5\] of the convex set, then that $g$ and $h$ would always give $c_{1}$ and $c_{2}$ that prove nonnegativity whenever $p$ is nonnegative on the interval. This yields $g$ and $h$ that are semialgebraic functions, but they would be "too complicated" for a simple test. For the sake of simplicity our choice of $g$ and $h$ will be such that they are only functions of *two* of the Bernstein coefficients each. Furthermore, by symmetry, we restrict our attention to those where $c_{1} = {g{(p_{0},p_{1},p_{2},p_{3})}} = {f{(p_{0},p_{2})}}$ and $c_{2} = {h{(p_{0},p_{1},p_{2},p_{3})}} = {f{(p_{3},p_{1})}}$ for some $f:{{\mathbb{R}}^{2}\rightarrow{\mathbb{R}}}$. Let $S{(f)}$ be the set Using a single $f$ for both $c_{1}$ and $c_{2}$ ensures that membership in $S{(f)}$ does not change when transforming $p$ by $x\rightarrow{1 - x}$. For our choice, we take ${f{(z_{1},z_{2})}} = {- {2\sqrt{3{(z_{1})}_{+}{(z_{2})}_{+}}}}$, which we denote as $f^{*}$. For reference, ${S{(f^{*})}} = {\mathcal{G}\mathcal{B}}$ and ${S{}} = {\mathcal{N}\mathcal{B}}$. Within this family, $S{(f^{*})}$ is maximal in the sense of the following proposition, which is proven in Appendix C. proptight If there exists a $p \in {{\mathcal{G}\mathcal{B}} \smallsetminus {\mathcal{N}\mathcal{B}}}$ such that both ${f{(p_{0},p_{2})}} \neq {f^{*}{(p_{0},p_{2})}}$ and ${f{(p_{3},p_{1})}} \neq {f^{*}{(p_{3},p_{1})}}$, then ${S{(f^{*})}} ⊄ {S{(f)}}$. Equivalently, if ${S{(f^{*})}} \subset {S{(f)}}$ then for every $p \in {{\mathcal{G}\mathcal{B}} \smallsetminus {\mathcal{N}\mathcal{B}}}$, either ${f{(p_{0},p_{2})}} = {f^{*}{(p_{0},p_{2})}}$ or ${f{(p_{3},p_{1})}} = {f^{*}{(p_{3},p_{1})}}$.

### Aside: an exact condition with the discriminant

One can also characterize strict positivity through the *discriminant* of a polynomial. As opposed to the second order cone constraints that require solving a convex optimization problem, this condition can be checked explicitly. The discriminant is defined as follows.

### Definition 7

The *discriminant* of a polynomial $p$ with leading coefficient $a_{n}$ in the monomial basis and roots $\alpha_{i}$ for $1 \leq i \leq n$ is Although not obvious from this definition, $D{(p)}$ is a polynomial in the (monomial or Bernstein) coefficients of $p$.

For now we are only concerned with cubic polynomials, so we explicitly compute the discriminant for this case in terms of Bernstein coefficients.

### Example 1

The discriminant of the polynomial $\sum_{i = 0}^{3}{p_{i}b_{i}{(x)}}$ is (a) The two-dimensional slice p0 = p3 = 1. A point is shaded if b0(x) + p1b1(x) + p2b2(x) + b3(x) is a polynomial in 𝒫 or 𝒟≥.

(b) The two-dimensional slice p0 = 1, p3 = 0. A point is shaded if b0(x) + p1b1(x) + p2b2(x) is a polynomial in 𝒫 or 𝒟≥.

Figure 4: The relationship between 𝒫 and the discriminant for two slices of the set of cubic polynomials. The axes of the graphs are p1 and p2. The bold black curves mark where the discriminant vanishes. Figure 3(a) shows that 𝒟≥ does not contain all of 𝒫. We remark that although the discriminant is irreducible, it may factor when restricted to a two-dimensional slice, as in Figure 3(b). This also shows that the discriminant can vanish even for polynomials that are not on the boundary of 𝒫. The dots mark the polynomials r and s used in Examples 2 and 3.

Polynomials with repeated roots provide an intuitive connection between the discriminant and the set of nonnegative polynomials. On the one hand, the discriminant of $p$ vanishes precisely when $p$ has repeated roots, as can be seen directly from the definition . On the other hand, the boundary of the set of polynomials nonnegative on $\mathbb{R}$ consists of polynomials with repeated roots. This connection via polynomials with repeated roots suggests that changes in nonnegativity can be characterized by changes in sign of the discriminant.

There is a caveat for using this intuition for nonnegativity on the interval: it matters whether the repeated root is actually *on* the interval -- it could be outside, or it could even be complex-valued. In those cases the discriminant would vanish, but $p$ may not on the boundary of $\mathcal{P}$. This concern is addressed by ensuring additional conditions, not just sign conditions on $D{(p)}$.

Theorem 4 carefully formalizes the connection but requires the definition of a few sets. The interior of the set $\mathcal{P}$, which we denote $\mathcal{P}^{\circ}$, is the set of strictly positive cubic polynomials on the closed interval $\lbrack 0,1\rbrack$. Similarly, $\mathcal{N}\mathcal{B}^{\circ}$ is the set of cubic polynomials with strictly positive Bernstein coefficients. Let $\mathcal{D}^{>}$ be the set of cubic polynomials $p$ such that ${p_{0},p_{3}} > 0$ and ${- {D{(p)}}} > 0$. Let $\mathcal{D}^{\geq}$ be the set of cubic $p$ polynomials such that ${p_{0},p_{3}} \geq 0$ and ${- {D{(p)}}} \geq 0$.^22^2In fact, $\mathcal{D}^{\geq}$ is not the closure of $\mathcal{D}^{>}$. To see this, note the polynomial $r$ in Example 2 is in $\mathcal{D}^{\geq}$ but is not the limit point of a sequence in $\mathcal{D}^{>}$. It is evident from Figure 3(a) ‣ Figure 4 ‣ 3.3 Aside: an exact condition with the discriminant ‣ 3 The cubic case ‣ Improved Nonnegativity Testing in the Bernstein Basis via Geometric Means") that $\mathcal{D}^{>}$ is not all of $\mathcal{P}^{\circ}$ (because $\mathcal{P}^{\circ}$ includes $\mathcal{N}\mathcal{B}^{\circ}$). All that is needed is to include $\mathcal{N}\mathcal{B}^{\circ}$: thmexactcubic $\mathcal{P}^{\circ} = {\mathcal{D}^{>} \cup {\mathcal{N}\mathcal{B}^{\circ}}}$. On the other hand, $\mathcal{P} \neq {\mathcal{D}^{\geq} \cup {\mathcal{N}\mathcal{B}}}$.^33^3It is easy to overlook these subtle complications on the boundary, but doing so could lead to imprecise results such as Proposition 2 of. If the discriminant of $p$ vanishes when $p \notin {\mathcal{N}\mathcal{B}}$, it is not possible to characterize the sign of $p$ solely based on this information. We can see this in Figure 3(b) ‣ Figure 4 ‣ 3.3 Aside: an exact condition with the discriminant ‣ 3 The cubic case ‣ Improved Nonnegativity Testing in the Bernstein Basis via Geometric Means"). The negative horizontal axis has vanishing discriminant but does not contain nonnegative polynomials. The left hand side of the parabola consists of nonnegative polynomials. To be completely explicit, we provide two polynomials, one from each of these sets, marked with a dot. These examples show that both $\mathcal{P}$ and its complement have a nonempty intersection with $\mathcal{D}^{\geq}$.

### Example 2

Let $r = {{({1 - x})}^{3} - {6x{({1 - x})}^{2}}}$. Not all the Bernstein coefficients are positive and the discriminant of $r$ is zero, but ${r{(\frac{1}{2})}} = {- \frac{5}{8}}$, so $r$ is not positive.

### Example 3

Let $s = {{{({1 - x})}^{3} - {6x{({1 - x})}^{2}}} + {3x^{2}{({1 - x})}}} = {{({1 - x})}{({1 - {4x}})}^{2}}$. Not all the Bernstein coefficients are positive and the discriminant of $s$ is zero. Nevertheless, the factored form demonstrates nonnegativity of $s$ on the interval.

While the exact condition discussed in this section has an explicit form, it only characterizes strictly positive polynomials.

A traditional proof of Theorem 4 would involve a somewhat tedious enumeration of cases. Instead of that route, we take a more modern computational approach and use a quantifier elimination program to "derive" the theorem. See Appendix D for a demonstration.

### An exact condition with $\mathcal{G}\mathcal{B}$

One can also use $\mathcal{G}\mathcal{B}$ to provide an exact characterization of nonnegativity. Recall that we have the strict containment ${\mathcal{G}\mathcal{B}} \subset \mathcal{P}$. Perhaps surprisingly, any element in $\mathcal{P}$ is actually the sum of two elements in the smaller set $\mathcal{G}\mathcal{B}$, i.e., The following proposition shows how to construct $\mathcal{P}$ from two convex subsets of $\mathcal{G}\mathcal{B}$ and yields as a corollary.

### Proposition 1

| | $S =$ | $\left\{ {\sum\limits_{i = 0}^{3}{s_{i}b_{i}^{3}{(x)}}} \middle| {\left(s_{0},s_{2};{\sqrt{\frac{3}{2}}s_{1}} \right) \in {\mathcal{Q}\textit{~and~}s_{3}} \geq 0} \right\}\textit{~and}$ | | \(20\) | | | $T =$ | $\left\{ {\sum\limits_{i = 0}^{3}{t_{i}b_{i}^{3}{(x)}}} \middle| {\left(t_{1},t_{3};{\sqrt{\frac{3}{2}}t_{2}} \right) \in {\mathcal{Q}\textit{~and~}t_{0}} \geq 0} \right\}.$ | | | Then, ${{S + T} = \mathcal{P}},$ which implies ${{\mathcal{G}\mathcal{B}} + {\mathcal{G}\mathcal{B}}} = \mathcal{P}$.

### Proof

Since ${S,T} \subseteq {\mathcal{G}\mathcal{B}}$, and ${\mathcal{G}\mathcal{B}} \subset \mathcal{P}$, we have ${S,T} \subset \mathcal{P}$. Furthermore, $\mathcal{P}$ is a cone, so ${S + T} \subset \mathcal{P}$. For the other direction, suppose that $p \in \mathcal{P}$. We will decompose $p = {s + t}$ and show $s \in S$ and $t \in T$. Let $c_{1},c_{2}$ be the constants guaranteed to exist for $p$ by Lemma 3. Let the Bernstein coefficients of $s$ be $(p_{0},\frac{c_{1}}{3},{p_{2} - \frac{c_{2}}{3}},0)$ and let the Bernstein coefficients of $t$ be $(0,{p_{1} - \frac{c_{1}}{3}},\frac{c_{2}}{3},p_{3})$. All that is left is to show that $s \in S$ and $t \in T$. First, $s \in S$ because ${(s_{0},s_{2};{\sqrt{\frac{3}{2}}s_{1}})} \in \mathcal{Q}$ if and only if ${(p_{0},{p_{2} - \frac{c_{2}}{3}};\frac{c_{1}}{\sqrt{6}})} \in \mathcal{Q}$, which is guaranteed by the choice of $c_{1}$ and $c_{2}$. The same argument shows $t \in T$. Hence the decomposition is valid. Therefore, $P \subset {S + T}$. ∎

## Arbitrary degree

Now we extend the definitions of $\mathcal{N}\mathcal{B}$, $\mathcal{P}$, and eventually $\mathcal{G}\mathcal{B}$ to arbitrary degree.

### Definition 8

$\mathcal{P}_{d}$ ("Positive") is the set of $p \in {{\mathbb{R}}_{d}{\lbrack x\rbrack}}$ such that $p$ is nonnegative on $\lbrack 0,1\rbrack$.

### Definition 9

$\mathcal{N}\mathcal{B}_{d}$ ("Nonnegative Bernstein") is the set of $p \in {{\mathbb{R}}_{d}{\lbrack x\rbrack}}$ such that $p$ has all nonnegative Bernstein coefficients.

In this section, we propose the corresponding generalization of $\mathcal{G}\mathcal{B}$. To accomplish this, one can attempt to generalize Lemma 3 for arbitrary degree. However, whereas in the cubic case the second order cone conditions are necessary and sufficient for nonnegativity, in the general case this requires instead a semidefinite program. This is too computationally expensive, so we restrict to only *tridiagonal* matrices, which will give an SOCP condition. We then make strategic choices for the decision variables in the SOCP.

To ease notation, define Recall that $m_{i} = {\frac{1}{2} \cdot \frac{{({i + 1})} \cdot {({{d - i} + 1})}}{i \cdot {({d - i})}}}$. Here is a sufficient condition for nonnegativity written in terms of second order cones and Bernstein coefficients. {restatable}lemgennonnegativesocp Let $p \in {{\mathbb{R}}_{d}{\lbrack x\rbrack}}$ with Bernstein coefficients ${\{ p_{i}\}}_{i = 0}^{d}$. Let $c_{0} = c_{d} = 0$. If there exist ${c_{1},\ldots,c_{d - 1}} \in {\mathbb{R}}$ such that for all $1 \leq i \leq {d - 1}$

### Proof

Throughout this proof we use $b_{i}$ to mean $b_{i}{(x)}$ for any $0 \leq x \leq 1$. Constraint is equivalent to By Lemma 4, for all $1 \leq i \leq {d - 1}$, ${(b_{i - 1},b_{i + 1};{\frac{1}{\sqrt{m_{i}}}b_{i}})} \in \mathcal{Q}$.

The inner product between constraint $i$ of Lemma 4 and the $i$th constraint of is by self-duality of the second order cone. Sum all of these results from $1 \leq i \leq {d - 1}$ to get In Appendix B we give an alternative proof of the lemma that shows is a restricted case of sums of squares, where the Gram matrix is constrained to be tridiagonal.

Unlike in the cubic case, Lemma 21 is only a sufficient condition for nonnegativity. To emphasize that it is sufficient but not necessary, consider the following example of a nonnegative polynomial for which is not feasible.

### Example 4

Let $p = {({{2x} - 1})}^{4}$. Clearly ${p{(x)}} \geq 0$. The Bernstein coefficients are $(1,{- 1},1,{- 1},1)$, but there are no feasible $c_{i}$ .

Just as in the cubic case, we can produce sufficient conditions for nonnegativity as follows. Fix an explicit formula for $c_{i}$ in Lemma 21. If a polynomial satisfies those fixed constraints then $p \in \mathcal{P}_{d}$. Setting $c_{i} = 0$ in this procedure gives the defining conditions of $\mathcal{N}\mathcal{B}_{d}$. We propose the choice which gives rise to the condition below. Define $p_{i} = 0$ if $i < 0$ or $i > d$.

### Definition 10

$\mathcal{G}\mathcal{B}_{d}$ is the set of $p \in {{\mathbb{R}}_{d}{\lbrack x\rbrack}}$ for which for every $0 \leq i \leq d$, The following theorem shows that this choice of $c_{i}$ is not worse than $c_{i} = 0$. {restatable}\Generalized Theorem [3.2\]thmgenoneintwointhree ${\mathcal{N}\mathcal{B}_{d}} \subset {\mathcal{G}\mathcal{B}_{d}} \subset \mathcal{P}_{d}$.

### Proof

For this proof we drop the subscript $d$ but it is understood that all polynomials are degree $d$. It is clear that if every $p_{i} \geq 0$, then they are all at least some nonpositive number, so $p \in {\mathcal{N}\mathcal{B}}$.

Next, we show that ${\mathcal{G}\mathcal{B}} \subset \mathcal{P}$. Let $p \in {\mathcal{G}\mathcal{B}_{d}}$. We claim that setting $c_{i}$ as in for every $i$ makes feasible. The second order cone condition is satisfied if and only if both of the following hold: $p_{i - 1} \geq c_{i - 1}$ and $p_{i + 1} \geq c_{i - 1}$: These are implied by the definition of $p \in {\mathcal{G}\mathcal{B}}$. ${2w_{i - 1}w_{i + 1}{({p_{i - 1} - c_{i - 1}})}{({p_{i + 1} - c_{i + 1}})}} \geq {m_{i}c_{i}^{2}}$: If either $p_{i - 1}$ or $p_{i + 1}$ are not positive, then $c_{i} = 0$. Since the two factors are nonnegative, the inequality holds in that case. Otherwise, when ${p_{i - 1},p_{i + 1}} \geq 0$, we have due to the nonpositivity of $c_{i - 1}$ and $c_{i + 1}$ and the definition of $c_{i}^{2}$.

Therefore, the second order cone condition is feasible with this choice, and so $p \in \mathcal{P}$. ∎

## Polynomial matrices

The same problems and approaches we considered for scalar polynomials generalize to matrix-valued polynomials, or polynomial matrices. A (symmetric) polynomial matrix $P{(x)}$ is given by where ${P_{0},\ldots,P_{d}} \in S^{n}$; that is, the coefficients are symmetric matrices of the same dimensions. Because $P{(x)}$ is symmetric, it has real eigenvalues for every $x$. Before, we were concerned with nonnegativity of polynomials. The analogous property for polynomial matrices is positive semidefiniteness. We want conditions on the $P_{i}$ that guarantee that ${P{(x)}} \succeq 0$ for all $0 \leq x \leq 1$.

The approaches from the scalar case can be extended to the polynomial matrix case. We define the matrix analogues of $\mathcal{P}$ and $\mathcal{N}\mathcal{B}$ as follows:

### Definition 11

$\mathcal{P}_{d}^{n}$ is the set of $n \times n$ symmetric polynomial matrices $P{(x)}$ whose entries are in ${\mathbb{R}}_{d}{\lbrack x\rbrack}$ and ${P{(x)}} \succeq 0$ for all $0 \leq x \leq 1$.

### Definition 12

$\mathcal{N}\mathcal{B}_{d}^{n}$ is the set of $n \times n$ symmetric polynomial matrices $P{(x)}$ whose entries are in ${\mathbb{R}}_{d}{\lbrack x\rbrack}$ and $P_{i} \succeq 0$ for every $0 \leq i \leq d$.

To define sets in the tradeoff space between these extremes, we generalize Lemma 21 to the polynomial matrix case. Recall the definitions of $m_{i}$ and $w_{i}$ from and. {restatable}lemgenmatrixnonnegativesocp Let ${P{(x)}} = {\sum_{i = 0}^{d}{b_{i}{(x)}P_{i}}}$ where $P_{i} \in S^{n}$. Let $C_{0}$ and $C_{d}$ be the zero matrix. If there exist $C_{i} \in {\mathbb{R}}^{n \times n}$ for $1 \leq i \leq {d - 1}$ such that for all $1 \leq i \leq {d - 1}$

### Proof

Let $\mathbf{1}_{n}$ be the $n \times n$ matrix of all 1's and $I_{n}$ be the $n \times n$ identity matrix. By Lemma 4, for every $0 \leq x \leq 1$. So on this domain, ${{B_{i}{(x)}} \otimes \mathbf{1}_{n}} \succeq 0$. Suppose the $C_{i}$ satisfy equation for $P$. The Schur product theorem implies the Hadamard product of ${B_{i}{(x)}} \otimes \mathbf{1}_{n}$ with the $i$th matrix in is positive semidefinite. Summing these Hadamard products over $1 \leq i \leq {d - 1}$ gives Finally, matrix congruence preserves positive semidefiniteness, so because the terms occurring twice have $w_{i} = \frac{1}{2}$ and the others have $w_{i} = 1$. Therefore $P \in \mathcal{P}_{d}^{n}$. ∎ Recall that in the scalar case our choice was given. This expression suggests that the choice for $C_{i}$ may require the matrix version of two natural operations: projection onto the "positive" part, and a generalized notion of geometric mean. Luckily, both of these are possible. As mentioned earlier, given a matrix $X$, its projection $X_{+}$ onto the positive semidefinite cone can be computed with an eigenvalue decomposition; details are presented in Appendix A. The key property of the scalar geometric mean that we want to extend is: given ${a,b} \geq 0$, their geometric mean is the largest number $x \geq 0$ such that For the matrix case, we can ask for the generalized property: given ${A,B} \succeq 0$ (which will be ${(P_{i - 1})}_{+}$ and ${(P_{i + 1})}_{+}$), their "geometric mean" should be an $X \succeq 0$ such that It turns out that the *matrix geometric mean* of $A$ and $B$ has exactly this property.

### Definition 13

Let ${A,B} \succ 0$. The *geometric mean* of $A$ and $B$, denoted $A\# B$, is given by One can extend the definition to all ${A,B} \succeq 0$ by continuity.

Although is not obviously symmetric in $A$ and $B$, it indeed holds that ${A\# B} = {B\# A}$. There are many other beautiful properties of the matrix geometric mean, including strong connections to Riemannian geometry; see e.g.. The following fact is the key property we need.

### Fact 1 (Theorem 3.4 of )

The geometric mean $A\# B$ is the largest (in the Loewner order) $X \in S^{n}$ such that holds.

With the correct notions of positive projection and geometric mean in place, we can now define $\mathcal{G}\mathcal{B}_{d}^{n}$ as a natural generalization of $\mathcal{G}\mathcal{B}_{d}$. Let $\mathbf{0}_{n}$ be the $n \times n$ zero matrix. Let $P_{i} = \mathbf{0}_{n}$ if $i < 0$ or $i > d$. We choose which appropriately generalizes and.

### Definition 14

$\mathcal{G}\mathcal{B}_{d}^{n}$ is the set of $n \times n$ polynomial matrices $\sum_{i = 0}^{d}{b_{i}{(x)}P_{i}}$ such that for all $0 \leq i \leq d$, Finally, we show this definition is in the trade space between $\mathcal{N}\mathcal{B}_{d}^{n}$ and $\mathcal{P}_{d}^{n}$, and this theorem implies Theorems 3.2 and 10.{restatable}thmarbitrarygeneralinclusions ${\mathcal{N}\mathcal{B}_{d}^{n}} \subset {\mathcal{G}\mathcal{B}_{d}^{n}} \subset \mathcal{P}_{d}^{n}$.

### Proof

First suppose that $P \in {\mathcal{N}\mathcal{B}_{d}^{n}}$. Since $P_{i} \succeq 0$, if $M \in S^{n}$ has nonpositive eigenvalues, then ${P_{i} - M} \succeq 0$. In particular, $- 1$ times the geometric mean of $P_{i - 1}$ and $P_{i + 1}$ has nonpositive eigenvalues. Therefore $P \in {\mathcal{G}\mathcal{B}_{d}^{n}}$.

Next we argue that if $P \in {\mathcal{G}\mathcal{B}_{d}^{n}}$ then choosing $C_{i}$ as in is feasible. If either $P_{i - 1}$ or $P_{i + 1}$ is indefinite, then the only thing to check is that both $P_{i - 1} - C_{i - 1} - C_{i - 1}^{T}$ and $P_{i + 1} - C_{i + 1} - C_{i + 1}^{T}$ are positive semidefinite (because the off-diagonal entries are 0). This is exactly the condition that $P \in {\mathcal{G}\mathcal{B}}$. On the other hand, if both are positive semidefinite, then we need to show By Fact 1. ‣ 5 Polynomial matrices ‣ Improved Nonnegativity Testing in the Bernstein Basis via Geometric Means"), This means for all ${x,y} \in {\mathbb{R}}^{n}$, | | $0$ | $\leq {\begin{pmatrix} | | \(40\) | | | | \end{pmatrix}^{T}\begin{pmatrix} | | | | | | \end{pmatrix}\begin{pmatrix} | | | | | | \end{pmatrix}^{T}\begin{pmatrix} | | | | | | \end{pmatrix}\begin{pmatrix} | | | so the first matrix in is positive semidefinite. The second matrix is positive semidefinite because the block diagonals are geometric means, which are positive semidefinite. Therefore the sum is as well. Hence $P \in \mathcal{P}_{d}^{n}$. ∎

## Numerical experiments

For every application that membership in $\mathcal{N}\mathcal{B}$ is used as a sufficient condition for nonnegativity, it could be worth considering how testing membership in $\mathcal{G}\mathcal{B}$ instead may provide a benefit. Our examples deal with certifying a lower bound $\delta$ on a polynomial $p$, or proving $p - \delta$ is nonnegative. We compare how well $\mathcal{N}\mathcal{B}$ and $\mathcal{G}\mathcal{B}$ work as termination criteria for the subdivision method.

Recall the subdivision method described in Section 2.2. The computation required by De Casteljau's algorithm in Step 2 exceeds the cost of checking $p \in S$ in Step 1 when $S = {\mathcal{N}\mathcal{B}}$ or $\mathcal{G}\mathcal{B}$, so saving on the number of subdivisions can provide a significant advantage. We therefore count the number of subdivisions required when using the two different nonnegativity criteria.

### Varying root locations

The first experiment considers the quadratic polynomials ${({x - t})}^{2}$, written in the cubic Bernstein basis. The rationale of using such a simple model is to gain a fundamental understanding of how the locations of roots affect the subdivision method. Generically, polynomials are locally quadratic near local minima, thus by studying subdivisions of quadratics one can hope to learn about the behavior of higher degree polynomials with several local minima.

Given a small fixed value of $\delta > 0$, in Figure 5 we report the number of subdivisions required to prove ${({x - t})}^{2} \geq {- \delta}$. The fractal pattern is related to the binary expansion of the root $t$. Both methods do better when a subdivision occurs near the minimizer. For example, ${({x - \frac{1}{2}})}^{2}$ only takes one subdivision because when we subdivide $\lbrack 0,1\rbrack$, the first subdivision split is at $x = \frac{1}{2}$. When $\mathcal{N}\mathcal{B}$ is the termination criterion, a small change in the location of the minimizer may have a big effect on the number of subdivisions required. On the other hand, $\mathcal{G}\mathcal{B}$ is less sensitive to the exact location of the minimizer. We can observe from Figure 5 that the number of subdivisions required with $\mathcal{G}\mathcal{B}$ is never bigger than the number required with $\mathcal{N}\mathcal{B}$.

Figure 5: Number of subdivisions required to prove (x − t)2 ≥ −δ for δ = 10−4 with the subdivision method and different nonnegativity criteria. When 𝒢ℬ is the nonnegativity criterion, the number of subdivisions is less sensitive to whether a subdivision location exactly coincides with t.

The same phenomenon is presented in a different way in Figure 6. We show the percentage of roots $t$ on $\lbrack 0,1\rbrack$ for which fewer than ${1,2,3,4,5},$ and 6 subdivisions are required with each of the nonnegativity criteria to prove ${({x - t})}^{2} \geq {- \delta}$ for a small $\delta > 0$. We see that a nontrivial portion of the ensemble requires just a couple subdivisions when we check nonnegativity with $\mathcal{G}\mathcal{B}$, whereas checking with $\mathcal{N}\mathcal{B}$ frequently requires the maximum number of subdivisions.

Figure 6: Percentage of instances for which the subdivision method requires no more than N subdivisions to prove (x − t)2 ≥ −δ (with δ = 10−4, and t uniformly distributed in ). Even with just a few subdivisions, a large number of the bounds can be proven with the subdivision method and 𝒢ℬ as a nonnegativity condition.

### Varying matrix size

The second experiment compares different termination criteria in the subdivision method for matrix-valued polynomials of varying sizes whose eigenvalues approach 0 for many $x$. In this case, the subdivisions $P^{1}{(x)}$ and $P^{2}{(x)}$ are defined so that For each $n$, we sample 100 $n \times n$ matrices of the form where the entries of $T$ are independently and identically distributed Gaussian random variables and all $\rho{(x)}$ are random cubic polynomials nonnegative on the interval. The random congruence transformation means that is still always positive semidefinite but implies the eigenvalues are not polynomials in $x$. An example of the eigenvalues for one such $10 \times 10$ matrix are given in Figure 7.

Figure 7: Eigenvalues of a random 10 × 10 polynomial matrix sampled according to. Notice that the eigenvalues are small for many x.

We run the subdivision algorithm on the matrix polynomials to prove ${P{(x)}} \succeq {- {\delta I}}$ using $\mathcal{N}\mathcal{B}$ and $\mathcal{G}\mathcal{B}$ as nonnegativity criteria. For each matrix we compute the difference in the number of subdivisions required with each criteria. The average and standard deviations across all 100 matrices are plotted in Figure 8. As the matrices get larger, the average number of subdivisions saved with $\mathcal{G}\mathcal{B}$ increases.

Figure 8: Number of subdivisions required with 𝒩ℬ or 𝒢ℬ as nonnegativity criteria to prove P(x) ≽ δI with δ = 10−4 for 100 random matrices sampled according to. The average number of subdivisions saved with 𝒢ℬ instead of 𝒩ℬ increases as the matrices get bigger. The percentage of subdivisions saved is roughly 20%. Vertical bars are one standard deviation of counts (left) or differences (right).

## Conclusion

We developed novel simple and explicit conditions to certify nonnegativity of Bernstein polynomials. The new tests better balance the tradeoffs between exact but expensive conditions, and the commonly used test based on nonnegative Bernstein coefficients. The method is based on making explicit choices for the decision variables in the SDP/SOCP characterizations of nonnegativity, bypassing the need to solve them numerically.

There are several related open areas for potential further work. An open question is whether there are other reasonable low-complexity choices for the decision variables (that may violate the hypotheses of Proposition 3.2 or that may not satisfy the conditions of Theorem 3.2). Generalizing the basic idea of Proposition 3.2 to higher degrees and the polynomial matrix case is also future work. Finally, it would be interesting to do a more comprehensive evaluation of how well these techniques perform in different applied settings.
