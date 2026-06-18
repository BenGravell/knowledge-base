<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In contemporary applied and computational mathematics, a frequent challenge is to bound the expectation of the spectral norm of a sum of independent random matrices. This quantity is controlled by the norm of the expected square of the random matrix and the expectation of the maximum squared norm achieved by one of the summands; there is also a weak dependence on the dimension of the random matrix. The purpose of this paper is to give a complete, elementary proof of this important, but underappreciated, inequality.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

In contemporary applied and computational mathematics, a frequent challenge is to bound the expectation of the spectral norm of a sum of independent random matrices. This quantity is controlled by the norm of the expected square of the random matrix and the expectation of the maximum squared norm achieved by one of the summands; there is also a weak dependence on the dimension of the random matrix. The purpose of this paper is to give a complete, elementary proof of this important, but underappreciated, inequality.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Key words and phrases", "weight": 1.0} -->

Probability inequality; random matrix; sum of independent random variables.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Motivation", "weight": 1.0} -->

Over the last decade, random matrices have become ubiquitous in applied and computational mathematics. As this trend accelerates, more and more researchers must confront random matrices as part of their work. Classical random matrix theory can be difficult to use, and it is often silent about the questions that come up in modern applications. As a consequence, it has become imperative to develop and disseminate new tools that are easy to use and that apply to a wide range of random matrices.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Matrix Concentration Inequalities", "weight": 1.0} -->

Matrix concentration inequalities are among the most popular of these new methods. For a random matrix $\mathbf{Z}$ with appropriate structure, these results use simple parameters associated with the random matrix to provide bounds of the form

<!-- chunk {"id": "body-0007", "role": "body", "section": "Matrix Concentration Inequalities", "weight": 1.0} -->

where $\left. \parallel \cdot \parallel \right.$ denotes the spectral norm, also known as the $\ell_{2}$ operator norm. These tools have already found a place in a huge number of mathematical research fields, including

<!-- chunk {"id": "body-0008", "role": "body", "section": "Matrix Concentration Inequalities", "weight": 1.0} -->

These references are chosen more or less at random from a long menu of possibilities. See the monograph for an overview of the main results on matrix concentration, many detailed applications, and additional background references.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The Expected Norm", "weight": 1.0} -->

The purpose of this paper is to provide a complete proof of the following important, but underappreciated, theorem. This result is adapted from \[, Thm. A.1\].

<!-- chunk {"id": "body-0010", "role": "body", "section": "Discussion", "weight": 1.5} -->

Before we continue, some remarks about Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") are in order. First, although it may seem restrictive to focus on independent sums, as in (1.1. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")), this model captures an enormous number of useful examples. See the monograph for justification.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have chosen the term *variance parameter* because the quantity (1.2. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) is a direct generalization of the variance of a scalar random variable. The passage from the first formula to the second formula in (1.2. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) is an immediate consequence of the assumption that the summands ${\mathbf{S}}_{i}$ are independent and have zero mean (see Section 5). We use the term *large-deviation parameter* because the quantity (1.3. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) reflects the part of the expected norm of the random matrix that is attributable to one of the summands taking an unusually large value. In practice, both parameters are easy to compute using matrix arithmetic and some basic probabilistic considerations.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Discussion", "weight": 1.5} -->

In applications, it is common that we need high-probability bounds on the norm of a random matrix. Typically, the bigger challenge is to estimate the expectation of the norm, which is what Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") achieves. Once we have a bound for the expectation, we can use scalar concentration inequalities, such as \[, Thm. 6.10\], to obtain high-probability bounds on the deviation between the norm and its mean value.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have stated Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") as a bound on the second moment of $\left\| {\mathbf{Z}} \right\|$ because this is the most natural form of the result.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Discussion", "weight": 1.5} -->

We can take $c^{\prime} = {1/8}$. The upper bound follows easily from (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) and Jensen's inequality. The lower bound requires the Khintchine--Kahane inequality.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Discussion", "weight": 1.5} -->

Observe that the lower and upper estimates in (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) differ only by the factor $C{({\mathbf{d}})}$. As a consequence, the lower bound has no explicit dimensional dependence, while the upper bound has only a weak dependence on the dimension. Under the assumptions of the theorem, it is not possible to make substantial improvements to either the lower bound or the upper bound. Section 7 provides examples that support this claim.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Discussion", "weight": 1.5} -->

In the theory of matrix concentration, one of the major challenges is to understand what properties of the random matrix $\mathbf{Z}$ allow us to remove the dimensional factor $C{({\mathbf{d}})}$ from the estimate (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")). This question is largely open, but the recent papers make some progress.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The Uncentered Case", "weight": 1.0} -->

Although Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") concerns a centered random matrix, it can also be used to study a general random matrix. The following result is an immediate corollary of Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach").

<!-- chunk {"id": "body-0018", "role": "body", "section": "History", "weight": 1.0} -->

Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") is not new. A somewhat weaker version of the upper bound appeared in Rudelson's work \[, Thm. 1\]; see also \[, Thm. 3.1\] and \[, Sec. 9\]. The first explicit statement of the upper bound appeared in \[, Thm. A.1\]. All of these results depend on the noncommutative Khintchine inequality. In our approach, the main innovation is a particularly easy proof of a Khintchine-type inequality for matrices, patterned after \[MJC^+^14, Cor 7.3\] and \[, Thm. 8.1\].

<!-- chunk {"id": "body-0019", "role": "body", "section": "History", "weight": 1.0} -->

The ideas behind the proof of the lower bound in Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") are older. This estimate depends on generic considerations about the behavior of a sum of independent random variables in a Banach space. These techniques are explained in detail in \[, Ch. 6\]. Our presentation expands on a proof sketch that appears in the monograph \[, Secs. 5.1.2 and 6.1.2\].

