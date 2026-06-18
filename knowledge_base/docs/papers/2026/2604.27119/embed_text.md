## Abstract

Random matrices now play a role in many parts of computational mathematics. To advance these applications, it is desirable to have tools that are flexible, easy to use, and powerful. Over the last 25 years, researchers have developed a remarkable family of results, called matrix concentration inequalities, that meet the criteria. This paper offers an invitation to the field of matrix concentration and its multifarious applications.

## Motivation

Random matrix theory emerged from applications in statistics (sample covariance matrices \[:Generalised-Product\]) and in nuclear physics (Hamiltonians of heavy nuclei \[:Characteristic-Vectors\]). The subject established itself within the mathematical firmament through deep connections to number theory (zeros of the Riemann zeta function \[:Pair-Correlation\]), operator algebras (free product factors \[:Free-Random\]), combinatorics (longest increasing subsequence \[:Distribution-Length\]), and beyond. Over the last generation, random matrices have attracted new attention in computational mathematics, starting with work in algorithms \[:Geometry-Graphs\] and in quantum information \[:Strong-Converse\], and expanding in waves that have touched the farthest shores.

The classic literature emphasizes random matrices that enjoy a harmonious mathematical structure, such as the independent and identically distributed (iid) entries of a Wigner matrix \[:Characteristic-Vectors\]. By now, we understand these models comprehensively \[:Spectral-Analysis,:Eigenvalue-Distribution\]. In contrast, contemporary applications often lead to random matrices of more baroque construction, such as a random set of columns drawn from a fixed data matrix \[:Introduction-Matrix, Sec. 5.2\]. The standard methods for studying random matrices have relatively little to say about these strange examples.

To advance into this frontier, researchers have developed new tools for applied random matrix theory, collectively called matrix concentration inequalities \[:Introduction-Matrix\]. These results offer several key benefits:

Flexibility. They apply to a large family of random matrices.

Ease of use. They reduce the analysis to a calculation of simple summary statistics.

Power. They accurately describe features of the random matrix model.

Matrix concentration has roots in Banach space geometry \[:Moduli-Smoothness,:Inegalites-Khintchine,:Random-Vectors\]; it also owes a heavy debt to research on quantum information theory \[:Strong-Converse\]. The core results crystallized in 2010 through the efforts of Oliveira \[:Concentration-Adjacency\] and the author \[:Freedmans-Inequality,:User-Friendly\]. My monograph \[:Introduction-Matrix\] collected many applications and popularized the theory. Matrix concentration soon became textbook material \[:High-Dimensional-Probability,:High-Dimensional-Statistics\], and it has now informed thousands of research papers.

The purpose of this memoir is to introduce the fundamental matrix concentration inequalities for independent sums and martingales. I will illustrate these tools through eight contemporary applications in uncertainty quantification, numerical linear algebra, spectral graph theory, high-dimensional statistics, and quantum information science. Parts of this work are adapted from my monograph \[:Introduction-Matrix\] and lecture notes \[:Matrix-Concentration-LN\].

### Concentration of random matrices

A random matrix is a matrix whose entries are random variables, not necessarily independent from each other. The distinctive concern of random matrix theory is the action of the random matrix as a random linear map between linear spaces. In that vein, we can investigate its geometric properties (reflected in operator norms or its action on sets) and its spectral features (singular values and singular vectors, eigenvalues and eigenvectors in the square case).

Matrix concentration studies the deviation of a random matrix ${\mathbf{S}} \in {\mathbb{C}}^{d_{1} \times d_{2}}$ from its expectation ${{\mathbb{E}}{\lbrack{\mathbf{S}}\rbrack}} \in {\mathbb{C}}^{d_{1} \times d_{2}}$, as measured in the spectral norm $\parallel \cdot \parallel$. For levels $t \geq 0$, we would like to control the tail probability

The expectation of the random matrix is computed componentwise; we always assume that this expectation is defined and finite. The spectral norm is also called the $\ell_{2}$ operator norm; it coincides with the largest singular value. If we control the deviation $\|{{\mathbf{S}} - {{\mathbb{E}}{\lbrack{\mathbf{S}}\rbrack}}}\|$, we also control other characteristics of the random matrix:

Singular values. The singular values of $\mathbf{S}$ and ${\mathbb{E}}{\lbrack{\mathbf{S}}\rbrack}$ are close.

Singular vectors. The singular vectors of $\mathbf{S}$ and ${\mathbb{E}}{\lbrack{\mathbf{S}}\rbrack}$ are close for isolated singular values.

Linear functionals. All linear functionals of $\mathbf{S}$ and ${\mathbb{E}}{\lbrack{\mathbf{S}}\rbrack}$ are comparable.

Many practical problems reduce to one of these considerations.

### Random matrix models

We cannot hope to make progress on the question (1.1) without imposing some restrictions on the random matrix. The challenge is to identify models that capture a wide range of examples, yet offer enough scaffolding to support strong theoretical guarantees. This paper focuses on two models inspired by the most basic scalar stochastic processes: independent sums and martingales. Our attention to these templates will be rewarded by a host of applications. Section˜6 outlines recent research and alternative models.

### Independent sums

A random matrix ${\mathbf{S}} \in {\mathbb{C}}^{d_{1} \times d_{2}}$ follows the independent sum model when it admits the decomposition

We use the term "statistical independence" to mark a contrast against linear independence. Let us emphasize that the entries within any particular matrix ${\mathbf{X}}_{k}$ may exhibit dependencies, but ${\mathbf{X}}_{k}$ cannot provide any information about events involving $({{\mathbf{X}}_{j}:{j \neq k}})$. Moreover, there may be many distinct decompositions of a random matrix as an independent sum. *Inter alia*, the independent sum model describes a random Monte Carlo approximation of a fixed matrix as an average of simple unbiased estimates \[:Introduction-Matrix, Sec. 6.2\].

We would like to capture information about the concentration of the independent sum $\mathbf{S}$ through summary statistics. In the scalar setting, we can achieve this goal with the Bernstein inequality \[:Concentration-Inequalities, Thm. 2.10\], which is arguably the most useful probability inequality for an independent sum of scalars. The matrix Bernstein inequality \[:User-Friendly, Thm. 6.2\] offers a perfect analogue in the matrix setting, where it may be the single most productive tool for studying random matrices. We present this result as Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory"). Section˜3 showcases applications to active subspace methods, stochastic rounding, graph sparsification, and quantum state tomography.

### Martingales

A matrix martingale is a sequence $({\mathbf{S}}_{0},{\mathbf{S}}_{1},{\mathbf{S}}_{2},\ldots)$ of random matrices with common dimension $d_{1} \times d_{2}$ that satisfies the "status quo" property:

Given what we know so far, our best estimate for the next matrix ${\mathbf{S}}_{k + 1}$ is the current matrix ${\mathbf{S}}_{k}$. As a simple example, the partial sums of an independent family of centered random matrices compose a matrix martingale. More generally, matrix martingales can model complicated sequences of random matrices that are revealed one step at a time, such as the iterates of a randomized algorithm that performs a linear algebra computation.

One of the most powerful tools for studying scalar martingale sequences is the Freedman inequality \[:Tail-Probabilities\], which is the martingale analog of the Bernstein inequality. The matrix Freedman inequality \[:Concentration-Adjacency,:Freedmans-Inequality\] generalizes the scalar result to matrix martingales. It allows us to treat sequences of random matrices that evolve adaptively, and it provides uniform control on the whole trajectory. We present this result as Theorem˜4.4. ‣ 4.2 Matrix Freedman ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory"). Section˜5 highlights applications to online covariance estimation, Cholesky decomposition with stochastic rounding, fast graph Laplacian solvers, and randomized approximation of quantum Hamiltonians.

### Notation

The Pascal notation $≔$ or $≕$ generates a definition. The symbols $\vee$ and $\land$ denote the infix maximum and minimum. We work over a scalar field ${\mathbb{F}} \in {\{{\mathbb{R}},{\mathbb{C}}\}}$, which is real or complex. The star ^∗^ delivers the (conjugate) transpose of a vector or matrix. The linear space ${\mathbb{F}}^{d}$ is equipped with the standard inner product ${\langle{\mathbf{b}},{\mathbf{a}}\rangle} ≔ {{\mathbf{b}}^{\ast}{\mathbf{a}}}$ and the associated $\ell_{2}$ norm $\parallel \cdot \parallel$.

In the space ${\mathbb{F}}^{d}$, the standard basis elements are $\mathbf{e}_{1},\ldots,\mathbf{e}_{d}$, and $\mathbf{1}$ is the vector of ones. The standard basis elements in a matrix space, such as ${\mathbb{F}}^{d_{1} \times d_{2}}$, are $\mathbf{E}_{ij}$. The identity matrix is $\mathbf{I}$. Dimensions are determined by context. We write $a_{ij}$ for the entries of a matrix $\mathbf{A}$, and we use the colon operator ${\mathbf{A}}{(i,:)}$ or ${\mathbf{A}}{(:,j)}$ to extract the $i$th row or $j$th column. For matrices, $\parallel \cdot \parallel$ is the spectral norm (aka the Schatten $\infty$-norm), $\parallel \cdot \parallel_{F}$ denotes the Frobenius norm (aka the Schatten $2$-norm), and $\parallel \cdot \parallel_{1}$ refers to the trace norm (aka the Schatten $1$-norm).

