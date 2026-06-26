## Abstract

In contemporary applied and computational mathematics, a frequent challenge is to bound the expectation of the spectral norm of a sum of independent random matrices. This quantity is controlled by the norm of the expected square of the random matrix and the expectation of the maximum squared norm achieved by one of the summands; there is also a weak dependence on the dimension of the random matrix. The purpose of this paper is to give a complete, elementary proof of this important, but underappreciated, inequality.

### Key words and phrases

Probability inequality; random matrix; sum of independent random variables.

### Mathematics Subject Classification

## Motivation

Over the last decade, random matrices have become ubiquitous in applied and computational mathematics. As this trend accelerates, more and more researchers must confront random matrices as part of their work. Classical random matrix theory can be difficult to use, and it is often silent about the questions that come up in modern applications. As a consequence, it has become imperative to develop and disseminate new tools that are easy to use and that apply to a wide range of random matrices.

### Matrix Concentration Inequalities

Matrix concentration inequalities are among the most popular of these new methods. For a random matrix $\mathbf{Z}$ with appropriate structure, these results use simple parameters associated with the random matrix to provide bounds of the form where $\left. \parallel \cdot \parallel \right.$ denotes the spectral norm, also known as the $\ell_{2}$ operator norm. These tools have already found a place in a huge number of mathematical research fields, including numerical linear algebra machine learning \[, LPSS^+^14\] mathematical signal processing computer graphics and vision quantum information theory theory of algorithms \[, CKM^+^14\] and These references are chosen more or less at random from a long menu of possibilities. See the monograph for an overview of the main results on matrix concentration, many detailed applications, and additional background references.

### The Expected Norm

The purpose of this paper is to provide a complete proof of the following important, but underappreciated, theorem. This result is adapted from \[, Thm. A.1\].

### Theorem I (The Expected Norm of an Independent Sum of Random Matrices)

Consider an independent family $\{\mathbf{S}_{1},\ldots,\mathbf{S}_{n}\}$ of random $d_{1} \times d_{2}$ complex-valued matrices with ${{\mathbb{E}}\mathbf{S}_{i}} = \mathbf{0}$ for each index $i$, and define Introduce the matrix variance parameter | | ${v{({\mathbf{Z}})}}:=$ | $\max\left\{ \left\| {{\mathbb{E}}\left\lbrack {{\mathbf{Z}}{\mathbf{Z}}^{\ast}} \right\rbrack} \right\|,\left\| {{\mathbb{E}}\left\lbrack {{\mathbf{Z}}^{\ast}{\mathbf{Z}}} \right\rbrack} \right\| \right\}$ | | (1.2) | | | $=$ | $\max\left\{ \left\| {\sum\limits_{i}{{\mathbb{E}}\left\lbrack {{\mathbf{S}}_{i}{\mathbf{S}}_{i}^{\ast}} \right\rbrack}} \right\|,\left\| {\sum\limits_{i}{{\mathbb{E}}\left\lbrack {{\mathbf{S}}_{i}^{\ast}{\mathbf{S}}_{i}} \right\rbrack}} \right\| \right\}$ | | | and the large deviation parameter Define the dimensional constant Then we have the matching estimates In the lower inequality, we can take $c:={1/4}$. The symbol $\left. \parallel \cdot \parallel \right.$ denotes the $\ell_{2}$ operator norm, also known as the spectral norm, and ^∗^ refers to the conjugate transpose operation. The map $\lceil \cdot \rceil$ returns the smallest integer that exceeds its argument.

The proof of this result occupies the bulk of this paper. Most of the page count is attributed to a detailed presentation of the required background material from linear algebra and probability. We have based the argument on the most elementary considerations possible, and we have tried to make the work self-contained. Once the reader has digested these ideas, the related---but more sophisticated ---approach in the paper \[MJC^+^14\] should be accessible.

### Discussion

Before we continue, some remarks about Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") are in order. First, although it may seem restrictive to focus on independent sums, as in (1.1. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")), this model captures an enormous number of useful examples. See the monograph for justification.

We have chosen the term *variance parameter* because the quantity (1.2. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) is a direct generalization of the variance of a scalar random variable. The passage from the first formula to the second formula in (1.2. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) is an immediate consequence of the assumption that the summands ${\mathbf{S}}_{i}$ are independent and have zero mean (see Section 5). We use the term *large-deviation parameter* because the quantity (1.3. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) reflects the part of the expected norm of the random matrix that is attributable to one of the summands taking an unusually large value. In practice, both parameters are easy to compute using matrix arithmetic and some basic probabilistic considerations.

In applications, it is common that we need high-probability bounds on the norm of a random matrix. Typically, the bigger challenge is to estimate the expectation of the norm, which is what Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") achieves. Once we have a bound for the expectation, we can use scalar concentration inequalities, such as \[, Thm. 6.10\], to obtain high-probability bounds on the deviation between the norm and its mean value.

We have stated Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") as a bound on the second moment of $\left\| {\mathbf{Z}} \right\|$ because this is the most natural form of the result. Equivalent bounds hold for the first moment: We can take $c' = {1/8}$. The upper bound follows easily from (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) and Jensen's inequality. The lower bound requires the Khintchine--Kahane inequality.

Observe that the lower and upper estimates in (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) differ only by the factor $C{({\mathbf{d}})}$. As a consequence, the lower bound has no explicit dimensional dependence, while the upper bound has only a weak dependence on the dimension. Under the assumptions of the theorem, it is not possible to make substantial improvements to either the lower bound or the upper bound. Section 7 provides examples that support this claim.

In the theory of matrix concentration, one of the major challenges is to understand what properties of the random matrix $\mathbf{Z}$ allow us to remove the dimensional factor $C{({\mathbf{d}})}$ from the estimate (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")). This question is largely open, but the recent papers \[ \] make some progress.

### The Uncentered Case

Although Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") concerns a centered random matrix, it can also be used to study a general random matrix. The following result is an immediate corollary of Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach").

### Theorem II