<!-- chunk {"id": "body-0020", "role": "body", "section": "Target Audience", "weight": 1.0} -->

This paper is intended for students and researchers who want to develop a detailed understanding of the foundations of matrix concentration. The preparation required is modest.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Target Audience", "weight": 1.0} -->

Basic Convexity. Some simple ideas from convexity play a role, notably the concept of a convex function and Jensen's inequality.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Target Audience", "weight": 1.0} -->

Intermediate Linear Algebra. The requirements from linear algebra are more substantial. The reader should be familiar with the spectral theorem for Hermitian (or symmetric) matrices, Rayleigh's variational principle, the trace of a matrix, and the spectral norm. The paper includes reminders about this material. The paper elaborates on some less familiar ideas, including inequalities for the trace and the spectral norm.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Target Audience", "weight": 1.0} -->

Intermediate Probability. The paper demands some comfort with probability. The most important concepts are expectation and the elementary theory of conditional expectation. We develop the other key ideas, including the notion of symmetrization.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Target Audience", "weight": 1.0} -->

Although many readers will find the background material unnecessary, it is hard to locate these ideas in one place and we prefer to make the paper self-contained. In any case, we provide detailed cross-references so that the reader may dive into the proofs of the main results without wading through the shallower part of the paper.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Roadmap", "weight": 1.0} -->

Section 2 and Section 3 contain the background material from linear algebra and probability. To prove the upper bound in Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), the key step is to establish the result for the special case of a sum of fixed matrices, each modulated by a random sign. This result appears in Section 4. In Section 5, we exploit this result to obtain the upper bound in (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")). In Section 6, we present the easier proof of the lower bound in (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")). Finally, Section 7 shows that it is not possible to improve (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) substantially.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Linear Algebra Background", "weight": 1.0} -->

Our aim is to make this paper as accessible as possible. To that end, this section presents some background material from linear algebra. Good references include. We also assume some familiarity with basic ideas from the theory of convexity, which may be found in the books.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Convexity", "weight": 1.0} -->

Let $V$ be a finite-dimensional linear space. A subset $E \subset V$ is *convex* when

<!-- chunk {"id": "body-0028", "role": "body", "section": "Convexity", "weight": 1.0} -->

Let $E$ be a convex subset of a linear space $V$. A function $f:{E\rightarrow{\mathbb{R}}}$ is *convex* if

<!-- chunk {"id": "body-0029", "role": "body", "section": "Convexity", "weight": 1.0} -->

We say that $f$ is *concave* when $- f$ is convex.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Vector Basics", "weight": 1.0} -->

Let ${\mathbb{C}}^{d}$ be the complex linear space of $d$-dimensional complex vectors, equipped with the usual componentwise addition and scalar multiplication. The $\ell_{2}$ norm $\left. \parallel \cdot \parallel \right.$ is defined on ${\mathbb{C}}^{d}$ via the expression

<!-- chunk {"id": "body-0031", "role": "body", "section": "Vector Basics", "weight": 1.0} -->

The symbol ^∗^ denotes the conjugate transpose of a vector. Recall that the $\ell_{2}$ norm is a convex function.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Vector Basics", "weight": 1.0} -->

The orthonormal basis also has the property

<!-- chunk {"id": "body-0033", "role": "body", "section": "Vector Basics", "weight": 1.0} -->

where $\mathbf{I}_{d}$ is the $d \times d$ identity matrix.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Matrix Basics", "weight": 1.0} -->

A *matrix* is a rectangular array of complex numbers. Addition and multiplication by a complex scalar are defined componentwise, and we can multiply two matrices with compatible dimensions. We write ${\mathbb{M}}^{d_{1} \times d_{2}}$ for the complex linear space of $d_{1} \times d_{2}$ matrices. The symbol ^∗^ also refers to the conjugate transpose operation on matrices.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Matrix Basics", "weight": 1.0} -->

A square matrix $\mathbf{H}$ is *Hermitian* when ${\mathbf{H}} = {\mathbf{H}}^{\ast}$. Hermitian matrices are sometimes called *conjugate symmetric*.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Matrix Basics", "weight": 1.0} -->

Note that the set ${\mathbb{H}}_{d}$ is a linear space over the real field.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Matrix Basics", "weight": 1.0} -->

An Hermitian matrix ${\mathbf{A}} \in {\mathbb{H}}_{d}$ is *positive semidefinite* when

<!-- chunk {"id": "body-0038", "role": "body", "section": "Matrix Basics", "weight": 1.0} -->

It is convenient to use the notation ${\mathbf{A}} \preccurlyeq {\mathbf{H}}$ to mean that ${\mathbf{H}} - {\mathbf{A}}$ is positive semidefinite. In particular, the relation $\mathbf{0} \preccurlyeq {\mathbf{H}}$ is equivalent to $\mathbf{H}$ being positive semidefinite. Observe that

<!-- chunk {"id": "body-0039", "role": "body", "section": "Matrix Basics", "weight": 1.0} -->

In other words, addition and nonnegative scaling preserve the positive-semidefinite property.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Basic Spectral Theory", "weight": 1.0} -->

Each Hermitian matrix ${\mathbf{H}} \in {\mathbb{H}}_{d}$ can be expressed in the form

<!-- chunk {"id": "body-0041", "role": "body", "section": "Basic Spectral Theory", "weight": 1.0} -->

where the $\lambda_{i}$ are uniquely determined real numbers, called *eigenvalues*, and $\{{\mathbf{u}}_{i}\}$ is an orthonormal basis for ${\mathbb{C}}^{d}$. The representation (2.2) is called an *eigenvalue decomposition*.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Basic Spectral Theory", "weight": 1.0} -->