The linear space ${\mathbb{M}}_{d}{({\mathbb{F}})}$ consists of $d \times d$ matrices with entries in $\mathbb{F}$, on which the operator $Tr$ computes the trace. The real-linear subspace ${\mathbb{H}}_{d}{({\mathbb{F}})}$ consists of the $d \times d$ Hermitian (i.e., conjugate-symmetric) matrices. The cone ${\mathbb{H}}_{d}^{+}{({\mathbb{F}})}$ contains the $d \times d$ positive-semidefinite (psd) matrices, and ${\mathbb{H}}_{d}^{+ +}{({\mathbb{F}})}$ is the cone of positive-definite matrices. For Hermitian matrices, the semidefinite partial order ${\mathbf{A}} \preccurlyeq {\mathbf{H}}$ signifies that ${\mathbf{H}} - {\mathbf{A}}$ is psd, while the maps $\lambda_{\max}$ and $\lambda_{\min}$ return the (algebraic) maximum and minimum eigenvalues.

The operator $\mathbb{E}$ computes the expectation of a random variable, and $\mathbb{P}$ reports the probability of an event. The symbol $\sim$ means "has the distribution." For a real random variable $X$, the function $\sup X$ specifies its least upper bound on the probability space. Within a master probability space, the function $\sigma{( \cdot )}$ returns the sigma-algebra generated by its arguments; the empty argument returns the trivial sigma-algebra.

The big-$\mathcal{O}$ notation is interpreted per the conventions of computer science.

## The matrix Bernstein inequality

Among matrix concentration inequalities, the single most important result is the matrix extension of the scalar Bernstein inequality \[:Concentration-Inequalities, Thm. 2.10\]. The matrix Bernstein inequality was established independently by Roberto I. Oliveira \[:Concentration-Adjacency\] in late 2009 and the author \[:User-Friendly\] in early 2010. We state the version of this result from \[:Introduction-Matrix, Thm. 6.1.1\].

### Theorem 2.1 (Matrix Bernstein)

Consider a statistically independent family $(\mathbf{X}_{1},\ldots,\mathbf{X}_{n})$ of $d_{1} \times d_{2}$ random matrices, real or complex, that are centered and uniformly bounded: ${{\mathbb{E}}{\lbrack\mathbf{X}_{k}\rbrack}} = \mathbf{0}$ and ${\|\mathbf{X}_{k}\|} \leq B$ for each index $k$. Form the sum, and calculate its matrix variance statistic:

Then the spectral norm of the sum satisfies the probability inequalities

The proof of Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory") parallels the proof of the scalar Bernstein inequality, but it requires sophisticated tools from matrix analysis. The argument will occupy the rest of this section. First, we elaborate on the meaning of the result.

The significant outcome of Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory") is the expectation bound (2.2. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")). In contrast, the tail bound (2.3. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")) is usually somewhat loose; it can be improved by combining the expectation bound (2.2. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")) with scalar concentration inequalities for the norm of an independent sum, such as \[:Concentration-Inequalities, Prob. 13.33\].

We remark that Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory") reproduces the scalar Bernstein inequality when it is applied to random scalars (i.e., $1 \times 1$ random matrices), so the numerical constants are sharp. The dimensional factor $({d_{1} + d_{2}})$ is a new feature in the matrix setting, and it is a necessary component of the bound; see subsection˜2.6.

Like the scalar variance, the matrix variance $v{({\mathbf{S}})}$ reflects the magnitude of the expected "square" of the centered random matrix, where we keep in mind that the non-Hermitian matrix $\mathbf{S}$ has two distinct squares ${\mathbf{S}}{\mathbf{S}}^{\ast}$ and ${\mathbf{S}}^{\ast}{\mathbf{S}}$. Both terms in the matrix variance are required, although they coincide when the sum is Hermitian. It is often convenient to express the matrix variance directly in terms of the summands:

The last identity exploits independence and centering. For simplicity, Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory") assumes that the matrix $\mathbf{S}$ is centered; otherwise, note that

The theorem now applies to the second term.

### Reduction to the Hermitian case

Let us commence with the proof of Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory"). It suffices to consider the complex case. Introduce the Hermitian dilation:

The map $\mathcal{H}$ is real-linear, and it preserves spectral data in the sense that ${\lambda_{\max}{({\mathcal{H}{({\mathbf{A}})}})}} = {- {\lambda_{\min}{({\mathcal{H}{({\mathbf{A}})}})}}} = {\|{\mathbf{A}}\|}$. As a consequence, to prove Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory"), we can pass to the random Hermitian matrix

Through this device, we can simply instate the assumption that the summands are Hermitian matrices.

### The matrix Laplace transform method

To extract information about the distribution of a bounded random *Hermitian* matrix ${\mathbf{S}} \in {{\mathbb{H}}_{d}{({\mathbb{C}})}}$, define the logarithm of the matrix moment generating function (briefly, the matrix log-mgf):

We apply a scalar function to an Hermitian matrix by applying the function to each eigenvalue without modifying the associated eigenspace. Ahlswede & Winter \[:Strong-Converse\] formulated the ideas in this subsection, while Oliveira \[:Concentration-Adjacency\] and the author \[:User-Friendly,:Introduction-Matrix\] crystallized the arguments.

Even in the matrix setting, we can pursue the same strategy that leads to exponential tail bounds in the scalar setting \[:Concentration-Inequalities, Chap. 2\]. When the parameter $\theta > 0$,

The first inequality is Markov's. Afterward, invoke the spectral mapping theorem to draw the eigenvalue map through the exponential, and note that the trace of a psd matrix dominates its maximum eigenvalue. The emergence of the trace exponential of the matrix log-mgf unlocks powerful tools for trace functions.

A similar calculation furnishes a bound for the expectation of the maximum eigenvalue. For each $\theta > 0$,

The first inequality is Jensen's. Once again, the matrix log-mgf controls the maximum eigenvalue.

### Subadditivity of the matrix log-mgf

In the scalar setting, the log-mgf of a sum of independent real random variables agrees with the sum of the log-mgfs:

The latter formula depends on the fact $e^{a + b} = {e^{a}e^{b}}$ for ${a,b} \in {\mathbb{R}}$, a property that catastrophically fails for matrices.

Remarkably, there is a substitute. I established a *subadditivity rule* for the matrix log-mgf \[:User-Friendly, Lem. 3.4\]:

In this expression, $({\mathbf{X}}_{1},\ldots,{\mathbf{X}}_{n})$ is a statistically independent family of bounded, Hermitian random matrices of the same dimension. In the proof of (2.8), the key ingredient is a deep concavity theorem of Lieb \[:Convex-Trace, Thm. 6\], which is one of the crown jewels of matrix analysis. See \[:Introduction-Matrix, Chap. 8\] for a detailed proof of Lieb's result.

### The matrix Bernstein log-mgf bound

The subadditivity rule (2.8) reduces the bound on the matrix log-mgf of a sum to individual bounds on the matrix log-mgfs of the summands. Classic scalar concentration inequalities \[:Concentration-Inequalities, Ch. 2\] provide inspiration about fruitful strategies for controlling the matrix log-mgfs \[:User-Friendly,:Introduction-Matrix\].

The matrix Bernstein inequality depends on the same type of log-mgf bound as the scalar Bernstein inequality \[:Concentration-Inequalities, Thm. 2.10\]. Indeed, the result \[:Introduction-Matrix, Lem. 6.1\] states that the matrix log-mgf of a bounded, centered, random Hermitian matrix ${\mathbf{X}} \in {{\mathbb{H}}_{d}{({\mathbb{C}})}}$ satisfies the relation

The semidefinite partial order ${\mathbf{A}} \preccurlyeq {\mathbf{H}}$ on Hermitian matrices means that ${\mathbf{H}} - {\mathbf{A}}$ is psd. The proof of (2.9) tracks the scalar argument. Expand the exponential function in the matrix log-mgf as a Taylor series, use the centering to remove the term with degree one, and apply the norm bound to control the terms with degree two and higher. We also employ the fact that the matrix logarithm respects the semidefinite partial order \[:Introduction-Matrix, Prop. 8.4.4\].

### Assembly line

We are prepared to establish Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory"). Consider the sum ${\mathbf{S}} ≔ {\sum_{k = 1}^{n}{\mathbf{X}}_{k}}$ of independent, random Hermitian matrices with dimension $d$ that satisfy ${{\mathbb{E}}{\lbrack{\mathbf{X}}_{k}\rbrack}} = \mathbf{0}$ and ${\|{\mathbf{X}}_{k}\|} \leq B$. Sequence the displays Eqs.˜2.6, 2.8, and 2.9 to arrive at the tail inequality

The parameter is restricted to the interval ${|\theta|} < {B/3}$. The first inequality depends on the fact that the trace exponential respects the semidefinite partial order \[:Introduction-Matrix, Ex. 8.1\]. The identity exploits the centering and independence of the summands. Afterward, bound the trace exponential by the dimension $d$ times the maximum eigenvalue, and use spectral mapping to recognize the matrix variance ${v{({\mathbf{S}})}} = {\lambda_{\max}{({{\mathbb{E}}{\lbrack{\mathbf{S}}^{2}\rbrack}})}}$.

Finally, in (2.10), set the parameter $\theta = {t/{({{v{({\mathbf{S}})}} + {{Bt}/3}})}}$ to reach the finished tail inequality

To establish the analogous tail bound (2.3. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")) for a general non-Hermitian sum, apply the Hermitian dilation (2.5) and invoke (2.11). The bound (2.2. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")) on the *expected* norm of the sum follows a similar argument starting from (2.7).

### Optimality

As noted, the expectation bound (2.2. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")) is the most significant outcome from Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory"). We can strengthen this bound, but not by very much. Introduce the tail content statistic:

The tail content satisfies $B_{2} \leq B$; the slackness of this inequality depends on the particular choice of summands. Using another style of argument based on symmetrization \[:Expected-Norm\], we can obtain a two-sided bound of the form

