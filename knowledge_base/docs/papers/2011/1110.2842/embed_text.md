<!-- arxiv-full-text:v1 {"arxiv_id": "1110.2842", "source": "ar5iv"} -->

## Introduction

Suppose that $x = {(x_{1},\ldots,x_{n})}$ is a random vector. Let $A \in {\mathbb{R}}^{m \times n}$ be a fixed matrix. A natural quantity that arises in many settings is the quadratic form ${\|{Ax}\|}^{2} = {x^{\top}{({A^{\top}A})}x}$. Throughout $\| v\|$ denotes the Euclidean norm of a vector $v$, and $\| M\|$ denotes the spectral (operator) norm of a matrix $M$. We are interested in how close ${\|{Ax}\|}^{2}$ is to its expectation.

Consider the special case where $x_{1},\ldots,x_{n}$ are independent standard Gaussian random variables. The following proposition provides an (upper) tail bound for ${\|{Ax}\|}^{2}$.

### Proposition 1

Let $A \in {\mathbb{R}}^{m \times n}$ be a matrix, and let $\Sigma:={A^{\top}A}$. Let $x = {(x_{1},\ldots,x_{n})}$ be an isotropic multivariate Gaussian random vector with mean zero. For all $t > 0$, The proof, given in Appendix A.2, is straightforward given the rotational invariance of the multivariate Gaussian distribution, together with a tail bound for linear combinations of $\chi^{2}$ random variables due to Laurent and Massart. We note that a slightly weaker form of Proposition 1 can be proved directly using Gaussian concentration.

In this note, we consider the case where $x = {(x_{1},\ldots,x_{n})}$ is a *subgaussian* random vector. By this, we mean that there exists a $\sigma \geq 0$, such that for all $\alpha \in {\mathbb{R}}^{n}$, We provide a sharp upper tail bound for this case analogous to one that holds in the Gaussian case (indeed, the same as Proposition 1 when $\sigma = 1$).

### Tail inequalities for sums of random vectors

One motivation for our main result comes from the following observations about sums of random vectors. Let $a_{1},\ldots,a_{n}$ be vectors in a Euclidean space, and let $A = {\lbrack{a_{1}{|\cdots|}a_{n}}\rbrack}$ be the matrix with $a_{i}$ as its $i$th column. Consider the squared norm of the random sum where $x:={(x_{1},\ldots,x_{n})}$ is a martingale difference sequence with ${{\mathbb{E}}{\lbrack\left. x_{i} \middle| {x_{1},\ldots,x_{i - 1}} \right.\rbrack}} = 0$ and ${{\mathbb{E}}{\lbrack\left. x_{i}^{2} \middle| {x_{1},\ldots,x_{i - 1}} \right.\rbrack}} = \sigma^{2}$. Under mild boundedness assumptions on the $x_{i}$, the probability that the squared norm in is much larger than its expectation falls off exponentially fast. This can be shown, for instance, using the following lemma by taking $u_{i} = {a_{i}x_{i}}$ (the proof is standard, but we give it for completeness in Appendix A.1).

### Proposition 2

Let $u_{1},\ldots,u_{n}$ be a martingale difference vector sequence (*i.e.*, ${{\mathbb{E}}{\lbrack\left. u_{i} \middle| {u_{1},\ldots,u_{i - 1}} \right.\rbrack}} = 0$ for all $i = {1,\ldots,n}$) such that for all $i = {1,\ldots,n}$, almost surely. For all $t > 0$, After squaring the quantities in the stated probabilistic event, Proposition 2 gives the bound with probability at least $1 - e^{- t}$ when the $x_{i}$ are almost surely bounded by $1$ (or any constant).

Unfortunately, this bound obtained from Proposition 2 can be suboptimal when the $x_{i}$ are subgaussian. For instance, if the $x_{i}$ are Rademacher random variables, so ${\Pr{\lbrack{x_{i} = {+ 1}}\rbrack}} = {\Pr{\lbrack{x_{i} = {- 1}}\rbrack}} = {1/2}$, then it is known that with probability at least $1 - e^{- t}$. A similar result holds for any subgaussian distribution on the $x_{i}$. This is an improvement over the previous bound because the deviation terms (*i.e.*, those involving $t$) can be significantly smaller, especially for large $t$.

In this work, we give a simple proof of with explicit constants that match the analogous bound when the $x_{i}$ are independent standard Gaussian random variables.

## Positive semidefinite quadratic forms

Our main theorem, given below, is a generalization of.

### Theorem 1

Let $A \in {\mathbb{R}}^{m \times n}$ be a matrix, and let $\Sigma:={A^{\top}A}$. Suppose that $x = {(x_{1},\ldots,x_{n})}$ is a random vector such that, for some $\mu \in {\mathbb{R}}^{n}$ and $\sigma \geq 0$, for all $\alpha \in {\mathbb{R}}^{n}$. For all $t > 0$,

