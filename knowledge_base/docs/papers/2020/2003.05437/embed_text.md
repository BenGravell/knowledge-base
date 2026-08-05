<!-- arxiv-full-text:v1 {"arxiv_id": "2003.05437", "source": "ar5iv"} -->

## Abstract

This paper develops nonasymptotic growth and concentration bounds for a product of independent random matrices. These results sharpen and generalize recent work of Henriksen--Ward, and they are similar in spirit to the results of Ahlswede--Winter and of Tropp for a sum of independent random matrices. The argument relies on the uniform smoothness properties of the Schatten trace classes.

The authors gratefully acknowledge the funding for this work. DH was supported under NSF grant DMS-1613861. JNW and RW were supported in part by the Institute for Advanced Study, where some of this research was conducted. JAT was supported under ONR Awards N00014-17-1-2146 and N00014-18-1-2363. RW also received support from AFOSR MURI Award N00014-17-S-F006.

## Motivation

Products of random matrices arise in many contemporary applications in the mathematics of data science. For instance, they describe the evolution of stochastic linear dynamical systems, which include popular stochastic algorithms for optimization such as Oja's algorithm for streaming principal component analysis and the randomized Kaczmarz method for solving linear systems. To understand the detailed behavior of these algorithms, such as the rate of convergence, we may seek out methods for studying a product of random matrices.

Unfortunately, the tools currently available in the literature are poorly adapted to these circumstances. Indeed, an instantiation of a stochastic optimization algorithm involves a finite product of finite-dimensional matrices, often with a particular structure (e.g., low-rank perturbations of the identity). But most existing theoretical results are limit laws that require the number of factors in the product or the dimension of the factors to tend to infinity. Furthermore, strong assumptions on the random matrices (e.g., independent and identically distributed entries) are usually required.

This paper offers some new tools for studying random matrix products that arise from stochastic optimization algorithms and related problems. The research is inspired by the recent paper of Henriksen and Ward. Our hope is to replicate the successful program for studying sums of random matrices, implemented in the works. In particular, we seek to develop methods that are flexible, easy to use, and powerful. We also aspire to use transparent theoretical arguments that can be adapted easily to new situations.

## Contributions

To motivate our work, we start with an elementary concentration inequality for a product of independent random numbers. We will generalize this bound, and others, to the matrix setting.

### Context: A Product of Random Numbers Near $1$

Consider an independent family ${\{ X_{1},X_{2},\ldots\}} \subset {\mathbb{R}}$ of bounded random variables that satisfy Form a product of random perturbations of $1$, and compute its mean: We anticipate that the random product $Z_{n}$ concentrates around its expectation ${{\mathbb{E}}Z_{n}} \approx e^{\mu}$.

To check this surmise, we can use standard methods from scalar concentration theory. For $s > 0$, The inequality follows from the numerical fact ${1 + a} \leq e^{a}$, valid for $a \in {\mathbb{R}}$. Hoeffding's inequality furnishes the bound At the small scale $s \leq e$, in which case ${\log{({1 + s})}} \geq {s/e}$, the growth bound (2.1) implies a subgaussian tail behavior: A similar inequality holds for the lower tail.

### Product of Random Perturbations of the Identity

We might hope that products of random matrices exhibit a similar behavior. Consider an independent family ${\{{\mathbf{X}}_{1},\ldots,{\mathbf{X}}_{n}\}} \subset {\mathbb{M}}_{d}$ of $d \times d$ matrices that satisfy Here are elsewhere, $\left. \parallel \cdot \parallel \right.$ is the spectral norm, that is, the $\ell_{2}$ operator norm. Form a product of random perturbations of the identity and compute its mean: Is it true that the spectral norm $\left\| {\mathbf{Z}}_{n} \right\|$ is proportional to $e^{\mu}$, where $\mu = \left\| {\mathbf{A}} \right\|$? Does the random product ${\mathbf{Z}}_{n}$ concentrate near its mean ${\mathbb{E}}{\mathbf{Z}}_{n}$?

These speculations are correct. Moreover, we can obtain bounds that parallel the scalar inequalities announced in the last subsection. Here is one particular result that follows from our analysis.

### Theorem I (Products of Perturbations of the Identity---Special case)

Consider an independent family ${\{\mathbf{X}_{1},\ldots,\mathbf{X}_{n}\}} \subset {\mathbb{M}}_{d}$ of random matrices that satisfy the hypotheses (2.3). Define $\mu:=\left\| \mathbf{A} \right\|$. The matrix product $\mathbf{Z}_{n}$ introduced in (2.4) satisfies the bounds Theorem I. ‣ 2.2. A Product of Random Perturbations of the Identity ‣ 2. Contributions ‣ Matrix Concentration for Products") follows from Corollary 6.1. ‣ 6.2. Bounds for the Product ‣ 6. Application: Random Perturbations of the Identity ‣ Matrix Concentration for Products").

As compared with the scalar bounds (2.1) and (2.2), the results in Theorem I. ‣ 2.2. A Product of Random Perturbations of the Identity ‣ 2. Contributions ‣ Matrix Concentration for Products") feature an additional dimensional factor $d$ in front of the exponential. This term leads to a dependency of $\log d$ in the bounds for products of random matrices. Otherwise, everything is the same, including the constants.

### Proof Strategy

How might one establish a result like Theorem I. ‣ 2.2. A Product of Random Perturbations of the Identity ‣ 2. Contributions ‣ Matrix Concentration for Products")? The derivation in Section 2.1 is valid only for products of random scalars. We cannot even begin to make this argument for matrices because the exponential of a sum of matrices generally does not equal the product of the exponentials.

In this paper, we take a completely different approach. The key is to observe that multiplying a random product ${\mathbf{Z}} \in {\mathbb{M}}_{d}$ by a statistically independent factor ${\mathbf{Y}} \in {\mathbb{M}}_{d}$ creates a predictable change plus a random perturbation: Since the second term has zero mean, conditional on $\mathbf{Z}$, we can exploit this orthogonality property to estimate the size of the product: The notation $\left. \parallel \cdot \parallel{}_{2} \right.$ refers to the Schatten $2$-norm, also known as the Frobenius norm. The last step introduces data about the random matrix $\mathbf{Y}$: the mean $m = \left\| {{\mathbb{E}}{\mathbf{Y}}} \right\|$ and the relative variance $v = {{\mathbb{E}}{\left\| {{\mathbf{Y}} - {{\mathbb{E}}{\mathbf{Y}}}} \right\|^{2}/\left\| {{\mathbb{E}}{\mathbf{Y}}} \right\|^{2}}}$. We can apply the same argument recursively to decompose the matrix $\mathbf{Z}$ into its own factors.

The approach in the last paragraph depends on the fact that $\left. \parallel \cdot \parallel{}_{2} \right.$ is the norm induced by the trace inner product. To undertake the same action for the spectral norm $\left. \parallel \cdot \parallel \right.$, we first need to approximate the spectral norm by the Schatten $p$-norm for $p \approx {\log d}$. Then we can invoke a remarkable geometric property of the Schatten $p$-norm, called *uniform smoothness*, as a substitute for the orthogonality law. See the paper for an introduction to this circle of ideas. Section 4 executes this method.

### Additional Results

We establish a family of norm inequalities for products of random matrices. The main result, Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"), gives a bound for the moments of a Schatten $p$-norm of a random product and a centered random product. From this fact, we derive expectation bounds, tail bounds, and matrix concentration inequalities. Many of these results hold under weaker assumptions than Theorem I. ‣ 2.2. A Product of Random Perturbations of the Identity ‣ 2. Contributions ‣ Matrix Concentration for Products"), addressing cases where the matrices have different means or are unbounded.

