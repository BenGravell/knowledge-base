<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Applied Random Matrix Theory

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Random matrices now play a role in many parts of computational mathematics. To advance these applications, it is desirable to have tools that are flexible, easy to use, and powerful. Over the last 25 years, researchers have developed a remarkable family of results, called matrix concentration inequalities, that meet the criteria. This paper offers an invitation to the field of matrix concentration and its multifarious applications.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

Random matrices now play a role in many parts of computational mathematics. To advance these applications, it is desirable to have tools that are flexible, easy to use, and powerful. Over the last 25 years, researchers have developed a remarkable family of results, called matrix concentration inequalities, that meet the criteria. This paper offers an invitation to the field of matrix concentration and its multifarious applications.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Motivation", "weight": 1.0} -->

Random matrix theory emerged from applications in statistics (sample covariance matrices \[:Generalised-Product\]) and in nuclear physics (Hamiltonians of heavy nuclei \[:Characteristic-Vectors\]). The subject established itself within the mathematical firmament through deep connections to number theory (zeros of the Riemann zeta function \[:Pair-Correlation\]), operator algebras (free product factors \[:Free-Random\]), combinatorics (longest increasing subsequence \[:Distribution-Length\]), and beyond. Over the last generation, random matrices have attracted new attention in computational mathematics, starting with work in algorithms \[:Geometry-Graphs\] and in quantum information \[:Strong-Converse\], and expanding in waves that have touched the farthest shores.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Motivation", "weight": 1.0} -->

The classic literature emphasizes random matrices that enjoy a harmonious mathematical structure, such as the independent and identically distributed (iid) entries of a Wigner matrix \[:Characteristic-Vectors\]. By now, we understand these models comprehensively \[:Spectral-Analysis,:Eigenvalue-Distribution\]. In contrast, contemporary applications often lead to random matrices of more baroque construction, such as a random set of columns drawn from a fixed data matrix \[:Introduction-Matrix, Sec. 5.2\]. The standard methods for studying random matrices have relatively little to say about these strange examples.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Motivation", "weight": 1.0} -->

To advance into this frontier, researchers have developed new tools for applied random matrix theory, collectively called matrix concentration inequalities \[:Introduction-Matrix\].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Motivation", "weight": 1.0} -->

Flexibility. They apply to a large family of random matrices.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Motivation", "weight": 1.0} -->

Ease of use. They reduce the analysis to a calculation of simple summary statistics.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Motivation", "weight": 1.0} -->

Power. They accurately describe features of the random matrix model.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Motivation", "weight": 1.0} -->

Matrix concentration has roots in Banach space geometry \[:Moduli-Smoothness,:Inegalites-Khintchine,:Random-Vectors\]; it also owes a heavy debt to research on quantum information theory \[:Strong-Converse\]. The core results crystallized in 2010 through the efforts of Oliveira \[:Concentration-Adjacency\] and the author \[:Freedmans-Inequality,:User-Friendly\]. My monograph \[:Introduction-Matrix\] collected many applications and popularized the theory. Matrix concentration soon became textbook material \[:High-Dimensional-Probability,:High-Dimensional-Statistics\], and it has now informed thousands of research papers.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Motivation", "weight": 1.0} -->

The purpose of this memoir is to introduce the fundamental matrix concentration inequalities for independent sums and martingales. I will illustrate these tools through eight contemporary applications in uncertainty quantification, numerical linear algebra, spectral graph theory, high-dimensional statistics, and quantum information science. Parts of this work are adapted from my monograph \[:Introduction-Matrix\] and lecture notes \[:Matrix-Concentration-LN\].

<!-- chunk {"id": "body-0012", "role": "body", "section": "Concentration of random matrices", "weight": 1.0} -->

A random matrix is a matrix whose entries are random variables, not necessarily independent from each other. The distinctive concern of random matrix theory is the action of the random matrix as a random linear map between linear spaces. In that vein, we can investigate its geometric properties (reflected in operator norms or its action on sets) and its spectral features (singular values and singular vectors, eigenvalues and eigenvectors in the square case).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Concentration of random matrices", "weight": 1.0} -->

Matrix concentration studies the deviation of a random matrix ${\mathbf{S}} \in {\mathbb{C}}^{d_{1} \times d_{2}}$ from its expectation ${{\mathbb{E}}{\lbrack{\mathbf{S}}\rbrack}} \in {\mathbb{C}}^{d_{1} \times d_{2}}$, as measured in the spectral norm $\parallel \cdot \parallel$. For levels $t \geq 0$, we would like to control the tail probability

<!-- chunk {"id": "body-0014", "role": "body", "section": "Concentration of random matrices", "weight": 1.0} -->

The expectation of the random matrix is computed componentwise; we always assume that this expectation is defined and finite. The spectral norm is also called the $\ell_{2}$ operator norm; it coincides with the largest singular value.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Concentration of random matrices", "weight": 1.0} -->

Singular values. The singular values of $\mathbf{S}$ and ${\mathbb{E}}{\lbrack{\mathbf{S}}\rbrack}$ are close.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Concentration of random matrices", "weight": 1.0} -->

Singular vectors. The singular vectors of $\mathbf{S}$ and ${\mathbb{E}}{\lbrack{\mathbf{S}}\rbrack}$ are close for isolated singular values.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Concentration of random matrices", "weight": 1.0} -->

Linear functionals. All linear functionals of $\mathbf{S}$ and ${\mathbb{E}}{\lbrack{\mathbf{S}}\rbrack}$ are comparable.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Concentration of random matrices", "weight": 1.0} -->

Many practical problems reduce to one of these considerations.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Random matrix models", "weight": 1.0} -->

We cannot hope to make progress on the question (1.1) without imposing some restrictions on the random matrix. The challenge is to identify models that capture a wide range of examples, yet offer enough scaffolding to support strong theoretical guarantees. This paper focuses on two models inspired by the most basic scalar stochastic processes: independent sums and martingales. Our attention to these templates will be rewarded by a host of applications. Section˜6 outlines recent research and alternative models.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Independent sums", "weight": 1.0} -->

