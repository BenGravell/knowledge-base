<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Matrix Concentration for Products

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper develops nonasymptotic growth and concentration bounds for a product of independent random matrices. These results sharpen and generalize recent work of Henriksen-Ward, and they are similar in spirit to the results of Ahlswede-Winter and of Tropp for a sum of independent random matrices. The argument relies on the uniform smoothness properties of the Schatten trace classes.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

This paper develops nonasymptotic growth and concentration bounds for a product of independent random matrices. These results sharpen and generalize recent work of Henriksen--Ward, and they are similar in spirit to the results of Ahlswede--Winter and of Tropp for a sum of independent random matrices. The argument relies on the uniform smoothness properties of the Schatten trace classes.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Abstract", "weight": 1.5} -->

The authors gratefully acknowledge the funding for this work. DH was supported under NSF grant DMS-1613861. JNW and RW were supported in part by the Institute for Advanced Study, where some of this research was conducted. JAT was supported under ONR Awards N00014-17-1-2146 and N00014-18-1-2363. RW also received support from AFOSR MURI Award N00014-17-S-F006.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Motivation", "weight": 1.0} -->

Products of random matrices arise in many contemporary applications in the mathematics of data science. For instance, they describe the evolution of stochastic linear dynamical systems, which include popular stochastic algorithms for optimization such as Oja's algorithm for streaming principal component analysis and the randomized Kaczmarz method for solving linear systems. To understand the detailed behavior of these algorithms, such as the rate of convergence, we may seek out methods for studying a product of random matrices.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Motivation", "weight": 1.0} -->

Unfortunately, the tools currently available in the literature are poorly adapted to these circumstances. Indeed, an instantiation of a stochastic optimization algorithm involves a finite product of finite-dimensional matrices, often with a particular structure (e.g., low-rank perturbations of the identity). But most existing theoretical results are limit laws that require the number of factors in the product or the dimension of the factors to tend to infinity. Furthermore, strong assumptions on the random matrices (e.g., independent and identically distributed entries) are usually required.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Motivation", "weight": 1.0} -->

This paper offers some new tools for studying random matrix products that arise from stochastic optimization algorithms and related problems. The research is inspired by the recent paper of Henriksen and Ward. Our hope is to replicate the successful program for studying sums of random matrices, implemented in the works. In particular, we seek to develop methods that are flexible, easy to use, and powerful. We also aspire to use transparent theoretical arguments that can be adapted easily to new situations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

To motivate our work, we start with an elementary concentration inequality for a product of independent random numbers. We will generalize this bound, and others, to the matrix setting.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Context: A Product of Random Numbers Near $1$", "weight": 1.0} -->

Consider an independent family ${\{ X_{1},X_{2},\ldots\}} \subset {\mathbb{R}}$ of bounded random variables that satisfy

<!-- chunk {"id": "body-0010", "role": "body", "section": "Context: A Product of Random Numbers Near $1$", "weight": 1.0} -->

We anticipate that the random product $Z_{n}$ concentrates around its expectation ${{\mathbb{E}}Z_{n}} \approx e^{\mu}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Context: A Product of Random Numbers Near $1$", "weight": 1.0} -->

To check this surmise, we can use standard methods from scalar concentration theory. For $s > 0$,

<!-- chunk {"id": "body-0012", "role": "body", "section": "Context: A Product of Random Numbers Near $1$", "weight": 1.0} -->

The inequality follows from the numerical fact ${1 + a} \leq e^{a}$, valid for $a \in {\mathbb{R}}$. Hoeffding's inequality furnishes the bound

<!-- chunk {"id": "body-0013", "role": "body", "section": "Context: A Product of Random Numbers Near $1$", "weight": 1.0} -->

At the small scale $s \leq e$, in which case ${\log{({1 + s})}} \geq {s/e}$, the growth bound (2.1)

<!-- chunk {"id": "body-0014", "role": "body", "section": "Context: A Product of Random Numbers Near $1$", "weight": 1.0} -->

A similar inequality holds for the lower tail.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Product of Random Perturbations of the Identity", "weight": 1.0} -->