To give a better indication of what we can prove, let us give an informal presentation of one of our main results, Corollary 5.4. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"). The statement concerns a general product ${\mathbf{Z}}_{n} = {{\mathbf{Y}}_{n}\cdots{\mathbf{Y}}_{1}}$ of independent random matrices of dimension $d$. Abbreviating $p = {1 + {2{\log d}}}$, we have the inequality We can interpret $v$ as the accumulated relative variance in the product.

For example, in the setting of Theorem I. ‣ 2.2. A Product of Random Perturbations of the Identity ‣ 2. Contributions ‣ Matrix Concentration for Products"), the quantity $v = {O{({b^{2}/n})}}$. It follows that In particular, $\left\| {\mathbf{Z}}_{n} \right\|$ is much closer to $e^{\mu}$ than to the worst-case bound $e^{b}$.

### Roadmap

We continue with an overview of related work in Section 3. Section 4 presents background results from matrix theory and high-dimensional probability. We establish our main results for general matrix products in Section 5. Afterward, Section 6 draws corollaries for a product of perturbations of the identity. Finally, we describe some refinements and extensions in Section 7.

## Related Work

Products of random matrices have been studied for decades, primarily within the fields of ergodic theory, control theory, random matrix theory, and free probability. More recently, applied mathematicians have developed results that are tailored to problems arising in data science. Almost all prior work is either asymptotic in the length of the product or asymptotic in the dimension of the matrices. This section contains an overview of these inquiries.

### Direct Connections

The most immediate precedent for our research is the recent paper of Henriksen and Ward. They were motivated by the problem of understanding streaming algorithms for covariance estimation. Their work gives, perhaps, the first explicit nonasymptotic bounds for a somewhat general product of random matrices with fixed dimension. The argument is based on the matrix Bernstein inequality and a combinatorial fact about set partitions.

Henriksen and Ward focus on the setting of Theorem I. ‣ 2.2. A Product of Random Perturbations of the Identity ‣ 2. Contributions ‣ Matrix Concentration for Products"), and they establish a bound of the form In contrast, our new result (2.7) replaces the worst-case factor $e^{b}$ with the more typical value $e^{\mu}$. We are also able to relax several of the assumptions.

Also in the setting of Theorem I. ‣ 2.2. A Product of Random Perturbations of the Identity ‣ 2. Contributions ‣ Matrix Concentration for Products"), several works obtain results on the asymptotic behavior of ${\mathbf{Z}}_{n}$. Berger establishes, via a semigroup argument based on the Chernoff product formula, that ${\mathbf{Z}}_{n}\rightarrow e^{\mathbf{A}}$ in probability as $n\rightarrow\infty$. Emme and Hubert recently obtained a refinement of this result: motivated by a problem in ergodic theory, they show that ${\mathbf{Z}}_{n}\rightarrow e^{\mathbf{A}}$ as $n\rightarrow\infty$ under the sole assumptions that ${\sum_{i = 1}^{n}{{\mathbf{X}}_{i}/n}}\rightarrow{\mathbf{A}}$ and ${\sum_{i = 1}^{n}{{\|{\mathbf{X}}_{i}\|}/n}} < \infty$. Their argument expands the product and computes the limit of the $k$th order term using an induction. Neither approach readily yields nonasymptotic bounds.

### Other Recent Applications

Some applied work on random matrix products has been driven by the empirical observation that stochastic gradient descent converges faster when the gradient approximations are sampled *without* replacement, rather than sampled *with* replacement. Some papers that investigate this question from the point of view of (nonasymptotic) matrix inequalities include. This specific problem has been solved by Gürbüzbalaban et al. using optimization theory. However, none of these results directly address the questions at hand.

Researchers studying randomly initialized deep neural networks have also developed theoretical analysis for products of random matrices; see. These results involve operations on matrices with independent entries, and they focus on the large-matrix limit.

### Ergodic Theory and Control Theory

Products of random matrices describe the evolution of a linear stochastic dynamical system. For this reason, they have been a subject of perennial interest within the literatures on ergodic theory and on control theory. For the most part, this research is concerned with properties of the asymptotics of infinite products of matrices (of fixed size). Let us give a few more details.

Consider a finite family $\mathcal{A} = {\{{\mathbf{A}}_{1},\ldots,{\mathbf{A}}_{s}\}} \subset {\mathbb{M}}_{d}$ of fixed matrices. Construct a random matrix ${\mathbf{X}} \in {\mathbb{M}}_{d}$ with the distribution The *Lyapunov exponent* of the set $\mathcal{A}$ is the quantity The Furstenberg--Kesten theorem establishes that $\lambda{(\mathcal{A})}$ exists almost surely, but approximating $\lambda{(\mathcal{A})}$ is algorithmically undecidable \[43, Thm. 2\]. As a consequence, we must be pessimistic about finding a completely satisfactory solution to the matrix concentration problem for products.

To learn more about Lyapunov exponents and to find additional references, see the paper for work in control theory and the paper for work in ergodic theory. Another major application of random products is to study the asymptotic behavior of a random walk on a group; we refer the reader to for more information.

### Random Matrix Theory and Free Probability

Products of random matrices have also been considered within random matrix theory and free probability. This connection is natural, but matrix products have received somewhat less attention than other kinds of random matrix models. In these contexts, it is common to study a product of a small number of matrices (two or three, say) in the limit as the dimension of the matrices grows.

Bai and Silverstein \[4, Chap. 4\] present a limit law for the sequence of products of a random matrix with iid entries and a random matrix whose spectral distribution has a deterministic limit. This theorem is motivated by a statistical application, multivariate analysis of variance. Note, however, that convergence of the spectral distribution does not determine the limit of the spectral norm.

Free probability gives a complete description of the spectral distribution of a product of two freely independent elements as the "multiplicative free convolution" of the spectral distributions of the factors. The connection to random matrix theory stems from the fact that a family of "adequately random" matrices becomes freely independent in the limit as the dimension of the matrices tends to infinity. See the book of Nica & Speicher for a digestible introduction; some other good treatments include. Free probability has significant applications in wireless communications.

For highly structured random matrices (invariant ensembles), it may be possible to obtain more detailed formulas for products. See for some recent work in this direction.

## Random Matrix Inequalities via Uniform Smoothness

To analyze products of random matrices, we exploit classic methods that were developed to study the evolution of a martingale taking values in a uniformly smooth Banach space. These ideas are relevant for us because the matrix Schatten classes (with power $2 \leq p < \infty$) enjoy a remarkable uniform smoothness property.

In this section, we outline the required background from matrix analysis and high-dimensional probability. Naor's tutorial paper serves as a model for our presentation, and it contains a more general treatment. See Section 4.6 for additional discussion about the history of these ideas.

### Notation and Background

We work in the complex field $\mathbb{C}$; identical results hold for the real field $\mathbb{R}$. We often use the infix notation for the minimum ($\land$) and the maximum ($\vee$) of two real numbers.

The operator $\mathbb{P}$ computes the probability on an event. The operator $\mathbb{E}$ computes the expectation of a random variable. Subscripts denote partial expectation; for example, ${\mathbb{E}}_{Z}$ is the expectation over the randomness in $Z$. Nonlinear functions, such as powers, bind before the expectation.