An Hermitian matrix $\mathbf{H}$ is positive semidefinite if and only if its eigenvalues $\lambda_{i}$ are all nonnegative. Indeed, using the eigenvalue decomposition (2.2), we see that

<!-- chunk {"id": "body-0043", "role": "body", "section": "Basic Spectral Theory", "weight": 1.0} -->

To verify the forward direction, select ${\mathbf{u}} = {\mathbf{u}}_{j}$ for each index $j$. The reverse direction should be obvious.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Basic Spectral Theory", "weight": 1.0} -->

For each nonnegative integer $r$, it is not hard to check that

<!-- chunk {"id": "body-0045", "role": "body", "section": "Basic Spectral Theory", "weight": 1.0} -->

In particular, ${\mathbf{H}}^{2p}$ is positive semidefinite for each nonnegative integer $p$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Rayleigh's Variational Principle", "weight": 1.0} -->

The *Rayleigh principle* is an attractive expression for the maximum eigenvalue $\lambda_{\max}{({\mathbf{H}})}$ of an Hermitian matrix ${\mathbf{H}} \in {\mathbb{H}}_{d}$. This result states that

<!-- chunk {"id": "body-0047", "role": "body", "section": "Rayleigh's Variational Principle", "weight": 1.0} -->

The maximum takes place over all unit-norm vectors ${\mathbf{u}} \in {\mathbb{C}}^{d}$. The identity (2.4) follows from the Lagrange multiplier theorem and the existence of the eigenvalue decomposition (2.2). Similarly, the minimum eigenvalue $\lambda_{\min}{({\mathbf{H}})}$ satisfies

<!-- chunk {"id": "body-0048", "role": "body", "section": "Rayleigh's Variational Principle", "weight": 1.0} -->

Rayleigh's principle implies that order relations for positive-semidefinite matrices lead to order relations for their eigenvalues.

<!-- chunk {"id": "body-0049", "role": "body", "section": "The Trace", "weight": 1.0} -->

The *trace* of a square matrix ${\mathbf{B}} \in {\mathbb{M}}^{d \times d}$ is defined as

<!-- chunk {"id": "body-0050", "role": "body", "section": "The Trace", "weight": 1.0} -->

It is clear that the trace is a linear functional on ${\mathbb{M}}^{d \times d}$. By direct calculation, one may verify that

<!-- chunk {"id": "body-0051", "role": "body", "section": "The Trace", "weight": 1.0} -->

This property is called the *cyclicity* of the trace.

<!-- chunk {"id": "body-0052", "role": "body", "section": "The Trace", "weight": 1.0} -->

This formula follows when we introduce the eigenvalue decomposition (2.2) into (2.6). Then we invoke the linearity and the cyclicity properties of the trace, as well as the properties of an orthonormal basis. We also instate the convention that monomials bind before the trace: ${{tr}{\mathbf{H}}^{r}}:={{tr}{\lbrack{\mathbf{H}}^{r}\rbrack}}$ for each nonnegative integer $r$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "The Spectral Norm", "weight": 1.0} -->

The maximum takes place over unit-norm vectors ${\mathbf{u}} \in {\mathbb{C}}^{d_{2}}$. We have the important identity

<!-- chunk {"id": "body-0054", "role": "body", "section": "The Spectral Norm", "weight": 1.0} -->

Furthermore, the spectral norm is a convex function, and it satisfies the triangle inequality.

<!-- chunk {"id": "body-0055", "role": "body", "section": "The Spectral Norm", "weight": 1.0} -->

Use the relations (2.3) and (2.9) to verify this fact.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Some Spectral Norm Inequalities", "weight": 1.0} -->

We need some basic inequalities for the spectral norm. First, note that

<!-- chunk {"id": "body-0057", "role": "body", "section": "Some Spectral Norm Inequalities", "weight": 1.0} -->

This point follows from (2.10) and (2.7) because the eigenvalues of a positive-semidefinite matrix are nonnegative.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Some Spectral Norm Inequalities", "weight": 1.0} -->

The next result uses the spectral norm to bound the trace of a product.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Fact 2.2 (Bound for the Trace of a Product)", "weight": 1.0} -->

Consider Hermitian matrices ${\mathbf{A},\mathbf{H}} \in {\mathbb{H}}_{d}$, and assume that $\mathbf{A}$ is positive semidefinite. Then

<!-- chunk {"id": "body-0060", "role": "body", "section": "GM--AM Inequality for the Trace", "weight": 1.0} -->

We require another substantial matrix inequality, which is one (of several) matrix analogs of the inequality between the geometric mean and the arithmetic mean.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Fact 2.4 (GM--AM Trace Inequality)", "weight": 1.0} -->

Consider Hermitian matrices ${\mathbf{H},\mathbf{W},\mathbf{Y}} \in {\mathbb{H}}_{d}$. For each nonnegative integer $r$ and each integer $q$ in the range $0 \leq q \leq {2r}$,

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 2.5 (The Power of Abstraction)", "weight": 1.0} -->