The paper \[:Expected-Norm\] provides examples to show that each term in (2.12) is necessary, so we cannot improve the bounds without a substantial amount of extra information (about the covariance structure of the random matrix). Section˜6 mentions some situations where improvements are possible.

## Independent sum model: Applications

In this section, we present some contemporary applications of the matrix Bernstein inequality in several areas of computational mathematics. As a caveat, these stylized applications may not reflect the intricacies of each problem. It is sometimes possible to find a simpler argument by invoking a more suitable matrix concentration inequality, and we can occasionally obtain sharper analyses using more complicated tools; see section˜6.

### Active subspace methods

In engineering design, researchers build computer models of complex physical systems that are governed by several input parameters. Key tasks include optimization of parameters, analysis of sensitivity to changes in parameters, and quantification of uncertainty about the system output. For example, an aeronautics engineer designs an airfoil by modifying its geometry to reach a target lift and drag coefficient. It is challenging to explore the parameter space of a complicated, nonlinear model, so it is common to seek reduced models. One basic methodology is to restrict our attention to the most salient directions in the input space, which we can identify through a random sampling procedure. The analysis of this approach depends on matrix concentration inequalities. This vignette is adapted from Constantine's book \[:Active-Subspaces, Chap. 3\]. The mathematics are similar with the classic problem of covariance estimation; see subsection˜5.1.

Let $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ be an $L$-Lipschitz, differentiable function that models a complicated system, and assume that we can evaluate its gradient $\nabla f$ at each point in the parameter space---but the computational cost is significant. As part of the model, introduce a random vector ${\mathbf{z}} \in {\mathbb{R}}^{d}$ that describes a distribution over the parameter space; this distribution is often interpreted as a Bayesian prior. To capture the variability of the function, introduce the psd sensitivity matrix

The quadratic form in $\mathbf{\Sigma}$ reflects the sensitivity of the function to directional perturbations in the input space:

The subspace spanned by the leading eigenvectors of $\mathbf{\Sigma}$ is called an *active subspace* of the model, because it captures the most salient directions in the input space.

We cannot evaluate the sensitivity matrix $\mathbf{\Sigma}$ explicitly, but we can construct a Monte Carlo approximation:

How many gradient samples suffice to approximate the sensitivity matrix $\mathbf{\Sigma}$? Can we determine the directions in which the model varies substantially?

### Theorem 3.1 (Sampling active subspaces \[:Active-Subspaces, Thm. 3.7\])

Let $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ be $L$-Lipschitz and differentiable. As in Eqs.˜3.1 and 3.2, consider the sensitivity matrix $\mathbf{\Sigma} \in {{\mathbb{H}}_{d}{({\mathbb{R}})}}$ and the empirical approximation ${\hat{\mathbf{\Sigma}}}_{n} \in {{\mathbb{H}}_{d}{({\mathbb{R}})}}$ determined by $n$ gradient samples. The expectation of the relative approximation error satisfies

For $\varepsilon \in {}$, the sample complexity $n \geq {{4\varepsilon^{- 2}L^{2}{\log{({2d})}}}/{\|\mathbf{\Sigma}\|}}$ results in expected relative error at most $\varepsilon$.

The ratio $r ≔ {L^{2}/{\|\mathbf{\Sigma}\|}}$ reflects the number of energetic dimensions in the model. Given $n = {\mathcal{O}{({r{\log d}})}}$ gradient samples, the estimator ${\hat{\mathbf{\Sigma}}}_{n}$ for the sensitivity matrix $\mathbf{\Sigma}$ allows us to find this active subspace. To reduce the relative error to a level $\varepsilon$, the estimator requires an additional factor of $\varepsilon^{- 2}$ samples, so the empirical approximation does not attain high accuracy. This is a familiar weakness of Monte Carlo methods.

### Proof 1 (Proof sketch)

The error in the Monte Carlo approximation is an instance of the independent sum model. Abbreviate ${\mathbf{y}}_{k} ≔ {{\nabla f}{({\mathbf{z}}_{k})}}$ for each index $k$. Since the function $f$ is $L$-Lipschitz, the random vectors satisfy the uniform bound ${\|{\mathbf{y}}_{k}\|} \leq L$. Introduce the matrix approximation error