The linear space ${\mathbb{C}}^{d \times r}$ contains all $d \times r$ matrices with complex entries. The algebra ${\mathbb{M}}_{d}$ consists of all $d \times d$ matrices with complex entries. We use the standard definitions of scalar multiplication, matrix addition, matrix multiplication, and the adjoint (i.e., conjugate transpose). Any statement about matrices that is not qualified with specific dimensions holds for all matrices with compatible dimensions. Nonlinear functions, such as matrix powers, bind before the trace. The matrix absolute value $|{\mathbf{A}}|:={({{\mathbf{A}}^{\ast}{\mathbf{A}}})}^{1/2}$, where ${( \cdot )}^{1/2}$ is the positive-semidefinite square root of a positive-semidefinite matrix.

We write $\left. \parallel \cdot \parallel \right.$ for the spectral norm on matrices; the spectral norm coincides with the maximum singular value, and it is also known as the $\ell_{2}$ operator norm. For each $p \geq 1$, the symbol $\left. \parallel \cdot \parallel{}_{p} \right.$ refers to the Schatten $p$-norm which returns the $\ell_{p}$ norm of the singular values of its argument. The symbol $S_{p}$ refers to a linear space of matrices (of fixed dimension), equipped with the Schatten $p$-norm.

For parameters ${p,q} \geq 1$, we define the $L_{q}{(S_{p})}$ norm of a random matrix $\mathbf{X}$ as The $L_{q}{(S_{p})}$ norm is an operator ideal norm, in the sense that This statement follows instantly from the analogous property of the Schatten $p$-norm.

We sometimes use the following simple inequalities for the moments of a random matrix $\mathbf{X}$: The equality follows from Lyapunov's inequality, combined with the fact that ${\||{\mathbf{X}}|\|}_{p,1} = {{\mathbb{E}}{\|{\mathbf{X}}\|}_{p}}$ for all $p \geq 1$.

### Uniform Smoothness for Matrices

Uniform smoothness ^11^1More precisely, we are considering uniformly smooth spaces whose modulus of smoothness has power type $2$. is a property of a normed space that describes how much the norm of a point changes under symmetric perturbation. Since the Schatten-2 space $S_{2}$ is an inner-product space, the parallelogram law gives an exact description of this phenomenon: Remarkably, in other Schatten classes, the parallelogram law is replaced by an inequality.

### Fact 4.1 (Uniform Smoothness for Schatten Classes)

Let $\mathbf{A},\mathbf{B}$ be matrices of the same size. For $p \geq 2$, The optimal constant $C_{p}:={p - 1}$. The inequality is reversed when $1 \leq p \leq 2$.

Fact 4.1. ‣ 4.2. Uniform Smoothness for Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") was first established by Tomczak-Jaegermann; she obtained the sharp constant $C_{p}$ when $p$ is an even number. Ball, Carlen, and Lieb \[5, Thm. 1\] determined that $C_{p}$ is the optimal constant for all values of $p$. Throughout the paper, we will continue to write $C_{p} = {p - 1}$.

### Uniform Smoothness for Random Matrices

Much as the Schatten class $S_{p}$ of matrices enjoys a uniform smoothness property, the normed space $L_{q}{(S_{p})}$ of random matrices is also uniformly smooth. When $2 \leq q \leq p$, this statement follows as an easy consequence of Fact 4.1. ‣ 4.2. Uniform Smoothness for Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products").

### Corollary 4.2 (Uniform Smoothness for Random Matrices)

Let $\mathbf{X},\mathbf{Y}$ be random matrices of the same size. When $2 \leq q \leq p$,

### Proof

Apply Lyapunov's inequality to the left-hand side of (4.3. ‣ 4.2. Uniform Smoothness for Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products")) to pass from the $p$th power to the $q$th power, and then transfer the exponent to the right-hand side to obtain the pointwise bound Take the expectation, and use the triangle inequality for the $L_{q/2}$ norm: Reinterpret the latter display using the $L_{q}{(S_{p})}$ norm $\left| \middle| \middle| \cdot \middle| \middle| \right|_{p,q}$. ∎

### Subquadratic Averages for Random Matrices

Corollary 4.2. ‣ 4.3. Uniform Smoothness for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") admits a powerful extension that controls how the norm of a matrix changes if we add a random matrix that has zero mean. This result is the main tool that we employ in our study of random products.

### Proposition 4.3 (Subquadratic Averages)

Consider random matrices $\mathbf{X},\mathbf{Y}$ of the same size that satisfy ${{\mathbb{E}}{\lbrack\left. \mathbf{Y} \middle| \mathbf{X} \right.\rbrack}} = \mathbf{0}$. When $2 \leq q \leq p$, The constant $C_{p} = {p - 1}$ is the best possible.

Ricard and Xu obtained a version of Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") in the more general setting of a von Neumann algebra. In their work, the expectation implicit in the $L_{q}$ norm is replaced by the projection onto a subalgebra. They emphasize that the key feature of their work is the determination of the sharp constant.

Here, we offer a very short proof of Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") with a suboptimal constant. The method is drawn from Naor's paper. Lemma A.1. ‣ Appendix A Supplementary Proofs ‣ Matrix Concentration for Products"), in the appendix, unspools an elementary argument that delivers the sharp constant.

### Proof

By Jensen's inequality, applied conditionally on $\mathbf{X}$, The second inequality is Lyapunov's; the third is Corollary 4.2. ‣ 4.3. Uniform Smoothness for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products"). Upon rearranging, we find that This is the stated result, with a spurious factor of $2$. ∎

### Matrix-Valued Martingales

To demonstrate the value of Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products"), let us explain how it leads to moment bounds for a matrix-valued martingale sequence. Consider a null matrix martingale ${\{{\mathbf{X}}_{1},\ldots,{\mathbf{X}}_{n}\}} \subset {\mathbb{M}}_{d}$ with difference sequence ${\{\mathbf{\Delta}_{1},\ldots,\mathbf{\Delta}_{n}\}} \subset {\mathbb{M}}_{d}$. That is, Applying Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") repeatedly, we arrive at the bound In words, the squared norm of the martingale is controlled by the sum of the squares of the norms of the martingale differences. The inequality (4.5) is a powerful extension of the orthogonality of the increments of a martingale taking values in an inner-product space, say $S_{2}$. The uniform smoothness constant $C_{p}$ shows how the geometry of the matrix space intermediates.

In this work, we will develop bounds for random matrix products by applying a similar technique to appropriately chosen decompositions of the product.

### History

The approach in this section has a long history. Let us summarize the contributions that are most relevant to our development.

For real numbers, the (sharp) uniform smoothness property in Fact 4.1. ‣ 4.2. Uniform Smoothness for Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") is known as the *two-point inequality*; it was established independently by Leonard Gross and Aline Bonami in the early 1970s, with later contributions by William Beckner. In 1974, the uniform smoothness property for the Schatten classes was obtained by Nicole Tomczak-Jaegermann. It took another 20 years before Ball, Carlen, and Lieb obtained the sharp uniform smoothness constants for all Schatten classes. The property dual to uniform smoothness is called *uniform convexity*. See for a detailed exposition.

Tomczak-Jaegermann \[37, Thm. 3.1\] also demonstrated that Rademacher averages are subquadratic in each Schatten space $S_{p}$ with $p \geq 2$; that is, the Banach space $S_{p}$ is *type 2*. This fact is a prototype for the more general result stated in Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products"). Tropp \[39, Sec. 4.8\] points out that parts of the Ahlswede--Winter \[1, App.\] theory of sums of independent random matrices already follow from Tomczak-Jaegermann's work. (In contrast, Tropp's matrix concentration inequalities are more closely related to a fact from operator theory, the noncommutative Khintchine inequality of Françoise Lust-Piquard; Tropp's results are derived using a theorem \[24, Thm. 6\] of Elliot Lieb.)

Assaf Naor traces the application of uniform convexity inequalities in the study of martingales to a 1975 paper of Gilles Pisier. Naor gives a nice introduction to this circle of ideas, which he uses to derive a general version of the Azuma inequality that holds in any uniformly smooth Banach space.