There is a cleaner, but more abstract, proof of the inequality (2.14. ‣ 2.9. GM–AM Inequality for the Trace ‣ 2. Linear Algebra Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")). Consider the left- and right-multiplication operators

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 2.5 (The Power of Abstraction)", "weight": 1.0} -->

Observe that powers of $\mathsf{W}$ and $\mathsf{Y}$ correspond to left- and right-multiplication by powers of $\mathbf{W}$ and $\mathbf{Y}$. Now, the operators $\mathsf{W}$ and $\mathsf{Y}$ commute, so there is a basis (orthonormal with respect to the trace inner product) for ${\mathbb{H}}_{d}$ in which they are simultaneously diagonalizable. Representing the operators in this basis, we can use (2.15) to check that

<!-- chunk {"id": "body-0064", "role": "body", "section": "The Hermitian Dilation", "weight": 1.0} -->

Last, we introduce the *Hermitian dilation* $\mathcal{H}{({\mathbf{B}})}$ of a rectangular matrix ${\mathbf{B}} \in {\mathbb{M}}^{d_{1} \times d_{2}}$. This is the Hermitian matrix

<!-- chunk {"id": "body-0065", "role": "body", "section": "The Hermitian Dilation", "weight": 1.0} -->

Note that the map $\mathcal{H}$ is real linear. By direct calculation,

<!-- chunk {"id": "body-0066", "role": "body", "section": "The Hermitian Dilation", "weight": 1.0} -->

We also have the spectral-norm identity

<!-- chunk {"id": "body-0067", "role": "body", "section": "The Hermitian Dilation", "weight": 1.0} -->

The first identity is (2.11); the second is (2.19). The norm of a block-diagonal Hermitian matrix is the maximum spectral norm of a block, which follows from the Rayleigh principle (2.4) with a bit of work. Finally, invoke the property (2.8).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Probability Background", "weight": 1.0} -->

This section contains some background material from the field of probability. Good references include the books.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Expectation", "weight": 1.0} -->

The symbol $\mathbb{E}$ denotes the expectation operator. We will not define expectation formally or spend any energy on technical details. No issues arise if we assume, for example, that all random variables are bounded.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Expectation", "weight": 1.0} -->

We use brackets to enclose the argument of the expectation when it is important for clarity, and we instate the convention that nonlinear functions bind before expectation. For instance, ${{\mathbb{E}}X^{p}}:={{\mathbb{E}}{\lbrack X^{p}\rbrack}}$ and ${{\mathbb{E}}{\max_{i}X_{i}}}:={{\mathbb{E}}{\lbrack{\max_{i}X_{i}}\rbrack}}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Expectation", "weight": 1.0} -->

Sometimes, we add a subscript to indicate a partial expectation. For example, if $J$ is a random variable, ${\mathbb{E}}_{J}$ refers to the average over $J$, with all other random variables fixed. We only use this notation when $J$ is independent from the other random variables, so there are no complications. In particular, we can compute iterated expectations: ${{\mathbb{E}}{\lbrack{{\mathbb{E}}_{J}{\lbrack \cdot \rbrack}}\rbrack}} = {{\mathbb{E}}{\lbrack \cdot \rbrack}}$ whenever all the expectations are finite.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Random Matrices", "weight": 1.0} -->

A *random matrix* is a matrix whose entries are complex random variables, not necessarily independent.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Random Matrices", "weight": 1.0} -->

As in the scalar case, if $\mathbf{W}$ and $\mathbf{Z}$ are independent,

<!-- chunk {"id": "body-0074", "role": "body", "section": "Random Matrices", "weight": 1.0} -->

Since the expectation is linear, it also commutes with all of the simple linear operations we perform on matrices.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Random Matrices", "weight": 1.0} -->

It suffices to take a naïve view of independence, expectation, and so forth. For the technically inclined, let $(\Omega,\mathcal{F},{\mathbb{P}})$ be a probability space. A $d_{1} \times d_{2}$ random matrix $\mathbf{Z}$ is simply a measurable function

<!-- chunk {"id": "body-0076", "role": "body", "section": "Random Matrices", "weight": 1.0} -->

for any collection of Borel^11^1Open sets in ${\mathbb{M}}^{d_{1} \times d_{2}}$ are defined with respect to the metric topology induced by the spectral norm. subsets $E_{i} \subset {\mathbb{M}}^{d_{1} \times d_{2}}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Inequalities for Expectation", "weight": 1.0} -->

We need several basic inequalities for expectation. We set these out for future reference. Let $X,Y$ be (arbitrary) real random variables. The Cauchy--Schwarz inequality states that

<!-- chunk {"id": "body-0078", "role": "body", "section": "Inequalities for Expectation", "weight": 1.0} -->

For $r \geq 1$, the triangle inequality states that

<!-- chunk {"id": "body-0079", "role": "body", "section": "Inequalities for Expectation", "weight": 1.0} -->

Each of these inequalities is vacuous precisely when its right-hand side is infinite.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Inequalities for Expectation", "weight": 1.0} -->

Jensen's inequality describes how expectation interacts with a convex or concave function; cf. (2.1). Let $X$ be a random variable taking values in a finite-dimensional linear space $V$, and let $f:{V\rightarrow{\mathbb{R}}}$ be a function. Then

<!-- chunk {"id": "body-0081", "role": "body", "section": "Inequalities for Expectation", "weight": 1.0} -->

The inequalities (3.3) also hold when we replace $\mathbb{E}$ with a partial expectation. Let us emphasize that these bounds do require that all of the expectations exist.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Symmetrization", "weight": 1.0} -->

Symmetrization is an important technique for studying the expectation of a function of independent random variables. The idea is to inject auxiliary randomness into the function. Then we condition on the original random variables and average with respect to the extra randomness. When the auxiliary random variables are more pliable, this approach can lead to significant simplifications.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Symmetrization", "weight": 1.0} -->

A *Rademacher* random variable $\varepsilon$ takes the two values $\pm 1$ with equal probability. The following result shows how we can use Rademacher random variables to study a sum of independent random matrices.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Fact 3.1 (Symmetrization)", "weight": 1.0} -->

Let ${\mathbf{S}_{1},\ldots,\mathbf{S}_{n}} \in {\mathbb{M}}^{d_{1} \times d_{2}}$ be independent random matrices. Let $\varepsilon_{1},\ldots,\varepsilon_{n}$ be independent Rademacher random variables that are also independent from the random matrices. For each $r \geq 1$,

<!-- chunk {"id": "body-0085", "role": "body", "section": "The Expected Norm of a Matrix Rademacher Series", "weight": 1.0} -->

To prove Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), our overall strategy is to use symmetrization. This approach allows us to reduce the study of an independent sum of random matrices to the study of a sum of fixed matrices modulated by independent Rademacher random variables. This type of random matrix is called a *matrix Rademacher series*. In this section, we establish a bound on the spectral norm of a matrix Rademacher series. This is the key technical step in the proof of Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach").