Consider an independent family $\{\mathbf{S}_{1},\ldots,\mathbf{S}_{n}\}$ of random $d_{1} \times d_{2}$ complex-valued matrices, not necessarily centered. Define Introduce the variance parameter and the large-deviation parameter Then we have the matching estimates We can take $c = {1/4}$, and the dimensional constant $C{(\mathbf{d})}$ is defined in (1.4. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")).

Theorem II can also be used to study $\left\| {\mathbf{R}} \right\|$ by combining it with the estimates These bounds follow from the triangle inequality for the spectral norm.

It is productive to interpret Theorem II as a perturbation result because it describes how far the random matrix $\mathbf{R}$ deviates from its mean ${\mathbb{E}}{\mathbf{R}}$. We can derive many useful consequences from a bound of the form This estimate shows that, on average, all of the singular values of $\mathbf{R}$ are close to the corresponding singular values of ${\mathbb{E}}{\mathbf{R}}$. It also implies that, on average, the singular vectors of $\mathbf{R}$ are close to the corresponding singular vectors of ${\mathbb{E}}{\mathbf{R}}$, provided that the associated singular values are isolated. Furthermore, we discover that, on average, each linear functional ${tr}{\lbrack{{\mathbf{C}}{\mathbf{R}}}\rbrack}$ is uniformly close to ${\mathbb{E}}{{tr}{\lbrack{{\mathbf{C}}{\mathbf{R}}}\rbrack}}$ for each fixed matrix ${\mathbf{C}} \in {\mathbb{M}}^{d_{2} \times d_{1}}$ with bounded Schatten $1$-norm $\left\| {\mathbf{C}} \right\|_{S_{1}} \leq 1$.

### History

Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") is not new. A somewhat weaker version of the upper bound appeared in Rudelson's work \[, Thm. 1\]; see also \[, Thm. 3.1\] and \[, Sec. 9\]. The first explicit statement of the upper bound appeared in \[, Thm. A.1\]. All of these results depend on the noncommutative Khintchine inequality \[ \]. In our approach, the main innovation is a particularly easy proof of a Khintchine-type inequality for matrices, patterned after \[MJC^+^14, Cor 7.3\] and \[, Thm. 8.1\].

The ideas behind the proof of the lower bound in Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") are older. This estimate depends on generic considerations about the behavior of a sum of independent random variables in a Banach space. These techniques are explained in detail in \[, Ch. 6\]. Our presentation expands on a proof sketch that appears in the monograph \[, Secs. 5.1.2 and 6.1.2\].

### Target Audience

This paper is intended for students and researchers who want to develop a detailed understanding of the foundations of matrix concentration. The preparation required is modest.

Basic Convexity. Some simple ideas from convexity play a role, notably the concept of a convex function and Jensen's inequality.

Intermediate Linear Algebra. The requirements from linear algebra are more substantial. The reader should be familiar with the spectral theorem for Hermitian (or symmetric) matrices, Rayleigh's variational principle, the trace of a matrix, and the spectral norm. The paper includes reminders about this material. The paper elaborates on some less familiar ideas, including inequalities for the trace and the spectral norm.

Intermediate Probability. The paper demands some comfort with probability. The most important concepts are expectation and the elementary theory of conditional expectation. We develop the other key ideas, including the notion of symmetrization.

Although many readers will find the background material unnecessary, it is hard to locate these ideas in one place and we prefer to make the paper self-contained. In any case, we provide detailed cross-references so that the reader may dive into the proofs of the main results without wading through the shallower part of the paper.

### Roadmap

Section 2 and Section 3 contain the background material from linear algebra and probability. To prove the upper bound in Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), the key step is to establish the result for the special case of a sum of fixed matrices, each modulated by a random sign. This result appears in Section 4. In Section 5, we exploit this result to obtain the upper bound in (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")). In Section 6, we present the easier proof of the lower bound in (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")). Finally, Section 7 shows that it is not possible to improve (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) substantially.

## Linear Algebra Background

Our aim is to make this paper as accessible as possible. To that end, this section presents some background material from linear algebra. Good references include \[ \]. We also assume some familiarity with basic ideas from the theory of convexity, which may be found in the books \[ \].

### Convexity

Let $V$ be a finite-dimensional linear space. A subset $E \subset V$ is *convex* when Let $E$ be a convex subset of a linear space $V$. A function $f:{E\rightarrow{\mathbb{R}}}$ is *convex* if We say that $f$ is *concave* when $- f$ is convex.

### Vector Basics

Let ${\mathbb{C}}^{d}$ be the complex linear space of $d$-dimensional complex vectors, equipped with the usual componentwise addition and scalar multiplication. The $\ell_{2}$ norm $\left. \parallel \cdot \parallel \right.$ is defined on ${\mathbb{C}}^{d}$ via the expression The symbol ^∗^ denotes the conjugate transpose of a vector. Recall that the $\ell_{2}$ norm is a convex function.

A family ${\{{\mathbf{u}}_{1},\ldots,{\mathbf{u}}_{d}\}} \subset {\mathbb{C}}^{d}$ is called an *orthonormal basis* if it satisfies the relations The orthonormal basis also has the property where $\mathbf{I}_{d}$ is the $d \times d$ identity matrix.

### Matrix Basics

A *matrix* is a rectangular array of complex numbers. Addition and multiplication by a complex scalar are defined componentwise, and we can multiply two matrices with compatible dimensions. We write ${\mathbb{M}}^{d_{1} \times d_{2}}$ for the complex linear space of $d_{1} \times d_{2}$ matrices. The symbol ^∗^ also refers to the conjugate transpose operation on matrices.

A square matrix $\mathbf{H}$ is *Hermitian* when ${\mathbf{H}} = {\mathbf{H}}^{\ast}$. Hermitian matrices are sometimes called *conjugate symmetric*. We introduce the set of $d \times d$ Hermitian matrices: Note that the set ${\mathbb{H}}_{d}$ is a linear space over the real field.

An Hermitian matrix ${\mathbf{A}} \in {\mathbb{H}}_{d}$ is *positive semidefinite* when It is convenient to use the notation ${\mathbf{A}} \preccurlyeq {\mathbf{H}}$ to mean that ${\mathbf{H}} - {\mathbf{A}}$ is positive semidefinite. In particular, the relation $\mathbf{0} \preccurlyeq {\mathbf{H}}$ is equivalent to $\mathbf{H}$ being positive semidefinite. Observe that In other words, addition and nonnegative scaling preserve the positive-semidefinite property.

For every matrix $\mathbf{B}$, both of its squares ${\mathbf{B}}{\mathbf{B}}^{\ast}$ and ${\mathbf{B}}^{\ast}{\mathbf{B}}$ are Hermitian and positive semidefinite.

### Basic Spectral Theory

Each Hermitian matrix ${\mathbf{H}} \in {\mathbb{H}}_{d}$ can be expressed in the form where the $\lambda_{i}$ are uniquely determined real numbers, called *eigenvalues*, and $\{{\mathbf{u}}_{i}\}$ is an orthonormal basis for ${\mathbb{C}}^{d}$. The representation (2.2) is called an *eigenvalue decomposition*.

An Hermitian matrix $\mathbf{H}$ is positive semidefinite if and only if its eigenvalues $\lambda_{i}$ are all nonnegative. Indeed, using the eigenvalue decomposition (2.2), we see that To verify the forward direction, select ${\mathbf{u}} = {\mathbf{u}}_{j}$ for each index $j$. The reverse direction should be obvious.

We define a *monomial* function of an Hermitian matrix ${\mathbf{H}} \in {\mathbb{H}}_{d}$ by repeated multiplication: For each nonnegative integer $r$, it is not hard to check that In particular, ${\mathbf{H}}^{2p}$ is positive semidefinite for each nonnegative integer $p$.

### Rayleigh's Variational Principle

The *Rayleigh principle* is an attractive expression for the maximum eigenvalue $\lambda_{\max}{({\mathbf{H}})}$ of an Hermitian matrix ${\mathbf{H}} \in {\mathbb{H}}_{d}$. This result states that The maximum takes place over all unit-norm vectors ${\mathbf{u}} \in {\mathbb{C}}^{d}$. The identity (2.4) follows from the Lagrange multiplier theorem and the existence of the eigenvalue decomposition (2.2). Similarly, the minimum eigenvalue $\lambda_{\min}{({\mathbf{H}})}$ satisfies We can obtain (2.5) by applying (2.4) to $- {\mathbf{H}}$.

Rayleigh's principle implies that order relations for positive-semidefinite matrices lead to order relations for their eigenvalues.

### Fact 2.1 (Monotonicity)

Let ${\mathbf{A},\mathbf{H}} \in {\mathbb{H}}_{d}$ be Hermitian matrices. Then

### Proof