At least as early as 1988, Donald Burkholder applied closely related convexity inequalities to derive sharp inequalities for martingales taking values in a Hilbert space. The paper of Éric Ricard and Quanhua Xu is a recent entry in this line of research.

## Product of Independent Random Matrices

In this section, we obtain our main results on the growth and concentration of a product of independent random matrices. Section 5.1 shows how to decompose a random product into pieces that we can control using a recursive argument. Based on these ideas, we derive Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"), a general bound on the moments of the norm of the matrix product. The moment estimate leads to a family of expectation bounds (Corollary 5.4. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) and probability bounds (Corollary 5.6. ‣ 5.4. Tail Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")).

The balance of the paper contains applications of these results (Section 6) and extensions of the method to other settings (Section 7).

### Decomposition of Random Products

Our approach is based on a recursive argument that describes how the product evolves as we include more factors. At each step, we decompose the product into a nonrandom term and a random term with mean zero. This formulation allows us to apply Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") on subquadratic averages.

Consider a fixed matrix ${\mathbf{Z}}_{0} \in {\mathbb{M}}_{d}$ and an independent family ${\{{\mathbf{Y}}_{1},{\mathbf{Y}}_{2},\ldots,{\mathbf{Y}}_{n}\}} \subset {\mathbb{M}}_{d}$ of random matrices. We can recursively construct products of these random matrices: Evidently, the last element of the sequence takes the form ${\mathbf{Z}}_{n} = {{\mathbf{Y}}_{n}\cdots{\mathbf{Y}}_{1}{\mathbf{Z}}_{0}}$. By independence, ${{\mathbb{E}}{\mathbf{Z}}_{n}} = {{({{\mathbb{E}}{\mathbf{Y}}_{n}})}\cdots{({{\mathbb{E}}{\mathbf{Y}}_{1}})}{\mathbf{Z}}_{0}}$.

The random product ${\mathbf{Z}}_{i}$ admits a simple decomposition into a mean term and a fluctuation term: Since ${\mathbf{Y}}_{i}$ is independent from ${\mathbf{Z}}_{i - 1}$, the second term is conditionally zero mean: The property (5.2) supports the use of Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products"). It is also helpful to have an explicit norm bound for the random fluctuation term: The first relation follows from the operator ideal property of the Schatten $p$-norm and the statistical independence of the random matrices ${\mathbf{Y}}_{i}$ and ${\mathbf{Z}}_{i - 1}$.

We can study the concentration properties of the product ${\mathbf{Z}}_{i}$ using a related decomposition: As in (5.2), the second term is a fluctuation that is conditionally zero mean. The fluctuation term satisfies the norm bound (5.3).

### Growth and Concentration

Our main result controls the growth of the moments of a product of independent random matrices. It also describes how well the random product concentrates around its expectation.

### Theorem 5.1 (Growth and Concentration of Products)

Consider a fixed matrix $\mathbf{Z}_{0} \in {\mathbb{C}}^{d \times r}$ and an independent family ${\{\mathbf{Y}_{1},\mathbf{Y}_{2},\ldots,\mathbf{Y}_{n}\}} \subset {\mathbb{M}}_{d}$ of random matrices. Form the product For parameters $2 \leq q \leq p$, assume that Define the product of means and the accumulated relative variance Then the random product $\mathbf{Z}_{n}$ satisfies the growth bound and the concentration bound

### Proof of Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"), relation (5.5. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"))

By the homogeneity of (5.5. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")), we may assume that $m_{i} = 1$ for each index $i$, so that also $M = 1$. As in (5.1), we have the decomposition Now, Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") implies that The second line follows from (5.3), and the third depends on our hypotheses about the factors ${\mathbf{Y}}_{i}$. The last relation requires the numerical inequality ${1 + a} \leq e^{a}$, valid for all $a \in {\mathbb{R}}$. By iteration, In the final step, we use the assumption that ${\mathbf{Z}}_{0}$ is not random to see that ${\|\left| {\mathbf{Z}}_{0} \right|\|}_{p,q} = \left\| {\mathbf{Z}}_{0} \right\|_{p}$. For $i = n$, the formula (5.7. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) is the advertised result. ∎

### Proof of Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"), relation (5.6. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"))

The pattern of argument is similar with the proof of (5.5. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")). By the homogeneity of (5.6. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")), we may assume that all $m_{i} = 1$ and that $M = 1$. As in (5.4), we have the decomposition Again, we invoke Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") to ascertain that The last inequality is our growth bound (5.7. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")). This recurrence relation delivers The equality holds because ${\mathbf{Z}}_{0}$ is not random. The last relation is a numerical inequality, whose proof appears in Lemma A.2. ∎ Observe that the difference between the bounds (5.5. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) and (5.6. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) is only visible when $C_{p}v$ is small, in which case This is the setting where the concentration result may be nontrivial.

The next two remarks contain some minor extensions of Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"). Similar extensions are possible at other points in this paper. For the most part, we omit these developments.

### Remark 5.2 (Growth from Concentration)

In some instances, we can improve over the growth bound (5.5. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) by applying the triangle inequality to the decomposition ${\mathbf{Z}}_{n} = {{({{\mathbb{E}}{\mathbf{Z}}_{n}})} + {({{\mathbf{Z}}_{n} - {{\mathbb{E}}{\mathbf{Z}}_{n}}})}}$ and invoking the concentration bound (5.6. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")): Similarly, we can apply Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") together with (5.6. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) to obtain Neither of these bounds represents a strict improvement over the other or over the growth bound (5.5. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")).

### Remark 5.3 (Uniform Bounds on Factors)

Potentially stronger estimates are possible if the factors are bounded in norm. Fix parameters $2 \leq q \leq p$. Suppose that $\left\| {\mathbf{Y}}_{i} \right\| \leq b_{i}$ almost surely and ${\|\left| {{\mathbf{Y}}_{i} - {{\mathbb{E}}{\mathbf{Y}}_{i}}} \right|\|}_{p,q} \leq {\sigma_{i}b_{i}}$ for each index $i$. Define $B = {\prod_{i = 1}^{n}b_{i}}$ and $v = {\sum_{i = 1}^{n}\sigma_{i}^{2}}$. Then Compare these results with (5.5. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")), (5.6. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")), and (5.8). As for the proof, the growth bound (5.9. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) is an immediate consequence of the definition ${\mathbf{Z}}_{n} = {{\mathbf{Y}}_{n}\cdots{\mathbf{Y}}_{1}{\mathbf{Z}}_{0}}$. The concentration result (5.10. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) follows if we repeat the proof of (5.6. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")), using the growth bound (5.9. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) in place of (5.5. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")).

### Expectation Bounds for the Spectral Norm

In many cases, we just need to know the expected value of the product $\left\| {\mathbf{Z}}_{n} \right\|$ or the expected value of the fluctuation $\left\| {{\mathbf{Z}}_{n} - {{\mathbb{E}}{\mathbf{Z}}_{n}}} \right\|$. We can obtain bounds for these quantities as an easy consequence of Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products").

### Corollary 5.4 (Expectation Bounds)