<!-- chunk {"id": "body-0086", "role": "body", "section": "Discussion", "weight": 1.5} -->

Before we establish Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), let us make a few comments. First, it is helpful to interpret the result in the same language we have used to state Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"). Introduce the matrix Rademacher series

<!-- chunk {"id": "body-0087", "role": "body", "section": "Discussion", "weight": 1.5} -->

Compute the matrix variance, defined in (1.2. ‣ 1.2. The Expected Norm ‣ 1.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Discussion", "weight": 1.5} -->

We may rewrite Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") as the statement that

<!-- chunk {"id": "body-0089", "role": "body", "section": "Discussion", "weight": 1.5} -->

In other words, Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") is a sharper version of Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") for the special case of a matrix Rademacher series.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Discussion", "weight": 1.5} -->

Next, we have focused on bounding the second moment of $\left\| {\mathbf{X}} \right\|$ because this is the most natural form of the result. Note that we also control the first moment because of Jensen's inequality (3.3):

<!-- chunk {"id": "body-0091", "role": "body", "section": "Discussion", "weight": 1.5} -->

A simple variant on the proof of Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") provides bounds for higher moments.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Discussion", "weight": 1.5} -->

Third, the dimensional factor on the right-hand side of (4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) is asymptotically sharp. Indeed, let us write $K{(d)}$ for the minimum possible constant in the inequality

<!-- chunk {"id": "body-0093", "role": "body", "section": "Discussion", "weight": 1.5} -->

The example in Section 7.1 shows that

<!-- chunk {"id": "body-0094", "role": "body", "section": "Discussion", "weight": 1.5} -->

In other words, (4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) cannot be improved without making further assumptions.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Discussion", "weight": 1.5} -->

Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") is a variant on the noncommutative Khintchine inequality, first established by Lust-Piquard and later improved by Pisier and by Buchholz. The noncommutative Khintchine inequality gives bounds for the Schatten norm of a matrix Rademacher series, rather than for the spectral norm. Rudelson pointed out that the noncommutative Khintchine inequality also implies bounds for the spectral norm of a matrix Rademacher series. In our presentation, we choose to control the spectral norm directly.

<!-- chunk {"id": "body-0096", "role": "body", "section": "The Spectral Norm and the Trace Moments", "weight": 1.0} -->

To begin the proof of Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), we introduce the random Hermitian matrix

<!-- chunk {"id": "body-0097", "role": "body", "section": "The Spectral Norm and the Trace Moments", "weight": 1.0} -->

Our goal is to bound the expected spectral norm of $\mathbf{X}$. We may proceed by estimating the expected trace of a power of the random matrix, which is known as a *trace moment*. Fix a nonnegative integer $p$. Observe that

<!-- chunk {"id": "body-0098", "role": "body", "section": "The Spectral Norm and the Trace Moments", "weight": 1.0} -->

The first identity is Jensen's inequality (3.3), applied to the concave function $t\mapsto t^{1/p}$. The second relation is (2.11). The final inequality is the bound (2.12) on the norm of the positive-semidefinite matrix ${\mathbf{X}}^{2p}$ by its trace.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Remark 4.2 (Higher Moments)", "weight": 1.0} -->

It should be clear that we can also bound expected powers of the spectral norm using the same technique. For simplicity, we omit this development.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Summation by Parts", "weight": 1.0} -->

To study the trace moments of the random matrix $\mathbf{X}$, we rely on a discrete analog of integration by parts. This approach is clearer if we introduce some more notation. For each index $i$, define the random matrices

<!-- chunk {"id": "body-0101", "role": "body", "section": "Summation by Parts", "weight": 1.0} -->

In other words, the distribution of ${\mathbf{X}}_{\varepsilon_{i}i}$ is the conditional distribution of the random matrix $\mathbf{X}$ given the value $\varepsilon_{i}$ of the $i$th Rademacher variable. This interpretation depends on the assumption that the Rademacher variables are independent.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Summation by Parts", "weight": 1.0} -->

Beginning with the trace moment, observe that

<!-- chunk {"id": "body-0103", "role": "body", "section": "Summation by Parts", "weight": 1.0} -->

In the second step, we simply write out the definition (4.3) of the random matrix $\mathbf{X}$ and use the linearity of the trace to draw out the sum. Then we write the expectation as an iterated expectation. To reach the next line, write out the partial expectation using the notation ${\mathbf{X}}_{\pm i}$ and the linearity of the trace.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Difference of Powers", "weight": 1.0} -->

Next, let us apply an algebraic identity to reduce the difference of powers in (4.5). For matrices ${{\mathbf{W}},{\mathbf{Y}}} \in {\mathbb{H}}_{d}$, it holds that

<!-- chunk {"id": "body-0105", "role": "body", "section": "Difference of Powers", "weight": 1.0} -->

To check this expression, just expand the matrix products and notice that the sum telescopes.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Difference of Powers", "weight": 1.0} -->