The condition ${\mathbf{A}} \preccurlyeq {\mathbf{H}}$ implies that the eigenvalues of ${\mathbf{H}} - {\mathbf{A}}$ are nonnegative. Therefore, Rayleigh's principle (2.5) yields for any unit-norm vector $\mathbf{v}$. Select a unit-norm vector $\mathbf{v}$ for which ${\lambda_{\max}{({\mathbf{A}})}} = {{\mathbf{v}}^{\ast}{\mathbf{A}}{\mathbf{v}}}$, and then rearrange: The last relation is Rayleigh's principle (2.4). ∎

### The Trace

The *trace* of a square matrix ${\mathbf{B}} \in {\mathbb{M}}^{d \times d}$ is defined as It is clear that the trace is a linear functional on ${\mathbb{M}}^{d \times d}$. By direct calculation, one may verify that This property is called the *cyclicity* of the trace.

The trace of an Hermitian matrix ${\mathbf{H}} \in {\mathbb{H}}_{d}$ can also be expressed in terms of its eigenvalues: This formula follows when we introduce the eigenvalue decomposition (2.2) into (2.6). Then we invoke the linearity and the cyclicity properties of the trace, as well as the properties of an orthonormal basis. We also instate the convention that monomials bind before the trace: ${{tr}{\mathbf{H}}^{r}}:={{tr}{\lbrack{\mathbf{H}}^{r}\rbrack}}$ for each nonnegative integer $r$.

### The Spectral Norm

The *spectral norm* of a matrix ${\mathbf{B}} \in {\mathbb{M}}^{d_{1} \times d_{2}}$ is defined as The maximum takes place over unit-norm vectors ${\mathbf{u}} \in {\mathbb{C}}^{d_{2}}$. We have the important identity Furthermore, the spectral norm is a convex function, and it satisfies the triangle inequality.

For an Hermitian matrix, the spectral norm can be written in terms of the eigenvalues: This discussion implies that Use the relations (2.3) and (2.9) to verify this fact.

### Some Spectral Norm Inequalities

We need some basic inequalities for the spectral norm. First, note that This point follows from (2.10) and (2.7) because the eigenvalues of a positive-semidefinite matrix are nonnegative.

The next result uses the spectral norm to bound the trace of a product.

### Fact 2.2 (Bound for the Trace of a Product)

Consider Hermitian matrices ${\mathbf{A},\mathbf{H}} \in {\mathbb{H}}_{d}$, and assume that $\mathbf{A}$ is positive semidefinite. Then

### Proof

Introducing the eigenvalue decomposition ${\mathbf{A}} = {\sum_{i}{\lambda_{i}{\mathbf{u}}_{i}{\mathbf{u}}_{i}^{\ast}}}$, we see that The first two relations follow from linearity and cyclicity of the trace. The first inequality depends on Rayleigh's principle (2.4) and the nonnegativity of the eigenvalues $\lambda_{i}$. The last bound follows from (2.9). ∎ We also need a bound for the norm of a sum of squared positive-semidefinite matrices.

### Fact 2.3 (Bound for a Sum of Squares)

Consider positive-semidefinite matrices ${\mathbf{A}_{1},\ldots,\mathbf{A}_{n}} \in {\mathbb{H}}_{d}$. Then

### Proof

Let $\mathbf{A}$ be positive semidefinite. We claim that Indeed, introducing the eigenvalue decomposition ${\mathbf{A}} = {\sum_{i}{\lambda_{i}{\mathbf{u}}_{i}{\mathbf{u}}_{i}^{\ast}}}$, we find that The first relation uses (2.3). Since $0 \leq \lambda_{i} \leq M$, the scalar coefficients in the sum are nonnegative. Therefore, the matrix ${M \cdot {\mathbf{A}}} - {\mathbf{A}}^{2}$ is positive semidefinite, which is what we needed to show.

Select $M:={{\max_{i}\lambda_{\max}}{({\mathbf{A}}_{i})}}$. The inequality (2.13) ensures that Summing these relations, we see that The monotonicity principle, Fact 2.1. ‣ 2.5. Rayleigh’s Variational Principle ‣ 2. Linear Algebra Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), yields the inequality We have used the fact that the maximum eigenvalue of an Hermitian matrix is positive homogeneous. Finally, recall that, per (2.10), the spectral norm of a positive-semidefinite matrix equals its maximum eigenvalue. ∎

### GM--AM Inequality for the Trace

We require another substantial matrix inequality, which is one (of several) matrix analogs of the inequality between the geometric mean and the arithmetic mean.

### Fact 2.4 (GM--AM Trace Inequality)

Consider Hermitian matrices ${\mathbf{H},\mathbf{W},\mathbf{Y}} \in {\mathbb{H}}_{d}$. For each nonnegative integer $r$ and each integer $q$ in the range $0 \leq q \leq {2r}$,

### Proof

The result (2.14. ‣ 2.9. GM–AM Inequality for the Trace ‣ 2. Linear Algebra Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) is a matrix version of the following numerical inequality. For ${\lambda,\mu} \geq 0$, To verify this bound, we may assume that ${\lambda,\mu} > 0$ because it is trivial to check when either $\lambda$ or $\mu$ equals zero. Notice that the left-hand side of the bound is a convex function of $\theta$ on the interval $\lbrack 0,1\rbrack$. This point follows easily from the representation The value of the convex function $f$ on the interval $\lbrack 0,1\rbrack$ is controlled by the maximum value it achieves at one of the endpoints: This inequality coincides with (2.15).

To prove (2.14. ‣ 2.9. GM–AM Inequality for the Trace ‣ 2. Linear Algebra Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) from (2.15), we use eigenvalue decompositions. The case $r = 0$ is immediate, so we may assume that $r \geq 1$. Let $q$ be an integer in the range $0 \leq q \leq {2r}$. Introduce eigenvalue decompositions: | | ${tr}\left\lbrack {{\mathbf{H}}{\mathbf{W}}^{q}{\mathbf{H}}{\mathbf{Y}}^{{2r} - q}} \right\rbrack$ | $= {{tr}\left\lbrack {{\mathbf{H}}\left({\sum\limits_{i = 1}^{d}{\lambda_{i}^{q}{\mathbf{u}}_{i}{\mathbf{u}}_{i}^{\ast}}} \right){\mathbf{H}}\left({\sum\limits_{j = 1}^{d}{\mu_{j}^{{2r} - q}{\mathbf{v}}_{j}{\mathbf{v}}_{j}^{\ast}}} \right)} \right\rbrack}$ | | (2.16) | | | | $= {\sum\limits_{{i,j} = 1}^{d}{{\lambda_{i}^{q}\mu_{j}^{{2r} - q}} \cdot {{tr}\left\lbrack {{\mathbf{H}}{\mathbf{u}}_{i}{\mathbf{u}}_{i}^{\ast}{\mathbf{H}}{\mathbf{v}}_{j}{\mathbf{v}}_{j}^{\ast}} \right\rbrack}}}$ | | | | | | ${\leq {\sum\limits_{{i,j} = 1}^{d}{{\left| \lambda_{i} \right|^{q}\left| \mu_{j} \right|^{{2r} - q}} \cdot \left| {{\mathbf{u}}_{i}^{\ast}{\mathbf{H}}{\mathbf{v}}_{j}} \right|^{2}}}}.$ | | | The first identity relies on the formula (2.3) for the eigenvalue decomposition of a monomial. The second step depends on the linearity of the trace. In the last line, we rewrite the trace using cyclicity, and the inequality emerges when we apply absolute values. The representation $\left| {{\mathbf{u}}_{i}^{\ast}{\mathbf{H}}{\mathbf{v}}_{j}} \right|^{2}$ emphasizes that this quantity is nonnegative, which we use to justify several inequalities.