Consider an independent sequence ${\{\mathbf{Y}_{1},\ldots,\mathbf{Y}_{n}\}} \subset {\mathbb{M}}_{d}$ of random matrices, and form the product $\mathbf{Z}_{n} = {\mathbf{Y}_{n}\cdots\mathbf{Y}_{1}}$. Assume that Let $M = {\prod_{i = 1}^{n}m_{i}}$ and $v = {\sum_{i = 1}^{n}\sigma_{i}^{2}}$. Then | | ${\mathbb{E}}\left\| {\mathbf{Z}}_{n} \right\|$ | ${\leq {{\exp\left(\sqrt{2v{({{2v} \vee {\log d}})}} \right)} \cdot M}}.$ | | (5.11) | | Provided that ${v{({1 + {2{\log d}}})}} \leq 1$, then also | | | ${\mathbb{E}}\left\| {{\mathbf{Z}}_{n} - {{\mathbb{E}}{\mathbf{Z}}_{n}}} \right\|$ | ${\leq {\sqrt{e^{2}v{({1 + {2{\log d}}})}} \cdot M}}.$ | | (5.12) |

### Proof

To apply Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"), we set ${\mathbf{Z}}_{0} = \mathbf{I}$ and choose the power $q = 2$.

To obtain the growth bound (5.11. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")), consider the Schatten norm of order $p = \sqrt{{2{({{2v} \vee {\log d}})}}/v}$. Note that $p \geq 2$ and that $\left\| {\mathbf{Z}}_{0} \right\|_{p} \leq d^{1/p} \leq e^{{pv}/2}$. Invoke Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"), relation (5.5. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")), to see that We used the fact that $C_{p} = {p - 1} < p$. This is the stated result.

To obtain the concentration bound (5.12. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")), consider the Schatten norm $p = {2{({1 + {\log d}})}}$. Note that $p \geq 2$ and that $\left\| {\mathbf{Z}}_{0} \right\|_{p} \leq d^{1/p} \leq \sqrt{e}$. Now, we use Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"), relation (5.6. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")), in a similar fashion. Assuming that ${C_{p}v} \leq 1$, The last bound is the numerical inequality ${e^{a} - 1} \leq {ea}$, valid when $a \in {\lbrack 0,1\rbrack}$. Finally, note that $C_{p} = {p - 1} = {1 + {2{\log d}}}$. ∎ The inequality (5.11. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) shows its power when each $\sigma_{i}$ is small. Assume that each $m_{i} = 1$ and $\sigma_{i} \leq {b/n}$ for a constant $b$. Then it is not hard to check that If $L\sqrt{{({2{\log d}})}/n}$ is close to zero, then (5.11. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) implies That is, ${\mathbb{E}}\left\| {\mathbf{Z}}_{n} \right\|$ is much closer to $\left\| {{\mathbb{E}}{\mathbf{Z}}_{n}} \right\|$ than to the worst-case value $e^{b}$.

### Remark 5.5 (Uniform Bounds on Factors)

Fix $p \geq 2$. Assume that $\left\| {\mathbf{Y}}_{i} \right\| \leq b_{i}$ almost surely and ${\|\left| {{\mathbf{Y}}_{i} - {{\mathbb{E}}{\mathbf{Y}}_{i}}} \right|\|}_{p,2} \leq {\sigma_{i}b_{i}}$ for each $i$. Let $v = {\sum_{i = 1}^{n}\sigma_{i}^{2}}$ and $B = {\prod_{i = 1}^{n}b_{i}}$. Then Remark 5.3. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products") implies that This improves the constant in (5.12. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) by a factor of $\sqrt{e}$, and it removes the condition that ${v{({1 + {2{\log d}}})}} \leq 1$.

### Tail Bounds for the Spectral Norm

The moment bounds in Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products") can also be upgraded to obtain tail bounds for $\left\| {\mathbf{Z}}_{n} \right\|$ and $\left\| {{\mathbf{Z}}_{n} - {{\mathbb{E}}{\mathbf{Z}}_{n}}} \right\|$.

### Corollary 5.6 (Tail Bounds)

Consider an independent sequence ${\{\mathbf{Y}_{1},\ldots,\mathbf{Y}_{n}\}} \subset {\mathbb{M}}_{d}$ of random matrices, and form the product $\mathbf{Z}_{n} = {\mathbf{Y}_{n}\cdots\mathbf{Y}_{1}}$. Assume that Let $M = {\prod_{i = 1}^{n}m_{i}}$ and $v = {\sum_{i = 1}^{n}\sigma_{i}^{2}}$. Then | | ${\mathbb{P}}\left\{ {\left\| {\mathbf{Z}}_{n} \right\| \geq {tM}} \right\}$ | $\leq {{d \cdot {\exp\left(\frac{- {\log^{2}t}}{2v} \right)}}\quad{\text{when~}{{\log t} \geq {2v}}\text}}$ | | (5.13) | | | ${\mathbb{P}}\left\{ {\left\| {{\mathbf{Z}}_{n} - {{\mathbb{E}}{\mathbf{Z}}_{n}}} \right\| \geq {tM}} \right\}$ | $\leq {{{({d \vee e})} \cdot {\exp\left(\frac{- t^{2}}{2e^{2}v} \right)}}\quad{\text{when~}{t \leq e}\text}}$ | | (5.14) |

### Proof

We begin with the proof of (5.13. ‣ 5.4. Tail Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")). By homogeneity, we may assume that $m_{i} = 1$ for each $i$, so also $M = 1$. Apply Markov's inequality and (4.2) to obtain To bound the $L_{p}{(S_{p})}$ norm, we will use Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products") with ${\mathbf{Z}}_{0} = \mathbf{I}$ and with $q = p$. Relation (5.5. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) gives We have used the fact that $\left\| {\mathbf{Z}}_{0} \right\|_{p}^{p} = \left\| \mathbf{I} \right\|_{p}^{p} = d$. Under the assumption that ${\log t} \geq {2v}$, we may select $p = {{({\log t})}/v} \geq 2$. This choice yields Sequence the last three displays to arrive at the bound (5.13. ‣ 5.4. Tail Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")).

We establish (5.14. ‣ 5.4. Tail Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) in an analogous fashion. The same argument, using relation (5.6. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")), implies that Supposing that ${t^{2}/{({e^{2}v})}} < 2$, the bound (5.14. ‣ 5.4. Tail Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) holds trivially because ${e \cdot {\exp{({- {t^{2}/{({2e^{2}v})}}})}}} \geq 1$. Otherwise, we may select the parameter $p = {t^{2}/{({e^{2}v})}} \geq 2$. Under the assumption that $t \leq e$, ${C_{p}v} \leq {pv} \leq {({t/e})}^{2} \leq 1$, so that ${e^{C_{p}v} - 1} \leq {{eC}_{p}v} \leq {t^{2}/e}$. Therefore, The last two displays imply (5.14. ‣ 5.4. Tail Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")). ∎

### Remark 5.7 (Uniform Bounds on Factors)

In the setting of Remark 5.5. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"), we have an unconditional variant of the concentration bound (5.14. ‣ 5.4. Tail Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")):

## Application: Random Perturbations of the Identity

This section treats the fundamental case where the factors ${\mathbf{Y}}_{i}$ in the product are independent, random perturbations of the identity. That is, ${\mathbf{Y}}_{i} = {\mathbf{I} + {\mathbf{X}}_{i}}$ where ${\{{\mathbf{X}}_{i}\}} \subset {\mathbb{M}}_{d}$ is an independent family. We will develop specialized theory for this class of problems, and we will use these results to compare our work with several recent papers.

### Iterative Algorithms

To motivate this development, observe that random perturbations of the identity arise from the analysis of the iterative scheme where ${\mathbf{X}}_{i}{\mathbf{u}}^{(i)}$ is a linear update to the current iterate ${\mathbf{u}}^{(i)}$. In this application, the norm of each ${\mathbf{X}}_{i}$ is proportional to the step size of the scheme, so it is typically small and it is controlled by the user. For example, the updates in Oja's algorithm take the form (6.1).