We might hope that products of random matrices exhibit a similar behavior. Consider an independent family ${\{{\mathbf{X}}_{1},\ldots,{\mathbf{X}}_{n}\}} \subset {\mathbb{M}}_{d}$ of $d \times d$ matrices that satisfy

<!-- chunk {"id": "body-0016", "role": "body", "section": "Product of Random Perturbations of the Identity", "weight": 1.0} -->

Here are elsewhere, $\left. \parallel \cdot \parallel \right.$ is the spectral norm, that is, the $\ell_{2}$ operator norm.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Product of Random Perturbations of the Identity", "weight": 1.0} -->

These speculations are correct. Moreover, we can obtain bounds that parallel the scalar inequalities announced in the last subsection. Here is one particular result that follows from our analysis.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Additional Results", "weight": 1.0} -->

We establish a family of norm inequalities for products of random matrices. The main result, Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"), gives a bound for the moments of a Schatten $p$-norm of a random product and a centered random product. From this fact, we derive expectation bounds, tail bounds, and matrix concentration inequalities. Many of these results hold under weaker assumptions than Theorem I. ‣ 2.2. A Product of Random Perturbations of the Identity ‣ 2. Contributions ‣ Matrix Concentration for Products"), addressing cases where the matrices have different means or are unbounded.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Additional Results", "weight": 1.0} -->

To give a better indication of what we can prove, let us give an informal presentation of one of our main results, Corollary 5.4. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"). The statement concerns a general product ${\mathbf{Z}}_{n} = {{\mathbf{Y}}_{n}\cdots{\mathbf{Y}}_{1}}$ of independent random matrices of dimension $d$. Abbreviating $p = {1 + {2{\log d}}}$, we have the inequality

<!-- chunk {"id": "body-0020", "role": "body", "section": "Additional Results", "weight": 1.0} -->

We can interpret $v$ as the accumulated relative variance in the product.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Additional Results", "weight": 1.0} -->

For example, in the setting of Theorem I. ‣ 2.2. A Product of Random Perturbations of the Identity ‣ 2. Contributions ‣ Matrix Concentration for Products"), the quantity $v = {O{({b^{2}/n})}}$. It follows that

<!-- chunk {"id": "body-0022", "role": "body", "section": "Roadmap", "weight": 1.0} -->

We continue with an overview of related work in Section 3. Section 4 presents background results from matrix theory and high-dimensional probability. We establish our main results for general matrix products in Section 5. Afterward, Section 6 draws corollaries for a product of perturbations of the identity. Finally, we describe some refinements and extensions in Section 7.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Direct Connections", "weight": 1.0} -->

The most immediate precedent for our research is the recent paper of Henriksen and Ward. They were motivated by the problem of understanding streaming algorithms for covariance estimation. Their work gives, perhaps, the first explicit nonasymptotic bounds for a somewhat general product of random matrices with fixed dimension. The argument is based on the matrix Bernstein inequality and a combinatorial fact about set partitions.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Direct Connections", "weight": 1.0} -->

Henriksen and Ward focus on the setting of Theorem I. ‣ 2.2. A Product of Random Perturbations of the Identity ‣ 2. Contributions ‣ Matrix Concentration for Products"), and they establish a bound of the form

<!-- chunk {"id": "body-0025", "role": "body", "section": "Direct Connections", "weight": 1.0} -->

In contrast, our new result (2.7) replaces the worst-case factor $e^{b}$ with the more typical value $e^{\mu}$. We are also able to relax several of the assumptions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Direct Connections", "weight": 1.0} -->

Also in the setting of Theorem I. ‣ 2.2. A Product of Random Perturbations of the Identity ‣ 2. Contributions ‣ Matrix Concentration for Products"), several works obtain results on the asymptotic behavior of ${\mathbf{Z}}_{n}$. Berger establishes, via a semigroup argument based on the Chernoff product formula, that ${\mathbf{Z}}_{n}\rightarrow e^{\mathbf{A}}$ in probability as $n\rightarrow\infty$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Direct Connections", "weight": 1.0} -->