### Remark 1

Note that when $\mu = 0$ and $\sigma = 1$ we have: which is the same as Proposition 1.

### Remark 2

Our proof actually establishes the following upper bounds on the moment generating function of ${\|{Ax}\|}^{2}$ for $0 \leq \eta < {1/{({2\sigma^{2}{\|\Sigma\|}})}}$: where $z$ is a vector of $m$ independent standard Gaussian random variables.

### Proof of Theorem 1

Let $z$ be a vector of $m$ independent standard Gaussian random variables (sampled independently of $x$). For any $\alpha \in {\mathbb{R}}^{m}$, Thus, for any $\lambda \in {\mathbb{R}}$ and $\varepsilon \geq 0$, Let $USV^{\top}$ be a singular value decomposition of $A$; where $U$ and $V$ are, respectively, matrices of orthonormal left and right singular vectors; and $S = {{diag}{(\sqrt{\rho_{1}},\ldots,\sqrt{\rho_{m}})}}$ is the diagonal matrix of corresponding singular values. Note that By rotational invariance, $y:={U^{\top}z}$ is an isotropic multivariate Gaussian random vector with mean zero. Therefore ${\|{A^{\top}z}\|}^{2} = {z^{\top}US^{2}U^{\top}z} = {{\rho_{1}y_{1}^{2}} + \cdots + {\rho_{m}y_{m}^{2}}}$ and ${\mu^{\top}A^{\top}z} = {\nu^{\top}y} = {{\nu_{1}y_{1}} + \cdots + {\nu_{m}y_{m}}}$, where $\nu:={SV^{\top}\mu}$ (note that ${\|\nu\|}^{2} = {\|{SV^{\top}\mu}\|}^{2} = {\|{A\mu}\|}^{2}$). Let $\gamma:={{\lambda^{2}\sigma^{2}}/2}$. By Lemma 1, for $0 \leq \gamma < {1/{({2{\|\rho\|}_{\infty}})}}$. Combining and gives for $0 \leq \gamma < {1/{({2{\|\rho\|}_{\infty}})}}$ and $\varepsilon \geq 0$. Choosing where ${h_{1}{(a)}}:={{1 + a} - \sqrt{1 + {2a}}}$, which has the inverse function ${h_{1}^{- 1}{(b)}} = {\sqrt{2b} + b}$. The result follows by setting $\tau:={{2\sqrt{{\|\rho\|}_{2}^{2}t}} + {2{\|\rho\|}_{\infty}t}} = {{2\sqrt{{{tr}{(\Sigma^{2})}}t}} + {2{\|\Sigma\|}t}}$. ∎ The following lemma is a standard estimate of the logarithmic moment generating function of a quadratic form in standard Gaussian random variables, proved much along the lines of the estimate due to Laurent and Massart.

### Lemma 1

Let $z$ be a vector of $m$ independent standard Gaussian random variables. Fix any non-negative vector $\alpha \in {\mathbb{R}}_{+}^{m}$ and any vector $\beta \in {\mathbb{R}}^{m}$. If $0 \leq \lambda < {1/{({2{\|\alpha\|}_{\infty}})}}$, then

### Proof

Fix $\lambda \in {\mathbb{R}}$ such that $0 \leq \lambda < {1/{({2{\|\alpha\|}_{\infty}})}}$, and let $\eta_{i}:={1/\sqrt{1 - {2\alpha_{i}\lambda}}} > 0$ for $i = {1,\ldots,m}$. We have The right-hand side can be bounded using the inequalities

### Example: fixed-design regression with subgaussian noise

We give a simple application of Theorem 1 to fixed-design linear regression with the ordinary least squares estimator.

Let $x_{1},\ldots,x_{n}$ be fixed design vectors in ${\mathbb{R}}^{d}$. Let the responses $y_{1},\ldots,y_{n}$ be random variables for which there exists $\sigma > 0$ such that for any ${\alpha_{1},\ldots,\alpha_{n}} \in {\mathbb{R}}$. This condition is satisfied, for instance, if for independent subgaussian zero-mean noise variables $\varepsilon_{1},\ldots,\varepsilon_{n}$. Let $\Sigma:={\sum_{i = 1}^{n}{{x_{i}x_{i}^{\top}}/n}}$, which we assume is invertible without loss of generality. Let be the coefficient vector of minimum expected squared error. The ordinary least squares estimator is given by The excess loss $R{(\hat{\beta})}$ of $\hat{\beta}$ is the difference between the expected squared error of $\hat{\beta}$ and that of $\beta$: It is easy to see that Note that in the case that ${{\mathbb{E}}{\lbrack{({y_{i} - {{\mathbb{E}}{\lbrack y_{i}\rbrack}}})}^{2}\rbrack}} = \sigma^{2}$ for each $i$, then so the tail inequality above is essentially tight when the $y_{i}$ are independent Gaussian random variables.