For now, we do not permit the random matrix ${\mathbf{X}}_{i}$ to depend on the sequence $\{{\mathbf{u}}^{(i)}\}$ of iterates. Later, in Section 7.3, we describe an extension of our approach to the setting where $\{{\mathbf{X}}_{i}\}$ is an adapted sequence. This variant allows for the study of a wider class of iterative algorithms.

### Bounds for the Product

First, we develop bounds for the growth and concentration of a product of perturbations of the identity. In Section 6.4, we develop results for the inverse of the product.

### Corollary 6.1 (Perturbations of the Identity)

Consider an independent family ${\{\mathbf{X}_{1},\ldots,\mathbf{X}_{n}\}} \subset {\mathbb{M}}_{d}$ of random matrices, and form the product $\mathbf{Z}_{n} = {{({\mathbf{I} + \mathbf{X}_{n}})}\cdots{({\mathbf{I} + \mathbf{X}_{1}})}}$. Assume that Define $\xi = {\sum_{i = 1}^{n}\xi_{i}}$ and $v = {\sum_{i = 1}^{n}\sigma_{i}^{2}}$. Then | | ${\mathbb{E}}\left\| {\mathbf{Z}}_{n} \right\|$ | $\leq {\exp\left({\xi + \sqrt{2v{\log d}}} \right)}$ | when ${2v} \leq {\log d}$; | | (6.2) | | | ${\mathbb{P}}\left\{ {\left\| {\mathbf{Z}}_{n} \right\| \geq {te^{\xi}}} \right\}$ | $\leq {d \cdot {\exp\left(\frac{- {\log^{2}t}}{2v} \right)}}$ | ${\text{when~}{{\log t} \geq {2v}}};$ | | (6.4) | | | ${\mathbb{P}}\left\{ {\left\| {{\mathbf{Z}}_{n} - {{\mathbb{E}}{\mathbf{Z}}_{n}}} \right\| \geq {te^{\xi}}} \right\}$ | $\leq {{({d \vee e})} \cdot {\exp\left(\frac{- t^{2}}{2e^{2}v} \right)}}$ | when $t \leq e$. | | (6.5) |

### Proof

Let ${\mathbf{Y}}_{i} = {\mathbf{I} + {\mathbf{X}}_{i}}$ for each index $i$. Then Furthermore, since $m_{i} \geq 1$, The results follow instantly from Corollary 5.4. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products") and Corollary 5.6. ‣ 5.4. Tail Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"). ∎

### Comparison with Prior Work

To clarify the meaning of Corollary 6.1. ‣ 6.2. Bounds for the Product ‣ 6. Application: Random Perturbations of the Identity ‣ Matrix Concentration for Products"), let us elaborate what it predicts when This situation can arise if we perform $n$ iterations of the iterative scheme (6.1) with a uniform step size of $1/n$. In this setting, Corollary 6.1. ‣ 6.2. Bounds for the Product ‣ 6. Application: Random Perturbations of the Identity ‣ Matrix Concentration for Products") implies that For $\delta \in {\lbrack 0,1\rbrack}$, with probability at least $1 - \delta$, Furthermore, if we assume that $\left\| {\mathbf{X}}_{i} \right\| \leq {T/n}$ almost surely for each $i$, then Remark 5.5. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products") implies that (6.6) and (6.7) hold without restriction.

The paper of Henriksen and Ward only contemplates the situation described in the last paragraph. It obtains a concentration bound of the form The salient improvement in (6.7) stems from the reduction of the factor $e^{L}$ to $e^{T}$. This difference is most pronounced when ${{\mathbb{E}}{\mathbf{X}}_{i}} = 0$ for each $i$, in which case the bound (6.7) removes the exponential factor entirely. Even under the assumption that ${\mathbf{X}}_{i} \succcurlyeq \mathbf{0}$ for all each $i$, it can happen that $L \geq {dT}$, so this refinement can make a big difference.

Last, we mention one instance that has special importance. Let ${\mathbf{A}} \in {\mathbb{M}}_{d}$ be a fixed matrix. Consider a triangular array ${\{{\mathbf{X}}_{i}^{(n)}:{{i \leq n}\text{~and~}{n \in {\mathbb{N}}}}\}} \subset {\mathbb{M}}_{d}$ of independent random matrices. For each index $n$, assume that Define the product The bound (6.7), combined with the first Borel--Cantelli Lemma, guarantees that This result is a special case of the limit theorem of Emme and Hubert \[13, Thm. 1.1\]. They do not require independence, but they only achieve an asymptotic result. Our analysis gives a rate of convergence that matches the corresponding bound (2.2) for scalar random variables.

### Bounds for the Inverse of a Product

In some applications, it is valuable to have a lower bound for the minimum singular value of a random product. Equivalently, we can seek an upper bound for the spectral norm of the inverse of the product. This section describes a situation where clean results are possible.

Consider the case where the factors ${\mathbf{Y}}_{i}$ are perturbations of the identity: ${\mathbf{Y}}_{i} = {\mathbf{I} + {\mathbf{X}}_{i}}$, where ${\mathbf{X}}_{i}$ is small enough to ensure that ${\mathbf{Y}}_{i}$ is invertible with probability $1$. In this setting, we can easily study the inverse of the product using Corollary 6.1. ‣ 6.2. Bounds for the Product ‣ 6. Application: Random Perturbations of the Identity ‣ Matrix Concentration for Products").

### Corollary 6.2 (Perturbations of the Identity: Inverses)

Frame the same hypotheses as in Corollary 6.1. ‣ 6.2. Bounds for the Product ‣ 6. Application: Random Perturbations of the Identity ‣ Matrix Concentration for Products"). Assume that ${\xi_{i} + \sigma_{i}} < 1$ for each index $i$, and define

### Proof

With the same notation as in Corollary 6.1. ‣ 6.2. Bounds for the Product ‣ 6. Application: Random Perturbations of the Identity ‣ Matrix Concentration for Products"), observe that ${\mathbf{Z}}_{n}^{- 1} = {{({\mathbf{I} + {\mathbf{X}}_{1}})}^{- 1}\cdots{({\mathbf{I} + {\mathbf{X}}_{n}})}^{- 1}}$. This is an independent product that can be bounded by applying the corollary. To do so, we simply need to express ${({\mathbf{I} + {\mathbf{X}}_{i}})}^{- 1} = {\mathbf{I} + {\overline{\mathbf{X}}}_{i}}$ for suitable random matrices ${\overline{\mathbf{X}}}_{i}$. The perturbation terms ${\overline{\mathbf{X}}}_{i}$ are obtained from the calculation It remains to develop estimates for the size of the perturbation.

The uniform bound $\left\| {\mathbf{X}}_{i} \right\| \leq {\left\| {{\mathbb{E}}{\mathbf{X}}_{i}} \right\| + \left\| {{\mathbf{X}}_{i} - {{\mathbb{E}}{\mathbf{X}}_{i}}} \right\|} \leq {\xi_{i} + \sigma_{i}} < 1$ implies that Therefore, the norm of the expected perturbation satisfies The fluctuations of the perturbation satisfy The results follow when we apply Corollary 6.1. ‣ 6.2. Bounds for the Product ‣ 6. Application: Random Perturbations of the Identity ‣ Matrix Concentration for Products") with the random matrices ${\overline{\mathbf{X}}}_{i}$ in place of the ${\mathbf{X}}_{i}$. ∎

## Improvements and Extensions

The argument underlying Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products") has several natural extensions. First, we develop sharper results for products of random contractions. In Section 7.2, we derive better estimates for a matrix product where the initial term is rectangular. In Section 7.3, we document the changes that are necessary in case the factors in the product are not independent but form an adapted sequence. Last, In Section 7.4, we explain how to develop a bound on the spectral radius of a product.