A random matrix ${\mathbf{S}} \in {\mathbb{C}}^{d_{1} \times d_{2}}$ follows the independent sum model when it admits the decomposition

<!-- chunk {"id": "body-0021", "role": "body", "section": "Independent sums", "weight": 1.0} -->

We use the term "statistical independence" to mark a contrast against linear independence. Let us emphasize that the entries within any particular matrix ${\mathbf{X}}_{k}$ may exhibit dependencies, but ${\mathbf{X}}_{k}$ cannot provide any information about events involving $({{\mathbf{X}}_{j}:{j \neq k}})$. Moreover, there may be many distinct decompositions of a random matrix as an independent sum. *Inter alia*, the independent sum model describes a random Monte Carlo approximation of a fixed matrix as an average of simple unbiased estimates \[:Introduction-Matrix, Sec. 6.2\].

<!-- chunk {"id": "body-0022", "role": "body", "section": "Independent sums", "weight": 1.0} -->

We would like to capture information about the concentration of the independent sum $\mathbf{S}$ through summary statistics. In the scalar setting, we can achieve this goal with the Bernstein inequality \[:Concentration-Inequalities, Thm. 2.10\], which is arguably the most useful probability inequality for an independent sum of scalars. The matrix Bernstein inequality \[:User-Friendly, Thm. 6.2\] offers a perfect analogue in the matrix setting, where it may be the single most productive tool for studying random matrices. We present this result as Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory"). Section˜3 showcases applications to active subspace methods, stochastic rounding, graph sparsification, and quantum state tomography.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Martingales", "weight": 1.0} -->

Given what we know so far, our best estimate for the next matrix ${\mathbf{S}}_{k + 1}$ is the current matrix ${\mathbf{S}}_{k}$. As a simple example, the partial sums of an independent family of centered random matrices compose a matrix martingale. More generally, matrix martingales can model complicated sequences of random matrices that are revealed one step at a time, such as the iterates of a randomized algorithm that performs a linear algebra computation.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Martingales", "weight": 1.0} -->

One of the most powerful tools for studying scalar martingale sequences is the Freedman inequality \[:Tail-Probabilities\], which is the martingale analog of the Bernstein inequality. The matrix Freedman inequality \[:Concentration-Adjacency,:Freedmans-Inequality\] generalizes the scalar result to matrix martingales. It allows us to treat sequences of random matrices that evolve adaptively, and it provides uniform control on the whole trajectory. We present this result as Theorem˜4.4. ‣ 4.2 Matrix Freedman ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory"). Section˜5 highlights applications to online covariance estimation, Cholesky decomposition with stochastic rounding, fast graph Laplacian solvers, and randomized approximation of quantum Hamiltonians.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The matrix Bernstein inequality", "weight": 1.0} -->

Among matrix concentration inequalities, the single most important result is the matrix extension of the scalar Bernstein inequality \[:Concentration-Inequalities, Thm. 2.10\]. The matrix Bernstein inequality was established independently by Roberto I. Oliveira \[:Concentration-Adjacency\] in late 2009 and the author \[:User-Friendly\] in early 2010. We state the version of this result from \[:Introduction-Matrix, Thm. 6.1.1\].

<!-- chunk {"id": "body-0026", "role": "body", "section": "Reduction to the Hermitian case", "weight": 1.0} -->

Let us commence with the proof of Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory"). It suffices to consider the complex case.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Reduction to the Hermitian case", "weight": 1.0} -->

The map $\mathcal{H}$ is real-linear, and it preserves spectral data in the sense that ${\lambda_{\max}{({\mathcal{H}{({\mathbf{A}})}})}} = {- {\lambda_{\min}{({\mathcal{H}{({\mathbf{A}})}})}}} = {\|{\mathbf{A}}\|}$. As a consequence, to prove Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory"), we can pass to the random Hermitian matrix

<!-- chunk {"id": "body-0028", "role": "body", "section": "Reduction to the Hermitian case", "weight": 1.0} -->

Through this device, we can simply instate the assumption that the summands are Hermitian matrices.

<!-- chunk {"id": "body-0029", "role": "body", "section": "The matrix Laplace transform method", "weight": 1.0} -->

We apply a scalar function to an Hermitian matrix by applying the function to each eigenvalue without modifying the associated eigenspace. Ahlswede & Winter \[:Strong-Converse\] formulated the ideas in this subsection, while Oliveira \[:Concentration-Adjacency\] and the author \[:User-Friendly,:Introduction-Matrix\] crystallized the arguments.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The matrix Laplace transform method", "weight": 1.0} -->

Even in the matrix setting, we can pursue the same strategy that leads to exponential tail bounds in the scalar setting \[:Concentration-Inequalities, Chap. 2\]. When the parameter $\theta > 0$,

<!-- chunk {"id": "body-0031", "role": "body", "section": "The matrix Laplace transform method", "weight": 1.0} -->

The first inequality is Markov's. Afterward, invoke the spectral mapping theorem to draw the eigenvalue map through the exponential, and note that the trace of a psd matrix dominates its maximum eigenvalue. The emergence of the trace exponential of the matrix log-mgf unlocks powerful tools for trace functions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The matrix Laplace transform method", "weight": 1.0} -->

A similar calculation furnishes a bound for the expectation of the maximum eigenvalue. For each $\theta > 0$,

<!-- chunk {"id": "body-0033", "role": "body", "section": "The matrix Laplace transform method", "weight": 1.0} -->

The first inequality is Jensen's. Once again, the matrix log-mgf controls the maximum eigenvalue.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Subadditivity of the matrix log-mgf", "weight": 1.0} -->

The latter formula depends on the fact $e^{a + b} = {e^{a}e^{b}}$ for ${a,b} \in {\mathbb{R}}$, a property that catastrophically fails for matrices.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Subadditivity of the matrix log-mgf", "weight": 1.0} -->

Remarkably, there is a substitute. I established a *subadditivity rule* for the matrix log-mgf \[:User-Friendly, Lem. 3.4\]:

<!-- chunk {"id": "body-0036", "role": "body", "section": "Subadditivity of the matrix log-mgf", "weight": 1.0} -->