Linearity of the trace allows us to draw out the sum over $q$, and we have used the observation that ${{\mathbf{X}}_{+ i} - {\mathbf{X}}_{- i}} = {2{\mathbf{H}}_{i}}$.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Bound for the Trace Moments", "weight": 1.0} -->

We are now in a position to obtain a bound for the trace moments of $\mathbf{X}$. Beginning with (4.7), we compute that

<!-- chunk {"id": "body-0108", "role": "body", "section": "Bound for the Trace Moments", "weight": 1.0} -->

The bound in the second line is the trace GM--AM inequality, Fact 2.4. ‣ 2.9. GM–AM Inequality for the Trace ‣ 2. Linear Algebra Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), with $r = {p - 1}$ and ${\mathbf{W}} = {\mathbf{X}}_{+ i}$ and ${\mathbf{Y}} = {\mathbf{X}}_{- i}$. To reach the third line, observe that the parenthesis in the second line is twice the partial expectation of ${\mathbf{X}}^{{2p} - 2}$ with respect to $\varepsilon_{i}$. Afterward, we use linearity of the expectation and the trace to draw in the sum over $i$, and then we combine the expectations. Last, invoke the trace inequality from Fact 2.2. ‣ 2.8. Some Spectral Norm Inequalities ‣ 2. Linear Algebra Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach").

<!-- chunk {"id": "body-0109", "role": "body", "section": "Iteration and the Spectral Norm Bound", "weight": 1.0} -->

Iterating this bound $p$ times, we arrive at the result

<!-- chunk {"id": "body-0110", "role": "body", "section": "Iteration and the Spectral Norm Bound", "weight": 1.0} -->

The expression (4.4) shows that we can control the expected spectral norm of $\mathbf{X}$ by means of a trace moment. Therefore, for any nonnegative integer $p$, it holds that

<!-- chunk {"id": "body-0111", "role": "body", "section": "Iteration and the Spectral Norm Bound", "weight": 1.0} -->

The second inequality is simply our bound (4.9). All that remains is to choose the value of $p$ to minimize the factor on the right-hand side.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Calculating the Constant", "weight": 1.0} -->

Finally, let us develop an accurate bound for the leading factor on the right-hand side of (4.10). We claim that

<!-- chunk {"id": "body-0113", "role": "body", "section": "Calculating the Constant", "weight": 1.0} -->

Given this estimate, select $p = {\lceil{\log d}\rceil}$ to reach

<!-- chunk {"id": "body-0114", "role": "body", "section": "Calculating the Constant", "weight": 1.0} -->

Introduce the inequality (4.12) into (4.10) to complete the proof of Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach").

<!-- chunk {"id": "body-0115", "role": "body", "section": "Calculating the Constant", "weight": 1.0} -->

The bracket in the second line is the trapezoid rule approximation of the integral in the third line. Since the integrand is concave, the trapezoid rule underestimates the integral. Exponentiating this formula, we arrive at (4.11).

<!-- chunk {"id": "body-0116", "role": "body", "section": "Context", "weight": 1.0} -->

The proof of Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") is really just a discrete, matrix version of the familiar calculation of the $({2p})$th moment of a centered normal random variable. Let us elaborate.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Context", "weight": 1.0} -->

where $\gamma \sim {\text{normal}{(0,\sigma^{2})}}$ and $f:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ is any function for which the integrals are finite. This result follows when we write the expectations as integrals with respect to the normal density tand invoke the usual integration by parts rule. Now, suppose that we wish to compute the $({2p})$th moment of $\gamma$. We have

<!-- chunk {"id": "body-0118", "role": "body", "section": "Context", "weight": 1.0} -->

The second identity is just (4.13) with the choice ${f{(t)}} = t^{{2p} - 1}$. Iterating (4.14), we discover that

<!-- chunk {"id": "body-0119", "role": "body", "section": "Context", "weight": 1.0} -->

In Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), the matrix variance parameter $v{({\mathbf{X}})}$ plays the role of the scalar variance $\sigma^{2}$.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Context", "weight": 1.0} -->

In fact, the link with Gaussian integration by parts is even stronger. Consider a matrix Gaussian series

<!-- chunk {"id": "body-0121", "role": "body", "section": "Context", "weight": 1.0} -->

where $\{\gamma_{i}\}$ is an independent family of standard normal variables. If we replace the discrete integration by parts in the proof of Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") with Gaussian integration by parts, the argument leads to the bound

<!-- chunk {"id": "body-0122", "role": "body", "section": "Context", "weight": 1.0} -->

This approach requires matrix calculus, but it is slightly simpler than the argument for matrix Rademacher series in other respects. See \[, Thm. 8.1\] for a proof of the noncommutative Khintchine inequality for Gaussian series along these lines.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Upper Bounds for the Expected Norm", "weight": 1.0} -->

We are now prepared to establish the upper bound for an arbitrary sum of independent random matrices. The argument is based on the specialized result, Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), for matrix Rademacher series. It proceeds by steps through more and more general classes of random matrices: first positive semidefinite, then Hermitian, and finally rectangular. Here is what we will show.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Lower Bounds for the Expected Norm", "weight": 1.0} -->

Finally, let us demonstrate that each of the upper bounds in Theorem 5.1. ‣ 5. Upper Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") is sharp up to the dimensional constant $C{(d)}$. The following result gives matching lower bounds in each of the three cases.

<!-- chunk {"id": "body-0125", "role": "body", "section": "The Positive-Semidefinite Case", "weight": 1.0} -->

The lower bound (6.1. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) in the positive-semidefinite case is relatively easy. Recall that

<!-- chunk {"id": "body-0126", "role": "body", "section": "The Positive-Semidefinite Case", "weight": 1.0} -->