Emme and Hubert recently obtained a refinement of this result: motivated by a problem in ergodic theory, they show that ${\mathbf{Z}}_{n}\rightarrow e^{\mathbf{A}}$ as $n\rightarrow\infty$ under the sole assumptions that ${\sum_{i = 1}^{n}{{\mathbf{X}}_{i}/n}}\rightarrow{\mathbf{A}}$ and ${\sum_{i = 1}^{n}{{\|{\mathbf{X}}_{i}\|}/n}} < \infty$. Their argument expands the product and computes the limit of the $k$th order term using an induction. Neither approach readily yields nonasymptotic bounds.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Other Recent Applications", "weight": 1.0} -->

Some applied work on random matrix products has been driven by the empirical observation that stochastic gradient descent converges faster when the gradient approximations are sampled *without* replacement, rather than sampled *with* replacement. Some papers that investigate this question from the point of view of (nonasymptotic) matrix inequalities include. This specific problem has been solved by Gürbüzbalaban et al. using optimization theory. However, none of these results directly address the questions at hand.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Other Recent Applications", "weight": 1.0} -->

Researchers studying randomly initialized deep neural networks have also developed theoretical analysis for products of random matrices; see. These results involve operations on matrices with independent entries, and they focus on the large-matrix limit.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Ergodic Theory and Control Theory", "weight": 1.0} -->

Products of random matrices describe the evolution of a linear stochastic dynamical system. For this reason, they have been a subject of perennial interest within the literatures on ergodic theory and on control theory. For the most part, this research is concerned with properties of the asymptotics of infinite products of matrices (of fixed size). Let us give a few more details.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Ergodic Theory and Control Theory", "weight": 1.0} -->

The *Lyapunov exponent* of the set $\mathcal{A}$ is the quantity

<!-- chunk {"id": "body-0032", "role": "body", "section": "Ergodic Theory and Control Theory", "weight": 1.0} -->

The Furstenberg--Kesten theorem establishes that $\lambda{(\mathcal{A})}$ exists almost surely, but approximating $\lambda{(\mathcal{A})}$ is algorithmically undecidable \[43, Thm. 2\]. As a consequence, we must be pessimistic about finding a completely satisfactory solution to the matrix concentration problem for products.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Ergodic Theory and Control Theory", "weight": 1.0} -->

To learn more about Lyapunov exponents and to find additional references, see the paper for work in control theory and the paper for work in ergodic theory. Another major application of random products is to study the asymptotic behavior of a random walk on a group; we refer the reader to for more information.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Random Matrix Theory and Free Probability", "weight": 1.0} -->

Products of random matrices have also been considered within random matrix theory and free probability. This connection is natural, but matrix products have received somewhat less attention than other kinds of random matrix models. In these contexts, it is common to study a product of a small number of matrices (two or three, say) in the limit as the dimension of the matrices grows.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Random Matrix Theory and Free Probability", "weight": 1.0} -->

Bai and Silverstein \[4, Chap. 4\] present a limit law for the sequence of products of a random matrix with iid entries and a random matrix whose spectral distribution has a deterministic limit. This theorem is motivated by a statistical application, multivariate analysis of variance. Note, however, that convergence of the spectral distribution does not determine the limit of the spectral norm.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Random Matrix Theory and Free Probability", "weight": 1.0} -->

Free probability gives a complete description of the spectral distribution of a product of two freely independent elements as the "multiplicative free convolution" of the spectral distributions of the factors. The connection to random matrix theory stems from the fact that a family of "adequately random" matrices becomes freely independent in the limit as the dimension of the matrices tends to infinity. See the book of Nica & Speicher for a digestible introduction; some other good treatments include. Free probability has significant applications in wireless communications.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Random Matrix Theory and Free Probability", "weight": 1.0} -->

For highly structured random matrices (invariant ensembles), it may be possible to obtain more detailed formulas for products. See for some recent work in this direction.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Random Matrix Inequalities via Uniform Smoothness", "weight": 1.0} -->

To analyze products of random matrices, we exploit classic methods that were developed to study the evolution of a martingale taking values in a uniformly smooth Banach space. These ideas are relevant for us because the matrix Schatten classes (with power $2 \leq p < \infty$) enjoy a remarkable uniform smoothness property.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Random Matrix Inequalities via Uniform Smoothness", "weight": 1.0} -->

In this section, we outline the required background from matrix analysis and high-dimensional probability. Naor's tutorial paper serves as a model for our presentation, and it contains a more general treatment. See Section 4.6 for additional discussion about the history of these ideas.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Uniform Smoothness for Matrices", "weight": 1.0} -->