Invoking the inequality (2.16) twice, we arrive at the bound | | ${{tr}\left\lbrack {{\mathbf{H}}{\mathbf{W}}^{q}{\mathbf{H}}{\mathbf{Y}}^{{2r} - q}} \right\rbrack} + {{tr}\left\lbrack {{\mathbf{H}}{\mathbf{W}}^{{2r} - q}{\mathbf{H}}{\mathbf{Y}}^{q}} \right\rbrack}$ | $\leq {\sum\limits_{{i,j} = 1}^{d}{\left({{\left| \lambda_{i} \right|^{q}\left| \mu_{j} \right|^{{2r} - q}} + {\left| \lambda_{i} \right|^{{2r} - q}\left| \mu_{j} \right|^{q}}} \right) \cdot \left| {{\mathbf{u}}_{i}^{\ast}{\mathbf{H}}{\mathbf{v}}_{j}} \right|^{2}}}$ | | (2.17) | | | | ${\leq {\sum\limits_{{i,j} = 1}^{d}{\left({\lambda_{i}^{2r} + \mu_{j}^{2r}} \right) \cdot \left| {{\mathbf{u}}_{i}^{\ast}{\mathbf{H}}{\mathbf{v}}_{j}} \right|^{2}}}}.$ | | | The second inequality is (2.15), with $\theta = {q/{({2r})}}$ and $\lambda = \lambda_{i}^{2r}$ and $\mu = \mu_{j}^{2r}$.

It remains to rewrite the right-hand side of (2.17) a more recognizable form. To that end, observe that In the first step, we return the squared magnitude to its representation as a trace. Then we use linearity to draw the sums back inside the trace. Next, invoke (2.3) to identify the powers ${\mathbf{W}}^{2r}$ and ${\mathbf{Y}}^{0} = \mathbf{I}_{d}$ and ${\mathbf{W}}^{0} = \mathbf{I}_{d}$ and ${\mathbf{Y}}^{2r}$. Last, use the cyclicity of the trace to combine the factors of $\mathbf{H}$. The result (2.14. ‣ 2.9. GM–AM Inequality for the Trace ‣ 2. Linear Algebra Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) follows from the linearity of the trace. ∎

### Remark 2.5 (The Power of Abstraction)