In this expression, $({\mathbf{X}}_{1},\ldots,{\mathbf{X}}_{n})$ is a statistically independent family of bounded, Hermitian random matrices of the same dimension. In the proof of (2.8), the key ingredient is a deep concavity theorem of Lieb \[:Convex-Trace, Thm. 6\], which is one of the crown jewels of matrix analysis. See \[:Introduction-Matrix, Chap. 8\] for a detailed proof of Lieb's result.

<!-- chunk {"id": "body-0037", "role": "body", "section": "The matrix Bernstein log-mgf bound", "weight": 1.0} -->

The subadditivity rule (2.8) reduces the bound on the matrix log-mgf of a sum to individual bounds on the matrix log-mgfs of the summands. Classic scalar concentration inequalities \[:Concentration-Inequalities, Ch. 2\] provide inspiration about fruitful strategies for controlling the matrix log-mgfs \[:User-Friendly,:Introduction-Matrix\].

<!-- chunk {"id": "body-0038", "role": "body", "section": "The matrix Bernstein log-mgf bound", "weight": 1.0} -->

The matrix Bernstein inequality depends on the same type of log-mgf bound as the scalar Bernstein inequality \[:Concentration-Inequalities, Thm. 2.10\]. Indeed, the result \[:Introduction-Matrix, Lem. 6.1\] states that the matrix log-mgf of a bounded, centered, random Hermitian matrix ${\mathbf{X}} \in {{\mathbb{H}}_{d}{({\mathbb{C}})}}$ satisfies the relation

<!-- chunk {"id": "body-0039", "role": "body", "section": "The matrix Bernstein log-mgf bound", "weight": 1.0} -->

The semidefinite partial order ${\mathbf{A}} \preccurlyeq {\mathbf{H}}$ on Hermitian matrices means that ${\mathbf{H}} - {\mathbf{A}}$ is psd. The proof of (2.9) tracks the scalar argument. Expand the exponential function in the matrix log-mgf as a Taylor series, use the centering to remove the term with degree one, and apply the norm bound to control the terms with degree two and higher. We also employ the fact that the matrix logarithm respects the semidefinite partial order \[:Introduction-Matrix, Prop. 8.4.4\].

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assembly line", "weight": 1.0} -->

We are prepared to establish Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory"). Consider the sum ${\mathbf{S}} ≔ {\sum_{k = 1}^{n}{\mathbf{X}}_{k}}$ of independent, random Hermitian matrices with dimension $d$ that satisfy ${{\mathbb{E}}{\lbrack{\mathbf{X}}_{k}\rbrack}} = \mathbf{0}$ and ${\|{\mathbf{X}}_{k}\|} \leq B$. Sequence the displays Eqs.˜2.6, 2.8, and 2.9 to arrive at the tail inequality

<!-- chunk {"id": "body-0041", "role": "body", "section": "Assembly line", "weight": 1.0} -->

The parameter is restricted to the interval ${|\theta|} < {B/3}$. The first inequality depends on the fact that the trace exponential respects the semidefinite partial order \[:Introduction-Matrix, Ex. 8.1\]. The identity exploits the centering and independence of the summands. Afterward, bound the trace exponential by the dimension $d$ times the maximum eigenvalue, and use spectral mapping to recognize the matrix variance ${v{({\mathbf{S}})}} = {\lambda_{\max}{({{\mathbb{E}}{\lbrack{\mathbf{S}}^{2}\rbrack}})}}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Assembly line", "weight": 1.0} -->

Finally, in (2.10), set the parameter $\theta = {t/{({{v{({\mathbf{S}})}} + {{Bt}/3}})}}$ to reach the finished tail inequality

<!-- chunk {"id": "body-0043", "role": "body", "section": "Assembly line", "weight": 1.0} -->

To establish the analogous tail bound (2.3. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")) for a general non-Hermitian sum, apply the Hermitian dilation (2.5) and invoke (2.11). The bound (2.2. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")) on the *expected* norm of the sum follows a similar argument starting from (2.7).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Optimality", "weight": 1.0} -->

As noted, the expectation bound (2.2. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")) is the most significant outcome from Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory"). We can strengthen this bound, but not by very much.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Optimality", "weight": 1.0} -->

The tail content satisfies $B_{2} \leq B$; the slackness of this inequality depends on the particular choice of summands. Using another style of argument based on symmetrization \[:Expected-Norm\], we can obtain a two-sided bound of the form

<!-- chunk {"id": "body-0046", "role": "body", "section": "Optimality", "weight": 1.0} -->

The paper \[:Expected-Norm\] provides examples to show that each term in (2.12) is necessary, so we cannot improve the bounds without a substantial amount of extra information (about the covariance structure of the random matrix). Section˜6 mentions some situations where improvements are possible.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Independent sum model: Applications", "weight": 1.0} -->

In this section, we present some contemporary applications of the matrix Bernstein inequality in several areas of computational mathematics. As a caveat, these stylized applications may not reflect the intricacies of each problem. It is sometimes possible to find a simpler argument by invoking a more suitable matrix concentration inequality, and we can occasionally obtain sharper analyses using more complicated tools; see section˜6.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Active subspace methods", "weight": 1.0} -->

In engineering design, researchers build computer models of complex physical systems that are governed by several input parameters. Key tasks include optimization of parameters, analysis of sensitivity to changes in parameters, and quantification of uncertainty about the system output. For example, an aeronautics engineer designs an airfoil by modifying its geometry to reach a target lift and drag coefficient. It is challenging to explore the parameter space of a complicated, nonlinear model, so it is common to seek reduced models. One basic methodology is to restrict our attention to the most salient directions in the input space, which we can identify through a random sampling procedure. The analysis of this approach depends on matrix concentration inequalities. This vignette is adapted from Constantine's book \[:Active-Subspaces, Chap. 3\]. The mathematics are similar with the classic problem of covariance estimation; see subsection˜5.1.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Active subspace methods", "weight": 1.0} -->