Uniform smoothness ^11^1More precisely, we are considering uniformly smooth spaces whose modulus of smoothness has power type $2$. is a property of a normed space that describes how much the norm of a point changes under symmetric perturbation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Uniform Smoothness for Matrices", "weight": 1.0} -->

Remarkably, in other Schatten classes, the parallelogram law is replaced by an inequality.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Fact 4.1 (Uniform Smoothness for Schatten Classes)", "weight": 1.0} -->

Let $\mathbf{A},\mathbf{B}$ be matrices of the same size. For $p \geq 2$,

<!-- chunk {"id": "body-0043", "role": "body", "section": "Fact 4.1 (Uniform Smoothness for Schatten Classes)", "weight": 1.0} -->

The optimal constant $C_{p}:={p - 1}$. The inequality is reversed when $1 \leq p \leq 2$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Fact 4.1 (Uniform Smoothness for Schatten Classes)", "weight": 1.0} -->

Fact 4.1. ‣ 4.2. Uniform Smoothness for Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") was first established by Tomczak-Jaegermann; she obtained the sharp constant $C_{p}$ when $p$ is an even number. Ball, Carlen, and Lieb \[5, Thm. 1\] determined that $C_{p}$ is the optimal constant for all values of $p$. Throughout the paper, we will continue to write $C_{p} = {p - 1}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Uniform Smoothness for Random Matrices", "weight": 1.0} -->

Much as the Schatten class $S_{p}$ of matrices enjoys a uniform smoothness property, the normed space $L_{q}{(S_{p})}$ of random matrices is also uniformly smooth. When $2 \leq q \leq p$, this statement follows as an easy consequence of Fact 4.1. ‣ 4.2. Uniform Smoothness for Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products").

<!-- chunk {"id": "body-0046", "role": "body", "section": "Subquadratic Averages for Random Matrices", "weight": 1.0} -->

Corollary 4.2. ‣ 4.3. Uniform Smoothness for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") admits a powerful extension that controls how the norm of a matrix changes if we add a random matrix that has zero mean. This result is the main tool that we employ in our study of random products.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Matrix-Valued Martingales", "weight": 1.0} -->

To demonstrate the value of Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products"), let us explain how it leads to moment bounds for a matrix-valued martingale sequence. Consider a null matrix martingale ${\{{\mathbf{X}}_{1},\ldots,{\mathbf{X}}_{n}\}} \subset {\mathbb{M}}_{d}$ with difference sequence ${\{\mathbf{\Delta}_{1},\ldots,\mathbf{\Delta}_{n}\}} \subset {\mathbb{M}}_{d}$. That is,

<!-- chunk {"id": "body-0048", "role": "body", "section": "Matrix-Valued Martingales", "weight": 1.0} -->

Applying Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") repeatedly, we arrive at the bound

<!-- chunk {"id": "body-0049", "role": "body", "section": "Matrix-Valued Martingales", "weight": 1.0} -->

In words, the squared norm of the martingale is controlled by the sum of the squares of the norms of the martingale differences. The inequality (4.5) is a powerful extension of the orthogonality of the increments of a martingale taking values in an inner-product space, say $S_{2}$. The uniform smoothness constant $C_{p}$ shows how the geometry of the matrix space intermediates.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Matrix-Valued Martingales", "weight": 1.0} -->

In this work, we will develop bounds for random matrix products by applying a similar technique to appropriately chosen decompositions of the product.

<!-- chunk {"id": "body-0051", "role": "body", "section": "History", "weight": 1.0} -->

The approach in this section has a long history. Let us summarize the contributions that are most relevant to our development.

<!-- chunk {"id": "body-0052", "role": "body", "section": "History", "weight": 1.0} -->

For real numbers, the (sharp) uniform smoothness property in Fact 4.1. ‣ 4.2. Uniform Smoothness for Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") is known as the *two-point inequality*; it was established independently by Leonard Gross and Aline Bonami in the early 1970s, with later contributions by William Beckner. In 1974, the uniform smoothness property for the Schatten classes was obtained by Nicole Tomczak-Jaegermann. It took another 20 years before Ball, Carlen, and Lieb obtained the sharp uniform smoothness constants for all Schatten classes. The property dual to uniform smoothness is called *uniform convexity*. See for a detailed exposition.