There is a cleaner, but more abstract, proof of the inequality (2.14. ‣ 2.9. GM–AM Inequality for the Trace ‣ 2. Linear Algebra Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")). Consider the left- and right-multiplication operators Observe that powers of $\mathsf{W}$ and $\mathsf{Y}$ correspond to left- and right-multiplication by powers of $\mathbf{W}$ and $\mathbf{Y}$. Now, the operators $\mathsf{W}$ and $\mathsf{Y}$ commute, so there is a basis (orthonormal with respect to the trace inner product) for ${\mathbb{H}}_{d}$ in which they are simultaneously diagonalizable. Representing the operators in this basis, we can use (2.15) to check that Now, calculate that We omit the details.

### The Hermitian Dilation

Last, we introduce the *Hermitian dilation* $\mathcal{H}{({\mathbf{B}})}$ of a rectangular matrix ${\mathbf{B}} \in {\mathbb{M}}^{d_{1} \times d_{2}}$. This is the Hermitian matrix Note that the map $\mathcal{H}$ is real linear. By direct calculation, We also have the spectral-norm identity To verify (2.20), calculate that The first identity is (2.11); the second is (2.19). The norm of a block-diagonal Hermitian matrix is the maximum spectral norm of a block, which follows from the Rayleigh principle (2.4) with a bit of work. Finally, invoke the property (2.8).

## Probability Background

This section contains some background material from the field of probability. Good references include the books \[ \].

### Expectation

The symbol $\mathbb{E}$ denotes the expectation operator. We will not define expectation formally or spend any energy on technical details. No issues arise if we assume, for example, that all random variables are bounded.

We use brackets to enclose the argument of the expectation when it is important for clarity, and we instate the convention that nonlinear functions bind before expectation. For instance, ${{\mathbb{E}}X^{p}}:={{\mathbb{E}}{\lbrack X^{p}\rbrack}}$ and ${{\mathbb{E}}{\max_{i}X_{i}}}:={{\mathbb{E}}{\lbrack{\max_{i}X_{i}}\rbrack}}$.

Sometimes, we add a subscript to indicate a partial expectation. For example, if $J$ is a random variable, ${\mathbb{E}}_{J}$ refers to the average over $J$, with all other random variables fixed. We only use this notation when $J$ is independent from the other random variables, so there are no complications. In particular, we can compute iterated expectations: ${{\mathbb{E}}{\lbrack{{\mathbb{E}}_{J}{\lbrack \cdot \rbrack}}\rbrack}} = {{\mathbb{E}}{\lbrack \cdot \rbrack}}$ whenever all the expectations are finite.

### Random Matrices

A *random matrix* is a matrix whose entries are complex random variables, not necessarily independent. We compute the expectation of a random matrix $\mathbf{Z}$ componentwise: As in the scalar case, if $\mathbf{W}$ and $\mathbf{Z}$ are independent, Since the expectation is linear, it also commutes with all of the simple linear operations we perform on matrices.

It suffices to take a naïve view of independence, expectation, and so forth. For the technically inclined, let $(\Omega,\mathcal{F},{\mathbb{P}})$ be a probability space. A $d_{1} \times d_{2}$ random matrix $\mathbf{Z}$ is simply a measurable function A family $\{{\mathbf{Z}}_{i}:{i = {1,\ldots,n}}\}$ of random matrices is independent when for any collection of Borel^11^1Open sets in ${\mathbb{M}}^{d_{1} \times d_{2}}$ are defined with respect to the metric topology induced by the spectral norm. subsets $E_{i} \subset {\mathbb{M}}^{d_{1} \times d_{2}}$.

### Inequalities for Expectation

We need several basic inequalities for expectation. We set these out for future reference. Let $X,Y$ be (arbitrary) real random variables. The Cauchy--Schwarz inequality states that For $r \geq 1$, the triangle inequality states that Each of these inequalities is vacuous precisely when its right-hand side is infinite.

Jensen's inequality describes how expectation interacts with a convex or concave function; cf. (2.1). Let $X$ be a random variable taking values in a finite-dimensional linear space $V$, and let $f:{V\rightarrow{\mathbb{R}}}$ be a function. Then | | $f{({{\mathbb{E}}X})}$ | $\leq {{{{\mathbb{E}}f}{(X)}}\quad{\text{when~}f\text{~is convex, and}}}$ | | (3.3) | | | ${{\mathbb{E}}f}{(X)}$ | $\leq {{f{({{\mathbb{E}}X})}}\quad{\text{when~}f\text{~is concave.}}}$ | | | The inequalities (3.3) also hold when we replace $\mathbb{E}$ with a partial expectation. Let us emphasize that these bounds do require that all of the expectations exist.

### Symmetrization

Symmetrization is an important technique for studying the expectation of a function of independent random variables. The idea is to inject auxiliary randomness into the function. Then we condition on the original random variables and average with respect to the extra randomness. When the auxiliary random variables are more pliable, this approach can lead to significant simplifications.

A *Rademacher* random variable $\varepsilon$ takes the two values $\pm 1$ with equal probability. The following result shows how we can use Rademacher random variables to study a sum of independent random matrices.

### Fact 3.1 (Symmetrization)

Let ${\mathbf{S}_{1},\ldots,\mathbf{S}_{n}} \in {\mathbb{M}}^{d_{1} \times d_{2}}$ be independent random matrices. Let $\varepsilon_{1},\ldots,\varepsilon_{n}$ be independent Rademacher random variables that are also independent from the random matrices. For each $r \geq 1$, This result holds whenever ${{\mathbb{E}}\left\| \mathbf{S}_{i} \right\|^{r}} < \infty$ for each index $i$.

### Proof

For notational simplicity, assume that $r = 1$. We discuss the general case at the end of the argument.

Let $\{{\mathbf{S}}_{i}':{i = {1,\ldots,n}}\}$ be an independent copy of the sequence $\{{\mathbf{S}}_{i}:{i = {1,\ldots,n}}\}$, and let ${\mathbb{E}}'$ denote partial expectation with respect to the independent copy. Then The first identity holds because ${{\mathbb{E}}'{\mathbf{S}}_{i}'} = {{\mathbb{E}}{\mathbf{S}}_{i}}$ by identical distribution. Since the spectral norm is convex, we can apply Jensen's inequality (3.3) conditionally to draw out the partial expectation ${\mathbb{E}}'$. Last, we combine the iterated expectation into a single expectation.

Observe that ${\mathbf{S}}_{i} - {\mathbf{S}}_{i}'$ has the same distribution as its negation ${\mathbf{S}}_{i}' - {\mathbf{S}}_{i}$. It follows that the independent sequence $\{{\varepsilon_{i}{({{\mathbf{S}}_{i} - {\mathbf{S}}_{i}'})}}:{i = {1,\ldots,n}}\}$ has the same distribution as $\{{{\mathbf{S}}_{i} - {\mathbf{S}}_{i}'}:{i = {1,\ldots,n}}\}$. Therefore, the expectation of any nonnegative function takes the same value for both sequences. In particular, The second step is the triangle inequality, and the last line follows from the identical distribution of $\{{\varepsilon_{i}{\mathbf{S}}_{i}}\}$ and $\{{- {\varepsilon_{i}{\mathbf{S}}_{i}'}}\}$. Combine the last two displays to obtain the upper bound.

To obtain results for $r > 1$, we pursue the same approach. We require the additional observation that $\left. \parallel \cdot \parallel{}_{r} \right.$ is a convex function, and we also need to invoke the triangle inequality (3.2). Finally, we remark that the lower bound follows from a similar procedure, so we omit the demonstration. ∎

## The Expected Norm of a Matrix Rademacher Series

To prove Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), our overall strategy is to use symmetrization. This approach allows us to reduce the study of an independent sum of random matrices to the study of a sum of fixed matrices modulated by independent Rademacher random variables. This type of random matrix is called a *matrix Rademacher series*. In this section, we establish a bound on the spectral norm of a matrix Rademacher series. This is the key technical step in the proof of Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach").

### Theorem 4.1 (Matrix Rademacher Series)

Let $\mathbf{H}_{1},\ldots,\mathbf{H}_{n}$ be fixed Hermitian matrices with dimension $d$. Let $\varepsilon_{1},\ldots,\varepsilon_{n}$ be independent Rademacher random variables. Then The proof of Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") occupies the bulk of this section, beginning with Section 4.2. The argument is really just a fancy version of the familiar calculation of the moments of a centered standard normal random variable; see Section 4.8 for details.

### Discussion

Before we establish Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), let us make a few comments. First, it is helpful to interpret the result in the same language we have used to state Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"). Introduce the matrix Rademacher series Compute the matrix variance, defined in (1.2. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")): We may rewrite Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") as the statement that In other words, Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") is a sharper version of Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") for the special case of a matrix Rademacher series.

Next, we have focused on bounding the second moment of $\left\| {\mathbf{X}} \right\|$ because this is the most natural form of the result. Note that we also control the first moment because of Jensen's inequality (3.3): A simple variant on the proof of Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") provides bounds for higher moments.

Third, the dimensional factor on the right-hand side of (4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) is asymptotically sharp. Indeed, let us write $K{(d)}$ for the minimum possible constant in the inequality The example in Section 7.1 shows that In other words, (4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) cannot be improved without making further assumptions.

Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") is a variant on the noncommutative Khintchine inequality, first established by Lust-Piquard and later improved by Pisier and by Buchholz. The noncommutative Khintchine inequality gives bounds for the Schatten norm of a matrix Rademacher series, rather than for the spectral norm. Rudelson pointed out that the noncommutative Khintchine inequality also implies bounds for the spectral norm of a matrix Rademacher series. In our presentation, we choose to control the spectral norm directly.

### The Spectral Norm and the Trace Moments

To begin the proof of Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), we introduce the random Hermitian matrix Our goal is to bound the expected spectral norm of $\mathbf{X}$. We may proceed by estimating the expected trace of a power of the random matrix, which is known as a *trace moment*. Fix a nonnegative integer $p$. Observe that The first identity is Jensen's inequality (3.3), applied to the concave function $t\mapsto t^{1/p}$. The second relation is (2.11). The final inequality is the bound (2.12) on the norm of the positive-semidefinite matrix ${\mathbf{X}}^{2p}$ by its trace.

### Remark 4.2 (Higher Moments)

It should be clear that we can also bound expected powers of the spectral norm using the same technique. For simplicity, we omit this development.

### Summation by Parts

To study the trace moments of the random matrix $\mathbf{X}$, we rely on a discrete analog of integration by parts. This approach is clearer if we introduce some more notation. For each index $i$, define the random matrices In other words, the distribution of ${\mathbf{X}}_{\varepsilon_{i}i}$ is the conditional distribution of the random matrix $\mathbf{X}$ given the value $\varepsilon_{i}$ of the $i$th Rademacher variable. This interpretation depends on the assumption that the Rademacher variables are independent.

Beginning with the trace moment, observe that | | ${\mathbb{E}}{{tr}{\mathbf{X}}^{2p}}$ | $= {{\mathbb{E}}{{tr}\left\lbrack {{\mathbf{X}} \cdot {\mathbf{X}}^{{2p} - 1}} \right\rbrack}}$ | | (4.5) | | | | $= {\sum\limits_{i = 1}^{n}{{\mathbb{E}}\left\lbrack {{\mathbb{E}}_{\varepsilon_{i}}{{tr}\left\lbrack {{\varepsilon_{i}{\mathbf{H}}_{i}} \cdot {\mathbf{X}}^{{2p} - 1}} \right\rbrack}} \right\rbrack}}$ | | | | | | $= {\frac{1}{2}{\sum\limits_{i = 1}^{n}{{\mathbb{E}}{{tr}\left\lbrack {{\mathbf{H}}_{i} \cdot \left({{\mathbf{X}}_{+ i}^{{2p} - 1} - {\mathbf{X}}_{- i}^{{2p} - 1}} \right)} \right\rbrack}}}}$ | | | In the second step, we simply write out the definition (4.3) of the random matrix $\mathbf{X}$ and use the linearity of the trace to draw out the sum. Then we write the expectation as an iterated expectation. To reach the next line, write out the partial expectation using the notation ${\mathbf{X}}_{\pm i}$ and the linearity of the trace.

### Difference of Powers

Next, let us apply an algebraic identity to reduce the difference of powers in (4.5). For matrices ${{\mathbf{W}},{\mathbf{Y}}} \in {\mathbb{H}}_{d}$, it holds that To check this expression, just expand the matrix products and notice that the sum telescopes.

Introducing the relation (4.6) with ${\mathbf{W}} = {\mathbf{X}}_{+ i}$ and ${\mathbf{Y}} = {\mathbf{X}}_{- i}$ into the formula (4.5), we find that | | ${\mathbb{E}}{{tr}{\mathbf{X}}^{2p}}$ | $= {\frac{1}{2}{\sum\limits_{i = 1}^{n}{{\mathbb{E}}{{tr}\left\lbrack {{\mathbf{H}}_{i} \cdot {\sum\limits_{q = 0}^{{2p} - 2}{{\mathbf{X}}_{+ i}^{q}\left({{\mathbf{X}}_{+ i} - {\mathbf{X}}_{- i}} \right){\mathbf{X}}_{- i}^{{2p} - 2 - q}}}} \right\rbrack}}}}$ | | (4.7) | | | | ${= {\sum\limits_{i = 1}^{n}{\sum\limits_{q = 0}^{{2p} - 2}{{\mathbb{E}}{{tr}\left\lbrack {{\mathbf{H}}_{i}{\mathbf{X}}_{+ i}^{q}{\mathbf{H}}_{i}{\mathbf{X}}_{- i}^{{2p} - 2 - q}} \right\rbrack}}}}}.$ | | | Linearity of the trace allows us to draw out the sum over $q$, and we have used the observation that ${{\mathbf{X}}_{+ i} - {\mathbf{X}}_{- i}} = {2{\mathbf{H}}_{i}}$.

### Bound for the Trace Moments

We are now in a position to obtain a bound for the trace moments of $\mathbf{X}$. Beginning with (4.7), we compute that | | ${\mathbb{E}}{{tr}{\mathbf{X}}^{2p}}$ | $= {\sum\limits_{i = 1}^{n}{\sum\limits_{q = 0}^{{2p} - 2}{{\mathbb{E}}{{tr}\left\lbrack {{\mathbf{H}}_{i}{\mathbf{X}}_{+ i}^{q}{\mathbf{H}}_{i}{\mathbf{X}}_{- i}^{{2p} - 2 - q}} \right\rbrack}}}}$ | | (4.8) | | | | $\leq {\sum\limits_{i = 1}^{n}{\frac{{2p} - 1}{2}{{\mathbb{E}}{{tr}\left\lbrack {{\mathbf{H}}_{i}^{2} \cdot \left({{\mathbf{X}}_{+ i}^{{2p} - 2} + {\mathbf{X}}_{- i}^{{2p} - 2}} \right)} \right\rbrack}}}}$ | | | | | | $= {{({{2p} - 1})} \cdot {\sum\limits_{i = 1}^{n}{{\mathbb{E}}{{tr}\left\lbrack {{\mathbf{H}}_{i}^{2} \cdot \left({{\mathbb{E}}_{\varepsilon_{i}}{\mathbf{X}}^{{2p} - 2}} \right)} \right\rbrack}}}}$ | | | | | | $= {{({{2p} - 1})} \cdot {{\mathbb{E}}{{tr}\left\lbrack {\left({\sum\limits_{i = 1}^{n}{\mathbf{H}}_{i}^{2}} \right) \cdot {\mathbf{X}}^{{2p} - 2}} \right\rbrack}}}$ | | | | | | ${\leq {{({{2p} - 1})} \cdot \left\| {\sum\limits_{i = 1}^{n}{\mathbf{H}}_{i}^{2}} \right\| \cdot {{\mathbb{E}}{{tr}{\mathbf{X}}^{{2p} - 2}}}}}.$ | | | The bound in the second line is the trace GM--AM inequality, Fact 2.4. ‣ 2.9. GM–AM Inequality for the Trace ‣ 2. Linear Algebra Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), with $r = {p - 1}$ and ${\mathbf{W}} = {\mathbf{X}}_{+ i}$ and ${\mathbf{Y}} = {\mathbf{X}}_{- i}$. To reach the third line, observe that the parenthesis in the second line is twice the partial expectation of ${\mathbf{X}}^{{2p} - 2}$ with respect to $\varepsilon_{i}$. Afterward, we use linearity of the expectation and the trace to draw in the sum over $i$, and then we combine the expectations. Last, invoke the trace inequality from Fact 2.2. ‣ 2.8. Some Spectral Norm Inequalities ‣ 2. Linear Algebra Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach").

### Iteration and the Spectral Norm Bound

The expression (4.8) shows that the trace moment is controlled by a trace moment with a smaller power: Iterating this bound $p$ times, we arrive at the result | | ${\mathbb{E}}{{tr}{\mathbf{X}}^{2p}}$ | $\leq {{{({{2p} - 1})}!!} \cdot \left\| {\sum\limits_{i = 1}^{n}{\mathbf{H}}_{i}^{2}} \right\|^{p} \cdot {{tr}{\mathbf{X}}^{0}}}$ | | (4.9) | The expression (4.4) shows that we can control the expected spectral norm of $\mathbf{X}$ by means of a trace moment. Therefore, for any nonnegative integer $p$, it holds that The second inequality is simply our bound (4.9). All that remains is to choose the value of $p$ to minimize the factor on the right-hand side.

### Calculating the Constant

Finally, let us develop an accurate bound for the leading factor on the right-hand side of (4.10). We claim that Given this estimate, select $p = {\lceil{\log d}\rceil}$ to reach Introduce the inequality (4.12) into (4.10) to complete the proof of Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach").

To check that (4.11) is valid, we use some tools from integral calculus: The bracket in the second line is the trapezoid rule approximation of the integral in the third line. Since the integrand is concave, the trapezoid rule underestimates the integral. Exponentiating this formula, we arrive at (4.11).

### Context

The proof of Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") is really just a discrete, matrix version of the familiar calculation of the $({2p})$th moment of a centered normal random variable. Let us elaborate. Recall the Gaussian integration by parts formula: where $\gamma \sim {\text{normal}{(0,\sigma^{2})}}$ and $f:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ is any function for which the integrals are finite. This result follows when we write the expectations as integrals with respect to the normal density tand invoke the usual integration by parts rule. Now, suppose that we wish to compute the $({2p})$th moment of $\gamma$. We have The second identity is just (4.13) with the choice ${f{(t)}} = t^{{2p} - 1}$. Iterating (4.14), we discover that In Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), the matrix variance parameter $v{({\mathbf{X}})}$ plays the role of the scalar variance $\sigma^{2}$.

In fact, the link with Gaussian integration by parts is even stronger. Consider a matrix Gaussian series where $\{\gamma_{i}\}$ is an independent family of standard normal variables. If we replace the discrete integration by parts in the proof of Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") with Gaussian integration by parts, the argument leads to the bound This approach requires matrix calculus, but it is slightly simpler than the argument for matrix Rademacher series in other respects. See \[, Thm. 8.1\] for a proof of the noncommutative Khintchine inequality for Gaussian series along these lines.

## Upper Bounds for the Expected Norm

We are now prepared to establish the upper bound for an arbitrary sum of independent random matrices. The argument is based on the specialized result, Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), for matrix Rademacher series. It proceeds by steps through more and more general classes of random matrices: first positive semidefinite, then Hermitian, and finally rectangular. Here is what we will show.