### Product of Contractions

Most of our results are designed for products of general random matrices. In some circumstances, the factors in the product are *contractions*, matrices whose singular values are bounded by one. For example, the randomized Kaczmarz algorithm can be expressed as the repeated application of random contractions. Other randomized linear fixed-point iterations take a similar form. This section derives sharper estimates for this important setting.

### Theorem 7.1 (Product of Contractions)

Consider an independent family ${\{\mathbf{Y}_{1},\ldots,\mathbf{Y}_{n}\}} \subset {\mathbb{M}}_{d}$ of random contractions; that is, $\left\| \mathbf{Y}_{i} \right\| \leq 1$. Form the random product $\mathbf{Z}_{n} = {\mathbf{Y}_{n}\cdots\mathbf{Y}_{1}}$. Assume that Define $M:={\prod_{i = 1}^{n}m_{i}}$ and $v:={\sum_{i = 1}^{n}\sigma_{i}^{2}}$. Then Furthermore, we have the tail bound To prove this result, we require a lemma that isolates the influence of each factor in the product. This step exploits the uniform bound on the singular values in an essential way.

### Lemma 7.2 (Random Contractions)

Let $\mathbf{Y} \in {\mathbb{M}}_{d}$ be a random contraction, and let $\mathbf{Z} \in {\mathbb{M}}_{d}$ be a random matrix that is independent from $\mathbf{Y}$. For $2 \leq q \leq p$,

### Proof

Write out the $L_{q}{(S_{p})}$ norm, and introduce matrix absolute values: The last relation can be verified using polar factorizations. Apply the Araki--Lieb--Thirring inequality \[9, Thm. IX.2.20\] to distribute the power onto the factors in the trace. We obtain The second inequality holds because a contraction satisfies $|{\mathbf{Y}}|^{p} \preccurlyeq |{\mathbf{Y}}|^{2}$ for each $p \geq 2$. The third inequality is Jensen's, justified because ${q/p} \leq 1$. Bounding the matrix in the center by its norm, This completes the analysis. ∎ With this result at hand, Theorem 7.1. ‣ 7.1. A Product of Contractions ‣ 7. Improvements and Extensions ‣ Matrix Concentration for Products") follows from familiar arguments.

### Proof of Theorem 7.1. ‣ 7.1. A Product of Contractions ‣ 7. Improvements and Extensions ‣ Matrix Concentration for Products")

Define ${\mathbf{Z}}_{0} = \mathbf{I}$ and ${\mathbf{Z}}_{i} = {{\mathbf{Y}}_{i}{\mathbf{Z}}_{i - 1}}$ for each index $i = {1,\ldots,n}$. We begin with the proof of (7.1. ‣ 7.1. A Product of Contractions ‣ 7. Improvements and Extensions ‣ Matrix Concentration for Products")). Since each factor is a contraction, it is clear that To obtain a less trivial bound on the expectation, we apply Lemma 7.2. ‣ 7.1. A Product of Contractions ‣ 7. Improvements and Extensions ‣ Matrix Concentration for Products") repeatedly. For $p \geq 2$, The statement (7.1. ‣ 7.1. A Product of Contractions ‣ 7. Improvements and Extensions ‣ Matrix Concentration for Products")) combines these two observations when we set $i = n$ and $p = 2$.

Let us continue with the proof of (7.2. ‣ 7.1. A Product of Contractions ‣ 7. Improvements and Extensions ‣ Matrix Concentration for Products")), which is analogous to the argument in Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")(5.6. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")). First, by expanding the inequality ${{\mathbb{E}}\left| {{\mathbf{Y}}_{i} - {{\mathbb{E}}{\mathbf{Y}}_{i}}} \right|^{2}} \succcurlyeq \mathbf{0}$, we see that $\mathbf{0} \preccurlyeq \left| {{\mathbb{E}}{\mathbf{Y}}_{i}} \right|^{2} \preccurlyeq {{\mathbb{E}}\left| {\mathbf{Y}}_{i} \right|^{2}}$. As a consequence, For $p \geq 2$, calculate that The second inequality is Lemma 7.2. ‣ 7.1. A Product of Contractions ‣ 7. Improvements and Extensions ‣ Matrix Concentration for Products"), and the third inequality requires (7.4). We have also used the fact that $m_{i}^{2} \leq m_{i}^{4/p}$ because $m_{i} \leq 1$. Unrolling the recursion, For $p = 2$, this result implies the advertised bound (7.2. ‣ 7.1. A Product of Contractions ‣ 7. Improvements and Extensions ‣ Matrix Concentration for Products")).

Finally, the tail inequality (7.3. ‣ 7.1. A Product of Contractions ‣ 7. Improvements and Extensions ‣ Matrix Concentration for Products")) follows from the estimate The last inequality follows from (7.5) and $C_{p} < p$. Bound the minimum with the power $p = {t^{2}/{({ev})}} \geq 2$ to complete the argument. ∎

### Low-Rank Products

So far, we have focused on the setting where the initial matrix ${\mathbf{Z}}_{0} = \mathbf{I}$. In many applications, we are interested in the action of the random product ${{\mathbf{Y}}_{n}\cdots{\mathbf{Y}}_{1}} \in {\mathbb{M}}_{d}$ on a specific matrix ${\mathbf{Z}}_{0} \in {\mathbb{C}}^{d \times r}$ with relatively few columns. In this case, the terms that the control the behavior of the product may be significantly smaller. Here is an example of the kinds of results one can achieve.

### Theorem 7.3 (Growth and Concentration of Low-Rank Products)

Consider a fixed matrix $\mathbf{Z}_{0} \in {\mathbb{C}}^{d \times r}$ and an independent sequence ${\{\mathbf{Y}_{1},\ldots,\mathbf{Y}_{n}\}} \subset {\mathbb{M}}_{d}$ of random matrices. Form the product $\mathbf{Z}_{n} = {\mathbf{Y}_{n}\cdots\mathbf{Y}_{1}\mathbf{Z}_{0}}$. Assume that where $\mathcal{P}_{r} \subset {\mathbb{M}}_{d}$ is the set of rank-$r$ orthogonal projectors. Define $M = {\prod_{i = 1}^{n}m_{i}}$ and $v = {\sum_{i = 1}^{n}\sigma_{i}^{2}}$. For each $p \geq 2$,

### Proof

Define ${\mathbf{Z}}_{i} = {{\mathbf{Y}}_{i}{\mathbf{Z}}_{i - 1}}$ for each index $i$. Since ${\mathbf{Z}}_{0} \in {\mathbb{C}}^{d \times r}$, the rank of each matrix ${\mathbf{Z}}_{i}$ is at most $r$. Thus, we can write ${\mathbf{Z}}_{i} = {{\mathbf{P}}_{i}{\mathbf{Z}}_{i}}$, where ${\mathbf{P}}_{i}$ is a rank-$r$ orthogonal projector that only depends on ${\mathbf{Y}}_{i},\ldots,{\mathbf{Y}}_{1}$ and ${\mathbf{Z}}_{0}$. As a consequence, We have used the fact that ${\mathbf{Y}}_{i}$ is independent from ${\mathbf{P}}_{i - 1}$ and from ${\mathbf{Z}}_{i - 1}$ to pass to the last line.

The rest of the proof runs along the same lines as the argument in Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"), using the last display in place of the bound (5.3). ∎ Let us offer a simple example to illustrate why Theorem 7.3. ‣ 7.2. Low-Rank Products ‣ 7. Improvements and Extensions ‣ Matrix Concentration for Products") can produce better outcomes than Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"). Consider a random matrix ${\mathbf{X}} \in {\mathbb{M}}_{d}$ with the distribution ${\mathbb{P}}\left\{ {\mathbf{X}} = \mathbf{e}_{j}\mathbf{e}_{j}{{}_{}^{\ast}\}} \right. = d^{- 1}$ for each $j = {1,\ldots,d}$. As usual, $\mathbf{e}_{j} \in {\mathbb{C}}^{d}$ is the $j$th standard basis vector. Construct the random matrix ${\mathbf{Y}} = {\mathbf{I} + {\varepsilon{\mathbf{X}}}}$, where $\varepsilon$ is a Rademacher random variable that is independent from $\mathbf{X}$. Clearly, ${{\mathbb{E}}{\mathbf{Y}}} = \mathbf{I}$. For any rank-$r$ orthogonal projector $\mathbf{P}$, By contrast, ${{\mathbb{E}}{\|{{\mathbf{Y}} - {{\mathbb{E}}{\mathbf{Y}}}}\|}^{2}} = {{\mathbb{E}}{\|{\mathbf{X}}\|}^{2}} = 1$. When $r \ll d$, this bound offers a significant improvement. instead of the ambient dimension $d$.

### Adapted Sequences

We can easily generalize our results on a product of independent random matrices to a product of adapted random matrices. This kind of extension is valuable for studying iterative algorithms where the choices made by the algorithm at a given step depend on the history of the iteration.

Let $(\Omega,\mathcal{F},{\mathbb{P}})$ be a probability space, and let $\mathcal{F}_{1} \subset \mathcal{F}_{2} \subset \cdots \subset \mathcal{F}_{n} \subset \mathcal{F}$ be a filtration. For each index $i = {1,\ldots,n}$, we write ${\mathbb{E}}_{i}$ for the expectation conditioned on the $\sigma$-algebra $\mathcal{F}_{i}$. The operator ${\mathbb{E}}_{0}:={\mathbb{E}}$ is the unconditional expectation.

We consider an adapted sequence ${\{{\mathbf{Y}}_{1},\ldots,{\mathbf{Y}}_{n}\}} \subset {\mathbb{M}}_{d}$ of random matrices; that is, each ${\mathbf{Y}}_{i}$ is measurable with respect to $\mathcal{F}_{i}$. The next result provides information about the growth and concentration properties of the product ${\mathbf{Z}}_{n} = {{\mathbf{Y}}_{n}\cdots{\mathbf{Y}}_{1}}$. Note that the natural concentration result compares ${\mathbf{Z}}_{n}$ with a product of conditional expectations, rather than the expectation of the product.

### Theorem 7.4 (Products of Adapted Random Matrices)

Consider a fixed matrix $\mathbf{Z}_{0} \in {\mathbb{M}}_{d}$ and an adapted sequence ${\{\mathbf{Y}_{1},\ldots,\mathbf{Y}_{n}\}} \subset {\mathbb{M}}_{d}$ of random matrices. Form the products Define $M = {\prod_{i = 1}^{n}m_{i}}$ and $v = {\sum_{i = 1}^{n}\sigma_{i}^{2}}$. For $2 \leq q \leq p$, the random product $\mathbf{Z}_{n}$ satisfies the growth and concentration bounds

### Proof

Recursively construct the products To bound the growth of ${\mathbf{Z}}_{i}$ and the concentration of ${\mathbf{Z}}_{i} - {\mathbf{F}}_{i}$, we simply need to update the argument from Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products").

To obtain (7.8. ‣ 7.3. Adapted Sequences ‣ 7. Improvements and Extensions ‣ Matrix Concentration for Products")), decompose Since ${\mathbb{E}}_{i - 1}{\mathbf{Y}}_{i}$ and ${\mathbf{Z}}_{i - 1}$ are both measurable with respect to $\mathcal{F}_{i - 1}$ and ${{\mathbb{E}}_{i - 1}{({{\mathbf{Y}}_{i} - {{\mathbb{E}}_{i - 1}{\mathbf{Y}}_{i}}})}} = \mathbf{0}$, the obvious variant of Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") implies that The second inequality follows from (4.1). This is the same recurrence we obtain in the proof of Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"), relation (5.5. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")). The rest of the argument is the same.