First, by Jensen's inequality (3.3) and the convexity of the spectral norm,

<!-- chunk {"id": "body-0127", "role": "body", "section": "The Positive-Semidefinite Case", "weight": 1.0} -->

Second, let $I$ be the minimum value of the index $i$ where $\max_{i}\left\| {\mathbf{T}}_{i} \right\|$ is achieved; note that $I$ is a random variable. Since the summands ${\mathbf{T}}_{i}$ are positive semidefinite, it is easy to see that

<!-- chunk {"id": "body-0128", "role": "body", "section": "The Positive-Semidefinite Case", "weight": 1.0} -->

Therefore, by the norm identity (2.10) for a positive-semidefinite matrix and the monotonicity of the maximum eigenvalue, Fact 2.1. ‣ 2.5. Rayleigh’s Variational Principle ‣ 2. Linear Algebra Background ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach"), we have

<!-- chunk {"id": "body-0129", "role": "body", "section": "The Positive-Semidefinite Case", "weight": 1.0} -->

Average the two bounds (6.4) and (6.5) to obtain

<!-- chunk {"id": "body-0130", "role": "body", "section": "The Positive-Semidefinite Case", "weight": 1.0} -->

To reach (6.1. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")), apply the numerical fact that ${2{({a + b})}} \geq \left( {\sqrt{a} + \sqrt{b}} \right)^{2}$, valid for all ${a,b} \geq 0$.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Hermitian Case", "weight": 1.0} -->

The Hermitian case (6.2. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) is similar in spirit, but the details are a little more involved. Recall that

<!-- chunk {"id": "body-0132", "role": "body", "section": "Hermitian Case", "weight": 1.0} -->

First, using the identity (2.11), we have

<!-- chunk {"id": "body-0133", "role": "body", "section": "Hermitian Case", "weight": 1.0} -->

The second relation is Jensen's inequality (3.3).

<!-- chunk {"id": "body-0134", "role": "body", "section": "Hermitian Case", "weight": 1.0} -->

To obtain the other part of our lower bound, we use the lower bound from the symmetrization result, Fact 3.1. ‣ 3.4. Symmetrization ‣ 3.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Hermitian Case", "weight": 1.0} -->

where $\{\varepsilon_{i}\}$ is an independent family of Rademacher random variables, independent from $\{{\mathbf{Y}}_{i}\}$. Now, we condition on the choice of $\{{\mathbf{Y}}_{i}\}$, and we compute the partial expectation with respect to the $\varepsilon_{i}$. Let $I$ be the minimum value of the index $i$ where $\max_{i}\left\| {\mathbf{Y}}_{i} \right\|^{2}$ is achieved. By Jensen's inequality (3.3), applied conditionally,

<!-- chunk {"id": "body-0136", "role": "body", "section": "Hermitian Case", "weight": 1.0} -->

Combining the last two displays and taking a square root, we discover that

<!-- chunk {"id": "body-0137", "role": "body", "section": "Hermitian Case", "weight": 1.0} -->

Average the two bounds (6.6) and (6.7) to conclude that (6.2. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) is valid.

<!-- chunk {"id": "body-0138", "role": "body", "section": "The Rectangular Case", "weight": 1.0} -->

The rectangular case (6.3. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) follows instantly from the Hermitian case when we apply (6.2. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) to the Hermitian dilation. Recall that

<!-- chunk {"id": "body-0139", "role": "body", "section": "The Rectangular Case", "weight": 1.0} -->

Define a random matrix $\mathbf{X}$ by applying the Hermitian dilation (2.18)

<!-- chunk {"id": "body-0140", "role": "body", "section": "The Rectangular Case", "weight": 1.0} -->

Since $\mathbf{X}$ is a sum of independent, centered, random Hermitian matrices, the bound (6.2. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) yields

<!-- chunk {"id": "body-0141", "role": "body", "section": "The Rectangular Case", "weight": 1.0} -->

Repeating the calculations in Section 5.3, we arrive at the advertised result (6.3. ‣ 6. Lower Bounds for the Expected Norm ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")).

<!-- chunk {"id": "body-0142", "role": "body", "section": "Optimality of Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach\")", "weight": 1.0} -->

The lower bounds and upper bounds in Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") match, except for the dimensional factor $C{({\mathbf{d}})}$. In this section, we show by example that neither the lower bounds nor the upper bounds can be sharpened substantially. More precisely, the logarithms cannot appear in the lower bound, and they must appear in the upper bound. As a consequence, unless we make further assumptions, Theorem I. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") cannot be improved except by constant factors and, in one place, by an iterated logarithm.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Upper Bound: Variance Term", "weight": 1.0} -->

First, let us show that the variance term in the upper bound in (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) must contain a logarithm. This example is drawn from \[, Sec. 6.1.2\].

<!-- chunk {"id": "body-0144", "role": "body", "section": "Upper Bound: Variance Term", "weight": 1.0} -->

For a large parameter $n$, consider the $d \times d$ random matrix

<!-- chunk {"id": "body-0145", "role": "body", "section": "Upper Bound: Variance Term", "weight": 1.0} -->

As before, $\{\varepsilon_{ij}\}$ is an independent family of Rademacher random variables, and $\mathbf{E}_{ii}$ is a $d \times d$ matrix with a one in the $(i,i)$ position and zeroes elsewhere. The variance parameter satisfies

<!-- chunk {"id": "body-0146", "role": "body", "section": "Upper Bound: Variance Term", "weight": 1.0} -->

The large deviation parameter satisfies

<!-- chunk {"id": "body-0147", "role": "body", "section": "Upper Bound: Variance Term", "weight": 1.0} -->