<!-- chunk {"id": "body-0053", "role": "body", "section": "History", "weight": 1.0} -->

Tomczak-Jaegermann \[37, Thm. 3.1\] also demonstrated that Rademacher averages are subquadratic in each Schatten space $S_{p}$ with $p \geq 2$; that is, the Banach space $S_{p}$ is *type 2*. This fact is a prototype for the more general result stated in Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products"). Tropp \[39, Sec. 4.8\] points out that parts of the Ahlswede--Winter \[1, App.\] theory of sums of independent random matrices already follow from Tomczak-Jaegermann's work. (In contrast, Tropp's matrix concentration inequalities are more closely related to a fact from operator theory, the noncommutative Khintchine inequality of Françoise Lust-Piquard; Tropp's results are derived using a theorem \[24, Thm. 6\] of Elliot Lieb.)

<!-- chunk {"id": "body-0054", "role": "body", "section": "History", "weight": 1.0} -->

Assaf Naor traces the application of uniform convexity inequalities in the study of martingales to a 1975 paper of Gilles Pisier. Naor gives a nice introduction to this circle of ideas, which he uses to derive a general version of the Azuma inequality that holds in any uniformly smooth Banach space.

<!-- chunk {"id": "body-0055", "role": "body", "section": "History", "weight": 1.0} -->

At least as early as 1988, Donald Burkholder applied closely related convexity inequalities to derive sharp inequalities for martingales taking values in a Hilbert space. The paper of Éric Ricard and Quanhua Xu is a recent entry in this line of research.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Product of Independent Random Matrices", "weight": 1.0} -->

In this section, we obtain our main results on the growth and concentration of a product of independent random matrices. Section 5.1 shows how to decompose a random product into pieces that we can control using a recursive argument. Based on these ideas, we derive Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"), a general bound on the moments of the norm of the matrix product. The moment estimate leads to a family of expectation bounds (Corollary 5.4. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) and probability bounds (Corollary 5.6. ‣ 5.4. Tail Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Product of Independent Random Matrices", "weight": 1.0} -->

The balance of the paper contains applications of these results (Section 6) and extensions of the method to other settings (Section 7).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Decomposition of Random Products", "weight": 1.0} -->

Our approach is based on a recursive argument that describes how the product evolves as we include more factors. At each step, we decompose the product into a nonrandom term and a random term with mean zero. This formulation allows us to apply Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") on subquadratic averages.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Decomposition of Random Products", "weight": 1.0} -->

The property (5.2) supports the use of Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products").

<!-- chunk {"id": "body-0060", "role": "body", "section": "Decomposition of Random Products", "weight": 1.0} -->

The first relation follows from the operator ideal property of the Schatten $p$-norm and the statistical independence of the random matrices ${\mathbf{Y}}_{i}$ and ${\mathbf{Z}}_{i - 1}$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Decomposition of Random Products", "weight": 1.0} -->

As in (5.2), the second term is a fluctuation that is conditionally zero mean. The fluctuation term satisfies the norm bound (5.3).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Growth and Concentration", "weight": 1.0} -->

Our main result controls the growth of the moments of a product of independent random matrices. It also describes how well the random product concentrates around its expectation.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 5.2 (Growth from Concentration)", "weight": 1.0} -->