### Theorem 5.1 (Expected Norm: Upper Bounds)

Define the dimensional constant ${C{(d)}}:={4{({1 + {2{\lceil{\log d}\rceil}}})}}$. The expected spectral norm of a sum of independent random matrices satisfies the following upper bounds.

The Positive-Semidefinite Case. Consider an independent family $\{{\mathbf{T}}_{1},\ldots,{\mathbf{T}}_{n}\}$ of random $d \times d$ positive-semidefinite matrices, and define the sum The Centered Hermitian Case. Consider an independent family $\{{\mathbf{Y}}_{1},\ldots,{\mathbf{Y}}_{n}\}$ of random $d \times d$ Hermitian matrices with ${{\mathbb{E}}{\mathbf{Y}}_{i}} = \mathbf{0}$ for each index $i$, and define the sum The Centered Rectangular Case. Consider an independent family $\{{\mathbf{S}}_{1},\ldots,{\mathbf{S}}_{n}\}$ of random $d_{1} \times d_{2}$ matrices with ${{\mathbb{E}}{\mathbf{S}}_{i}} = \mathbf{0}$ for each index $i$, and define the sum The proof of Theorem 5.1. ‣ 5. Upper Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") takes up the rest of this section. The presentation includes notes about the provenance of various parts of the argument.