Therefore, the variance term drives the upper bound (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")). For this example, it is easy to estimate the norm directly. Indeed,

<!-- chunk {"id": "body-0148", "role": "body", "section": "Upper Bound: Variance Term", "weight": 1.0} -->

Here, $\{\gamma_{i}\}$ is an independent family of standard normal variables, and the first approximation follows from the central limit theorem. The norm of a diagonal matrix is the maximum absolute value of one of the diagonal entries. Last, we use the well-known fact that the expected maximum among $d$ squared standard normal variables is asymptotic to $2{\log d}$. In summary,

<!-- chunk {"id": "body-0149", "role": "body", "section": "Upper Bound: Variance Term", "weight": 1.0} -->

We conclude that the variance term in the upper bound must carry a logarithm. Furthermore, it follows that Theorem 4.1. ‣ 4. The Expected Norm of a Matrix Rademacher Series ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach") is numerically sharp.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Upper Bound: Large-Deviation Term", "weight": 1.0} -->

Next, we verify that the large-deviation term in the upper bound in (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) must also contain a logarithm, although the bound is slightly suboptimal. This example is drawn from \[, Sec. 6.1.2\].

<!-- chunk {"id": "body-0151", "role": "body", "section": "Upper Bound: Large-Deviation Term", "weight": 1.0} -->

For a large parameter $n$, consider the $d \times d$ random matrix

<!-- chunk {"id": "body-0152", "role": "body", "section": "Upper Bound: Large-Deviation Term", "weight": 1.0} -->

where $\{\delta_{ij}\}$ is an independent family of $\text{bernoulli}\left( n^{- 1} \right)$ random variables. That is, $\delta_{ij}$ takes only the values zero and one, and its expectation is $n^{- 1}$. The variance parameter for the random matrix is

<!-- chunk {"id": "body-0153", "role": "body", "section": "Upper Bound: Large-Deviation Term", "weight": 1.0} -->

Therefore, the large-deviation term drives the upper bound in (1.5. ‣ 1.2. The Expected Norm ‣ 1.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Upper Bound: Large-Deviation Term", "weight": 1.0} -->

On the other hand, by direct calculation

<!-- chunk {"id": "body-0155", "role": "body", "section": "Upper Bound: Large-Deviation Term", "weight": 1.0} -->

Here, $\{ Q_{i}\}$ is an independent family of $\text{poisson}{}$ random variables, and the first approximation follows from the Poisson limit of a binomial. The second approximation depends on a (messy) calculation for the expected squared maximum of a family of independent Poisson variables. We see that the large deviation term in the upper bound (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) cannot be improved, except by an iterated logarithm factor.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Lower Bound: Variance Term", "weight": 1.0} -->

Next, we argue that there are examples where the variance term in the lower bound from (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) cannot have a logarithmic factor.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Lower Bound: Variance Term", "weight": 1.0} -->

Consider a $d \times d$ random matrix of the form

<!-- chunk {"id": "body-0158", "role": "body", "section": "Lower Bound: Variance Term", "weight": 1.0} -->

Here, $\{\varepsilon_{ij}\}$ is an independent family of Rademacher random variables. The variance parameter satisfies

<!-- chunk {"id": "body-0159", "role": "body", "section": "Lower Bound: Variance Term", "weight": 1.0} -->

Therefore, the variance term controls the lower bound in (1.5. ‣ 1.2. The Expected Norm ‣ 1.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Lower Bound: Variance Term", "weight": 1.0} -->

Meanwhile, it can be shown that the norm of the random matrix $\mathbf{Z}$ satisfies

<!-- chunk {"id": "body-0161", "role": "body", "section": "Lower Bound: Variance Term", "weight": 1.0} -->

See the paper for an elegant proof of this nontrivial result. We see that the variance term in the lower bound in (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) cannot have a logarithmic factor.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Lower Bound: Large-Deviation Term", "weight": 1.0} -->

Finally, we produce an example where the large-deviation term in the lower bound from (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) cannot have a logarithmic factor.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Lower Bound: Large-Deviation Term", "weight": 1.0} -->

Consider a $d \times d$ random matrix of the form

<!-- chunk {"id": "body-0164", "role": "body", "section": "Lower Bound: Large-Deviation Term", "weight": 1.0} -->

Here, $\{ P_{i}\}$ is an independent family of symmetric random variables whose tails satisfy

<!-- chunk {"id": "body-0165", "role": "body", "section": "Lower Bound: Large-Deviation Term", "weight": 1.0} -->

The key properties of these variables are that

<!-- chunk {"id": "body-0166", "role": "body", "section": "Lower Bound: Large-Deviation Term", "weight": 1.0} -->

The second expression just describes the asymptotic order of the expected maximum. We quickly compute that the variance term satisfies

<!-- chunk {"id": "body-0167", "role": "body", "section": "Lower Bound: Large-Deviation Term", "weight": 1.0} -->

Meanwhile, the large-deviation factor satisfies

<!-- chunk {"id": "body-0168", "role": "body", "section": "Lower Bound: Large-Deviation Term", "weight": 1.0} -->

Therefore, the large-deviation term drives the lower bound (1.5. ‣ 1.2. The Expected Norm ‣ 1.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Lower Bound: Large-Deviation Term", "weight": 1.0} -->

On the other hand, by direct calculation,

<!-- chunk {"id": "body-0170", "role": "body", "section": "Lower Bound: Large-Deviation Term", "weight": 1.0} -->

We conclude that the large-deviation term in the lower bound (1.5. ‣ 1.2. The Expected Norm ‣ 1. Motivation ‣ The Expected Norm of a Sum of Independent Random Matrices: An Elementary Approach")) cannot carry a logarithmic factor.