Let $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ be an $L$-Lipschitz, differentiable function that models a complicated system, and assume that we can evaluate its gradient $\nabla f$ at each point in the parameter space---but the computational cost is significant. As part of the model, introduce a random vector ${\mathbf{z}} \in {\mathbb{R}}^{d}$ that describes a distribution over the parameter space; this distribution is often interpreted as a Bayesian prior. To capture the variability of the function, introduce the psd sensitivity matrix

<!-- chunk {"id": "body-0050", "role": "body", "section": "Active subspace methods", "weight": 1.0} -->

The subspace spanned by the leading eigenvectors of $\mathbf{\Sigma}$ is called an *active subspace* of the model, because it captures the most salient directions in the input space.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Active subspace methods", "weight": 1.0} -->

How many gradient samples suffice to approximate the sensitivity matrix $\mathbf{\Sigma}$? Can we determine the directions in which the model varies substantially?

<!-- chunk {"id": "body-0052", "role": "body", "section": "Stochastic rounding", "weight": 1.0} -->

Conventional computer architectures offer floating-point numbers with 16 decimal digits of precision or more. Driven by contemporary applications, computer engineers have started to develop new architectures with far lower precision---sometimes as few as 4 or 8 bits (i.e., 1--2 digits). At this extreme, large numerical errors can accumulate as we round successive calculations to the nearest machine-representable number. One way to mitigate these errors is to design computer systems that perform *stochastic rounding*. To analyze linear algebra computations that employ stochastic rounding, we can exploit matrix concentration tools. This section offers an idealized treatment of the simplest problem; see \[CFH+22:Stochastic-Rounding\] for more texture.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Stochastic rounding", "weight": 1.0} -->

A floating-point number system is a finite set of machine-representable numbers $\mathsf{F} \subset {\mathbb{R}}$. Ignoring underflow and overflow, a (deterministic) rounding rule approximates each real number $a \in {\mathbb{R}}$ by a floating-point number ${\text{float}{(a)}} \in \mathsf{F}$ that admits the relative-error bound

<!-- chunk {"id": "body-0054", "role": "body", "section": "Stochastic rounding", "weight": 1.0} -->

In IEEE double-precision arithmetic, the unit-roundoff parameter $\text{u} = 2^{- 53} \approx 10^{- 16}$, and the rounding rule must satisfy additional requirements to meet the standard \[CFH+22:Stochastic-Rounding, Tabs. 1, 2\]. As an alternative, a *stochastic rounding rule* maps each real number $a \in {\mathbb{R}}$ to a *random* floating-point number ${\text{sr}{(a)}} \in \mathsf{F}$ that satisfies

<!-- chunk {"id": "body-0055", "role": "body", "section": "Stochastic rounding", "weight": 1.0} -->

In words, stochastic rounding is unbiased, and it commits a relative error on the order of the unit roundoff.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Stochastic rounding", "weight": 1.0} -->

Suppose that we round each entry of a real-valued matrix stochastically to the nearest floating-point number. How much damage will we do? How does this bound compare with deterministic rounding?

<!-- chunk {"id": "body-0057", "role": "body", "section": "Graph sparsification", "weight": 1.0} -->

A combinatorial graph encodes the pairwise relationships among a family of objects. We may ask whether it is possible to find a simpler graph (with fewer edges) that preserves structural properties of the original graph, such as the weights of vertex cuts and the mixing time of a random walk. Spielman & Srivastava \[:Graph-Sparsification\] showed how to achieve this goal by randomly sampling edges from the graph. We can analyze the procedure with matrix concentration.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Graph sparsification", "weight": 1.0} -->