The upper bound in Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") follows instantly from Case of Theorem 5.1. ‣ 5. Upper Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"). We just introduce the notation $v{({\mathbf{Z}})}$ for the variance parameter, and we calculate that The first expression follows immediately from the definition of $\mathbf{Z}$ and the linearity of the expectation; the second identity holds because the random matrices ${\mathbf{S}}_{i}$ are independent and have mean zero. The formula for ${\mathbb{E}}\left\lbrack {{\mathbf{Z}}^{\ast}{\mathbf{Z}}} \right\rbrack$ is valid for precisely the same reasons.

### Proof of the Positive-Semidefinite Case

Recall that $\mathbf{W}$ is a random $d \times d$ positive-semidefinite matrix of the form Let us introduce notation for the quantity of interest: By the triangle inequality for the spectral norm, The second inequality follows from symmetrization, Fact 3.1. ‣ 3.4. Symmetrization ‣ 3. Probability Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"). In this expression, $\{\varepsilon_{i}\}$ is an independent family of Rademacher random variables, independent from $\{{\mathbf{T}}_{i}\}$. Conditioning on the choice of the random matrices ${\mathbf{T}}_{i}$, we apply Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") via the bound (4.2): The operator ${\mathbb{E}}_{\mathbf{ε}}$ averages over the choice of the Rademacher random variables, with the matrices ${\mathbf{T}}_{i}$ fixed. Now, since the matrices ${\mathbf{T}}_{i}$ are positive-semidefinite, The first inequality is Fact 2.3. ‣ 2.8. Some Spectral Norm Inequalities ‣ 2. Linear Algebra Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), and the second is the Cauchy--Schwarz inequality (3.1) for expectation. In the last step, we identified a copy of the quantity $E$.

Combine the last three displays to see that For any ${\alpha,\beta} \geq 0$, the quadratic inequality $t^{2} \leq {\alpha + {\betat}}$ implies that because the square root is subadditive. Applying this fact to the quadratic relation (5.4) for $E^{1/2}$, we obtain Square both sides to reach the conclusion (5.1. ‣ 5. Upper Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")).

This argument is adapted from Rudelson's paper, which develops a version of this result for the case where the matrices ${\mathbf{T}}_{i}$ have rank one; see also. The paper contains the first estimates for the constants. Magen & Zouzias observed that similar considerations apply when the matrices ${\mathbf{T}}_{i}$ have higher rank. The complete result (5.1. ‣ 5. Upper Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) first appeared in \[, App.\]. The constants in this paper are marginally better. Related bounds for Schatten norms appear in \[MJC^+^14, Sec. 7\] and.

The results described in the last paragraph are all matrix versions of the classical inequalities due to Rosenthal \[, Lem. 1\]. These bounds can be interpreted as polynomial moment versions of the Chernoff inequality.

### Proof of the Hermitian Case

The result (5.2. ‣ 5. Upper Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) for Hermitian matrices is a corollary of Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") and the positive-semidefinite result (5.1. ‣ 5. Upper Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")). Recall that $\mathbf{X}$ is a $d \times d$ random Hermitian matrix of the form We may calculate that The first inequality follows from the symmetrization procedure, Fact 3.1. ‣ 3.4. Symmetrization ‣ 3. Probability Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"). The second inequality applies Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), conditional on the choice of ${\mathbf{Y}}_{i}$. The remaining expectation contains a sum of independent positive-semidefinite matrices. Therefore, we may invoke (5.1. ‣ 5. Upper Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) with ${\mathbf{T}}_{i} = {\mathbf{Y}}_{i}^{2}$. We obtain Combine the last two displays to reach Rewrite this expression to reach (5.2. ‣ 5. Upper Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")).

A version of the result (5.2. ‣ 5. Upper Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) first appeared in \[, App.\]; the constants here are marginally better. Related results for the Schatten norm appear in the papers \[ MJC^+^14, \]. These bounds are matrix extensions of the scalar inequalities due to Rosenthal \[, Thm. 3\] and to Rosén \[, Thm. 1\]; see also Nagaev--Pinelis \[, Thm. 2\]. They can be interpreted as the polynomial moment inequalities that sharpen the Bernstein inequality.

### Proof of the Rectangular Case