In some instances, we can improve over the growth bound (5.5. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) by applying the triangle inequality to the decomposition ${\mathbf{Z}}_{n} = {{({{\mathbb{E}}{\mathbf{Z}}_{n}})} + {({{\mathbf{Z}}_{n} - {{\mathbb{E}}{\mathbf{Z}}_{n}}})}}$ and invoking the concentration bound (5.6. ‣ 5.2. Growth and Concentration ‣ 5.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 5.2 (Growth from Concentration)", "weight": 1.0} -->

Similarly, we can apply Proposition 4.3. ‣ 4.4. Subquadratic Averages for Random Matrices ‣ 4. Random Matrix Inequalities via Uniform Smoothness ‣ Matrix Concentration for Products") together with (5.6. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) to obtain

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 5.2 (Growth from Concentration)", "weight": 1.0} -->

Neither of these bounds represents a strict improvement over the other or over the growth bound (5.5. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 5.3 (Uniform Bounds on Factors)", "weight": 1.0} -->

Compare these results with (5.5. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")), (5.6. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")), and (5.8). As for the proof, the growth bound (5.9. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) is an immediate consequence of the definition ${\mathbf{Z}}_{n} = {{\mathbf{Y}}_{n}\cdots{\mathbf{Y}}_{1}{\mathbf{Z}}_{0}}$. The concentration result (5.10. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) follows if we repeat the proof of (5.6.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 5.3 (Uniform Bounds on Factors)", "weight": 1.0} -->

‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")), using the growth bound (5.9. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) in place of (5.5. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Expectation Bounds for the Spectral Norm", "weight": 1.0} -->

In many cases, we just need to know the expected value of the product $\left\| {\mathbf{Z}}_{n} \right\|$ or the expected value of the fluctuation $\left\| {{\mathbf{Z}}_{n} - {{\mathbb{E}}{\mathbf{Z}}_{n}}} \right\|$. We can obtain bounds for these quantities as an easy consequence of Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products").

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 5.5 (Uniform Bounds on Factors)", "weight": 1.0} -->

This improves the constant in (5.12. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) by a factor of $\sqrt{e}$, and it removes the condition that ${v{({1 + {2{\log d}}})}} \leq 1$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Tail Bounds for the Spectral Norm", "weight": 1.0} -->

The moment bounds in Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products") can also be upgraded to obtain tail bounds for $\left\| {\mathbf{Z}}_{n} \right\|$ and $\left\| {{\mathbf{Z}}_{n} - {{\mathbb{E}}{\mathbf{Z}}_{n}}} \right\|$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 5.7 (Uniform Bounds on Factors)", "weight": 1.0} -->

In the setting of Remark 5.5. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products"), we have an unconditional variant of the concentration bound (5.14. ‣ 5.4. Tail Bounds for the Spectral Norm ‣ 5.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Application: Random Perturbations of the Identity", "weight": 1.0} -->

This section treats the fundamental case where the factors ${\mathbf{Y}}_{i}$ in the product are independent, random perturbations of the identity. That is, ${\mathbf{Y}}_{i} = {\mathbf{I} + {\mathbf{X}}_{i}}$ where ${\{{\mathbf{X}}_{i}\}} \subset {\mathbb{M}}_{d}$ is an independent family. We will develop specialized theory for this class of problems, and we will use these results to compare our work with several recent papers.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Iterative Algorithms", "weight": 1.0} -->

To motivate this development, observe that random perturbations of the identity arise from the analysis of the iterative scheme

<!-- chunk {"id": "body-0074", "role": "body", "section": "Iterative Algorithms", "weight": 1.0} -->

where ${\mathbf{X}}_{i}{\mathbf{u}}^{(i)}$ is a linear update to the current iterate ${\mathbf{u}}^{(i)}$. In this application, the norm of each ${\mathbf{X}}_{i}$ is proportional to the step size of the scheme, so it is typically small and it is controlled by the user. For example, the updates in Oja's algorithm take the form (6.1).

<!-- chunk {"id": "body-0075", "role": "body", "section": "Iterative Algorithms", "weight": 1.0} -->

For now, we do not permit the random matrix ${\mathbf{X}}_{i}$ to depend on the sequence $\{{\mathbf{u}}^{(i)}\}$ of iterates. Later, in Section 7.3, we describe an extension of our approach to the setting where $\{{\mathbf{X}}_{i}\}$ is an adapted sequence. This variant allows for the study of a wider class of iterative algorithms.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Bounds for the Product", "weight": 1.0} -->

First, we develop bounds for the growth and concentration of a product of perturbations of the identity. In Section 6.4, we develop results for the inverse of the product.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Comparison with Prior Work", "weight": 1.0} -->

To clarify the meaning of Corollary 6.1. ‣ 6.2. Bounds for the Product ‣ 6. Application: Random Perturbations of the Identity ‣ Matrix Concentration for Products"), let us elaborate what it predicts when

<!-- chunk {"id": "body-0078", "role": "body", "section": "Comparison with Prior Work", "weight": 1.0} -->