Consider a connected, weighted, undirected graph $(\mathsf{V},w)$. The graph comprises a set $\mathsf{V} ≔ {\{ 1,\ldots,n\}}$ of vertices and a symmetric function $w:{{\mathsf{V} \times \mathsf{V}}\rightarrow{\mathbb{R}}_{+}}$ that assigns a nonnegative weight to each pair of vertices. We require that $w_{ii} = 0$ and $w_{ij} = w_{ji}$ for all ${i,j} \in \mathsf{V}$. The number of edges $m ≔ {\#{\{{i < j}:{w_{ij} > 0}\}}}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Graph sparsification", "weight": 1.0} -->

We can also represent the graph by means of the graph Laplacian ${\mathbf{L}} \in {{\mathbb{H}}_{n}^{+}{({\mathbb{R}})}}$, which is the psd matrix

<!-- chunk {"id": "body-0060", "role": "body", "section": "Graph sparsification", "weight": 1.0} -->

The sum involves $m$ nonzero terms. Since the graph is connected, ${{null}{({\mathbf{L}})}} = {{span}{\{\mathbf{1}\}}}$. Without further notice, we restrict $\mathbf{L}$ to the $({n - 1})$-dimensional subspace where it is nonsingular.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Graph sparsification", "weight": 1.0} -->

If the graph models an electrical network whose wires have conductances $w_{ij}$, then the effective resistance $\varrho_{ij}$ is the voltage required to push one unit of current from vertex $i$ to vertex $j$. Observe that ${\sum_{i < j}{w_{ij}\varrho_{ij}}} = {n - 1}$. We can approximate all $m$ of the nonzero effective resistances in $\mathcal{O}{({m{\log n}})}$ arithmetic operations \[:Graph-Sparsification, Thm. 2\].

<!-- chunk {"id": "body-0062", "role": "body", "section": "Graph sparsification", "weight": 1.0} -->

The spectral equivalence (3.6) ensures that the sparse graph is structurally similar with the original graph. We plan to construct a spectral sparsifier $\hat{\mathbf{L}}$ by randomly sampling edges according to a carefully chosen probability distribution. Introduce the random matrix ${\mathbf{Y}} \in {{\mathbb{H}}_{d}^{+}{({\mathbb{R}})}}$ with distribution

<!-- chunk {"id": "body-0063", "role": "body", "section": "Graph sparsification", "weight": 1.0} -->

In other words, $\mathbf{Y}$ is the Laplacian of a weighted edge between a pair $(i,j)$ of vertices, chosen with probability proportional to the weight $w_{ij}$ and the effective resistance $\varrho_{ij}$. It is easy to confirm that ${{\mathbb{E}}{\lbrack{\mathbf{Y}}\rbrack}} = {\mathbf{L}}$, so the random matrix $\mathbf{Y}$ is an unbiased estimator for the Laplacian $\mathbf{L}$ of the original graph.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Graph sparsification", "weight": 1.0} -->

How many edges $q$ suffice to achieve the approximation guarantee (3.6)?

<!-- chunk {"id": "body-0065", "role": "body", "section": "Quantum tomography", "weight": 1.0} -->

The state of a finite-dimensional quantum system, such as a register in a quantum computer, is characterized by a finite-dimensional psd matrix. We can probe the system by taking measurements, but the laws of quantum mechanics imply that each measurement returns a random number. As a consequence, methods for reconstructing the state of a quantum system lead to problems involving random matrices. Matrix concentration tools offer a quick way to analyze quantum state estimators. This section summarizes a lecture by Richard Kueng (see \[:Matrix-Concentration-LN, Lec. 3\]), which distills ideas from a paper of Guţa et al. \[:Fast-State-Tomography\]. Related ideas animate the theory of classical shadows, a major recent advance in quantum information science \[:Predicting-Many\].

<!-- chunk {"id": "body-0066", "role": "body", "section": "Quantum tomography", "weight": 1.0} -->

Second, the quantum system "collapses". Therefore, to characterize a quantum system, we must prepare several copies in the same state and measure each one to obtain statistical evidence about the state.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Quantum tomography", "weight": 1.0} -->

The vectors ${\mathbf{u}}_{1},\ldots,{\mathbf{u}}_{m}$ composing a complex projective 2-design are arranged very regularly over the complex sphere. Examples include systems of "mutually unbiased" orthonormal bases and systems of equiangular lines \[:Matrix-Concentration-LN, Ex. 3.3\]. This type of measurement system can stably distinguish any pair of density matrices.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Quantum tomography", "weight": 1.0} -->

To reconstruct a quantum system with density matrix ${\mathbf{ρ}} \in \mathcal{D}_{d}$, we perform a measurement to sample the random variable $J$. Then we build a random Hermitian matrix ${\mathbf{Y}} \in {{\mathbb{H}}_{d}{({\mathbb{C}})}}$ according to the rule

<!-- chunk {"id": "body-0069", "role": "body", "section": "Quantum tomography", "weight": 1.0} -->

This calculation follows from (3.8) and (3.9). By repeating the measurement on $n$ independent (i.e., unentangled) copies of the quantum system, each with density matrix $\mathbf{ρ}$, we can obtain an estimator

<!-- chunk {"id": "body-0070", "role": "body", "section": "Quantum tomography", "weight": 1.0} -->

How many independent measurements suffice to approximate the underlying density matrix?

<!-- chunk {"id": "body-0071", "role": "body", "section": "Concentration for matrix martingales", "weight": 1.0} -->

The full majesty of the framework for exponential matrix concentration comes into view when we extend it to dynamically evolving sequences of matrices.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Matrix martingales", "weight": 1.0} -->

Fix a probability space. A *filtration* is an increasing sequence of sigma-algebras $\mathcal{F}_{0} \subseteq \mathcal{F}_{1} \subseteq \mathcal{F}_{2} \subseteq \cdots$ inside the master sigma-algebra. A matrix martingale is a sequence $({\mathbf{S}}_{0},{\mathbf{S}}_{1},{\mathbf{S}}_{2},\ldots)$ of complex random matrices with common dimension $d_{1} \times d_{2}$ that satisfies three properties. For each index $k = {0,1,2,\ldots}$, the sequence is

<!-- chunk {"id": "body-0073", "role": "body", "section": "Matrix martingales", "weight": 1.0} -->

Adapted. Each random matrix ${\mathbf{S}}_{k}$ is measurable with respect to $\mathcal{F}_{k}$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Matrix martingales", "weight": 1.0} -->

The difference sequence consists of the matrices ${\mathbf{X}}_{k} ≔ {{\mathbf{S}}_{k} - {\mathbf{S}}_{k - 1}}$ with $k \geq 1$. Each member of the difference sequence is conditionally centered: ${{\mathbb{E}}{\lbrack\left. {\mathbf{X}}_{k} \middle| \mathcal{F}_{k - 1} \right.\rbrack}} = \mathbf{0}$. Matrix martingales model a wide range of examples.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Example 4.3 (Lévy--Doob martingale)", "weight": 1.0} -->

Then $(\mathbf{S}_{0},\mathbf{S}_{1},\mathbf{S}_{2},\ldots)$ composes a martingale with respect to the filtration.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Example 4.3 (Lévy--Doob martingale)", "weight": 1.0} -->

To avoid technicalities, we only consider finite martingale sequences $({\mathbf{S}}_{0},\ldots,{\mathbf{S}}_{n})$. Furthermore, we require the elements of the martingale to be uniformly bounded in the sense that ${\sup{\|{\mathbf{S}}_{k}\|}} \leq B_{\infty} < {+ \infty}$ for each index $k = {0,\ldots,n}$. The filtration may be suppressed if it is determined by context.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Matrix Freedman", "weight": 1.0} -->

To analyze a matrix martingale, the most valuable theorem is the matrix Freedman inequality, originally due to Roberto I. Oliveira \[:Concentration-Adjacency\]. The author exploited the subadditivity (2.8) of the matrix log-mgf to refine Oliveira's result and to establish some other matrix martingale inequalities \[:Freedmans-Inequality\]. The version stated here follows from \[:Freedmans-Inequality, Cor. 1.3, Thm. 3.1\].

<!-- chunk {"id": "body-0078", "role": "body", "section": "The log-mgf supermartingale", "weight": 1.0} -->

As in the proof of Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory"), we can and will employ the Hermitian dilation (2.5) to restrict our attention to Hermitian random matrices.

<!-- chunk {"id": "body-0079", "role": "body", "section": "The log-mgf supermartingale", "weight": 1.0} -->

Applying the subadditivity rule (2.8) for the matrix log-mgf conditionally, we quickly verify that ${{\mathbb{E}}{\lbrack\left. {M_{k}{(\theta)}} \middle| \mathcal{F}_{k - 1} \right.\rbrack}} \leq {M_{k - 1}{(\theta)}}$ for each $k = {1,\ldots,n}$. In other words, $({{M_{k}{(\theta)}}:{k = {0,\ldots,n}}})$ composes a positive supermartingale. We can study the trajectory of the matrix martingale by bounding the supermartingale \[:Concentration-Adjacency,:Freedmans-Inequality\]. The approach here is adapted from Howard et al. \[:Time-Uniform-Chernoff\].

<!-- chunk {"id": "body-0080", "role": "body", "section": "Matrix martingales: Applications", "weight": 1.0} -->

In this section, we outline some applications of the matrix Freedman inequality in computational mathematics. This technique is particularly valuable for handling sequences of matrices that evolve adaptively, and it provides uniform control over the entire trajectory of the process.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Uniform covariance estimation", "weight": 1.0} -->

We would like to obtain a confidence region for the entire sequence of covariance estimates, ensuring simultaneous coverage at all times. The following statement is adapted from Howard et al. \[:Time-Uniform-Nonparametric, Sec. 4.3\].

<!-- chunk {"id": "body-0082", "role": "body", "section": "Cholesky decomposition with stochastic rounding", "weight": 1.0} -->

Most numerical algorithms proceed in stages, and the numerical errors compound at each step of the process. Traditional analyses model these errors deterministically, and error bounds increase linearly with the number of steps in the algorithm. More recently, researchers have started to make a close accounting of error propagation under probabilistic models, where the errors accumulate more slowly because of cancelations. Martingale methods offer an elegant technique for tracking random errors that depend on the past history of the algorithm. Connolly & Higham \[:Probabilistic-Rounding\] have employed this approach to give a probabilistic analysis of the Householder QR algorithm. In the same spirit, this section offers a stylized analysis of the Cholesky factorization algorithm under a stochastic rounding model (cf. subsection˜3.2).

<!-- chunk {"id": "body-0083", "role": "body", "section": "Cholesky decomposition with stochastic rounding", "weight": 1.0} -->

In actual practice, we commit floating-point errors when we reduce the residual---but we can extract a column from the residual without further error. If we employ stochastic rounding, then the residual update becomes

<!-- chunk {"id": "body-0084", "role": "body", "section": "Cholesky decomposition with stochastic rounding", "weight": 1.0} -->

The stochastic error ${\mathbf{Y}}_{k}$ is a random symmetric matrix that depends on the previous residual. The sigma-algebra $\mathcal{F}_{k - 1} ≔ {\sigma{({\mathbf{R}}_{0},\ldots,{\mathbf{R}}_{k - 1})}}$ captures the history of the algorithm through step $k - 1$. As in subsection˜3.2, each entry of ${\mathbf{Y}}_{k}$ satisfies the rounding properties in (3.4), conditional on $\mathcal{F}_{k - 1}$, and each entry is rounded independently of the others (modulo symmetry). We frame the assumptions that

<!-- chunk {"id": "body-0085", "role": "body", "section": "Cholesky decomposition with stochastic rounding", "weight": 1.0} -->

The third property follows because ${{diag}{({\mathbf{A}})}} = \mathbf{I}$ and ${diag}{({\mathbf{R}}_{k - 1})}$ only decreases at each step. The second property holds if the computed residual ${\mathbf{R}}_{k - 1}$ remains psd and satisfies ${\|{\mathbf{R}}_{k - 1}\|} \leq {2{\|{\mathbf{A}}\|}}$. Under mild assumptions, these conditions can be justified with some additional effort. We also demand that no underflow or overflow occurs.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Cholesky decomposition with stochastic rounding", "weight": 1.0} -->

Using these approximations, we can calculate the error in the completed triangular factorization ${\mathbf{C}} ≔ {\mathbf{C}}_{d}$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Cholesky decomposition with stochastic rounding", "weight": 1.0} -->

In other words, the sequence of approximations composes a matrix martingale with difference sequence $({{\mathbf{Y}}_{k}:{k = {1,\ldots,d}}})$. We can use this martingale to assess the accumulated rounding error in the Cholesky decomposition.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Fast Laplacian solvers", "weight": 1.0} -->

As in subsection˜3.3, consider a weighted, connected, undirected graph on $n$ vertices with Laplacian matrix ${\mathbf{L}} \in {{\mathbb{H}}_{n}^{+}{({\mathbb{R}})}}$. A linear system in the Laplacian matrix takes the form

<!-- chunk {"id": "body-0089", "role": "body", "section": "Fast Laplacian solvers", "weight": 1.0} -->

This type of linear system arises in a dizzying range of applications, including numerical discretizations of elliptic PDEs, clustering and partitioning of data, and network flow problems \[:Laplacian-Paradigm\]. The basic algorithm for (5.3) starts by computing a Cholesky decomposition ${\mathbf{L}} = {{\mathbf{C}}{\mathbf{C}}^{\ast}}$, and it solves the linear system by two steps of triangular substitution. In general, this approach requires $\mathcal{O}{(n^{3})}$ operations, which is often prohibitive. Can we do better?

<!-- chunk {"id": "body-0090", "role": "body", "section": "Fast Laplacian solvers", "weight": 1.0} -->

Spielman & Teng \[:Nearly-Linear-Time\] gave an affirmative answer by devising a theoretical Laplacian solver that runs in time linear in the number $m$ of edges in the graph and polylogarithmic in the number $n$ of vertices. After a train of refinements, Kyng & Sachdeva \[:Approximate-Gaussian\] designed a *practical* Laplacian solver that runs in time $\mathcal{O}{({m{\log^{3}n}})}$. Their algorithm, SparseCholesky, performs an approximate Cholesky decomposition by randomly sparsifying the Schur complement at each step. The analysis relies on matrix martingales. See \[:Matrix-Concentration-LN\] for another account.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Fast Laplacian solvers", "weight": 1.0} -->

Here is the intuition. When we apply the Cholesky method to a graph Laplacian, each Schur complement step eliminates a vertex from the graph by adding a clique to the remaining vertices of the graph. The method is expensive because the clique involves up to $n - k$ vertices and up to ${({n - k})}^{2}$ edges at step $k$. Yet, as we saw in subsection˜3.3, we can dramatically sparsify a graph by randomly sampling edges in proportion to their effective resistances. In this spirit, SparseCholesky starts with residual ${\mathbf{R}}_{0} ≔ {\mathbf{L}}$ and triangular factor ${\mathbf{C}}_{0} ≔ \mathbf{0}$. It performs the steps

<!-- chunk {"id": "body-0092", "role": "body", "section": "Fast Laplacian solvers", "weight": 1.0} -->

The Sparsify method produces a random, unbiased approximation to the matrix ${\mathbf{c}}_{k}{\mathbf{c}}_{k}^{\ast}$, which contains the Laplacian of the clique. After sparsification, the remaining number of edges equals the number of neighbors of vertex $k$ in the residual graph ${\mathbf{R}}_{k - 1}$. The full algorithm requires several other innovations: it splits edges into smaller pieces to reduce their weights; it maintains estimates for the effective resistances to implement the sparsification step; and it eliminates vertices in a random order to limit the average number of neighbors. As in subsection˜5.2, this procedure results in a matrix martingale, namely ${\mathbf{S}}_{k} ≔ {{\mathbf{R}}_{k} + {{\mathbf{C}}_{k}{\mathbf{C}}_{k}^{\ast}}}$ for $k = {0,1,2,{\ldotsd}}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Fast Laplacian solvers", "weight": 1.0} -->

We can analyze this martingale using the matrix Freedman inequality (Theorem˜4.4. ‣ 4.2 Matrix Freedman ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory")). Here is the outcome.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Randomized Trotter formulas", "weight": 1.0} -->

The evolution of a quantum mechanical system is governed by a Hamiltonian matrix ${\mathbf{H}} \in {{\mathbb{H}}_{d}{({\mathbb{C}})}}$. The state of the system at time $t \geq 0$ takes the form

<!-- chunk {"id": "body-0095", "role": "body", "section": "Randomized Trotter formulas", "weight": 1.0} -->

A basic goal of quantum information science is to simulate the action $\mathbf{\Phi}_{t}$ induced by a complicated Hamiltonian through the application of simpler Hamiltonians. Randomized methods can provide effective algorithms for this task. This section summarizes a result of Chen et al. \[:Concentration-Random\] that builds on work of Campbell \[:Random-Compiler\].

<!-- chunk {"id": "body-0096", "role": "body", "section": "Randomized Trotter formulas", "weight": 1.0} -->

The statistic $L$ measures the interaction strength within the Hamiltonian. This model encompasses applications in quantum chemistry and quantum physics. For clarity, fix the time horizon for the simulation at $t = 1$.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Randomized Trotter formulas", "weight": 1.0} -->

In other words, we simulate the action of the full Hamiltonian $\mathbf{H}$ by performing a series of short simulations with the simpler Hamiltonians ${\mathbf{H}}_{m}$. This is a randomized variant of the Lie--Trotter--Suzuki product formulas that are widely used to approximate the matrix exponential of a sum. We can analyze the quality of the simulation using matrix martingale methods.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Matrix concentration: Extensions", "weight": 1.0} -->

Over the last few years, researchers have made significant advances in understanding the behavior of the independent sum model. These results require a detour into the study of Gaussian random matrices, which serve as ideal models for independent sums. First, we outline some improvements of matrix concentration for Gaussian random matrices, and then we explain how Gaussian models can capture the spectral features of an independent sum of random matrices. Last, we mention several other random matrix models that remain under active study.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Variance statistics", "weight": 1.0} -->

We can describe the behavior of random matrix models more fully by employing a broader family of variance statistics. Introduce the real inner product

<!-- chunk {"id": "body-0100", "role": "body", "section": "Variance statistics", "weight": 1.0} -->

Variance functions are in correspondence with psd quadratic forms on ${\mathbb{F}}^{d_{1} \times d_{2}}$, treated as a real linear space.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Variance statistics", "weight": 1.0} -->

The variance function ${\mathsf{V}\mathsf{a}\mathsf{r}}{\lbrack{\mathbf{S}}\rbrack}$ packs up all the second-order statistics of the random matrix. In particular, it completely determines the matrix variance $v{({\mathbf{S}})}$, defined in (2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")).

<!-- chunk {"id": "body-0102", "role": "body", "section": "Second-order matrix Khinchin inequalities", "weight": 1.0} -->

The lower bound involves Gaussian isoperimetry \[:Gaussian-Measures, Cor. 3\]; the upper bound relies on exponential matrix concentration arguments \[:Introduction-Matrix, Thm. 4.1.1\]. Both inequalities are saturated.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Second-order matrix Khinchin inequalities", "weight": 1.0} -->

To improve on the matrix Khinchin inequality (6.2), we need extra information about the variance function of the Gaussian matrix.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Second-order matrix Khinchin inequalities", "weight": 1.0} -->

The interaction energy $w{({\mathbf{Z}})}$ can be much smaller than the matrix variance $v{({\mathbf{Z}})}$, but they are incomparable. Heuristically, the interaction energy is small when $\mathbf{Z}$ is "highly noncommutative." This statistic supports a second-order refinement of the matrix Khinchin inequality \[:Matrix-Concentration, Cor. 2.2 and Lem. 2.5\]:

<!-- chunk {"id": "body-0105", "role": "body", "section": "Second-order matrix Khinchin inequalities", "weight": 1.0} -->

When ${w{({\mathbf{Z}})}} \ll {v{({\mathbf{Z}})}}$, then the result (6.3) improves over (6.2). As a simple example, consider a real Ginibre matrix ${\mathbf{G}} \in {{\mathbb{M}}_{d}{({\mathbb{R}})}}$, which is a $d \times d$ matrix with iid standardized Gaussian entries. The matrix variance ${v{({\mathbf{G}})}} = d$, while the interaction energy ${w{({\mathbf{G}})}} = 2$. Thus,

<!-- chunk {"id": "body-0106", "role": "body", "section": "Second-order matrix Khinchin inequalities", "weight": 1.0} -->

The latter inequality is the stronger one, and its first term is numerically sharp.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Second-order matrix Khinchin inequalities", "weight": 1.0} -->

Roughly speaking, the logarithmic factor in (6.2) arises when the Hermitian dilations of two independent copies ${\mathcal{H}{({\mathbf{Z}})}},{\mathcal{H}{({\mathbf{Z}}^{\prime})}}$ of the Gaussian matrix "almost commute" with each other, in an appropriate sense. To quantify this insight, inspired by free probability, I introduced a subtle statistic called the matrix alignment \[:Second-Order-Matrix, Def. 3.1\]. For a special class of Gaussian matrices, I also established a preliminary version of the second-order Khinchin inequality \[:Second-Order-Matrix, Thm. 3.1\] that reveals how the matrix alignment arises.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Second-order matrix Khinchin inequalities", "weight": 1.0} -->

The finished result (6.3) was obtained through additional insights of Bandeira et al. \[:Spectral-Norm,:Matrix-Concentration\]. The latter papers use matrix alignment statistics to compare the spectral norm of a Gaussian matrix with the spectral norm of a free probability model (namely, an operator semicircle) that admits explicit formulas. The role of the interaction energy $w{({\mathbf{Z}})}$ is to provide a computable bound for the matrix alignment \[:Spectral-Norm, Rem. 3.3\]. Similar results hold for other spectral properties, such as the support of the spectrum and the mean singular value distribution.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Independent sums: Gaussian comparison", "weight": 1.0} -->

Let us return to a more general setting.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Independent sums: Gaussian comparison", "weight": 1.0} -->

Let $\text{V} ≔ {\text{Var}{\lbrack{\mathbf{S}}\rbrack}}$ be the variance function of the sum. The multivariate central limit theorem suggests that we should compare $\mathbf{S}$ with the centered Gaussian random matrix ${\mathbf{Z}} \sim {\text{normal}{(\mathbf{0},\text{V})}}$, but it is not clear how to quantify the difference between their distributions.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Independent sums: Gaussian comparison", "weight": 1.0} -->

Under weak assumptions, we can obtain detailed nonasymptotic comparisons for *spectral properties* of the independent sum $\mathbf{S}$ and the Gaussian model $\mathbf{Z}$. Brailovskaya & van Handel \[:Universality-Sharp, Cor. 2.7\] established that

<!-- chunk {"id": "body-0112", "role": "body", "section": "Independent sums: Gaussian comparison", "weight": 1.0} -->

In view of the matrix Khinchin inequality (6.2), the Gaussian matrix satisfies ${{\mathbb{E}}{\|{\mathbf{Z}}\|}} \approx \sqrt{v{({\mathbf{Z}})}} = \sqrt{v{({\mathbf{S}})}}$. The weak variance term $\sqrt{v_{\ast}{({\mathbf{S}})}}$ is often negligible. Therefore, in case $B^{2} \ll {v{({\mathbf{S}})}}$, the discrepancy between the expected norms is much smaller than the expected norm of the Gaussian matrix. In other words, when the bound $B$ on the summands is sufficiently small, we can accurately approximate ${\mathbb{E}}{\|{\mathbf{S}}\|}$ by way of estimates for ${\mathbb{E}}{\|{\mathbf{Z}}\|}$.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Independent sums: Gaussian comparison", "weight": 1.0} -->

The second-order matrix Khinchin inequality (6.3) provides one such estimate.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Independent sums: Gaussian comparison", "weight": 1.0} -->

Brailovskaya & van Handel \[:Universality-Sharp\] developed Gaussian comparisons, similar with (6.4), for other spectral statistics of the independent sum, including the support of the spectrum and the mean distribution of the singular values. Their arguments rely on Stein's method, cumulant expansions, Möbius inversion, and a selection of matrix inequalities. My paper \[:Universality-Laws\] offers an alternative proof of their results, based on the method of exchangeable pairs. I recently obtained another type of Gaussian comparison \[:Comparison-Theorems-min,:Comparison-Theorems-max\] for the extreme eigenvalues of an independent sum; the proof exploits a deep result from matrix analysis, called Stahl's theorem \[:Proof-BMV\].

<!-- chunk {"id": "body-0115", "role": "body", "section": "Independent sums: Gaussian comparison", "weight": 1.0} -->

We conclude with a critical observation. For independent sums, the latest matrix concentration results, such as Eqs.˜6.3 and 6.4, offer new insights. Nevertheless, it may be difficult to deploy these inequalities in applications, such as the ones in section˜3, because we often lack fine-grained information about the variance function of the random matrix model. As a consequence, classic matrix concentration tools (e.g., Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")) and the more recent refinements play complementary roles.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Other models", "weight": 1.0} -->

While the matrix concentration theory for the independent sum model is rather complete, other types of random matrix models remain mysterious and have continued to attract attention. Citations are limited to a few typical papers, as there is not enough space to do justice to this rich literature.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Other models", "weight": 1.0} -->

The nonlinear random matrix model concerns a matrix-valued function of underlying random variables that are usually (but not always) independent. Results for this model include matrix Efron--Stein inequalities \[:Efron-Stein-Inequalities\] and (local) matrix Poincaré inequalities \[:Poincare-Inequalities,:Nonlinear-Matrix\]. There are also specialized results for matrix-valued polynomial chaos \[BLN+25:Matrix-Chaos\]. A related challenge arises from random matrix models with dependencies, such as the sum of fixed matrices modulated by negatively correlated scalar random variables; some recent progress on these questions appears in \[:Scalar-Matrix\]. In addition to matrix martingales, researchers have also treated other types of sequential processes, such as matrix-valued Markov chains; for example, see \[:Concentration-Inequalities\]. Another line of work \[BGJ+25:Tensor-Concentration\] pursues extensions of matrix concentration to random tensors.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Other models", "weight": 1.0} -->

Many of the models in the last paragraph emerged from problems in combinatorics and algorithms, and the theoretical results have led to satisfying progress. Thus, research on matrix concentration tools remains active, and it continues to make a profound impact on applications.