Finally, we establish the rectangular result (5.3. ‣ 5. Upper Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")). Recall that $\mathbf{Z}$ is a $d_{1} \times d_{2}$ random rectangular matrix of the form Set $d:={d_{1} + d_{2}}$, and form a random $d \times d$ Hermitian matrix $\mathbf{X}$ by dilating $\mathbf{Z}$: The Hermitian dilation $\mathcal{H}$ is defined in (2.18); the second relation holds because the dilation is a real-linear map.

Evidently, the random matrix $\mathbf{X}$ is a sum of independent, centered, random Hermitian matrices $\mathcal{H}{({\mathbf{S}}_{i})}$. Therefore, we may apply (5.2. ‣ 5. Upper Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) to $\mathbf{X}$ to see that Since the dilation preserves norms (2.20), the left-hand side of (5.5) is exactly what we want: To simplify the first term on the right-hand side of (5.5), invoke the formula (2.19) for the square of the dilation: The second identity relies on the fact that the norm of a block-diagonal matrix is the maximum norm of a diagonal block. To simplify the second term on the right-hand side of (5.5), we use (2.20) again: Introduce the last three displays into (5.5) to arrive at the result (5.3. ‣ 5. Upper Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")).

The result (5.3. ‣ 5. Upper Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) first appeared in the monograph \[, Eqn. (6.16)\] with (possibly) incorrect constants. The current paper contains the first complete presentation of the bound.

## Lower Bounds for the Expected Norm

Finally, let us demonstrate that each of the upper bounds in Theorem 5.1. ‣ 5. Upper Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") is sharp up to the dimensional constant $C{(d)}$. The following result gives matching lower bounds in each of the three cases.

### Theorem 6.1 (Expected Norm: Lower Bounds)

The expected spectral norm of a sum of independent random matrices satisfies the following lower bounds.

The Positive-Semidefinite Case. Consider an independent family $\{{\mathbf{T}}_{1},\ldots,{\mathbf{T}}_{n}\}$ of random $d \times d$ positive-semidefinite matrices, and define the sum The Centered Hermitian Case. Consider an independent family $\{{\mathbf{Y}}_{1},\ldots,{\mathbf{Y}}_{n}\}$ of random $d \times d$ Hermitian matrices with ${{\mathbb{E}}{\mathbf{Y}}_{i}} = \mathbf{0}$ for each index $i$, and define the sum The Centered Rectangular Case. Consider an independent family $\{{\mathbf{S}}_{1},\ldots,{\mathbf{S}}_{n}\}$ of random $d_{1} \times d_{2}$ matrices with ${{\mathbb{E}}{\mathbf{S}}_{i}} = \mathbf{0}$ for each index $i$, and define the sum The rest of the section describes the proof of Theorem 6.1. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach").

The lower bound in Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") is an immediate consequence of Case of Theorem 6.1. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"). We simply introduce the notation $v{({\mathbf{Z}})}$ for the variance parameter.

### The Positive-Semidefinite Case

The lower bound (6.1. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) in the positive-semidefinite case is relatively easy. Recall that First, by Jensen's inequality (3.3) and the convexity of the spectral norm, Second, let $I$ be the minimum value of the index $i$ where $\max_{i}\left\| {\mathbf{T}}_{i} \right\|$ is achieved; note that $I$ is a random variable. Since the summands ${\mathbf{T}}_{i}$ are positive semidefinite, it is easy to see that Therefore, by the norm identity (2.10) for a positive-semidefinite matrix and the monotonicity of the maximum eigenvalue, Fact 2.1. ‣ 2.5. Rayleigh’s Variational Principle ‣ 2. Linear Algebra Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), we have Take the expectation to arrive at Average the two bounds (6.4) and (6.5) to obtain To reach (6.1. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")), apply the numerical fact that ${2{({a + b})}} \geq \left({\sqrt{a} + \sqrt{b}} \right)^{2}$, valid for all ${a,b} \geq 0$.

### Hermitian Case

The Hermitian case (6.2. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) is similar in spirit, but the details are a little more involved. Recall that First, using the identity (2.11), we have The second relation is Jensen's inequality (3.3).

To obtain the other part of our lower bound, we use the lower bound from the symmetrization result, Fact 3.1. ‣ 3.4. Symmetrization ‣ 3. Probability Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"): where $\{\varepsilon_{i}\}$ is an independent family of Rademacher random variables, independent from $\{{\mathbf{Y}}_{i}\}$. Now, we condition on the choice of $\{{\mathbf{Y}}_{i}\}$, and we compute the partial expectation with respect to the $\varepsilon_{i}$. Let $I$ be the minimum value of the index $i$ where $\max_{i}\left\| {\mathbf{Y}}_{i} \right\|^{2}$ is achieved. By Jensen's inequality (3.3), applied conditionally, Combining the last two displays and taking a square root, we discover that Average the two bounds (6.6) and (6.7) to conclude that (6.2. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) is valid.

### The Rectangular Case

The rectangular case (6.3. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) follows instantly from the Hermitian case when we apply (6.2. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) to the Hermitian dilation. Recall that Define a random matrix $\mathbf{X}$ by applying the Hermitian dilation (2.18) to $\mathbf{Z}$: Since $\mathbf{X}$ is a sum of independent, centered, random Hermitian matrices, the bound (6.2. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) yields Repeating the calculations in Section 5.3, we arrive at the advertised result (6.3. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")).

## Optimality of Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")

The lower bounds and upper bounds in Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") match, except for the dimensional factor $C{({\mathbf{d}})}$. In this section, we show by example that neither the lower bounds nor the upper bounds can be sharpened substantially. More precisely, the logarithms cannot appear in the lower bound, and they must appear in the upper bound. As a consequence, unless we make further assumptions, Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") cannot be improved except by constant factors and, in one place, by an iterated logarithm.

### Upper Bound: Variance Term

First, let us show that the variance term in the upper bound in (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) must contain a logarithm. This example is drawn from \[, Sec. 6.1.2\].

For a large parameter $n$, consider the $d \times d$ random matrix As before, $\{\varepsilon_{ij}\}$ is an independent family of Rademacher random variables, and $\mathbf{E}_{ii}$ is a $d \times d$ matrix with a one in the $(i,i)$ position and zeroes elsewhere. The variance parameter satisfies The large deviation parameter satisfies Therefore, the variance term drives the upper bound (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")). For this example, it is easy to estimate the norm directly. Indeed, Here, $\{\gamma_{i}\}$ is an independent family of standard normal variables, and the first approximation follows from the central limit theorem. The norm of a diagonal matrix is the maximum absolute value of one of the diagonal entries. Last, we use the well-known fact that the expected maximum among $d$ squared standard normal variables is asymptotic to $2{\log d}$. In summary, We conclude that the variance term in the upper bound must carry a logarithm. Furthermore, it follows that Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") is numerically sharp.

### Upper Bound: Large-Deviation Term

Next, we verify that the large-deviation term in the upper bound in (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) must also contain a logarithm, although the bound is slightly suboptimal. This example is drawn from \[, Sec. 6.1.2\].

For a large parameter $n$, consider the $d \times d$ random matrix where $\{\delta_{ij}\}$ is an independent family of $\text{bernoulli}\left(n^{- 1} \right)$ random variables. That is, $\delta_{ij}$ takes only the values zero and one, and its expectation is $n^{- 1}$. The variance parameter for the random matrix is The large deviation parameter is Therefore, the large-deviation term drives the upper bound in (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")): On the other hand, by direct calculation Here, $\{ Q_{i}\}$ is an independent family of $\text{poisson}{}$ random variables, and the first approximation follows from the Poisson limit of a binomial. The second approximation depends on a (messy) calculation for the expected squared maximum of a family of independent Poisson variables. We see that the large deviation term in the upper bound (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) cannot be improved, except by an iterated logarithm factor.

### Lower Bound: Variance Term

Next, we argue that there are examples where the variance term in the lower bound from (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) cannot have a logarithmic factor.

Consider a $d \times d$ random matrix of the form Here, $\{\varepsilon_{ij}\}$ is an independent family of Rademacher random variables. The variance parameter satisfies The large-deviation parameter is Therefore, the variance term controls the lower bound in (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")): Meanwhile, it can be shown that the norm of the random matrix $\mathbf{Z}$ satisfies See the paper for an elegant proof of this nontrivial result. We see that the variance term in the lower bound in (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) cannot have a logarithmic factor.

### Lower Bound: Large-Deviation Term

Finally, we produce an example where the large-deviation term in the lower bound from (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) cannot have a logarithmic factor.

Consider a $d \times d$ random matrix of the form Here, $\{ P_{i}\}$ is an independent family of symmetric random variables whose tails satisfy The key properties of these variables are that The second expression just describes the asymptotic order of the expected maximum. We quickly compute that the variance term satisfies Meanwhile, the large-deviation factor satisfies Therefore, the large-deviation term drives the lower bound (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")): On the other hand, by direct calculation, We conclude that the large-deviation term in the lower bound (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) cannot carry a logarithmic factor.