To obtain (7.9. ‣ 7.3. Adapted Sequences ‣ 7. Improvements and Extensions ‣ Matrix Concentration for Products")), decompose As before, Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") implies that This is the same recurrence that arose when we established Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"), relation (5.6. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")). The balance of the argument is identical. ∎

### The Spectral Radius

Products of matrices are closely related to the evolution of discrete-time linear dynamical systems. In this context, it may be more natural to study the *spectral radius* of the matrix product, rather than its spectral norm. Bounds for the spectral radius follow as corollary of our work, owing to the following classical fact.

### Fact 7.5 (Schur)

Let $\mathbf{M} \in {\mathbb{M}}_{d}$ be a square matrix. The spectral radius $\varrho{(\mathbf{M})}$ is defined as the maximum absolute value of an eigenvalue of $\mathbf{M}$. It satisfies the variational principle The infimum takes place over all invertible matrices $\mathbf{S}$. In particular ${\varrho{(\mathbf{M})}} \leq \left\| \mathbf{M} \right\|$.

Let us give an indication of the kinds of results that are possible.

### Corollary 7.6 (Expectation Bounds for the Spectral Radius)

Consider an independent sequence ${\{\mathbf{Y}_{1},\ldots,\mathbf{Y}_{n}\}} \subset {\mathbb{M}}_{d}$ of random matrices, and form the product $\mathbf{Z}_{n} = {\mathbf{Y}_{n}\cdots\mathbf{Y}_{1}}$. Let $\mathbf{S} \in {\mathbb{M}}_{d}$ be a fixed invertible matrix, and assume that Let $M = {\prod_{i = 1}^{n}m_{i}}$ and $v = {\sum_{i = 1}^{n}\sigma_{i}^{2}}$. Then

### Proof

Combine Corollary 5.4. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products") and Fact 7.5. ‣ 7.4. The Spectral Radius ‣ 7. Improvements and Extensions ‣ Matrix Concentration for Products"). ∎

### Prospects

We have developed a collection of nonasymptotic bounds for products of random matrices. These results hold under simple and easily verifiable conditions, and they give accurate predictions about the behavior of some particular instances (e.g., products of iid random perturbations of the identity). The proofs are based on foundational results about the geometry of the Schatten classes, and they can easily be adapted to treat variants of the problems under consideration.

A disappointing feature of our results is that they do not account for interactions between the matrix factors. For example, when ${\mathbf{Y}}_{i} = {\mathbf{I} + {{\mathbf{X}}_{i}/n}}$ for bounded, independent matrix perturbations ${\mathbf{X}}_{i}$, we have shown that However, when the matrices ${\mathbf{X}}_{i}$ commute almost surely, it is easy to show the sharper bound The results of Emme and Hubert establish that ${\lim_{n\rightarrow\infty}{\log{{\mathbb{E}}{\|{{\mathbf{Y}}_{n}\cdots{\mathbf{Y}}_{1}}\|}}}} = {\lim_{n\rightarrow\infty}{\left\| {\sum_{i = 1}^{n}{{\mathbb{E}}{\mathbf{X}}_{i}}} \right\|/n}}$. It therefore seems reasonable to conjecture that a refined bound of the latter type exists in more generality. The growth bounds discussed in Remark 5.2 imply a statement of the form but the error term is not sharp. This type of bound would echo Tropp's improvements to the Ahlswede--Winter results for a sum of independent random matrices. At present, it is not clear whether this refinement is possible, nor what technical arguments would lead there.