The summands $({\mathbf{X}}_{k})$ compose an independent family of bounded, centered, random Hermitian matrices with common dimension $d$. The statistics appearing in the matrix Bernstein inequality (Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")) satisfy

The stated result follows from (2.2. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")).

### Stochastic rounding

Conventional computer architectures offer floating-point numbers with 16 decimal digits of precision or more. Driven by contemporary applications, computer engineers have started to develop new architectures with far lower precision---sometimes as few as 4 or 8 bits (i.e., 1--2 digits). At this extreme, large numerical errors can accumulate as we round successive calculations to the nearest machine-representable number. One way to mitigate these errors is to design computer systems that perform *stochastic rounding*. To analyze linear algebra computations that employ stochastic rounding, we can exploit matrix concentration tools. This section offers an idealized treatment of the simplest problem; see \[CFH+22:Stochastic-Rounding\] for more texture.

A floating-point number system is a finite set of machine-representable numbers $\mathsf{F} \subset {\mathbb{R}}$. Ignoring underflow and overflow, a (deterministic) rounding rule approximates each real number $a \in {\mathbb{R}}$ by a floating-point number ${\text{float}{(a)}} \in \mathsf{F}$ that admits the relative-error bound

In IEEE double-precision arithmetic, the unit-roundoff parameter $\text{u} = 2^{- 53} \approx 10^{- 16}$, and the rounding rule must satisfy additional requirements to meet the standard \[CFH+22:Stochastic-Rounding, Tabs. 1, 2\]. As an alternative, a *stochastic rounding rule* maps each real number $a \in {\mathbb{R}}$ to a *random* floating-point number ${\text{sr}{(a)}} \in \mathsf{F}$ that satisfies

In words, stochastic rounding is unbiased, and it commits a relative error on the order of the unit roundoff.

Suppose that we round each entry of a real-valued matrix stochastically to the nearest floating-point number. How much damage will we do? How does this bound compare with deterministic rounding?

### Theorem 3.2 (Stochastic rounding)

Consider a matrix $\mathbf{A} \in {\mathbb{R}}^{d_{1} \times d_{2}}$. For $p \in {\{ 1,2\}}$, define the norms

Form a random matrix ${\text{sr}{(\mathbf{A})}} \in \mathsf{F}^{d_{1} \times d_{2}}$ by independently rounding each entry of $\mathbf{A}$, honoring the rule (3.4). Then

In contrast, the deterministic rule (3.3) only guarantees that ${\|{\mathbf{A} - {\text{float}{(\mathbf{A})}}}\|} \leq {\text{u} \cdot {\|\mathbf{A}\|}_{{rc},1}}$.

To interpret the result, it is helpful to consider a square matrix with dimension $d$ whose entries all have similar magnitudes. In this case, the stochastic rounding bound is governed by the norm ${\|{\mathbf{A}}\|}_{{rc},2}$, which is proportional to $\sqrt{d}$. Meanwhile, the deterministic rounding bound depends on ${\|{\mathbf{A}}\|}_{{rc},1}$, which is proportional to the matrix dimension $d$. This contrast indicates that stochastic rounding confers a significant benefit.

### Proof 2 (Proof sketch)

The matrix of rounding errors is an instance of the independent sum model:

The summands ${\mathbf{X}}_{ij} ≔ {\varepsilon_{ij}a_{ij}\mathbf{E}_{ij}}$ are bounded, centered independent random matrices with dimension $d_{1} \times d_{2}$. A short calculation confirms that the parameters in the matrix Bernstein inequality (Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")) satisfy

The bound on the expectation of the error follows directly from (2.2. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")). The error bound for deterministic rounding holds because ${\|{\mathbf{M}}\|} \leq {\|{\mathbf{M}}\|}_{{rc},1}$ for any matrix $\mathbf{M}$; see \[:Matrix-Analysis-2ed, Prob. 5.6P21\].

In fact, the error estimate for stochastic rounding in Theorem˜3.2. ‣ 3.2 Stochastic rounding ‣ 3 Independent sum model: Applications ‣ Applied Random Matrix Theory") admits a modest refinement:

This bound follows from a specialized result \[:Extremal-Random, Thm. 1.4\] for random matrices with independent entries, plus a symmetrization argument \[:High-Dimensional-Probability, Lem. 6.4.2\]. For most practical use cases, the improvement is insubstantial.

### Graph sparsification

A combinatorial graph encodes the pairwise relationships among a family of objects. We may ask whether it is possible to find a simpler graph (with fewer edges) that preserves structural properties of the original graph, such as the weights of vertex cuts and the mixing time of a random walk. Spielman & Srivastava \[:Graph-Sparsification\] showed how to achieve this goal by randomly sampling edges from the graph. We can analyze the procedure with matrix concentration.

Consider a connected, weighted, undirected graph $(\mathsf{V},w)$. The graph comprises a set $\mathsf{V} ≔ {\{ 1,\ldots,n\}}$ of vertices and a symmetric function $w:{{\mathsf{V} \times \mathsf{V}}\rightarrow{\mathbb{R}}_{+}}$ that assigns a nonnegative weight to each pair of vertices. We require that $w_{ii} = 0$ and $w_{ij} = w_{ji}$ for all ${i,j} \in \mathsf{V}$. The number of edges $m ≔ {\#{\{{i < j}:{w_{ij} > 0}\}}}$.

We can also represent the graph by means of the graph Laplacian ${\mathbf{L}} \in {{\mathbb{H}}_{n}^{+}{({\mathbb{R}})}}$, which is the psd matrix

The sum involves $m$ nonzero terms. Since the graph is connected, ${{null}{({\mathbf{L}})}} = {{span}{\{\mathbf{1}\}}}$. Without further notice, we restrict $\mathbf{L}$ to the $({n - 1})$-dimensional subspace where it is nonsingular. Define the effective resistance of each vertex pair in the graph:

If the graph models an electrical network whose wires have conductances $w_{ij}$, then the effective resistance $\varrho_{ij}$ is the voltage required to push one unit of current from vertex $i$ to vertex $j$. Observe that ${\sum_{i < j}{w_{ij}\varrho_{ij}}} = {n - 1}$. We can approximate all $m$ of the nonzero effective resistances in $\mathcal{O}{({m{\log n}})}$ arithmetic operations \[:Graph-Sparsification, Thm. 2\].

Our goal is to produce a *sparse* graph whose Laplacian matrix $\hat{\mathbf{L}} \in {{\mathbb{H}}_{n}^{+}{({\mathbb{R}})}}$ is comparable with the original Laplacian $\mathbf{L}$ in the semidefinite partial order:

The spectral equivalence (3.6) ensures that the sparse graph is structurally similar with the original graph. We plan to construct a spectral sparsifier $\hat{\mathbf{L}}$ by randomly sampling edges according to a carefully chosen probability distribution. Introduce the random matrix ${\mathbf{Y}} \in {{\mathbb{H}}_{d}^{+}{({\mathbb{R}})}}$ with distribution

In other words, $\mathbf{Y}$ is the Laplacian of a weighted edge between a pair $(i,j)$ of vertices, chosen with probability proportional to the weight $w_{ij}$ and the effective resistance $\varrho_{ij}$. It is easy to confirm that ${{\mathbb{E}}{\lbrack{\mathbf{Y}}\rbrack}} = {\mathbf{L}}$, so the random matrix $\mathbf{Y}$ is an unbiased estimator for the Laplacian $\mathbf{L}$ of the original graph. By averaging $q$ independent copies of $\mathbf{Y}$, we obtain the Laplacian of a random sparse graph with at most $q$ edges:

How many edges $q$ suffice to achieve the approximation guarantee (3.6)?

### Theorem 3.3 (Graph sparsification \[:Graph-Sparsification, Thm. 1\])

Let $\mathbf{L}$ be the Laplacian (3.5) of a weighted graph on $n$ vertices, and let $\hat{\mathbf{L}}$ be the Laplacian (3.7) of a random sparse graph with at most $q$ edges. With probability at least $1 - \delta$, the random matrix $\hat{\mathbf{L}}$ is an $\varepsilon$-approximation of $\mathbf{L}$ in the sense (3.6) provided that $q \geq {3\varepsilon^{- 2}n{\log{({{2n}/\delta})}}}$.

The result ensures that we can approximate a graph on $n$ vertices by a sparse graph with $q = {\mathcal{O}{({n{\log n}})}}$ edges, regardless of the number $m$ of edges in the original graph. We pay an extra factor $\varepsilon^{- 2}$ in the number of edges $q$ to achieve accuracy $\varepsilon$. Although the randomized method is simple and efficient, there is a more expensive deterministic algorithm that finds an $\varepsilon$-spectral sparsifier with just $q = {\mathcal{O}{({n/\varepsilon^{2}})}}$ edges \[:Twice-Ramanujan\].

### Proof 3 (Proof sketch)

Define the linear map ${\mathbf{\Phi}{({\mathbf{A}})}} ≔ {{\mathbf{L}}^{- {1/2}}{\mathbf{A}}{\mathbf{L}}^{- {1/2}}}$ on symmetric matrices that act on ${range}{({\mathbf{L}})}$. The spectral equivalence (3.6) is the same as the requirement that ${{\|{\mathbf{\Phi}{({\hat{\mathbf{L}} - {\mathbf{L}}})}}\|} \leq \varepsilon}.$ The matrix inside the norm can be written as an independent sum of centered random matrices acting on an $({n - 1})$-dimensional space:

To activate the matrix Bernstein inequality (Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")), check that

The result now follows from the tail inequality (2.3. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")). For details, see \[:Matrix-Concentration-LN, Sec. 5.2\].

### Quantum tomography

The state of a finite-dimensional quantum system, such as a register in a quantum computer, is characterized by a finite-dimensional psd matrix. We can probe the system by taking measurements, but the laws of quantum mechanics imply that each measurement returns a random number. As a consequence, methods for reconstructing the state of a quantum system lead to problems involving random matrices. Matrix concentration tools offer a quick way to analyze quantum state estimators. This section summarizes a lecture by Richard Kueng (see \[:Matrix-Concentration-LN, Lec. 3\]), which distills ideas from a paper of Guţa et al. \[:Fast-State-Tomography\]. Related ideas animate the theory of classical shadows, a major recent advance in quantum information science \[:Predicting-Many\].

We model a quantum system by means of its density matrix, which is a complex psd matrix with trace one. The convex, compact set $\mathcal{D}_{d} ≔ {\{{{\mathbf{ρ}} \in {{\mathbb{H}}_{d}^{+}{({\mathbb{C}})}}}:{{{Tr}{\lbrack{\mathbf{ρ}}\rbrack}} = 1}\}}$ collects the density matrices of dimension $d$. Next, a quantum measurement is a family ${\{{\mathbf{H}}_{1},\ldots,{\mathbf{H}}_{m}\}} \subset {{\mathbb{H}}_{d}^{+}{({\mathbb{C}})}}$ of psd matrices that partitions the identity: ${\sum_{j = 1}^{m}{\mathbf{H}}_{j}} = \mathbf{I}$. When we apply the measurement to a quantum system with density matrix ${\mathbf{ρ}} \in \mathcal{D}_{d}$, two things happen. First, we sample a discrete random variable $J$ with distribution

Second, the quantum system "collapses". Therefore, to characterize a quantum system, we must prepare several copies in the same state and measure each one to obtain statistical evidence about the state.

For simplicity, we consider a special type of quantum measurement, called a complex projective 2-design. Here, each of the measurement matrices has rank one: ${\mathbf{H}}_{j} = {{({d/m})}{\mathbf{u}}_{j}{\mathbf{u}}_{j}^{\ast}}$ where ${\mathbf{u}}_{j} \in {\mathbb{C}}^{d}$ is a unit-norm vector. Moreover, these measurements support the reconstruction property

The vectors ${\mathbf{u}}_{1},\ldots,{\mathbf{u}}_{m}$ composing a complex projective 2-design are arranged very regularly over the complex sphere. Examples include systems of "mutually unbiased" orthonormal bases and systems of equiangular lines \[:Matrix-Concentration-LN, Ex. 3.3\]. This type of measurement system can stably distinguish any pair of density matrices.

To reconstruct a quantum system with density matrix ${\mathbf{ρ}} \in \mathcal{D}_{d}$, we perform a measurement to sample the random variable $J$. Then we build a random Hermitian matrix ${\mathbf{Y}} \in {{\mathbb{H}}_{d}{({\mathbb{C}})}}$ according to the rule

The random matrix $\mathbf{Y}$ serves as an unbiased estimator for the density matrix:

This calculation follows from (3.8) and (3.9). By repeating the measurement on $n$ independent (i.e., unentangled) copies of the quantum system, each with density matrix $\mathbf{ρ}$, we can obtain an estimator

How many independent measurements suffice to approximate the underlying density matrix?

### Theorem 3.4 (Quantum tomography)

Let ${\mathbf{ρ}} \in \mathcal{D}_{d}$ be a density matrix with dimension $d$. Using a complex projective 2-design (3.9), perform a quantum measurement on each of $n$ independent quantum systems with common state $\mathbf{ρ}$. Form the sample-average estimator $\mathbf{S}_{n}$, as in (3.10). For $\varepsilon \in {}$,

In particular, the sample complexity $n \geq {5\varepsilon^{- 2}d{\log{({{2d}/\delta})}}}$ yields a failure probability no greater than $\delta \in {}$.

### Proof 4 (Proof sketch)

To apply the matrix Bernstein inequality (Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")) to the estimator (3.10), simply compute

The statement follows quickly from (2.3. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")).

While the sample average estimator (3.10) is unbiased, it generally does not produce a density matrix. Moreover, the trace norm yields a more interpretable distance between density matrices than the spectral norm. To address these concerns, define the projected state estimator using the Frobenius norm:

Lemma 3.9 of \[:Matrix-Concentration-LN\] ensures that the projected state estimator satisfies the trace-norm bound

As a consequence, we arrive at an upper bound for the sample complexity of the projected state estimator:

This bound implies that the projected state estimator ${\hat{\mathbf{ρ}}}_{n}$ nearly achieves the *optimal* sample complexity that is possible in this setting \[Haa+17:Sample-Optimal-Tomography\].

## Concentration for matrix martingales

The full majesty of the framework for exponential matrix concentration comes into view when we extend it to dynamically evolving sequences of matrices.

### Matrix martingales

Fix a probability space. A *filtration* is an increasing sequence of sigma-algebras $\mathcal{F}_{0} \subseteq \mathcal{F}_{1} \subseteq \mathcal{F}_{2} \subseteq \cdots$ inside the master sigma-algebra. A matrix martingale is a sequence $({\mathbf{S}}_{0},{\mathbf{S}}_{1},{\mathbf{S}}_{2},\ldots)$ of complex random matrices with common dimension $d_{1} \times d_{2}$ that satisfies three properties. For each index $k = {0,1,2,\ldots}$, the sequence is

Adapted. Each random matrix ${\mathbf{S}}_{k}$ is measurable with respect to $\mathcal{F}_{k}$.

Integrable. The expected norm is finite: ${{\mathbb{E}}{\|{\mathbf{S}}_{k}\|}} < {+ \infty}$.

Status quo. The conditional expectation ${{\mathbb{E}}{\lbrack\left. {\mathbf{S}}_{k + 1} \middle| \mathcal{F}_{k} \right.\rbrack}} = {\mathbf{S}}_{k}$.

The difference sequence consists of the matrices ${\mathbf{X}}_{k} ≔ {{\mathbf{S}}_{k} - {\mathbf{S}}_{k - 1}}$ with $k \geq 1$. Each member of the difference sequence is conditionally centered: ${{\mathbb{E}}{\lbrack\left. {\mathbf{X}}_{k} \middle| \mathcal{F}_{k - 1} \right.\rbrack}} = \mathbf{0}$. Matrix martingales model a wide range of examples.

### Example 4.1 (Adapted sums)

Let $\mathbf{S}_{0} ≔ \mathbf{A}$ be a fixed matrix. For each index $k \geq 1$, suppose that $\mathbf{S}_{k} ≔ {\mathbf{S}_{k - 1} + \mathbf{X}_{k}}$ where the increments are conditionally centered: ${{\mathbb{E}}{\lbrack\left. \mathbf{X}_{k} \middle| {\mathbf{X}_{0},\ldots,\mathbf{X}_{k - 1}} \right.\rbrack}} = \mathbf{0}$. Then $(\mathbf{S}_{0},\mathbf{S}_{1},\mathbf{S}_{2},\ldots)$ is a matrix martingale with respect to the filtration $\mathcal{F}_{k} ≔ {\sigma{(\mathbf{S}_{0},\mathbf{X}_{1},\ldots,\mathbf{X}_{k})}}$ defined for $k \geq 0$.

### Example 4.2 (Adapted products)

Let $\mathbf{S}_{0} ≔ \mathbf{A}$ be a fixed matrix. Suppose that $\mathbf{S}_{k} ≔ {\mathbf{Y}_{k}\mathbf{S}_{k - 1}}$ where the factors satisfy ${{\mathbb{E}}{\lbrack\left. \mathbf{Y}_{k} \middle| {\mathbf{S}_{0},\ldots,\mathbf{S}_{k - 1}} \right.\rbrack}} = \mathbf{I}$. Then $(\mathbf{S}_{0},\mathbf{S}_{1},\mathbf{S}_{2},\ldots)$ composes a matrix martingale with respect to the filtration $\mathcal{F}_{k} ≔ {\sigma{(\mathbf{S}_{0},\mathbf{Y}_{1},\ldots,\mathbf{Y}_{k})}}$ defined for $k \geq 0$.

### Example 4.3 (Lévy--Doob martingale)

Fix a filtration $\mathcal{F}_{0} \subseteq \mathcal{F}_{1} \subseteq \mathcal{F}_{2} \subseteq \ldots$. Let $\mathbf{S}$ be a random $d_{1} \times d_{2}$ matrix with ${{\mathbb{E}}{\|\mathbf{S}\|}} < {+ \infty}$. Construct the sequence of conditional expectations:

Then $(\mathbf{S}_{0},\mathbf{S}_{1},\mathbf{S}_{2},\ldots)$ composes a martingale with respect to the filtration.

To avoid technicalities, we only consider finite martingale sequences $({\mathbf{S}}_{0},\ldots,{\mathbf{S}}_{n})$. Furthermore, we require the elements of the martingale to be uniformly bounded in the sense that ${\sup{\|{\mathbf{S}}_{k}\|}} \leq B_{\infty} < {+ \infty}$ for each index $k = {0,\ldots,n}$. The filtration may be suppressed if it is determined by context.

### Matrix Freedman

To analyze a matrix martingale, the most valuable theorem is the matrix Freedman inequality, originally due to Roberto I. Oliveira \[:Concentration-Adjacency\]. The author exploited the subadditivity (2.8) of the matrix log-mgf to refine Oliveira's result and to establish some other matrix martingale inequalities \[:Freedmans-Inequality\]. The version stated here follows from \[:Freedmans-Inequality, Cor. 1.3, Thm. 3.1\].

### Theorem 4.4 (Matrix Freedman)

Consider a finite matrix martingale sequence $(\mathbf{S}_{0},\ldots,\mathbf{S}_{n})$ consisting of $d_{1} \times d_{2}$ matrices, real or complex. Suppose that the elements of the difference sequence $(\mathbf{X}_{1},\ldots,\mathbf{X}_{n})$ are uniformly bounded: ${\|\mathbf{X}_{k}\|} \leq B$. Introduce the conditional quadratic variation sequence:

For parameters ${v,t} \geq 0$, we have the probability inequalities

The rest of this section presents a proof of Theorem˜4.4. ‣ 4.2 Matrix Freedman ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory") that combines ideas from my paper \[:Freedmans-Inequality\] and from the survey of Howard et al. \[:Time-Uniform-Chernoff\]. First, we dilate on the meaning of the result.

The conditional quadratic variation $V_{k}$ is the martingale analogue of the matrix variance; cf. (2.4). At each step $j$ of the process, we compute the expected "squares" of the element ${\mathbf{X}}_{j}$ in the difference sequence, given data $\mathcal{F}_{j - 1}$ about the previous position of the martingale, and we combine the results. Thus, $V_{k}$ is a random variable that reflects the total observed volatility of the matrix martingale up to time $k$. When the difference sequence $({\mathbf{X}}_{1},\ldots,{\mathbf{X}}_{n})$ is statistically independent, each $V_{k}$ reduces to the matrix variance $v{({\mathbf{S}}_{k})}$.

The probability inequalities Eqs.˜4.1. ‣ 4.2 Matrix Freedman ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory") and 4.2. ‣ 4.2 Matrix Freedman ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory") state that the norm of the martingale element $\|{\mathbf{S}}_{k}\|$ is unlikely to be large when the conditional quadratic variation $V_{k}$ is bounded above. The first inequality (4.1. ‣ 4.2 Matrix Freedman ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory")) formulates a clean bound on the tail probability, while the second inequality provides a direct bound on the level of $\|{\mathbf{S}}_{k}\|$. Let us emphasize that both estimates provide uniform control on the *entire trajectory* of the matrix martingale.

### The log-mgf supermartingale

As in the proof of Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory"), we can and will employ the Hermitian dilation (2.5) to restrict our attention to Hermitian random matrices.

Consider a bounded Hermitian matrix martingale $({\mathbf{S}}_{0},\ldots,{\mathbf{S}}_{n})$ taking values in ${\mathbb{H}}_{d}{({\mathbb{C}})}$, with initial condition ${\mathbf{S}}_{0} ≔ \mathbf{0}$ and with difference sequence $({\mathbf{X}}_{1},\ldots,{\mathbf{X}}_{n})$. For a parameter $\theta \in {\mathbb{R}}$, define the *conditional* log-mgfs and their partial sums:

The element ${{\mathbf{W}}_{k}{(\theta)}} \in {{\mathbb{H}}_{d}{({\mathbb{C}})}}$ of the log-mgf process reflects the total volatility of the martingale up to time $k$.

To track the evolution of the matrix martingale, let us pass to a real-valued random sequence:

Applying the subadditivity rule (2.8) for the matrix log-mgf conditionally, we quickly verify that ${{\mathbb{E}}{\lbrack\left. {M_{k}{(\theta)}} \middle| \mathcal{F}_{k - 1} \right.\rbrack}} \leq {M_{k - 1}{(\theta)}}$ for each $k = {1,\ldots,n}$. In other words, $({{M_{k}{(\theta)}}:{k = {0,\ldots,n}}})$ composes a positive supermartingale. We can study the trajectory of the matrix martingale by bounding the supermartingale \[:Concentration-Adjacency,:Freedmans-Inequality\]. The approach here is adapted from Howard et al. \[:Time-Uniform-Chernoff\].

### Proposition 4.5 (Matrix martingale: Eigenvalue bounds)

Consider a finite matrix martingale $(\mathbf{S}_{0},\ldots,\mathbf{S}_{n})$ taking values in ${\mathbb{H}}_{d}{({\mathbb{C}})}$ with log-mgf process $({\mathbf{W}_{1}{(\theta)}},\ldots,{\mathbf{W}_{n}{(\theta)}})$, as in (4.3). For parameters ${\theta,\alpha} > 0$,

### Proof 5

The log-mgf supermartingale (4.4) admits a lower bound involving the eigenvalues of the sequences:

For the inequality, note that the trace dominates the maximum eigenvalue; then apply spectral mapping and Weyl's perturbation theorem \[:Matrix-Analysis, Cor. III.2.6\]. Ville's inequality for positive supermartingales \[:Time-Uniform-Chernoff, Lem. 1\] implies

This is the advertised result.

### Proof of Matrix Freedman

To invoke Proposition˜4.5. ‣ 4.3 The log-mgf supermartingale ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory"), we seek a bound for the maximum eigenvalue of the log-mgf process $({{{\mathbf{W}}_{k}{(\theta)}}:{k = {0,\ldots,n}}})$. In the setting of Theorem˜4.4. ‣ 4.2 Matrix Freedman ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory"), each element of the difference sequence admits a bound on the conditional log-mgf of the Bernstein type (2.9):

By Weyl's monotonicity theorem \[:Matrix-Analysis, Cor. III.2.3\],

Proposition˜4.5. ‣ 4.3 The log-mgf supermartingale ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory") yields

In the Hermitian setting, we obtain an analog of the first matrix Freedman tail bound (4.1. ‣ 4.2 Matrix Freedman ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory")) by selecting $\alpha = t$ and $\theta = {\sqrt{t}/{({\sqrt{v/2} + {{B\sqrt{t}}/3}})}}$. The second tail bound (4.2. ‣ 4.2 Matrix Freedman ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory")) follows from the first tail bound by inverting the function of $t$ and making a simple bound; see \[:Concentration-Inequalities, Secs. 2.4 and 2.8\]. Finally, we extend to a general (non-Hermitian) matrix martingale by applying these two bounds to the Hermitian dilation (2.5).

## Matrix martingales: Applications

In this section, we outline some applications of the matrix Freedman inequality in computational mathematics. This technique is particularly valuable for handling sequences of matrices that evolve adaptively, and it provides uniform control over the entire trajectory of the process.

### Uniform covariance estimation

Consider a centered random vector ${\mathbf{y}} \in {\mathbb{R}}^{d}$ that is uniformly bounded: ${{\mathbb{E}}{\lbrack{\mathbf{y}}\rbrack}} = \mathbf{0}$ and ${\|{\mathbf{y}}\|} \leq L$. Its covariance matrix takes the form $\mathbf{\Sigma} ≔ {{\mathbb{E}}{\lbrack{{\mathbf{y}}{\mathbf{y}}^{\ast}}\rbrack}}$. Given iid samples ${\mathbf{y}}_{1},{\mathbf{y}}_{2},{\mathbf{y}}_{3},\ldots$ from the distribution, we can construct a sequence of empirical covariance estimates:

We would like to obtain a confidence region for the entire sequence of covariance estimates, ensuring simultaneous coverage at all times. The following statement is adapted from Howard et al. \[:Time-Uniform-Nonparametric, Sec. 4.3\].

### Theorem 5.1 (Uniform covariance estimation \[:Time-Uniform-Nonparametric, Sec. 4.3\])

Let $\mathbf{y} \in {\mathbb{R}}^{d}$ be a bounded, centered random vector with ${\|\mathbf{y}\|} \leq L$ and covariance matrix $\mathbf{\Sigma}$. As in (5.1), construct the sequence $({{\hat{\mathbf{\Sigma}}}_{n}:{n \in {\mathbb{N}}}})$ of empirical covariance estimates. The following uniform confidence region attains confidence level ${1 - \delta} \in {}$:

The ratio $r ≔ {L^{2}/{\|\mathbf{\Sigma}\|}}$ reflects the number of dimensions where the random vector has substantial fluctuation. We need $n = {\mathcal{O}{({r{\log d}})}}$ samples to reliably estimate the covariance in these directions. As the number $n$ of samples continues to increase, the size of confidence region decreases at a rate $\sqrt{n^{- 1}{\log{\log n}}}$. The log-log factor is required to correct for occasional extreme fluctuations. More precise asymptotic results follow from the law of the iterated logarithm in a Banach space \[:Probability-Banach, Thm. 8.2\].

### Proof 6 (Proof sketch)

For a parameter $N \in {\mathbb{N}}$, introduce the finite martingale sequence

The difference sequence $({\mathbf{X}}_{k})$ consists of iid centered random matrices of dimension $d$. A short calculation gives

The matrix Freedman inequality (4.1. ‣ 4.2 Matrix Freedman ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory")) ensures that

Dividing each element ${\mathbf{S}}_{n}$ by the factor $n \cdot {\|\mathbf{\Sigma}\|}$ and limiting the index $n$ to the range $\lbrack{N/2},N\rbrack$, we find

The key insight is to apply the last inequality on dyadic intervals: $N = 2^{j}$ for $j = {1,2,3,\ldots}$ at the level $t_{j} = {\log{({{4j^{2}d}/\delta})}} \leq {2{\log{({{2d{\log{({en})}}}/\delta})}}}$. Combine the results with a union bound, then take the complement.

### Cholesky decomposition with stochastic rounding

Most numerical algorithms proceed in stages, and the numerical errors compound at each step of the process. Traditional analyses model these errors deterministically, and error bounds increase linearly with the number of steps in the algorithm. More recently, researchers have started to make a close accounting of error propagation under probabilistic models, where the errors accumulate more slowly because of cancelations. Martingale methods offer an elegant technique for tracking random errors that depend on the past history of the algorithm. Connolly & Higham \[:Probabilistic-Rounding\] have employed this approach to give a probabilistic analysis of the Householder QR algorithm. In the same spirit, this section offers a stylized analysis of the Cholesky factorization algorithm under a stochastic rounding model (cf. subsection˜3.2).

Let ${\mathbf{A}} \in {{\mathbb{H}}_{d}^{+ +}{({\mathbb{R}})}}$ be a positive-definite matrix. For clarity of interpretation, we assume that ${{diag}{({\mathbf{A}})}} = \mathbf{I}$. Cholesky's method iteratively produces a factorization ${\mathbf{A}} = {{\mathbf{C}}{\mathbf{C}}^{\ast}}$ where ${\mathbf{C}} \in {{\mathbb{M}}_{d}{({\mathbb{R}})}}$ is lower triangular. Define the initial residual ${\mathbf{R}}_{0} ≔ {\mathbf{A}}$ and the initial triangular factor ${\mathbf{C}}_{0} ≔ \mathbf{0}$. At the $k$th step, reduce the residual ${\mathbf{R}}_{k - 1}$ by performing a Schur complement with respect to its $k$th column:

This procedure zeroes out the $k$th row and column from ${\mathbf{R}}_{k - 1}$, while placing ${\mathbf{c}}_{k}$ in the $k$th column of ${\mathbf{C}}_{k}$. The matrix ${\mathbf{C}}_{k}$ remains lower triangular. At each step, the residual and the partial triangular factorization compose the original matrix: ${\mathbf{A}} = {{\mathbf{R}}_{k} + {{\mathbf{C}}_{k}{\mathbf{C}}_{k}^{\ast}}}$. After $d$ steps, ${\mathbf{R}}_{d} = \mathbf{0}$ and ${{\mathbf{C}}_{d}{\mathbf{C}}_{d}^{\ast}} = {\mathbf{A}}$. Each step requires $\mathcal{O}{(d^{2})}$ arithmetic operations, for a total cost of $\mathcal{O}{(d^{3})}$.

In actual practice, we commit floating-point errors when we reduce the residual---but we can extract a column from the residual without further error. If we employ stochastic rounding, then the residual update becomes

The stochastic error ${\mathbf{Y}}_{k}$ is a random symmetric matrix that depends on the previous residual. The sigma-algebra $\mathcal{F}_{k - 1} ≔ {\sigma{({\mathbf{R}}_{0},\ldots,{\mathbf{R}}_{k - 1})}}$ captures the history of the algorithm through step $k - 1$. As in subsection˜3.2, each entry of ${\mathbf{Y}}_{k}$ satisfies the rounding properties in (3.4), conditional on $\mathcal{F}_{k - 1}$, and each entry is rounded independently of the others (modulo symmetry). We frame the assumptions that

The third property follows because ${{diag}{({\mathbf{A}})}} = \mathbf{I}$ and ${diag}{({\mathbf{R}}_{k - 1})}$ only decreases at each step. The second property holds if the computed residual ${\mathbf{R}}_{k - 1}$ remains psd and satisfies ${\|{\mathbf{R}}_{k - 1}\|} \leq {2{\|{\mathbf{A}}\|}}$. Under mild assumptions, these conditions can be justified with some additional effort. We also demand that no underflow or overflow occurs.

The computed residuals ${\mathbf{R}}_{k}$ and the partial triangular factorizations ${\mathbf{C}}_{k}{\mathbf{C}}_{k}^{\ast}$ induce a sequence of approximations of the original matrix:

Using these approximations, we can calculate the error in the completed triangular factorization ${\mathbf{C}} ≔ {\mathbf{C}}_{d}$.

In other words, the sequence of approximations composes a matrix martingale with difference sequence $({{\mathbf{Y}}_{k}:{k = {1,\ldots,d}}})$. We can use this martingale to assess the accumulated rounding error in the Cholesky decomposition.

### Theorem 5.2 (Cholesky decomposition with stochastic rounding)

Let $\mathbf{A} \in {{\mathbb{H}}_{d}^{+ +}{({\mathbb{R}})}}$ be a $d \times d$ positive-definite matrix with ${{diag}{(\mathbf{A})}} = \mathbf{I}$. As described above, compute the Cholesky decomposition $\mathbf{C}\mathbf{C}^{\ast}$ with a stochastic rounding procedure that satisfies the assumption (5.2). The resulting factorization admits the error bound

For the Cholesky decomposition, the classic deterministic rounding error analysis \[:Accuracy-Stability, Chap. 10\] gives a bound for the entrywise error ${\|{{{\mathbf{C}}{\mathbf{C}}^{\ast}} - {\mathbf{A}}}\|}_{\max}$ that is proportional to $\text{u} \cdot d$. For stochastic rounding, the stylized analysis here indicates that the entrywise error is typically on the order of $\text{u} \cdot \sqrt{d{\|{\mathbf{A}}\|}}$. The factor $\sqrt{d}$ improvement can be significant. A full comparison with deterministic rounding falls outside our ambit.

### Proof 7 (Proof sketch)

We need to consider a more fine-grained martingale to exploit the fact that matrix entries are rounded independently. Decompose each error matrix as ${\mathbf{Y}}_{k} = {\sum_{i \leq j}{\mathbf{X}}_{ijk}}$, where ${\mathbf{X}}_{ijk}$ describes the rounding error in the $(i,j)$ and $(j,i)$ entries of ${\mathbf{Y}}_{k}$. For each $k$, the family $({{\mathbf{X}}_{ijk}:{i \leq j}})$ is conditionally independent, given $\mathcal{F}_{k - 1}$. According to (5.2), the parameters in the matrix Freedman inequality (Theorem˜4.4. ‣ 4.2 Matrix Freedman ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory")) satisfy

The result follows from the matrix Freedman inequality (4.1. ‣ 4.2 Matrix Freedman ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory")).

### Fast Laplacian solvers

As in subsection˜3.3, consider a weighted, connected, undirected graph on $n$ vertices with Laplacian matrix ${\mathbf{L}} \in {{\mathbb{H}}_{n}^{+}{({\mathbb{R}})}}$. A linear system in the Laplacian matrix takes the form

This type of linear system arises in a dizzying range of applications, including numerical discretizations of elliptic PDEs, clustering and partitioning of data, and network flow problems \[:Laplacian-Paradigm\]. The basic algorithm for (5.3) starts by computing a Cholesky decomposition ${\mathbf{L}} = {{\mathbf{C}}{\mathbf{C}}^{\ast}}$, and it solves the linear system by two steps of triangular substitution. In general, this approach requires $\mathcal{O}{(n^{3})}$ operations, which is often prohibitive. Can we do better?

Spielman & Teng \[:Nearly-Linear-Time\] gave an affirmative answer by devising a theoretical Laplacian solver that runs in time linear in the number $m$ of edges in the graph and polylogarithmic in the number $n$ of vertices. After a train of refinements, Kyng & Sachdeva \[:Approximate-Gaussian\] designed a *practical* Laplacian solver that runs in time $\mathcal{O}{({m{\log^{3}n}})}$. Their algorithm, SparseCholesky, performs an approximate Cholesky decomposition by randomly sparsifying the Schur complement at each step. The analysis relies on matrix martingales. See \[:Matrix-Concentration-LN\] for another account.

Here is the intuition. When we apply the Cholesky method to a graph Laplacian, each Schur complement step eliminates a vertex from the graph by adding a clique to the remaining vertices of the graph. The method is expensive because the clique involves up to $n - k$ vertices and up to ${({n - k})}^{2}$ edges at step $k$. Yet, as we saw in subsection˜3.3, we can dramatically sparsify a graph by randomly sampling edges in proportion to their effective resistances. In this spirit, SparseCholesky starts with residual ${\mathbf{R}}_{0} ≔ {\mathbf{L}}$ and triangular factor ${\mathbf{C}}_{0} ≔ \mathbf{0}$. It performs the steps

The Sparsify method produces a random, unbiased approximation to the matrix ${\mathbf{c}}_{k}{\mathbf{c}}_{k}^{\ast}$, which contains the Laplacian of the clique. After sparsification, the remaining number of edges equals the number of neighbors of vertex $k$ in the residual graph ${\mathbf{R}}_{k - 1}$. The full algorithm requires several other innovations: it splits edges into smaller pieces to reduce their weights; it maintains estimates for the effective resistances to implement the sparsification step; and it eliminates vertices in a random order to limit the average number of neighbors. As in subsection˜5.2, this procedure results in a matrix martingale, namely ${\mathbf{S}}_{k} ≔ {{\mathbf{R}}_{k} + {{\mathbf{C}}_{k}{\mathbf{C}}_{k}^{\ast}}}$ for $k = {0,1,2,{\ldotsd}}$. We can analyze this martingale using the matrix Freedman inequality (Theorem˜4.4. ‣ 4.2 Matrix Freedman ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory")). Here is the outcome.

### Theorem 5.3 (Sparse Cholesky approximation \[:Approximate-Gaussian\])

Let $\mathbf{L} \in {{\mathbb{H}}_{d}^{+}{({\mathbb{R}})}}$ be a weighted graph Laplacian, as in (3.5). With probability at least $1 - d^{- 1}$, the SparseCholesky algorithm produces an approximate Cholesky factorization $\mathbf{C}\mathbf{C}^{\ast}$ with the spectral guarantee

The lower-triangular matrix $\mathbf{C}$ has $\mathcal{O}{({m{\log^{2}n}})}$ nonzero entries. The expected runtime is $\mathcal{O}{({m{\log^{3}n}})}$ operations.

Once we have computed the approximate Cholesky decomposition ${\mathbf{L}} \approx {{\mathbf{C}}{\mathbf{C}}^{\ast}}$, we can solve the linear system (5.3) using preconditioned conjugate gradient (PCG) with the triangular preconditioner ${\mathbf{C}}^{- 1}$.

### Proposition 5.4 (Fast Laplacian solvers \[:Approximate-Gaussian\])

Given the triangular matrix $\mathbf{C}$ computed by the SparseCholesky algorithm, the PCG algorithm solves the consistent Laplacian system (5.3) to relative error $\varepsilon$ in the Dirichlet energy norm after $\mathcal{O}{({m{\log^{2}{(n)}}{\log{({1/\varepsilon})}}})}$ arithmetic operations.

For a sparse graph with $m = {\mathcal{O}{(n)}}$ edges, the total cost of solving the Laplacian system (5.3) to fixed accuracy is just $\mathcal{O}{({n{\log^{3}n}})}$ operations. For a dense graph with $m = {\mathcal{O}{(n^{2})}}$ edges, the total cost is $\mathcal{O}{({n^{2}{\log^{3}n}})}$ operations. Both results compare favorably with the $\mathcal{O}{(n^{3})}$ cost of the classic method based on a full Cholesky factorization.

### Randomized Trotter formulas

The evolution of a quantum mechanical system is governed by a Hamiltonian matrix ${\mathbf{H}} \in {{\mathbb{H}}_{d}{({\mathbb{C}})}}$. The state of the system at time $t \geq 0$ takes the form

A basic goal of quantum information science is to simulate the action $\mathbf{\Phi}_{t}$ induced by a complicated Hamiltonian through the application of simpler Hamiltonians. Randomized methods can provide effective algorithms for this task. This section summarizes a result of Chen et al. \[:Concentration-Random\] that builds on work of Campbell \[:Random-Compiler\].

Suppose that the Hamiltonian can be expressed as a sum of many "simple" Hermitian terms:

The statistic $L$ measures the interaction strength within the Hamiltonian. This model encompasses applications in quantum chemistry and quantum physics. For clarity, fix the time horizon for the simulation at $t = 1$. Given a parameter $n \in {\mathbb{N}}$, construct a random unitary matrix by drawing a random term from the Hamiltonian according to an importance sampling distribution:

To approximate the unitary matrix ${\mathbf{U}} ≔ e^{- {i{\mathbf{H}}}}$, form a product of $n$ independent copies of $\mathbf{Y}$:

In other words, we simulate the action of the full Hamiltonian $\mathbf{H}$ by performing a series of short simulations with the simpler Hamiltonians ${\mathbf{H}}_{m}$. This is a randomized variant of the Lie--Trotter--Suzuki product formulas that are widely used to approximate the matrix exponential of a sum. We can analyze the quality of the simulation using matrix martingale methods.

### Theorem 5.5 (Random product formulas \[:Concentration-Random, Thm. 1\])

Consider a Hamiltonian of the form (5.4) with interaction strength $L$, and form the unitary matrix $\mathbf{U} ≔ e^{- {i\mathbf{H}}}$. Fix parameters ${\varepsilon,\delta} \in {}$ where $\varepsilon \leq L$. For $n \geq {40\varepsilon^{- 2}L^{2}{\log{({{2d}/\delta})}}}$, construct a random unitary matrix $\mathbf{Q}$ with $n$ factors via the random product formula Eq.˜5.6. Then

This result states that, with high probability, the random product formula (5.6) approximates the evolution of the quantum Hamiltonian for *all* initial states. The number $n$ of factors in the product does not depend on the number $M$ of summands in the Hamiltonian (5.4), but it grows quadratically with the interaction strength $L$. For comparison, the number of factors in a deterministic product formula depends linearly on the number $M$ of summands in the Hamiltonian, but more weakly on the interaction strength $L$. As a consequence, random product formulas are most effective for short-time simulations of Hamiltonians with many summands.

### Proof 8 (Proof sketch)

The quantity of interest depends on the spectral-norm distance between the two unitaries:

This point follows from the triangle inequality, unitary invariance, and the operator ideal property of the trace norm. The right-hand side consists of a random fluctuation term and a deterministic bias:

By statistical independence of the factors in (5.6), the expectation ${{\mathbb{E}}{\lbrack{\mathbf{Q}}\rbrack}} = {({{\mathbb{E}}{\lbrack{\mathbf{Y}}\rbrack}})}^{n}$.

The bias term admits a bound that depends on the interaction strength $L$ of the Hamiltonian:

The first inequality follows from repeated application of the triangle inequality and unitary invariance, while the second inequality requires a second-order approximation of the matrix exponential. See \[:Concentration-Random, Lem. 3.5 and 3.6\] for the details. We insist that ${L^{2}/n} \leq {\varepsilon/2}$ to control the bias term.

For the fluctuation term, we introduce a Lévy--Doob martingale. Let $\mathcal{F}_{k} ≔ {\sigma{({\mathbf{Y}}_{1},\ldots,{\mathbf{Y}}_{k})}}$, and define

Observe that ${\mathbf{S}}_{n} = {\mathbf{Q}}$ and ${\mathbf{S}}_{0} = {{\mathbb{E}}{\lbrack{\mathbf{Q}}\rbrack}}$. Construct the difference sequence ${\mathbf{X}}_{k} ≔ {{\mathbf{S}}_{k} - {\mathbf{S}}_{k - 1}}$ for $k = {1,\ldots,n}$. By first-order approximation of the matrix exponential, the difference sequence satisfies uniform bounds

See \[:Concentration-Random, Prop. 3.3\] for the details. The matrix Freedman inequality (4.2. ‣ 4.2 Matrix Freedman ‣ 4 Concentration for matrix martingales ‣ Applied Random Matrix Theory")) now implies a probability inequality for ${flux} = {\|{{\mathbf{S}}_{n} - {\mathbf{S}}_{0}}\|}$ at level $t = {\varepsilon/2}$. Combine the bias and fluctuation to get a tail bound for the quantity $E$.

## Matrix concentration: Extensions

Over the last few years, researchers have made significant advances in understanding the behavior of the independent sum model. These results require a detour into the study of Gaussian random matrices, which serve as ideal models for independent sums. First, we outline some improvements of matrix concentration for Gaussian random matrices, and then we explain how Gaussian models can capture the spectral features of an independent sum of random matrices. Last, we mention several other random matrix models that remain under active study.

### Variance statistics

We can describe the behavior of random matrix models more fully by employing a broader family of variance statistics. Introduce the real inner product

The variance function of a random matrix ${\mathbf{S}} \in {\mathbb{F}}^{d_{1} \times d_{2}}$ is defined as

Variance functions are in correspondence with psd quadratic forms on ${\mathbb{F}}^{d_{1} \times d_{2}}$, treated as a real linear space.

The variance function ${\mathsf{V}\mathsf{a}\mathsf{r}}{\lbrack{\mathbf{S}}\rbrack}$ packs up all the second-order statistics of the random matrix. In particular, it completely determines the matrix variance $v{({\mathbf{S}})}$, defined in (2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")). We can also introduce the weak variance, which is related to the tail behavior of the sum: ${{v_{\ast}{({\mathbf{S}})}} ≔ {\sup_{{\|{\mathbf{A}}\|}_{1} \leq 1}{{\mathsf{V}\mathsf{a}\mathsf{r}}{\lbrack{\mathbf{S}}\rbrack}{({\mathbf{A}})}}}}.$ The weak variance $v_{\ast}{({\mathbf{S}})}$ is always smaller than the matrix variance $v{({\mathbf{S}})}$, and often much smaller.

### Gaussian matrix models

A random matrix is Gaussian when each of its linear marginals is Gaussian. More precisely, ${\mathbf{Z}} \in {\mathbb{F}}^{d_{1} \times d_{2}}$ is Gaussian if and only if the random variable ${\langle{\mathbf{Z}},{\mathbf{A}}\rangle}_{Re}$ follows a real Gaussian distribution for each matrix ${\mathbf{A}} \in {\mathbb{F}}^{d_{1} \times d_{2}}$. A Gaussian random matrix is fully characterized by its expectation ${\mathbb{E}}{\lbrack{\mathbf{Z}}\rbrack}$ and by its variance function ${\mathsf{V}\mathsf{a}\mathsf{r}}{\lbrack{\mathbf{Z}}\rbrack}$. For a specified expectation matrix ${\mathbf{M}} \in {\mathbb{F}}^{d_{1} \times d_{2}}$ and a variance function $\mathsf{V}:{{\mathbb{F}}^{d_{1} \times d_{2}}\rightarrow{\mathbb{R}}_{+}}$, we denote the (unique) Gaussian distribution with these statistics by $\text{normal}{({\mathbf{M}},\mathsf{V})}$.

### Second-order matrix Khinchin inequalities

The norm of a Gaussian matrix $\mathbf{Z}$ satisfies an elegant matrix concentration bound, called the matrix Khinchin inequality, originating in work of Lust-Piquard \[:Inegalites-Khintchine\]:

The lower bound involves Gaussian isoperimetry \[:Gaussian-Measures, Cor. 3\]; the upper bound relies on exponential matrix concentration arguments \[:Introduction-Matrix, Thm. 4.1.1\]. Both inequalities are saturated.

To improve on the matrix Khinchin inequality (6.2), we need extra information about the variance function of the Gaussian matrix. Define the interaction energy to be twice the maximum eigenvalue of the quadratic form:

The interaction energy $w{({\mathbf{Z}})}$ can be much smaller than the matrix variance $v{({\mathbf{Z}})}$, but they are incomparable. Heuristically, the interaction energy is small when $\mathbf{Z}$ is "highly noncommutative." This statistic supports a second-order refinement of the matrix Khinchin inequality \[:Matrix-Concentration, Cor. 2.2 and Lem. 2.5\]:

When ${w{({\mathbf{Z}})}} \ll {v{({\mathbf{Z}})}}$, then the result (6.3) improves over (6.2). As a simple example, consider a real Ginibre matrix ${\mathbf{G}} \in {{\mathbb{M}}_{d}{({\mathbb{R}})}}$, which is a $d \times d$ matrix with iid standardized Gaussian entries. The matrix variance ${v{({\mathbf{G}})}} = d$, while the interaction energy ${w{({\mathbf{G}})}} = 2$. Thus,

The latter inequality is the stronger one, and its first term is numerically sharp.

Roughly speaking, the logarithmic factor in (6.2) arises when the Hermitian dilations of two independent copies ${\mathcal{H}{({\mathbf{Z}})}},{\mathcal{H}{({\mathbf{Z}}^{\prime})}}$ of the Gaussian matrix "almost commute" with each other, in an appropriate sense. To quantify this insight, inspired by free probability, I introduced a subtle statistic called the matrix alignment \[:Second-Order-Matrix, Def. 3.1\]. For a special class of Gaussian matrices, I also established a preliminary version of the second-order Khinchin inequality \[:Second-Order-Matrix, Thm. 3.1\] that reveals how the matrix alignment arises.

The finished result (6.3) was obtained through additional insights of Bandeira et al. \[:Spectral-Norm,:Matrix-Concentration\]. The latter papers use matrix alignment statistics to compare the spectral norm of a Gaussian matrix with the spectral norm of a free probability model (namely, an operator semicircle) that admits explicit formulas. The role of the interaction energy $w{({\mathbf{Z}})}$ is to provide a computable bound for the matrix alignment \[:Spectral-Norm, Rem. 3.3\]. Similar results hold for other spectral properties, such as the support of the spectrum and the mean singular value distribution.

### Independent sums: Gaussian comparison

Let us return to a more general setting. Consider an independent sum of bounded, centered random matrices with dimension $d_{1} \times d_{2}$:

Let $\text{V} ≔ {\text{Var}{\lbrack{\mathbf{S}}\rbrack}}$ be the variance function of the sum. The multivariate central limit theorem suggests that we should compare $\mathbf{S}$ with the centered Gaussian random matrix ${\mathbf{Z}} \sim {\text{normal}{(\mathbf{0},\text{V})}}$, but it is not clear how to quantify the difference between their distributions.

Under weak assumptions, we can obtain detailed nonasymptotic comparisons for *spectral properties* of the independent sum $\mathbf{S}$ and the Gaussian model $\mathbf{Z}$. Brailovskaya & van Handel \[:Universality-Sharp, Cor. 2.7\] established that

In view of the matrix Khinchin inequality (6.2), the Gaussian matrix satisfies ${{\mathbb{E}}{\|{\mathbf{Z}}\|}} \approx \sqrt{v{({\mathbf{Z}})}} = \sqrt{v{({\mathbf{S}})}}$. The weak variance term $\sqrt{v_{\ast}{({\mathbf{S}})}}$ is often negligible. Therefore, in case $B^{2} \ll {v{({\mathbf{S}})}}$, the discrepancy between the expected norms is much smaller than the expected norm of the Gaussian matrix. In other words, when the bound $B$ on the summands is sufficiently small, we can accurately approximate ${\mathbb{E}}{\|{\mathbf{S}}\|}$ by way of estimates for ${\mathbb{E}}{\|{\mathbf{Z}}\|}$. The second-order matrix Khinchin inequality (6.3) provides one such estimate.

Brailovskaya & van Handel \[:Universality-Sharp\] developed Gaussian comparisons, similar with (6.4), for other spectral statistics of the independent sum, including the support of the spectrum and the mean distribution of the singular values. Their arguments rely on Stein's method, cumulant expansions, Möbius inversion, and a selection of matrix inequalities. My paper \[:Universality-Laws\] offers an alternative proof of their results, based on the method of exchangeable pairs. I recently obtained another type of Gaussian comparison \[:Comparison-Theorems-min,:Comparison-Theorems-max\] for the extreme eigenvalues of an independent sum; the proof exploits a deep result from matrix analysis, called Stahl's theorem \[:Proof-BMV\].

We conclude with a critical observation. For independent sums, the latest matrix concentration results, such as Eqs.˜6.3 and 6.4, offer new insights. Nevertheless, it may be difficult to deploy these inequalities in applications, such as the ones in section˜3, because we often lack fine-grained information about the variance function of the random matrix model. As a consequence, classic matrix concentration tools (e.g., Theorem˜2.1. ‣ 2 The matrix Bernstein inequality ‣ Applied Random Matrix Theory")) and the more recent refinements play complementary roles.

### Other models

While the matrix concentration theory for the independent sum model is rather complete, other types of random matrix models remain mysterious and have continued to attract attention. Citations are limited to a few typical papers, as there is not enough space to do justice to this rich literature.

The nonlinear random matrix model concerns a matrix-valued function of underlying random variables that are usually (but not always) independent. Results for this model include matrix Efron--Stein inequalities \[:Efron-Stein-Inequalities\] and (local) matrix Poincaré inequalities \[:Poincare-Inequalities,:Nonlinear-Matrix\]. There are also specialized results for matrix-valued polynomial chaos \[BLN+25:Matrix-Chaos\]. A related challenge arises from random matrix models with dependencies, such as the sum of fixed matrices modulated by negatively correlated scalar random variables; some recent progress on these questions appears in \[:Scalar-Matrix\]. In addition to matrix martingales, researchers have also treated other types of sequential processes, such as matrix-valued Markov chains; for example, see \[:Concentration-Inequalities\]. Another line of work \[BGJ+25:Tensor-Concentration\] pursues extensions of matrix concentration to random tensors.

Many of the models in the last paragraph emerged from problems in combinatorics and algorithms, and the theoretical results have led to satisfying progress. Thus, research on matrix concentration tools remains active, and it continues to make a profound impact on applications.