This situation can arise if we perform $n$ iterations of the iterative scheme (6.1) with a uniform step size of $1/n$. In this setting, Corollary 6.1. ‣ 6.2. Bounds for the Product ‣ 6. Application: Random Perturbations of the Identity ‣ Matrix Concentration for Products") implies that

<!-- chunk {"id": "body-0079", "role": "body", "section": "Comparison with Prior Work", "weight": 1.0} -->

For $\delta \in {\lbrack 0,1\rbrack}$, with probability at least $1 - \delta$,

<!-- chunk {"id": "body-0080", "role": "body", "section": "Comparison with Prior Work", "weight": 1.0} -->

Furthermore, if we assume that $\left\| {\mathbf{X}}_{i} \right\| \leq {T/n}$ almost surely for each $i$, then Remark 5.5. ‣ 5.3. Expectation Bounds for the Spectral Norm ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products") implies that (6.6) and (6.7) hold without restriction.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Comparison with Prior Work", "weight": 1.0} -->

The paper of Henriksen and Ward only contemplates the situation described in the last paragraph. It obtains a concentration bound of the form

<!-- chunk {"id": "body-0082", "role": "body", "section": "Comparison with Prior Work", "weight": 1.0} -->

The salient improvement in (6.7) stems from the reduction of the factor $e^{L}$ to $e^{T}$. This difference is most pronounced when ${{\mathbb{E}}{\mathbf{X}}_{i}} = 0$ for each $i$, in which case the bound (6.7) removes the exponential factor entirely. Even under the assumption that ${\mathbf{X}}_{i} \succcurlyeq \mathbf{0}$ for all each $i$, it can happen that $L \geq {dT}$, so this refinement can make a big difference.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Comparison with Prior Work", "weight": 1.0} -->

Last, we mention one instance that has special importance. Let ${\mathbf{A}} \in {\mathbb{M}}_{d}$ be a fixed matrix. Consider a triangular array ${\{{\mathbf{X}}_{i}^{(n)}:{{i \leq n}\text{~and~}{n \in {\mathbb{N}}}}\}} \subset {\mathbb{M}}_{d}$ of independent random matrices. For each index $n$, assume that

<!-- chunk {"id": "body-0084", "role": "body", "section": "Comparison with Prior Work", "weight": 1.0} -->

The bound (6.7), combined with the first Borel--Cantelli Lemma, guarantees that

<!-- chunk {"id": "body-0085", "role": "body", "section": "Comparison with Prior Work", "weight": 1.0} -->

This result is a special case of the limit theorem of Emme and Hubert \[13, Thm. 1.1\]. They do not require independence, but they only achieve an asymptotic result. Our analysis gives a rate of convergence that matches the corresponding bound (2.2) for scalar random variables.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Bounds for the Inverse of a Product", "weight": 1.0} -->

In some applications, it is valuable to have a lower bound for the minimum singular value of a random product. Equivalently, we can seek an upper bound for the spectral norm of the inverse of the product. This section describes a situation where clean results are possible.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Bounds for the Inverse of a Product", "weight": 1.0} -->

Consider the case where the factors ${\mathbf{Y}}_{i}$ are perturbations of the identity: ${\mathbf{Y}}_{i} = {\mathbf{I} + {\mathbf{X}}_{i}}$, where ${\mathbf{X}}_{i}$ is small enough to ensure that ${\mathbf{Y}}_{i}$ is invertible with probability $1$. In this setting, we can easily study the inverse of the product using Corollary 6.1. ‣ 6.2. Bounds for the Product ‣ 6. Application: Random Perturbations of the Identity ‣ Matrix Concentration for Products").

<!-- chunk {"id": "body-0088", "role": "body", "section": "Improvements and Extensions", "weight": 1.0} -->

The argument underlying Theorem 5.1. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products") has several natural extensions. First, we develop sharper results for products of random contractions. In Section 7.2, we derive better estimates for a matrix product where the initial term is rectangular. In Section 7.3, we document the changes that are necessary in case the factors in the product are not independent but form an adapted sequence. Last, In Section 7.4, we explain how to develop a bound on the spectral radius of a product.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Product of Contractions", "weight": 1.0} -->

