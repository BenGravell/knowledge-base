<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Tail Inequality for Quadratic Forms of Subgaussian Random Vectors

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We prove an exponential probability tail inequality for positive semidefinite quadratic forms in a subgaussian random vector. The bound is analogous to one that holds when the vector has independent Gaussian entries.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Suppose that $x = {(x_{1},\ldots,x_{n})}$ is a random vector. Let $A \in {\mathbb{R}}^{m \times n}$ be a fixed matrix. A natural quantity that arises in many settings is the quadratic form ${\|{Ax}\|}^{2} = {x^{\top}{({A^{\top}A})}x}$. Throughout $\| v\|$ denotes the Euclidean norm of a vector $v$, and $\| M\|$ denotes the spectral (operator) norm of a matrix $M$. We are interested in how close ${\|{Ax}\|}^{2}$ is to its expectation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consider the special case where $x_{1},\ldots,x_{n}$ are independent standard Gaussian random variables. The following proposition provides an (upper) tail bound for ${\|{Ax}\|}^{2}$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Tail inequalities for sums of random vectors", "weight": 1.0} -->

One motivation for our main result comes from the following observations about sums of random vectors. Let $a_{1},\ldots,a_{n}$ be vectors in a Euclidean space, and let $A = {\lbrack{a_{1}{|\cdots|}a_{n}}\rbrack}$ be the matrix with $a_{i}$ as its $i$th column. Consider the squared norm of the random sum where $x:={(x_{1},\ldots,x_{n})}$ is a martingale difference sequence with ${{\mathbb{E}}{\lbrack\left. x_{i} \middle| {x_{1},\ldots,x_{i - 1}} \right.\rbrack}} = 0$ and ${{\mathbb{E}}{\lbrack\left.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Tail inequalities for sums of random vectors", "weight": 1.0} -->

x_{i}^{2} \middle| {x_{1},\ldots,x_{i - 1}} \right.\rbrack}} = \sigma^{2}$. Under mild boundedness assumptions on the $x_{i}$, the probability that the squared norm in is much larger than its expectation falls off exponentially fast. This can be shown, for instance, using the following lemma by taking $u_{i} = {a_{i}x_{i}}$ (the proof is standard, but we give it for completeness in Appendix A.1).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Positive semidefinite quadratic forms", "weight": 1.0} -->

Our main theorem, given below, is a generalization of.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Note that when $\mu = 0$ and $\sigma = 1$ we have: which is the same as Proposition 1.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Our proof actually establishes the following upper bounds on the moment generating function of ${\|{Ax}\|}^{2}$ for $0 \leq \eta < {1/{({2\sigma^{2}{\|\Sigma\|}})}}$: where $z$ is a vector of $m$ independent standard Gaussian random variables.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Example: fixed-design regression with subgaussian noise", "weight": 1.0} -->

We give a simple application of Theorem 1 to fixed-design linear regression with the ordinary least squares estimator.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Example: fixed-design regression with subgaussian noise", "weight": 1.0} -->

Let $x_{1},\ldots,x_{n}$ be fixed design vectors in ${\mathbb{R}}^{d}$. Let the responses $y_{1},\ldots,y_{n}$ be random variables for which there exists $\sigma > 0$ such that for any ${\alpha_{1},\ldots,\alpha_{n}} \in {\mathbb{R}}$. This condition is satisfied, for instance, if for independent subgaussian zero-mean noise variables $\varepsilon_{1},\ldots,\varepsilon_{n}$. Let $\Sigma:={\sum_{i = 1}^{n}{{x_{i}x_{i}^{\top}}/n}}$, which we assume is invertible without loss of generality. Let be the coefficient vector of minimum expected squared error.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Example: fixed-design regression with subgaussian noise", "weight": 1.0} -->

The ordinary least squares estimator is given by The excess loss $R{(\hat{\beta})}$ of $\hat{\beta}$ is the difference between the expected squared error of $\hat{\beta}$ and that of $\beta$: It is easy to see that Note that in the case that ${{\mathbb{E}}{\lbrack{({y_{i} - {{\mathbb{E}}{\lbrack y_{i}\rbrack}}})}^{2}\rbrack}} = \sigma^{2}$ for each $i$, then so the tail inequality above is essentially tight when the $y_{i}$ are independent Gaussian random variables.