Most of our results are designed for products of general random matrices. In some circumstances, the factors in the product are *contractions*, matrices whose singular values are bounded by one. For example, the randomized Kaczmarz algorithm can be expressed as the repeated application of random contractions. Other randomized linear fixed-point iterations take a similar form. This section derives sharper estimates for this important setting.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Low-Rank Products", "weight": 1.0} -->

So far, we have focused on the setting where the initial matrix ${\mathbf{Z}}_{0} = \mathbf{I}$. In many applications, we are interested in the action of the random product ${{\mathbf{Y}}_{n}\cdots{\mathbf{Y}}_{1}} \in {\mathbb{M}}_{d}$ on a specific matrix ${\mathbf{Z}}_{0} \in {\mathbb{C}}^{d \times r}$ with relatively few columns. In this case, the terms that the control the behavior of the product may be significantly smaller. Here is an example of the kinds of results one can achieve.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Adapted Sequences", "weight": 1.0} -->

We can easily generalize our results on a product of independent random matrices to a product of adapted random matrices. This kind of extension is valuable for studying iterative algorithms where the choices made by the algorithm at a given step depend on the history of the iteration.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Adapted Sequences", "weight": 1.0} -->

We consider an adapted sequence ${\{{\mathbf{Y}}_{1},\ldots,{\mathbf{Y}}_{n}\}} \subset {\mathbb{M}}_{d}$ of random matrices; that is, each ${\mathbf{Y}}_{i}$ is measurable with respect to $\mathcal{F}_{i}$. The next result provides information about the growth and concentration properties of the product ${\mathbf{Z}}_{n} = {{\mathbf{Y}}_{n}\cdots{\mathbf{Y}}_{1}}$. Note that the natural concentration result compares ${\mathbf{Z}}_{n}$ with a product of conditional expectations, rather than the expectation of the product.

<!-- chunk {"id": "body-0093", "role": "body", "section": "The Spectral Radius", "weight": 1.0} -->

Products of matrices are closely related to the evolution of discrete-time linear dynamical systems. In this context, it may be more natural to study the *spectral radius* of the matrix product, rather than its spectral norm. Bounds for the spectral radius follow as corollary of our work, owing to the following classical fact.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Fact 7.5 (Schur)", "weight": 1.0} -->

Let $\mathbf{M} \in {\mathbb{M}}_{d}$ be a square matrix. The spectral radius $\varrho{(\mathbf{M})}$ is defined as the maximum absolute value of an eigenvalue of $\mathbf{M}$. It satisfies the variational principle

<!-- chunk {"id": "body-0095", "role": "body", "section": "Fact 7.5 (Schur)", "weight": 1.0} -->

The infimum takes place over all invertible matrices $\mathbf{S}$. In particular ${\varrho{(\mathbf{M})}} \leq \left\| \mathbf{M} \right\|$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Fact 7.5 (Schur)", "weight": 1.0} -->

Let us give an indication of the kinds of results that are possible.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Prospects", "weight": 1.0} -->

We have developed a collection of nonasymptotic bounds for products of random matrices. These results hold under simple and easily verifiable conditions, and they give accurate predictions about the behavior of some particular instances (e.g., products of iid random perturbations of the identity). The proofs are based on foundational results about the geometry of the Schatten classes, and they can easily be adapted to treat variants of the problems under consideration.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Prospects", "weight": 1.0} -->

A disappointing feature of our results is that they do not account for interactions between the matrix factors. For example, when ${\mathbf{Y}}_{i} = {\mathbf{I} + {{\mathbf{X}}_{i}/n}}$ for bounded, independent matrix perturbations ${\mathbf{X}}_{i}$, we have shown that

<!-- chunk {"id": "body-0099", "role": "body", "section": "Prospects", "weight": 1.0} -->

However, when the matrices ${\mathbf{X}}_{i}$ commute almost surely, it is easy to show the sharper bound

<!-- chunk {"id": "body-0100", "role": "body", "section": "Prospects", "weight": 1.0} -->

but the error term is not sharp. This type of bound would echo Tropp's improvements to the Ahlswede--Winter results for a sum of independent random matrices. At present, it is not clear whether this refinement is possible, nor what technical arguments would lead there.
