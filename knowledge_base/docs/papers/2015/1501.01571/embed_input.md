<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Introduction to Matrix Concentration Inequalities

Topics include Graphs, Matrix concentration inequalities, Random matrix.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In recent years, random matrices have come to play a major role in computational mathematics, but most of the classical areas of random matrix theory remain the province of experts. Over the last decade, with the advent of matrix concentration inequalities, research has advanced to the point where we can conquer many (formerly) challenging problems with a page or two of arithmetic. The aim of this monograph is to describe the most successful methods from this area along with some interesting examples that these techniques can illuminate.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Random matrix theory has grown into a vital area of probability, and it has found applications in many other fields. To motivate the results in this monograph, we begin with an overview of the connections between random matrix theory and computational mathematics. We introduce the basic ideas underlying our approach, and we state one of our main results on the behavior of random matrices. As an application, we examine the properties of the sample covariance estimator, a random matrix that arises in statistics. Afterward, we summarize the other types of results that appear in these notes, and we assess the novelties in this presentation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Historical Origins", "weight": 1.0} -->

Random matrix theory sprang from several different sources in the first half of the 20th century.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Historical Origins", "weight": 1.0} -->

- Geometry of Numbers. Peter Forrester [, p. v] traces the field of random matrix theory to work of Hurwitz, who defined the invariant integral over a Lie group. Specializing this analysis to the orthogonal group, we can reinterpret this integral as the expectation of a function of a uniformly random orthogonal matrix. - Multivariate Statistics. Another early example of a random matrix appeared in the work of John Wishart. Wishart was studying the behavior of the sample covariance estimator for the covariance matrix of a multivariate normal random vector. He showed that the estimator, which is a random matrix, has the distribution that now bears his name. Statisticians have often used random matrices as models for multivariate data. - Numerical Linear Algebra. In their remarkable work [vNG47,] on computational methods for solving systems of linear equations, von Neumann and Goldstine considered a random matrix model for the floating-point errors that arise from an LU decomposition. 1 They obtained a high-probability bound for the norm of the random matrix, which they 1 von Neumann and Goldstine invented and analyzed this algorithm before they had any digital computer on which to implement it!

<!-- chunk {"id": "body-0006", "role": "body", "section": "Historical Origins", "weight": 1.0} -->

See for a historical account. took as an estimate for the error the procedure might typically incur. Curiously, in subsequent years, numerical linear algebraists became very suspicious of probabilistic techniques, and only in recent years have randomized algorithms reappeared in this field. See the surveys for more details and references.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Historical Origins", "weight": 1.0} -->

Nuclear Physics. In the early 1950s, physicists had reached the limits of deterministic analytical techniques for studying the energy spectra of heavy atoms undergoing slow nuclear reactions. Eugene Wigner was the first researcher to surmise that a random matrix with appropriate symmetries might serve as a suitable model for the Hamiltonian of the quantummechanicalsystemthatdescribes the reaction. The eigenvalues of this random matrix model the possible energy levels of the system. See Mehta's book [, §1.1] for an account of all this.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Historical Origins", "weight": 1.0} -->

In each area, the motivation was quite different and led to distinct sets of questions. Later, random matrices began to percolate into other fields such as graph theory (the Erd˝ os-Rényi model for a random graph) and number theory (as a model for the spacing of zeros of the Riemann zeta function ).

<!-- chunk {"id": "body-0009", "role": "body", "section": "The Modern Random Matrix", "weight": 1.0} -->

By now, random matrices are ubiquitous. They arise throughout modern mathematics and statistics, as well as in many branches of science and engineering. Random matrices have several different purposes that we may wish to distinguish. They can be used within randomized computer algorithms; they serve as models for data and for physical phenomena; and they are subjects of mathematical inquiry. This section offers a taste of these applications. Note that the ideas and references here reflect the author's interests, and they are far from comprehensive!

<!-- chunk {"id": "body-0010", "role": "body", "section": "Algorithmic Applications", "weight": 1.0} -->

The striking mathematical properties of random matrices can be harnessed to develop algorithms for solving many different problems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Algorithmic Applications", "weight": 1.0} -->

Computing Matrix Approximations. Random matrices can be used to develop fast algorithms for computing a truncated singular-value decomposition. In this application, we multiply a large input matrix by a smaller random matrix to extract information about the dominant singular vectors of the input matrix. The seed of this idea appears in [, DFK ⊕ 99]. The survey explains how to implement this method in practice, while the two monographs cover more theoretical aspects.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Algorithmic Applications", "weight": 1.0} -->

Sparsification. One way to accelerate spectral computations on large matrices is to replace the original matrix by a sparse proxy that has similar spectral properties. An elegant way to produce the sparse proxy is to zero out entries of the original matrix at random while rescaling the entries that remain. This approach was proposed, and the papers contain recent innovations. Related ideas play an important role in Spielman and Teng's work on fast algorithms for solving linear systems.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Algorithmic Applications", "weight": 1.0} -->

Subsampling of Data. In large-scale machine learning, one may need to subsample data randomly to reduce the computational costs of fitting a model. For instance, we can combine random sampling with the Nyström decomposition to obtain a randomized approximation of a kernel matrix. This method was introduced by Williams & Seeger. The paper provides the first theoretical analysis, and the survey contains more complete results.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Algorithmic Applications", "weight": 1.0} -->

Dimension Reduction. A basic template in the theory of algorithms invokes randomized projection to reduce the dimension of a computational problem. Many types of dimension reduction are based on properties of random matrices. The two papers established the mathematical foundations of this approach. The earliest applications in computer science appear in the work. Many contemporary variants depend on ideas and.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Algorithmic Applications", "weight": 1.0} -->

Combinatorial Optimization. One approach to solving a computationally difficult optimization problem is to relax (i.e., enlarge) the constraint set so the problem becomes tractable, to solve the relaxed problem, and then to use a randomized procedure to map the solution back to the original constraint set [, §4.3]. This technique is called relaxation and rounding. For hard optimization problems involving a matrix variable, the analysis of the rounding procedure often involves ideas from random matrix theory.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Algorithmic Applications", "weight": 1.0} -->

Compressed Sensing. When acquiring data about an object with relatively few degrees of freedomascompared with the ambient dimension, we may be able to sieve out the important information from the object by taking a small number of random measurements, where the number of measurements is comparable to the number of degrees of freedom [GGI ⊕ 02 ]. This observation is now referred to as compressed sensing. Randommatrices play a central role in the design and analysis of measurement procedures. For example, see.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Modeling", "weight": 1.0} -->

Random matrices also appear as models for multivariate data or multivariate phenomena. By studying the properties of these models, we may hope to understand the typical behavior of a data-analysis algorithm or a physical system.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Modeling", "weight": 1.0} -->

Sparse Approximation for Random Signals. Sparse approximation has become an important problem in statistics, signal processing, machine learning and other areas. One model for a 'typical' sparse signal poses the assumption that the nonzero coefficients that generate the signal are chosen at random. When analyzing methods for identifying the sparse set of coefficients, we must study the behavior of a random column submatrix drawn from the model matrix.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Modeling", "weight": 1.0} -->

Demixing of Structured Signals. In data analysis, it is common to encounter a mixture of two structured signals, and the goal is to extract the two signals using prior information about the structures. A common model for this problem assumes that the signals are randomly oriented with respect to each other, which means that it is usually possible to discriminate the underlying structures. Random orthogonal matrices arise in the analysis of estimation techniques for this problem.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Modeling", "weight": 1.0} -->

Stochastic Block Model. One probabilistic framework for describing community structure in a network assumes that each pair of individuals in the same community has a relationship with high probability, while each pair of individuals drawn from different communities has a relationship with lower probability. This is referred to as the stochastic block model. It is quite common to analyze algorithms for extracting community structure from data by positing that this model holds. See for a recent contribution, as well as a summary of the extensive literature.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Modeling", "weight": 1.0} -->

High-Dimensional Data Analysis. More generally, random models are pervasive in the analysis of statistical estimation procedures for high-dimensional data. Random matrix theory plays a key role in this field.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Modeling", "weight": 1.0} -->

Wireless Communication. Random matrices are commonly used as models for wireless channels. See the book of Tulino and Verdú for more information.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Modeling", "weight": 1.0} -->

In these examples, it is important to recognize that random models may not coincide very well with reality, but they allow us to get a sense of what might be possible in some generic cases.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Theoretical Aspects", "weight": 1.0} -->

Randommatrices are frequently studied for their intrinsic mathematical interest. In some fields, they provide examples of striking phenomena. In other areas, they furnish counterexamples to 'intuitive' conjectures. Here are a few disparate problems where random matrices play a role.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Theoretical Aspects", "weight": 1.0} -->

Combinatorics. An expander graph has the property that every small set of vertices has edges linking it to a large proportion of the vertices. The expansion property is closely related to the spectral behavior of the adjacency matrix of the graph. The easiest construction of an expander involves a random matrix argument [, §9.2].

<!-- chunk {"id": "body-0026", "role": "body", "section": "Theoretical Aspects", "weight": 1.0} -->

Numerical Analysis. For worst-case examples, the Gaussian elimination method for solving a linear system is not numerically stable. In practice, however, stability problems rarely arise. One explanation for this phenomenon is that, with high probability, a small random perturbation of any fixed matrix is well conditioned. As a consequence, it can be shown that Gaussian elimination is stable for most matrices.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Theoretical Aspects", "weight": 1.0} -->

High-Dimensional Geometry. Dvoretzky's Theorem states that, when N is large, the unit ball of each N -dimensional Banach space has a slice of dimension n … log N that is close to a Euclidean ball with dimension n. It turns out that a random slice of dimension n realizes this property. This result can be framed as a statement about spectral properties of a random matrix.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Theoretical Aspects", "weight": 1.0} -->

QuantumInformation Theory. Random matrices appear as counterexamples for a number of conjectures in quantum information theory. Here is one instance. In classical information theory, the total amount of information that we can transmit through a pair of channels equals the sum of the information we can send through each channel separately. It was conjectured that the same property holds for quantum channels. In fact, a pair of quantum channels can have strictly larger capacity than a single channel. This result depends on a random matrix construction. See for related work.

<!-- chunk {"id": "body-0029", "role": "body", "section": "RandomMatrices for the People", "weight": 1.0} -->

Historically, random matrix theory has been regarded as a very challenging field. Even now, many well-established methods are only comprehensible to researchers with significant experience, and it may take months of intensive effort to prove new results. There are a small number of classes of random matrices that have been studied so completely that we know almost everything about them. Yet, moving beyond this terra firma, one quickly encounters examples where classical methods are brittle.

<!-- chunk {"id": "body-0030", "role": "body", "section": "RandomMatrices for the People", "weight": 1.0} -->

We hope to democratize random matrix theory. These notes describe tools that deliver useful information about a wide range of random matrices. In many cases, a modest amount of straightforward arithmetic leads to strong results. The methods here should be accessible to computational scientists working in a variety of fields. Indeed, the techniques in this work have already found an extensive number of applications.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Basic Questions in Random Matrix Theory", "weight": 1.0} -->

Random matrices merit special attention because they have spectral properties that are quite different from familiar deterministic matrices. Here are some of the questions we might want to investigate.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Basic Questions in Random Matrix Theory", "weight": 1.0} -->

- What is the expectation of the maximum eigenvalue of a random Hermitian matrix? What about the minimum eigenvalue? - How is the maximum eigenvalue of a random Hermitian matrix distributed? What is the probability that it takes values substantially different from its mean? What about the minimumeigenvalue? - What is the expected spectral norm of a random matrix? What is the probability that the norm takes a value substantially different from its mean? - What about the other eigenvalues or singular values? Can we say something about the 'typical' spectrum of a random matrix? - Can we say anything about the eigenvectors or singular vectors? For instance, is each one distributed almost uniformly on the sphere? - Wecanalsoask questions about the operator norm of a random matrix acting as a map between two normed linear spaces. In this case, the geometry of the domain and codomain play a role.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Basic Questions in Random Matrix Theory", "weight": 1.0} -->

In this work, we focus on the first three questions above. We study the expectation of the extreme eigenvalues of a random Hermitian matrix, and we attempt to provide bounds on the probability that they take an unusual value. As an application of these results, we can control the expected spectral norm of a general matrix and bound the probability of a large deviation. These are the most relevant problems in many (but not all!) applications. The remaining questions are also important, but we will not touch on them here. We recommend the book for a friendly introduction to other branches of random matrix theory.

<!-- chunk {"id": "body-0034", "role": "body", "section": "RandomMatrices as Independent Sums", "weight": 1.0} -->

Our approach to random matrices depends on a fundamental principle: In applications, it is common that a random matrix can be expressed as a sum of independent random matrices.

<!-- chunk {"id": "body-0035", "role": "body", "section": "RandomMatrices as Independent Sums", "weight": 1.0} -->

The examples that appear in these notes should provide ample evidence for this claim. For now, let us describe a specific problem that will serve as an illustration throughout the Introduction. We hope this example is complicated enough to be interesting but simple enough to elucidate the main points.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example: The Sample Covariance Estimator", "weight": 1.0} -->

Let x ∅ (X 1,..., Xp) be a complex random vector with zero mean: E x ∅ 0. The covariance matrix A of the random vector x is the positive-semidefinite matrix The star / refers to the conjugate transpose operation, and the standard basis matrix E j k has a one in the (j, k) position and zeros elsewhere. In other words, the (j, k) entry of the sample covariance matrix A records the covariance between the j th and k th entry of the vector x.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example: The Sample Covariance Estimator", "weight": 1.0} -->

One basic problem in statistical practice is to estimate the covariance matrix from data. Imagine that we have access to n independent samples x 1,..., x n, each distributed the same way as x. The sample covariance estimator Y is the random matrix The random matrix Y is an unbiased estimator 2 for the sample covariance matrix: E Y ∅ A. Observe that the sample covariance estimator Y fi ts neatly into our paradigm: The sample covariance estimator can be expressed as a sum of independent randommatrices.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example: The Sample Covariance Estimator", "weight": 1.0} -->

This is precisely the type of decomposition that allows us to apply the tools in these notes.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Exponential Concentration Inequalities for Matrices", "weight": 1.0} -->

An important challenge in probability theory is to study the probability that a real random variable Z takes a value substantially different from its mean. That is, we seek a bound of the form 2 The formula (1.5.2) supposes that the random vector x is known to have zero mean. Otherwise, we have to make an adjustment to incorporate an estimate for the sample mean. for a positive parameter t. When Z is expressed as a sum of independent random variables, the literature contains many tools for addressing this problem. See for an overview.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Exponential Concentration Inequalities for Matrices", "weight": 1.0} -->

For a random matrix Z, a variant of (1.6.1) is the question of whether Z deviates substantially from its mean value. We might frame this question as Here and elsewhere, κ′κ denotes the spectral norm of a matrix. As noted, it is frequently possible to decompose Z as a sum of independent random matrices. We might even dream that established methods for studying the scalar concentration problem (1.6.1) extend to (1.6.2).

<!-- chunk {"id": "body-0041", "role": "body", "section": "The Bernstein Inequality", "weight": 1.0} -->

To explain what kind of results we have in mind, let us return to the scalar problem (1.6.1). First, to simplify formulas, we assume that the real random variable Z has zero mean: E Z ∅ 0. If not, we can simply center the random variable by subtracting its mean. Second, and more restrictively, we suppose that Z can be expressed as a sum of independent, real random variables.

<!-- chunk {"id": "body-0042", "role": "body", "section": "The Bernstein Inequality", "weight": 1.0} -->

To control Z, we rely on two types of information: global properties of the sum (such as its meanandvariance) and local properties of the summands (such as their maximum fluctuation). These pieces of data are usually easy to obtain. Together, they determine how well Z concentrates around zero, its mean value.

<!-- chunk {"id": "body-0043", "role": "body", "section": "The Bernstein Inequality", "weight": 1.0} -->

Theorem 1.6.1 (Bernstein Inequality). Let S 1,..., Sn be independent, centered, real random variables, and assume that each one is uniformly bounded: Introduce the sum Z ∅ P n k ∅ 1 Sk, and let v (Z) denote the variance of the sum: See [, §2.8] for a proof of this result. We refer to Theorem 1.6.1 as an exponential concentration inequality because it yields exponentially decaying bounds on the probability that Z deviates substantially from its mean.

<!-- chunk {"id": "body-0044", "role": "body", "section": "The Matrix Bernstein Inequality", "weight": 1.0} -->

What is truly astonishing is that the scalar Bernstein inequality, Theorem 1.6.1, lifts directly to matrices. Let us emphasize this remarkable fact: There are exponential concentration inequalities for the spectral norm of a sum of independent random matrices.

<!-- chunk {"id": "body-0045", "role": "body", "section": "The Matrix Bernstein Inequality", "weight": 1.0} -->

Then As a consequence, once we decompose a random matrix as an independent sum, we can harness global properties (such as the mean and the variance) and local properties (such as a uniform bound on the summands) to obtain detailed information about the norm of the sum. As in the scalar case, it is usually easy to acquire the input data for the inequality. But the output of the inequality is highly nontrivial.

<!-- chunk {"id": "body-0046", "role": "body", "section": "The Matrix Bernstein Inequality", "weight": 1.0} -->

To illustrate these claims, we will state one of the major results from this monograph. This theorem is a matrix extension of Bernstein's inequality that was developed independently in the two papers. After presenting the result, we give some more details about its interpretation. In the next section, we apply this result to study the covariance estimation problem.

<!-- chunk {"id": "body-0047", "role": "body", "section": "The Matrix Bernstein Inequality", "weight": 1.0} -->

Theorem 1.6.2 (Matrix Bernstein). Let S 1,..., S n be independent, centered random matrices with common dimension d 1 ≤ d 2, and assume that each one is uniformly bounded Introduce the sum and let v (Z) denote the matrix variance statistic of the sum: The proof of this result appears in Chapter 6.

<!-- chunk {"id": "body-0048", "role": "body", "section": "The Matrix Bernstein Inequality", "weight": 1.0} -->

To appreciate what Theorem 1.6.2 means, it is valuable to make a direct comparison with the scalar version, Theorem 1.6.1. In both cases, we express the object of interest as an independent sum, and we instate a uniform bound on the summands.

<!-- chunk {"id": "body-0049", "role": "body", "section": "The Matrix Bernstein Inequality", "weight": 1.0} -->

- The variance v (Z) in the result for matrices can be interpreted as the magnitude of the expected squared deviation of Z from its mean. The formula reflects the fact that a general matrix B has two different squares BB / and B / B. For an Hermitian matrix, the two squares coincide. - The tail bound has a dimensional factor d 1 ⊕ d 2 that depends on the size of the matrix. This factor reduces to two in the scalar setting. In the matrix case, it limits the range of t where the tail bound is informative. - We have included a bound for E κ Z κ. This estimate is not particularly interesting in the scalar setting, but it is usually quite challenging to prove results of this type for matrices. In fact, the expectation bound is often more useful than the tail bound.

<!-- chunk {"id": "body-0050", "role": "body", "section": "The Matrix Bernstein Inequality", "weight": 1.0} -->

The latter point deserves amplification: The expectation bound (1.6.6) is the most important aspect of the matrix Bernstein inequality.

<!-- chunk {"id": "body-0051", "role": "body", "section": "The Matrix Bernstein Inequality", "weight": 1.0} -->

For further discussion of this result, turn to Chapter 6. Chapters 4 and 7 contain related results and interpretations.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Example: The Sample Covariance Estimator", "weight": 1.0} -->

We will apply the matrix Bernstein inequality, Theorem 1.6.2, to measure how well the sample covariance estimator approximates the true covariance matrix. As before, let x be a zero-mean randomvector with dimension p. Introduce the p ≤ p covariance matrix A ∅ E (xx /). Suppose we have n independent samples x 1,..., x n with the same distribution as x. Form the p ≤ p sample covariance estimator Our goal is to study how the spectral-norm distance κ Y ϒ A κ between the sample covariance and the true covariance depends on the number n of samples.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Example: The Sample Covariance Estimator", "weight": 1.0} -->

Weare in a situation where it is quite easy to see how the matrix Bernstein inequality applies. Define the random deviation Z of the estimator Y from the true covariance matrix A: The random matrices S k are independent, identically distributed, and centered. To apply Theorem 1.6.2, we need to find a uniform bound L for the summands, and we need to control the matrix variance statistic v (Z).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Example: The Sample Covariance Estimator", "weight": 1.0} -->

First, let us develop a uniform bound on the spectral norm of each summand. We may calculate that The first relation is the triangle inequality. The second follows from the assumption that x is bounded and the observation that This expression depends on Jensen's inequality and the hypothesis that x is bounded.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Example: The Sample Covariance Estimator", "weight": 1.0} -->

Second, we need to bound the matrix variance statistic v (Z) defined in (1.6.4). The matrix Z is Hermitian, so the two squares in this formula coincide with each other: Weneed to determine the variance of each summand. By direct calculation, The expression H ≼ T means that T ϒ H is positive semidefinite. We used the norm bound for the random vector x and the fact that expectation preserves the semidefinite order. In the last step, we dropped the negative-semidefinite term ϒ A 2. Summing this relation over k, we reach The matrix is positive-semidefinite because it is a sum of squares of Hermitian matrices. Extract the spectral norm to arrive at Wehave now collected the information we need to analyze the sample covariance estimator.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Example: The Sample Covariance Estimator", "weight": 1.0} -->

Wecan invoke the estimate (1.6.6) from the matrix Bernstein inequality, Theorem 1.6.2, with the uniform bound L ∅ 2 B / n and the variance bound v (Z) · B κ A κ / n. Weattain In other words, the error in approximating the sample covariance matrix is not too large when we have a sufficient number of samples. If we wish to obtain a relative error on the order of ", we may take It is often the case that B ∅ Const ′ p, so we discover that n ∅ Const ′ " ϒ 2 p log p samples are sufficient for the sample covariance estimator to provide a relatively accurate estimate of the true covariance matrix A. This bound is qualitatively sharp for worst-case distributions.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Example: The Sample Covariance Estimator", "weight": 1.0} -->

The analysis in this section applies to many other examples. We encapsulate the argument in Corollary 6.2.1, which we use to study several more problems.

<!-- chunk {"id": "body-0058", "role": "body", "section": "History of this Example", "weight": 1.0} -->

Covariance estimation may be the earliest application of matrix concentration tools in random matrix theory. Rudelson, building on a suggestion of Pisier, showed how to use the noncommutative Khintchine inequality to obtain essentially optimal bounds on the sample covariance estimator of a bounded random vector. The tutorial of Roman Vershynin offers an overview of this problem as well as many results and references. The analysis of the sample covariance matrix here is adapted from the technical. It leads to a result similar with the one Rudelson obtained.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Optimality of the Matrix Bernstein Inequality", "weight": 1.0} -->

Theorem 1.6.2 can be sharpened very little because it applies to every random matrix Z of the form (1.6.3). Let us say a few words about optimality now, postponing the details to §6.1.2.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Optimality of the Matrix Bernstein Inequality", "weight": 1.0} -->

Suppose that Z is a random matrix of the form (1.6.3). To make the comparison simpler, we also insist that each summand S k is a symmetric random variable; that is, S k and ϒ S k have the same distribution for each index k. Introduce the quantity In §6.1.2, we will argue that these assumptions imply In other words, the scale of E κ Z κ 2 must depend on the matrix variance statistic v (Z) and the average upper bound L 2 ? for the summands. The quantity L ∅ sup κ S k κ that appears in the matrix Bernstein inequality always exceeds L ?, sometimes by a large margin, but they capture the same type of information.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Optimality of the Matrix Bernstein Inequality", "weight": 1.0} -->

The significant difference between the lower and upper bound in (1.6.7) comes from the dimensional factor log( d 1 ⊕ d 2). There are random matrices Z for which the lower bound gives a more accurate reflection of E κ Z κ 2, but there are also many random matrices where the upper bound describes the behavior correctly. At present, there is no method known for distinguishing between these two extremes under the model (1.6.3) for the random matrix.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Optimality of the Matrix Bernstein Inequality", "weight": 1.0} -->

The tail bound (1.6.5) provides a useful tool in practice, but it is not necessarily the best way to collect information about large deviation probabilities. To obtain more precise results, we recommend using the expectation bound (1.6.6) to control E κ Z κ and then applying scalar concentration inequalities to estimate P { κ Z κ ÷ E κ Z κ⊕ t }. The book offers a good treatment of the methods that are available for establishing scalar concentration.

<!-- chunk {"id": "body-0063", "role": "body", "section": "The Arsenal of Results", "weight": 1.0} -->

The Bernstein inequality is probably the most familiar exponential tail bound for a sum of independent random variables, but there are many more. It turns out that essentially all of these scalar results admit extensions that hold for random matrices. In fact, many of the established techniques for scalar concentration have analogs in the matrix setting.

<!-- chunk {"id": "body-0064", "role": "body", "section": "What's Here", "weight": 1.0} -->

This monograph focuses on a few key exponential concentration inequalities for a sum of independent random matrices, and it describes some specific applications of these results.

<!-- chunk {"id": "body-0065", "role": "body", "section": "What's Here", "weight": 1.0} -->

Matrix Gaussian Series. A matrix Gaussian series is a random matrix that can be expressed as a sum of fixed matrices, each weighted by an independent standard normal random variable. This formulation includes a surprising number of examples. The most important are undoubtedly Wigner matrices and rectangular Gaussian matrices. Another interesting case is a Toeplitz matrix with Gaussian entries. The analysis of matrix Gaussian series appears in Chapter 4.

<!-- chunk {"id": "body-0066", "role": "body", "section": "What's Here", "weight": 1.0} -->

Matrix Rademacher Series. A matrix Rademacher series is a random matrix that can be written as a sum of fixed matrices, each weighted by an independent Rademacher random variable. 3 This construction includes things like random sign matrices, as well as a fixed matrix whose entries are modulated by random signs. There are also interesting examples that arise in combinatorial optimization. We treat these problems in Chapter 4.

<!-- chunk {"id": "body-0067", "role": "body", "section": "What's Here", "weight": 1.0} -->

Matrix Chernoff Bounds. ThematrixChernoff bounds apply to a random matrix that can be decomposed as a sum of independent, random positive-semidefinite matrices whose maximumeigenvalues are subject to a uniform bound. These results allow us to obtain information about the norm of a random submatrix drawn from a fixed matrix. They are also appropriate for studying the Laplacian matrix of a random graph. See Chapter 5.

<!-- chunk {"id": "body-0068", "role": "body", "section": "What's Here", "weight": 1.0} -->

Matrix Bernstein Bounds. The matrix Bernstein inequality concerns a random matrix that can be expressed as a sum of independent, centered random matrices that admit a uniform spectral-norm bound. This result has many applications, including the analysis of randomizedalgorithms for matrix sparsification and matrix multiplication. It can also be used to study the random features paradigm for approximating a kernel matrix. Chapter 6 contains this material.

<!-- chunk {"id": "body-0069", "role": "body", "section": "What's Here", "weight": 1.0} -->

Intrinsic Dimension Bounds. Some matrix concentration inequalities can be improved when the random matrix has limited spectral content in most dimensions. In this situation, we may be able to obtain bounds that do not depend on the ambient dimension. See Chapter 7 for details.

<!-- chunk {"id": "body-0070", "role": "body", "section": "What's Here", "weight": 1.0} -->

We have chosen to present these results because they are illustrative, and they have already found concrete applications.

<!-- chunk {"id": "body-0071", "role": "body", "section": "What's Not Here", "weight": 1.0} -->

The program of extending scalar concentration results to the matrix setting has been quite fruitful, and there are many useful results beyond the ones that we detail. Let us mention some of the other tools that are available. For further information, see the annotated bibliography.

<!-- chunk {"id": "body-0072", "role": "body", "section": "What's Not Here", "weight": 1.0} -->

First, there are additional exponential concentration inequalities for a sum of independent random matrices. All of the following results can be established within the framework of this monograph.

<!-- chunk {"id": "body-0073", "role": "body", "section": "What's Not Here", "weight": 1.0} -->

- Matrix Hoeffding. This result concerns a sum of independent random matrices whose squares are subject to semidefinite upper bounds [, §7]. - Matrix Bennett. This estimate sharpens the tail bound from the matrix Bernstein inequality [, §6]. - Matrix Bernstein, Unbounded Case. The matrix Bernstein inequality extends to the case where the moments of the summands grow at a controlled rate. See [, §6] or. - Matrix Bernstein, Nonnegative Summands. The lower tail of the Bernstein inequality can be improved when the summands are positive semidefinite; this result extends to the matrix setting. By a different argument, the dimensional factor can be removed from this bound for a class of interesting examples [, Thm. 3.1].

<!-- chunk {"id": "body-0074", "role": "body", "section": "What's Not Here", "weight": 1.0} -->

3 A Rademacher random variable takes the two values ♣ 1 with equal probability.

<!-- chunk {"id": "body-0075", "role": "body", "section": "What's Not Here", "weight": 1.0} -->

The approach in this monograph can be adapted to obtain exponential concentration for matrix-valued martingales.

<!-- chunk {"id": "body-0076", "role": "body", "section": "What's Not Here", "weight": 1.0} -->

- Matrix Azuma. This is the martingale version of the matrix Hoeffding bound [, §7]. - Matrix Bounded Differences. The matrix Azuma inequality gives bounds for the spectral norm of a matrix-valued function of independent random variables [, §7]. - Matrix Freedman. This result can be viewed as the martingale extension of the matrix Bernstein inequality.

<!-- chunk {"id": "body-0077", "role": "body", "section": "What's Not Here", "weight": 1.0} -->

The technical report explains how to extend other bounds for a sum of independent random matrices to the martingale setting.

<!-- chunk {"id": "body-0078", "role": "body", "section": "What's Not Here", "weight": 1.0} -->

Polynomial moment inequalities provide bounds for the expected trace of a power of a randommatrix. Moment inequalities for a sum of independent random matrices can provide useful information when the summands have heavy tails or else a uniform bound does not reflect the typical size of the summands.

<!-- chunk {"id": "body-0079", "role": "body", "section": "What's Not Here", "weight": 1.0} -->

- Matrix Khintchine. The matrix Khintchine inequality is the polynomial version of the exponential bounds for matrix Gaussian series and matrix Rademacher series. This result is presented in (4.7.1). See the papers or [MJC ⊕ 14, Cor. 7.3] for proofs. - MatrixMomentInequalities. Thematrix Chernoff inequality admits a polynomial variant; the simplest form appears in (5.1.9). The matrix Bernstein inequality also has a polynomial variant, stated in (6.1.6). These bounds are drawn from [, App.].

<!-- chunk {"id": "body-0080", "role": "body", "section": "What's Not Here", "weight": 1.0} -->

The methods that lead to polynomial moment inequalities differ substantially from the techniques in this monograph, so we cannot include the proofs here. The annotated bibliography includes references to the large literature on moment inequalities for random matrices.

<!-- chunk {"id": "body-0081", "role": "body", "section": "What's Not Here", "weight": 1.0} -->

Recently, Lester Mackey and the author, in collaboration with Daniel Paulin and several other researchers [MJC ⊕ 14, ], have developed another framework for establishing matrix concentration. This approach extends a scalar argument, introduced by Chatterjee, that depends on exchangeable pairs and Markov chain couplings. The method of exchangeable pairs delivers both exponential concentration inequalities and polynomial moment inequalities for random matrices, and it can reproduce many of the bounds mentioned above.

<!-- chunk {"id": "body-0082", "role": "body", "section": "What's Not Here", "weight": 1.0} -->

- Polynomial Efron-Stein Inequality for Matrices. This bound is a matrix version of the polynomial Efron-Stein inequality [, Thm. 1]. It controls the polynomial moments of a centered random matrix that is a function of independent random variables [, Thm. 4.2]. - Exponential Efron-Stein Inequality for Matrices. This bound is the matrix extension of the exponential Efron-Stein inequality [, Thm. 1]. It leads to exponential concentration inequalities for a centered random matrix constructed from independent random variables [, Thm. 4.3].

<!-- chunk {"id": "body-0083", "role": "body", "section": "What's Not Here", "weight": 1.0} -->

Another significant advantage is that the method of exchangeable pairs can sometimes handle random matrices built from dependent random variables. Although the simplest version of the exchangeable pairs argument is more elementary than the approach in this monograph, it takes a lot of effort to establish the more useful inequalities. With some regret, we have chosen not to include this material because the method and results are accessible to a narrower audience.

<!-- chunk {"id": "body-0084", "role": "body", "section": "What's Not Here", "weight": 1.0} -->

Finally, we remark that the modified logarithmic Sobolev inequalities of also extend to the matrix setting. Unfortunately, the matrix variants do not seem to be as useful as the scalar results.

<!-- chunk {"id": "body-0085", "role": "body", "section": "About This Monograph", "weight": 1.0} -->

This monograph is intended for graduate students and researchers in computational mathematics who want to learn some modern techniques for analyzing random matrices. The preparation required is minimal. We assume familiarity with calculus, applied linear algebra, the basic theory of normed spaces, and classical probability theory up through the elementary concentration inequalities (such as Markov and Bernstein). Beyond the basics, which can be gleaned from any good textbook, we include all the required background in Chapter 2.

<!-- chunk {"id": "body-0086", "role": "body", "section": "About This Monograph", "weight": 1.0} -->

The material here is based primarily on the paper 'User-Friendly Tail Bounds for Sums of Random Matrices' by the present author.

<!-- chunk {"id": "body-0087", "role": "body", "section": "About This Monograph", "weight": 1.0} -->

- Examples and Applications. Many of the papers on matrix concentration give limited information about how the results can be used to solve problems of interest. A major part of these notes consists of worked examples and applications that indicate how matrix concentration inequalities apply to practical questions. - Expectation Bounds. This work collects bounds for the expected value of the spectral norm of a random matrix and bounds for the expectation of the smallest and largest eigenvalues of a random symmetric matrix. Some of these useful results have appeared piecemeal in the literature [, MJC ⊕ 14], but they have not been included in a unified presentation. - Optimality. We explain why each matrix concentration inequality is (nearly) optimal. This presentation includes examples to show that each term in each bound is necessary to describe some particular phenomenon. - Intrinsic Dimension Bounds. Over the last few years, there have been some refinements to the basic matrix concentration bounds that improve the dependence on dimension. We describe a new framework that allows us to prove these results with ease. - Lieb's Theorem. The matrix concentration inequalities in this monograph depend on a deep theorem [, Thm. 6] from matrix analysis due to Elliott Lieb.

<!-- chunk {"id": "body-0088", "role": "body", "section": "About This Monograph", "weight": 1.0} -->

We provide a complete proof of this result, along with all the background required to understand the argument. - Annotated Bibliography. We have included a list of the major works on matrix concentration, including a short summary of the main contributions of these papers. We hope this catalog will be a valuable guide for further reading.

<!-- chunk {"id": "body-0089", "role": "body", "section": "About This Monograph", "weight": 1.0} -->

The organization of the notes is straightforward. Chapter 2 contains background material that is needed for the analysis. Chapter 3 describes the framework for developing exponential concentration inequalities for matrices. Chapter 4 presents the first set of results and examples, concerning matrix Gaussian and Rademacher series. Chapter 5 introduces the matrix Chernoff bounds and their applications, and Chapter 6 expands on our discussion of the matrix Bernstein inequality. Chapter 7 shows how to sharpen some of the results so that they depend on an intrinsic dimension parameter. Chapter 8 contains the proof of Lieb's theorem. We conclude with resources on matrix concentration and a bibliography.

<!-- chunk {"id": "body-0090", "role": "body", "section": "About This Monograph", "weight": 1.0} -->

To make the presentation smoother, we have not followed all of the conventions for scholarly articles in journals. In particular, almost all the citations appear in the notes at the end of each chapter. Our aim has been to explain the ideas as clearly as possible, rather than to interrupt the narrative with an elaborate genealogy of results.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Matrix Functions & Probability with Matrices", "weight": 1.0} -->

We begin the main development with a short overview of the background material that is required to understand the proofs and, to a lesser extent, the statements of matrix concentration inequalities. We have been careful to provide cross-references to these foundational results, so most readers will be able to proceed directly to the main theoretical development in Chapter 3 or the discussion of specific random matrix inequalities in Chapters 4, 5, and 6.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Overview", "weight": 1.0} -->

Section 2.1 covers material from matrix theory concerning the behavior of matrix functions. Section 2.2 reviews relevant results from probability, especially the parts involving matrices.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Matrix Theory Background", "weight": 1.0} -->

Let us begin with the results we require from the field of matrix analysis.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Conventions", "weight": 1.0} -->

We write R and C for the real and complex fields. A matrix is a finite, two-dimensional array of complex numbers. Many parts of the discussion do not depend on the size of a matrix, so we specify dimensions only when it really matters. Readers who wish to think about real-valued matrices will find that none of the results require any essential modification in this setting.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Spaces of Vectors", "weight": 1.0} -->

The symbol C d denotes the complex linear space consisting of d -dimensional column vectors with complex entries, equipped with the usual componentwise addition and multiplication by a complex scalar. We endow this space with the standard ' 2 inner product The symbol / denotes the complex conjugate of a number, as well as the conjugate transpose of a vector or matrix. The inner product induces the ' 2 norm: Similarly, the real linear space R d consists of d -dimensional column vectors with real entries, equipped with the usual componentwise addition and multiplication by a real scalar. The inner product and ' 2 norm on R d are defined by the same relations as for C d.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Spaces of Matrices", "weight": 1.0} -->

Wewrite M d 1 ≤ d 2 for the complex linear space consisting of d 1 ≤ d 2 matrices with complex entries, equipped with the usual componentwise addition and multiplication by a complex scalar. It is convenient to identify C d with the space M d ≤ 1. We write M d for the algebra of d ≤ d square, complex matrices. The term 'algebra' just means that we can multiply two matrices in M d to obtain another matrix in M d.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Topology & Convergence", "weight": 1.0} -->

Wecan endow the space of matrices with the Frobenius norm: Observe that the Frobenius norm on M d ≤ 1 coincides with the ' 2 norm (2.1.1) on C d.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Topology & Convergence", "weight": 1.0} -->

The Frobenius norm induces a norm topology on the space of matrices. In particular, given a sequence { B n: n ∅ 1,2,3,...}  M d 1 ≤ d 2, the symbol Open and closed sets are also defined with respect to the Frobenius-norm topology. Every other norm topology on M d 1 ≤ d 2 induces the same notions of convergence and open sets. We use the same topology for the normed linear spaces C d and M d.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Basic Vectors and Matrices", "weight": 1.0} -->

Wewrite 0 for the zero vector or the zero matrix, while I denotes the identity matrix. Occasionally, we add a subscript to specify the dimension. For instance, I d is the d ≤ d identity.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Basic Vectors and Matrices", "weight": 1.0} -->

The standard basis for the linear space C d consists of standard basis vectors. The standard basis vector e k is a column vector with a one in position k and zeros elsewhere. We also write e for the column vector whose entries all equal one. There is a related notation for the standard basis of M d 1 ≤ d 2. Wewrite E j k for the standard basis matrix with a one in position ( j, k ) and zeros elsewhere. The dimension of a standard basis vector and a standard basis matrix is typically determined by the context.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Basic Vectors and Matrices", "weight": 1.0} -->

A square matrix Q that satisfies QQ / ∅ I ∅ Q / Q is called a unitary matrix. We reserve the letter Q for a unitary matrix. Readers who prefer the real setting may prefer to regard Q as an orthogonal matrix.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Hermitian Matrices and Eigenvalues", "weight": 1.0} -->

An Hermitian matrix A is a square matrix that satisfies A ∅ A /. A useful intuition from operator theory is that Hermitian matrices are analogous with real numbers, while general square matrices are analogous with complex numbers.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Hermitian Matrices and Eigenvalues", "weight": 1.0} -->

We write H d for the collection of d ≤ d Hermitian matrices. The set H d is a linear space over the real field. That is, we can add Hermitian matrices and multiply them by real numbers. The space H d inherits the Frobenius-norm topology from M d. Weadopt Parlett's convention that bold Latin and Greek letters that are symmetric around the vertical axis ( A, H,..., Y; ¢, £,..., › ) always represent Hermitian matrices.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Hermitian Matrices and Eigenvalues", "weight": 1.0} -->

Each Hermitian matrix A 2 H d has an eigenvalue decomposition The diagonal entries of / are real numbers, which are referred to as the eigenvalues of A. The unitary matrix Q in the eigenvalue decomposition is not determined completely, but the list of eigenvalues is unique modulo permutations. The eigenvalues of an Hermitian matrix are often referred to as its spectrum.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Hermitian Matrices and Eigenvalues", "weight": 1.0} -->

We denote the algebraic minimum and maximum eigenvalues of an Hermitian matrix A, min(A) and, max(A). The extreme eigenvalue maps are positive homogeneous: There is an important relationship between minimum and maximum eigenvalues: The fact (2.1.5) warns us that we must be careful passing scalars through an eigenvalue map.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Hermitian Matrices and Eigenvalues", "weight": 1.0} -->

This work rarely requires any eigenvalues of an Hermitian matrix aside from the minimum and maximum. When they do arise, we usually order the other eigenvalues in the weakly decreasing sense: Onoccasion, it is more natural to arrange eigenvalues in the weakly increasing sense: To prevent confusion, we will accompany this notation with a reminder.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Hermitian Matrices and Eigenvalues", "weight": 1.0} -->

Readers who prefer the real setting may read 'symmetric' in place of 'Hermitian.' In this case, the eigenvalue decomposition involves an orthogonal matrix Q. Note, however, that the term 'symmetric' has a different meaning when applied to random variables!

<!-- chunk {"id": "body-0108", "role": "body", "section": "The Trace of a Square Matrix", "weight": 1.0} -->

The trace of a square matrix, denoted by tr, is the sum of its diagonal entries.

<!-- chunk {"id": "body-0109", "role": "body", "section": "The Trace of a Square Matrix", "weight": 1.0} -->

The trace is unitarily invariant: In particular, the existence of an eigenvalue decomposition (2.1.3) shows that the trace of an Hermitian matrix equals the sum of its eigenvalues. 1 Another valuable relation connects the trace with the Frobenius norm: This expression follows from the definitions (2.1.2) and (2.1.6) and a short calculation.

<!-- chunk {"id": "body-0110", "role": "body", "section": "The Semidefinite Partial Order", "weight": 1.0} -->

A matrix A 2 H d is positive semidefinite when it satisfies Equivalently, a matrix A is positive semidefinite when it is Hermitian and its eigenvalues are all nonnegative. Similarly, we say that A 2 H d is positive definite when Equivalently, A is positive definite when it is Hermitian and its eigenvalues are all positive.

<!-- chunk {"id": "body-0111", "role": "body", "section": "The Semidefinite Partial Order", "weight": 1.0} -->

Positive-semidefinite and positive-definite matrices play a special role in matrix theory, analogous with the role of nonnegative and positive numbers in real analysis. In particular, observe that the square of an Hermitian matrix is always positive semidefinite. The square of a nonsingular Hermitian matrix is always positive definite.

<!-- chunk {"id": "body-0112", "role": "body", "section": "The Semidefinite Partial Order", "weight": 1.0} -->

The family of positive-semidefinite matrices in H d forms a closed convex cone. 2 This geometric fact follows easily from the definition (2.1.9). Indeed, for each vector u 2 C d, the condition describes a closed halfspace in H d. As a consequence, the family of positive-semidefinite matrices in H d is an intersection of closed halfspaces. Therefore, it is a closed convex set. To see why this convex set is a cone, just note that A positive semidefinite implies fiA is positive semidefinite for fi ÷ 0.

<!-- chunk {"id": "body-0113", "role": "body", "section": "The Semidefinite Partial Order", "weight": 1.0} -->

1 This fact also holds true for a general square matrix.

<!-- chunk {"id": "body-0114", "role": "body", "section": "The Semidefinite Partial Order", "weight": 1.0} -->

2 A convex cone is a subset C of a linear space that is closed under conic combinations. That is, ¿ 1 x 1 ⊕ ¿ 2 x 2 2 C for all x 1, x 2 2 C and all ¿ 1, ¿ 2 ∪ 0. Equivalently, C is a set that is both convex and positively homogeneous.

<!-- chunk {"id": "body-0115", "role": "body", "section": "The Semidefinite Partial Order", "weight": 1.0} -->

Beginning from (2.1.10), similar considerations show that the family of positive-definite matrices in H d forms an (open) convex cone.

<!-- chunk {"id": "body-0116", "role": "body", "section": "The Semidefinite Partial Order", "weight": 1.0} -->

Wemaynowdefinethe semidefinite partial order ≼ onthe real-linear space H d using the rule In particular, we write A ≽ 0 to indicate that A is positive semidefinite and A ℜ 0 to indicate that A is positive definite. For a diagonal matrix /, the expression / ≽ 0 means that each entry of / is nonnegative.

<!-- chunk {"id": "body-0117", "role": "body", "section": "The Semidefinite Partial Order", "weight": 1.0} -->

The semidefinite order is preserved by conjugation, a simple fact whose importance cannot be overstated.

<!-- chunk {"id": "body-0118", "role": "body", "section": "The Semidefinite Partial Order", "weight": 1.0} -->

Proposition2.1.1 (Conjugation Rule). Let A and H be Hermitian matrices of the same dimension, and let B be a general matrix with compatible dimensions. Then Finally, we remark that the trace of a positive-semidefinite matrix is at least as large as its maximum eigenvalue: This property follows from the definition of a positive-semidefinite matrix and the fact that the trace of A equals the sum of the eigenvalues.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Standard Matrix Functions", "weight": 1.0} -->

Let us describe the most direct method for extending a function on the real numbers to a function on Hermitian matrices. The basic idea is to apply the function to each eigenvalue of the matrix to construct a new matrix.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Standard Matrix Functions", "weight": 1.0} -->

Definition 2.1.2 (Standard Matrix Function). Let f: I ! R where I is an interval of the real line. Consider a matrix A 2 H d whose eigenvalues are contained in I. Define the matrix f (A) 2 H d using an eigenvalue decomposition of A: In particular, we can apply f to a real diagonal matrix by applying the function to each diagonal entry.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Standard Matrix Functions", "weight": 1.0} -->

It can be verified that the definition of f ( A ) does not depend on which eigenvalue decomposition A ∅ Q / Q / that we choose. Any matrix function that arises in this fashion is called a standard matrix function.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Standard Matrix Functions", "weight": 1.0} -->

To confirm that this definition is sensible, consider the power function f ( t ) ∅ t q for a natural number q. When A is Hermitian, the power function f ( A ) ∅ A q, where A q is the q -fold product of A.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Standard Matrix Functions", "weight": 1.0} -->

For an Hermitian matrix A, whenever we write the power function A q or the exponential e A or the logarithm log A, we are always referring to a standard matrix function. Note that we only define the matrix logarithm for positive-definite matrices, and non-integer powers are only valid for positive-semidefinite matrices.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Standard Matrix Functions", "weight": 1.0} -->

The following result is an immediate, but important, consequence of the definition of a standard matrix function.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Standard Matrix Functions", "weight": 1.0} -->

Proposition 2.1.3 (Spectral Mapping Theorem). Let f: I ! R be a function on an interval I of the real line, and let A be an Hermitian matrix whose eigenvalues are contained in I. If, is an eigenvalue of A, then f is an eigenvalue of f ( A ).

<!-- chunk {"id": "body-0126", "role": "body", "section": "Standard Matrix Functions", "weight": 1.0} -->

Whenarealfunction has a power series expansion, we can also represent the standard matrix function with the same power series expansion. Indeed, suppose that f: I ! R is defined on an interval I of the real line, and assume that the eigenvalues of A are contained in I. Then This formula can be verified using an eigenvalue decomposition of A and the definition of a standard matrix function.

<!-- chunk {"id": "body-0127", "role": "body", "section": "The Transfer Rule", "weight": 1.0} -->

In most cases, the 'obvious' generalization of an inequality for real-valued functions fails to hold in the semidefinite order. Nevertheless, there is one class of inequalities for real functions that extends to give semidefinite relationships for standard matrix functions.

<!-- chunk {"id": "body-0128", "role": "body", "section": "The Transfer Rule", "weight": 1.0} -->

Proposition 2.1.4 (Transfer Rule). Let f and g be real-valued functions defined on an interval I of the real line, and let A be an Hermitian matrix whose eigenvalues are contained in I. Then Proof. Decompose A ∅ Q / Q /. It is immediate that f (/) ≼ g (/). The Conjugation Rule (2.1.12) allows us to conjugate this relation by Q. Finally, we invoke Definition 2.1.2, of a standard matrix function, to complete the argument.

<!-- chunk {"id": "body-0129", "role": "body", "section": "The Matrix Exponential", "weight": 1.0} -->

For any Hermitian matrix A, we can introduce the matrix exponential e A using Definition 2.1.2. Equivalently, we can use a power series expansion: The Spectral Mapping Theorem, Proposition 2.1.3, implies that the exponential of an Hermitian matrix is always positive definite.

<!-- chunk {"id": "body-0130", "role": "body", "section": "The Matrix Exponential", "weight": 1.0} -->

Weoften work with the trace of the matrix exponential: This function has a monotonicity property that we use extensively. For Hermitian matrices A and H with the same dimension, Weestablish this result in §8.3.2.

<!-- chunk {"id": "body-0131", "role": "body", "section": "The Matrix Logarithm", "weight": 1.0} -->

We can define the matrix logarithm as a standard matrix function. The matrix logarithm is also the functional inverse of the matrix exponential: Avaluable fact about the matrix logarithm is that it preserves the semidefinite order. For positivedefinite matrices A and H with the same dimension, We establish this result in §8.4.4. Let us stress that the matrix exponential does not have any operator monotonicity property analogous with (2.1.18)!

<!-- chunk {"id": "body-0132", "role": "body", "section": "Singular Values of Rectangular Matrices", "weight": 1.0} -->

A general matrix does not have an eigenvalue decomposition, but it admits a different representation that is just as useful. Every d 1 ≤ d 2 matrix B has a singular value decomposition The unitary matrices Q 1 and Q 2 have dimensions d 1 ≤ d 1 and d 2 ≤ d 2, respectively. The inner matrix § has dimension d 1 ≤ d 2, and we use the term diagonal in the sense that only the diagonal entries (§) j j may be nonzero.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Singular Values of Rectangular Matrices", "weight": 1.0} -->

The diagonal entries of § are called the singular values of B, and they are denoted as j (B). The singular values are determined completely modulo permutations, and it is conventional to arrange them in weakly decreasing order: There is an important relationship between singular values and eigenvalues. A general matrix has two squares associated with it, BB / and B / B, both of which are positive semidefinite. We can use a singular value decomposition of B to construct eigenvalue decompositions of the two squares: The two squares of § are square, diagonal matrices with nonnegative entries. Conversely, we can always extract a singular value decomposition from the eigenvalue decompositions of the two squares.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Singular Values of Rectangular Matrices", "weight": 1.0} -->

Wecan write the Frobenius norm of a matrix in terms of the singular values: This expression follows from the expression (2.1.8) for the Frobenius norm, the property (2.1.20) of the singular value decomposition, and the unitary invariance (2.1.7) of the trace.

<!-- chunk {"id": "body-0135", "role": "body", "section": "The Spectral Norm", "weight": 1.0} -->

The spectral norm of an Hermitian matrix A is defined by the relation For a general matrix B, the spectral norm is defined to be the largest singular value: These two definitions are consistent for Hermitian matrices because of (2.1.20). When applied to a row vector or a column vector, the spectral norm coincides with the ' 2 norm (2.1.1).

<!-- chunk {"id": "body-0136", "role": "body", "section": "The Spectral Norm", "weight": 1.0} -->

Wewill often need the fact that This identity also follows from (2.1.20).

<!-- chunk {"id": "body-0137", "role": "body", "section": "The Stable Rank", "weight": 1.0} -->

In several of the applications, we need an analytic measure of the collinearity of the rows and columns of a matrix called the stable rank. For a general matrix B, the stable rank is defined as The stable rank is a lower bound for the algebraic rank: This point follows when we use (2.1.21) and (2.1.23) to express the two norms in terms of the singular values of B. In contrast to the algebraic rank, the stable rank is a continuous function of the matrix, so it is more suitable for numerical applications.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Dilations", "weight": 1.0} -->

An extraordinarily fruitful idea from operator theory is to embed matrices within larger block matrices, called dilations. Dilations have an almost magical power. In this work, we will use dilations to extend matrix concentration inequalities from Hermitian matrices to general matrices.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Dilations", "weight": 1.0} -->

Definition 2.1.5 (Hermitian Dilation). The Hermitian dilation is the map from a general matrix to an Hermitian matrix defined by It is clear that the Hermitian dilation is a real-linear map. Furthermore, the dilation retains important spectral information. To see why, note that the square of the dilation satisfies We discover that the squared eigenvalues of H (B) coincide with the squared singular values of B, along with an appropriate number of zeros. As a consequence, κ H (B) κ ∅ κ B κ. Moreover, Wewill invoke the identity (2.1.28) repeatedly.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Dilations", "weight": 1.0} -->

One way to justify the first relation in (2.1.28) is to introduce the first columns u 1 and u 2 of the unitary matrices Q 1 and Q 2 that appear in the singular value decomposition B ∅ Q 1 § Q / 2. Then we may calculate that Indeed, the spectral norm of B equals its largest singular value 1(B), which coincides with u / 1 Bu 2 by construction of u 1 and u 2. The second identity relies on a direct calculation. The first inequality follows from the variational representation of the maximum eigenvalue as a Rayleigh quotient; this fact can also be derived as a consequence of (2.1.3). The second inequality depends on the definition (2.1.22) of the spectral norm of an Hermitian matrix.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Other Matrix Norms", "weight": 1.0} -->

There are a number of other matrix norms that arise sporadically in this work. The Schatten 1-norm of a matrix can be defined as the sum of its singular values: The entrywise ' 1 norm of a matrix is defined as because of the Cauchy-Schwarz inequality.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Probability with Matrices", "weight": 1.0} -->

Wecontinue with some material from probability, focusing on connections with matrices.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Conventions", "weight": 1.0} -->

We prefer to avoid abstraction and unnecessary technical detail, so we frame the standing assumption that all random variables are sufficiently regular that we are justified in computing expectations, interchanging limits, and so forth. The manipulations we perform are valid if we assume that all random variables are bounded, but the results hold in broader circumstances if we instate appropriate regularity conditions.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Conventions", "weight": 1.0} -->

Since the expectation operator is linear, we typically do not use parentheses with it. We instate the convention that powers and products take precedence over the expectation operator. In particular, This position helps us reduce the clutter of parentheses. We sometimes include extra delimiters when it is helpful for clarity.

<!-- chunk {"id": "body-0145", "role": "body", "section": "SomeScalar Random Variables", "weight": 1.0} -->

Weuse consistent notation for some of the basic scalar random variables.

<!-- chunk {"id": "body-0146", "role": "body", "section": "SomeScalar Random Variables", "weight": 1.0} -->

Standard normal variables. Wereserve the letter for a NORMAL random variable. That is, is a real Gaussian with mean zero and variance one.

<!-- chunk {"id": "body-0147", "role": "body", "section": "SomeScalar Random Variables", "weight": 1.0} -->

- Rademacher random variables. Wereserve the letter % for a random variable that takes the two values ♣ 1 with equal probability.

<!-- chunk {"id": "body-0148", "role": "body", "section": "SomeScalar Random Variables", "weight": 1.0} -->

Bernoulli random variables. A BERNOULLI( p ) random variable takes the value one with probability p and the value zero with probability 1 ϒ p, where p 2. We use the letters -and » for Bernoulli random variables.

<!-- chunk {"id": "body-0149", "role": "body", "section": "RandomMatrices", "weight": 1.0} -->

Let (›, F, P) be a probability space. A random matrix Z is a measurable map It is more natural to think of the entries of Z as complex random variables that may or may not be correlated with each other. We reserve the letters X and Y for random Hermitian matrices, while the letter Z denotes a general random matrix.

<!-- chunk {"id": "body-0150", "role": "body", "section": "RandomMatrices", "weight": 1.0} -->

A finite sequence { Z k } of random matrices is independent when for every collection { Fk } of Borel subsets of M d 1 ≤ d 2.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Expectation", "weight": 1.0} -->

The expectation of a random matrix Z ∅ [Zjk] is simply the matrix formed by taking the componentwise expectation. That is, Under mild assumptions, expectation commutes with linear and real-linear maps. Indeed, expectation commutes with multiplication by a fixed matrix: In particular, the product rule for the expectation of independent random variables extends to matrices: Weuse these identities liberally, without any further comment.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Inequalities for Expectation", "weight": 1.0} -->

Markov's inequality states that a nonnegative (real) random variable X obeys the probability bound The Markov inequality is a central tool for establishing concentration inequalities.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Inequalities for Expectation", "weight": 1.0} -->

Jensen's inequality describes how averaging interacts with convexity. Let Z be a random matrix, and let h be a real-valued function on matrices. Then The family of positive-semidefinite matrices in H d forms a convex cone, and the expectation of a random matrix can be viewed as a convex combination. Therefore, expectation preserves the semidefinite order: Weuse this result many times without direct reference.

<!-- chunk {"id": "body-0154", "role": "body", "section": "The Variance of a Random Hermitian Matrix", "weight": 1.0} -->

The variance of a real random variable Y is defined as the expected squared deviation from the mean: There are a number of natural extensions of this concept in the matrix setting that play a role in our theory.

<!-- chunk {"id": "body-0155", "role": "body", "section": "The Variance of a Random Hermitian Matrix", "weight": 1.0} -->

Suppose that Y is a random Hermitian matrix. We can define a matrix-valued variance: The matrix Var (Y) is always positive semidefinite. We can interpret the (j, k) entry of this matrix as the covariance between the j th and k th columns of Y: where we have written y: j for the j th column of Y.

<!-- chunk {"id": "body-0156", "role": "body", "section": "The Variance of a Random Hermitian Matrix", "weight": 1.0} -->

The matrix-valued variance contains a lot of information about the fluctuations of the random matrix. We can summarize Var (Y) using a single number v (Y), which we call the matrix variance statistic: To understand what this quantity means, one may wish to rewrite it as Roughly speaking, the matrix variance statistic describes the maximum variance of Yu for any unit vector u.

<!-- chunk {"id": "body-0157", "role": "body", "section": "The Variance of a Sum of Independent, Random Hermitian Matrices", "weight": 1.0} -->

The matrix-valued variance interacts beautifully with a sum of independent random matrices. Consider a finite sequence { X k } of independent, random Hermitian matrices with common dimension d. Introduce the sum Y ∅ P k X k. Then This identity matches the familiar result for the variance of a sum of independent scalar random variables. It follows that the matrix variance statistic satisfies The fact that the sum remains inside the norm is very important. Indeed, the best general inequalities between v (Y) and the matrix variance statistics v (X k) of the summands are These relations can be improved in some special cases. For example, when the matrices X k are identically distributed, the left-hand inequality becomes an identity.

<!-- chunk {"id": "body-0158", "role": "body", "section": "The Variance of a Rectangular Random Matrix", "weight": 1.0} -->

We will often work with non-Hermitian random matrices. In this case, we need to account for the fact that a general matrix has two different squares. Suppose that Z is a random matrix with dimension d 1 ≤ d 2. Define The matrix Var 1(Z) is a positive-semidefinite matrix with dimension d 1 ≤ d 1, and it describes the fluctuation of the rows of Z. Thematrix Var 2(Z) is a positive-semidefinite matrix with dimension d 2 ≤ d 2, and it reflects the fluctuation of the columns of Z. For an Hermitian random matrix Y, In other words, the two variances coincide in the Hermitian setting.

<!-- chunk {"id": "body-0159", "role": "body", "section": "The Variance of a Rectangular Random Matrix", "weight": 1.0} -->

As before, it is valuable to reduce these matrix-valued variances to a single scalar parameter. Wedefine the matrix variance statistic of a general random matrix Z as When Z is Hermitian, the definition (2.2.8) coincides with the original definition (2.2.4).

<!-- chunk {"id": "body-0160", "role": "body", "section": "The Variance of a Rectangular Random Matrix", "weight": 1.0} -->

To promote a deeper appreciation for the formula (2.2.8), let us explain how it arises from the Hermitian dilation (2.1.26). By direct calculation, The first identity is the definition (2.2.3) of the matrix-valued variance. The second line follows from the formula (2.1.27) for the square of the dilation. The last identity depends on the definition (2.2.7) of the two matrix-valued variances. Therefore, using the definitions (2.2.4) and (2.2.8) of the matrix variance statistics, The second identity holds because the spectral norm of a block-diagonal matrix is the maximum norm achieved by one of the diagonal blocks.

<!-- chunk {"id": "body-0161", "role": "body", "section": "The Variance of a Sum of Independent Random Matrices", "weight": 1.0} -->

As in the Hermitian case, the matrix-valued variances interact nicely with an independent sum. Consider a finite sequence { S k } of independent random matrices with the same dimension. Form the sum Z ∅ P k S k. Repeating the calculation leading up to (2.2.6), we find that In summary, the matrix variance statistic of an independent sum satisfies This formula arises time after time.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Notes", "weight": 1.0} -->

Everything in this chapter is firmly established. We have culled the results that are relevant to our discussion. Let us give some additional references for readers who would like more information.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Matrix Analysis", "weight": 1.0} -->

Ourtreatmentofmatrixanalysis is drawn from Bhatia's excellent books on matrix analysis. The two books of Horn & Johnson also serve as good general references. Higham's work is a generous source of information about matrix functions. Other valuable resources include Carlen's lecture notes, the book of Petz, and the book of Hiai & Petz.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Probability with Matrices", "weight": 1.0} -->

The classic introduction to probability is the two-volume treatise of Feller. The book of Grimmett & Stirzaker offers a good treatment of probability theory and random processes at an intermediate level. For a more theoretical presentation, consider the book of Shiryaev.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Probability with Matrices", "weight": 1.0} -->

There are too many books on random matrix theory for us to include a comprehensive list; here is a selection that the author finds useful. Tao's book gives a friendly introduction to some of the major aspects of classical and modern random matrix theory. The lecture notes of Kemp are also extremely readable. The survey of Vershynin provides a good summary of techniques from asymptotic convex geometry that are relevant to random matrix theory. The works of Mardia, Kent, & Bibby and Muirhead present classical results on random matrices that are particularly useful in statistics, while Bai & Silverstein contains a comprehensive modern treatment. Nica and Speicher offer an entrée to the beautiful field of free probability. Mehta's treatise was the first book on random matrix theory available, and it remains solid.

<!-- chunk {"id": "body-0166", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

This chapter contains the core part of the analysis that ultimately delivers matrix concentration inequalities. Readers who are only interested in the concentration inequalities themselves or the example applications may wish to move on to Chapters 4, 5, and 6.

<!-- chunk {"id": "body-0167", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

In the scalar setting, the Laplace transform method provides a simple but powerful way to develop concentration inequalities for a sum of independent random variables. This technique is sometimes referred to as the 'Bernstein trick' or 'Chernoff bounding.' For a primer, we recommend[, Chap. 2].

<!-- chunk {"id": "body-0168", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

In the matrix setting, there is a very satisfactory extension of this argument that allows us to prove concentration inequalities for a sum of independent random matrices. As in the scalar case, the matrix Laplace transform method is both easy to use and incredibly useful. In contrast to the scalar case, the arguments that lead to matrix concentration are no longer elementary. The purpose of this chapter is to install the framework we need to support these results. Fortunately, in practical applications, all of the technical difficulty remains invisible.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Overview", "weight": 1.0} -->

We first define matrix analogs of the moment generating function and the cumulant generating function, which pack up information about the fluctuations of a random Hermitian matrix. Section 3.2 explains how we can use the matrix mgf to obtain probability inequalities for the maximumeigenvalue of a random Hermitian matrix. The next task is to develop a bound for the mgf of a sum of independent random matrices using information about the summands. In §3.3, we discuss the challenges that arise; §3.4 presents the ideas we need to overcome these obstacles. Section 3.5 establishes that the classical result on additivity of cumulants has a companion in the matrix setting. This result allows us to develop a collection of abstract probability inequalities in §3.6 that we can specialize to obtain matrix Chernoff bounds, matrix Bernstein bounds, and so forth.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Matrix Moments and Cumulants", "weight": 1.0} -->

At the heart of the Laplace transform method are the moment generating function (mgf) and the cumulant generating function (cgf) of a random variable. We begin by presenting matrix versions of the mgf and cgf.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Matrix Moments and Cumulants", "weight": 1.0} -->

Definition 3.1.1 (Matrix Mgf and Cgf). Let X be a random Hermitian matrix. The matrix moment generating function MX and the matrix cumulant generating function ¥ X are given by Note that the expectations may not exist for all values of.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Matrix Moments and Cumulants", "weight": 1.0} -->

The matrix mgf MX and matrix cgf ¥ X contain information about how much the random matrix X varies. We aim to exploit the data encoded in these functions to control the eigenvalues.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Matrix Moments and Cumulants", "weight": 1.0} -->

Let us take a moment to expand on Definition 3.1.1; this discussion is not important for subsequent developments. Observe that the matrix mgf and cgf have formal power series expansions: We call the coefficients E X q matrix moments, and we refer to ' q as a matrix cumulant. The matrix cumulant ' q has a formal expression as a (noncommutative) polynomial in the matrix moments up to order q. In particular, the first cumulant is the mean and the second cumulant is the variance: The matrix variance was introduced in (2.2.3). Higher-order cumulants are harder to write down and interpret.

<!-- chunk {"id": "body-0174", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

In the scalar setting, the Laplace transform method allows us to obtain tail bounds for a random variable in terms of its mgf. The starting point for our theory is the observation that a similar result holds in the matrix setting.

<!-- chunk {"id": "body-0175", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

Proposition 3.2.1 (Tail Bounds for Eigenvalues). Let Y be a random Hermitian matrix. For all t 2 R, In words, we can control the tail probabilities of the extreme eigenvalues of a random matrix by producing a bound for the trace of the matrix mgf. The proof of this fact parallels the classical argument, but there is a twist.

<!-- chunk {"id": "body-0176", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

Proof. Webegin with (3.2.1). Fix a positive number, and observe that The first identity holds because a 7! e a is a monotone increasing function, so the event does not change under the mapping. The second relation is Markov's inequality (2.2.1). The last holds because the maximum eigenvalue is a positive-homogeneous map, as stated in (2.1.4). To control the exponential, note that The first identity depends on the Spectral Mapping Theorem, Proposition 2.1.3, and the fact that the exponential function is increasing. The inequality follows because the exponential of an Hermitian matrix is positive definite, and (2.1.13) shows that the maximum eigenvalue of a positivedefinite matrix is dominated by the trace. Combine the latter two displays to reach This inequality is valid for any positive, so we may take an infimum to achieve the tightest possible bound.

<!-- chunk {"id": "body-0177", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

To prove (3.2.2), we use a similar approach. Fix a negative number, and calculate that Thefunction a 7! e a reverses the inequality in the event because it is monotone decreasing. The last identity depends on the relationship (2.1.5) between minimum and maximum eigenvalues. Finally, we introduce the inequality (3.2.3) for the trace exponential and minimize over negative values of.

<!-- chunk {"id": "body-0178", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

In the proof of Proposition 3.2.1, it may seem crude to bound the maximum eigenvalue by the trace. In fact, our overall approach leads to matrix concentration inequalities that are sharp for specific examples (see the discussion in §§4.1.2, 5.1.2, and 6.1.2), so we must conclude that the loss in this bound is sometimes inevitable. At the same time, this maneuver allows us to exploit some amazing convexity properties of the trace exponential.

<!-- chunk {"id": "body-0179", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

Wecan adapt the proof of Proposition 3.2.1 to obtain bounds for the expectation of the maximum eigenvalue of a random Hermitian matrix. This argument does not have a perfect analog in the scalar setting.

<!-- chunk {"id": "body-0180", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

Proposition 3.2.2 (Expectation Bounds for Eigenvalues). Let Y be a random Hermitian matrix. Then Proof. We establish the bound (3.2.4); the proof of (3.2.5) is quite similar. Fix a positive number, and calculate that The first identity holds because the maximum eigenvalue is a positive-homogeneous map, as stated in (2.1.4). The second relation is Jensen's inequality. The third follows when we use the Spectral Mapping Theorem, Proposition 2.1.3, to draw the eigenvalue map through the exponential. The final inequality depends on the fact (2.1.13) that the trace of a positive-definite matrix dominates the maximum eigenvalue.

<!-- chunk {"id": "body-0181", "role": "body", "section": "The Failure of the Matrix Mgf", "weight": 1.0} -->

We would like the use the Laplace transform bounds from Section 3.2 to study a sum of independent random matrices. In the scalar setting, the Laplace transform method is effective for studying an independent sum because the mgf and the cgf decompose. In the matrix case, the situation is more subtle, and the goal of this section is to indicate where things go awry.

<!-- chunk {"id": "body-0182", "role": "body", "section": "The Failure of the Matrix Mgf", "weight": 1.0} -->

Consider an independent sequence { Xk } of real random variables. The mgf of the sum satisfies a multiplication rule: The first identity is the definition of an mgf. The second relation holds because the exponential mapconverts a sum of real scalars to a product, and the third relation requires the independence of the random variables. The last identity, again, is the definition.

<!-- chunk {"id": "body-0183", "role": "body", "section": "The Failure of the Matrix Mgf", "weight": 1.0} -->

At first, we might imagine that a similar relationship holds for the matrix mgf. Consider an independent sequence { X k } of random Hermitian matrices. Perhaps, Unfortunately, this hope shatters when we subject it to interrogation.

<!-- chunk {"id": "body-0184", "role": "body", "section": "The Failure of the Matrix Mgf", "weight": 1.0} -->

It is not hard to find the reason that (3.3.2) fails. The identity (3.3.1) depends on the fact that the scalar exponential converts a sum into a product. In contrast, for Hermitian matrices, If we introduce the trace, the situation improves somewhat: The result (3.3.3) is known as the Golden-Thompson inequality, a famous theorem from statistical physics. Unfortunately, the analogous bound may fail for three matrices: It seems that we have reached an impasse.

<!-- chunk {"id": "body-0185", "role": "body", "section": "The Failure of the Matrix Mgf", "weight": 1.0} -->

What if we consider the cgf instead? The cgf of a sum of independent real random variables satisfies an addition rule: The relation (3.3.4) follows when we extract the logarithm of the multiplication rule (3.3.1). This result looks like a more promising candidate for generalization because a sum of Hermitian matrices remains Hermitian. We might hope that As stated, this putative identity also fails. Nevertheless, the addition rule (3.3.4) admits a very satisfactory extension to matrices. In contrast with the scalar case, the proof involves much deeper considerations.

<!-- chunk {"id": "body-0186", "role": "body", "section": "ATheoremof Lieb", "weight": 1.0} -->

To find the appropriate generalization of the addition rule for cgfs, we turn to the literature on matrix analysis. Here, we discover a famous result of Elliott Lieb on the convexity properties of the trace exponential function.

<!-- chunk {"id": "body-0187", "role": "body", "section": "ATheoremof Lieb", "weight": 1.0} -->

Theorem 3.4.1 (Lieb). Fix an Hermitian matrix H with dimension d. The function is a concave map on the convex cone of d ≤ d positive-definite matrices.

<!-- chunk {"id": "body-0188", "role": "body", "section": "ATheoremof Lieb", "weight": 1.0} -->

In the scalar case, the analogous function a 7! exp( h ⊕ log a ) is linear, so this result describes a new type of phenomenon that emerges when we move to the matrix setting. We present a complete proof of Theorem 3.4.1 in Chapter 8.

<!-- chunk {"id": "body-0189", "role": "body", "section": "ATheoremof Lieb", "weight": 1.0} -->

For now, let us focus on the consequences of this remarkable result. Lieb's Theorem is valuable to us because the Laplace transform bounds from Section 3.2 involve the trace exponential function. To highlight the connection, we rephrase Theorem 3.4.1 in probabilistic terms.

<!-- chunk {"id": "body-0190", "role": "body", "section": "ATheoremof Lieb", "weight": 1.0} -->

Corollary 3.4.2. Let H be a fixed Hermitian matrix, and let X be a random Hermitian matrix of the same dimension. Then Proof. Introduce the random matrix Y ∅ e X. Then Thefirst identity follows from the interpretation (2.1.17) of the matrix logarithm as the functional inverse of the matrix exponential. Theorem 3.4.1 shows that the trace function is concave in Y, so Jensen's inequality (2.2.2) allows us to draw the expectation inside the function.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Subadditivity of the Matrix Cgf", "weight": 1.0} -->

We are now prepared to generalize the addition rule (3.3.4) for scalar cgfs to the matrix setting. The following result is fundamental to our approach to random matrices.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Subadditivity of the Matrix Cgf", "weight": 1.0} -->

Lemma3.5.1 (Subadditivity of Matrix Cgfs). Consider a finite sequence { X k } of independent, random, Hermitian matrices of the same dimension. Then The parallel between the additivity rule (3.3.4) and the subadditivity rule (3.5.2) is striking. With our level of preparation, it is easy to prove this result. We just apply the bound from Corollary 3.4.2 repeatedly.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Subadditivity of the Matrix Cgf", "weight": 1.0} -->

Equivalently, Proof. Without loss of generality, we assume that ∅ 1 by absorbing the parameter into the randommatrices. Let E k denote the expectation with respect to X k, the remaining random matrices held fixed. Abbreviate Wecanintroduceiterated expectations because of the tower property of conditional expectation. To bound the expectation E m for an index m ∅ 1,2,3,..., n, we invoke Corollary 3.4.2 with the fixed matrix H equal to This argument is legitimate because H m is independent from X m.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Subadditivity of the Matrix Cgf", "weight": 1.0} -->

The formulation (3.5.2) follows from (3.5.1) when we substitute the expression (3.1.1) for the matrix cgf and make some algebraic simplifications.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Master Bounds for Sums of Independent Random Matrices", "weight": 1.0} -->

Finally, we can present some general results on the behavior of a sum of independent random matrices. At this stage, we simply combine the Laplace transform bounds with the subadditivity of the matrix cgf to obtain abstract inequalities. Later, we will harness properties of the summands to develop more concrete estimates that apply to specific examples of interest.

<!-- chunk {"id": "body-0196", "role": "body", "section": "Master Bounds for Sums of Independent Random Matrices", "weight": 1.0} -->

Theorem 3.6.1 (Master Bounds for a Sum of Independent Random Matrices). Consider a finite sequence { X k } of independent, random, Hermitian matrices of the same size. Then Furthermore, for all t 2 R, Proof. Substitute the subadditivity rule for matrix cgfs, Lemma 3.5.1, into the two matrix Laplace transform results, Proposition 3.2.1 and Proposition 3.2.2.

<!-- chunk {"id": "body-0197", "role": "body", "section": "Master Bounds for Sums of Independent Random Matrices", "weight": 1.0} -->

In this chapter, we have focused on probability inequalities for the extreme eigenvalues of a sum of independent random matrices. Nevertheless, these results also give information about the spectral norm of a sum of independent, random, rectangular matrices because we can apply them to the Hermitian dilation (2.1.26) of the sum. Instead of presenting a general theorem, we find it more natural to extend individual results to the non-Hermitian case.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Notes", "weight": 1.0} -->

This section includes some historical discussion about the results we have described in this chapter, along with citations for the results that we have established.

<!-- chunk {"id": "body-0199", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

The idea of lifting the 'Bernstein trick' to the matrix setting is due to two researchers in quantum information theory, Rudolf Ahlswede and Andreas Winter, who were working on a problem concerning transmission of information through a quantum channel. Their paper contains a version of the matrix Laplace transform result, Proposition 3.2.1, along with a substantial number of related foundational ideas. Their work is one of the major inspirations for the tools that are described in these notes.

<!-- chunk {"id": "body-0200", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

Thestatement of Proposition 3.2.1 and the proof that we present appear in the paper of Roberto Oliveira. The subsequent result on expectations, Proposition 3.2.2, first appeared in the paper.

<!-- chunk {"id": "body-0201", "role": "body", "section": "Subadditivity of Cumulants", "weight": 1.0} -->

The major impediment to applying the matrix Laplace transform method is the need to produce a bound for the trace of the matrix moment generating function (the trace mgf). This is where all the technical difficulty in the argument resides.

<!-- chunk {"id": "body-0202", "role": "body", "section": "Subadditivity of Cumulants", "weight": 1.0} -->

Ahlswede & Winter [, App.] proposed an approach for bounding the trace mgf of an independent sum, based on a repeated application of the Golden-Thompson inequality (3.3.3). Their argument leads to a cumulant bound of the form when the random Hermitian matrices X k have dimension d. In other words, Ahlswede & Winter bound the cumulant of a sum in terms of the sum of the maximum eigenvalues of the cumulants. There are cases where the bound (3.7.1) is equivalent with Lemma 3.5.1. For example, the estimates coincide when each matrix X k is identically distributed. In general, however, the estimate (3.7.1) leads to fundamentally weaker results than our bound from Lemma 3.5.1. In the worst case, the approach of Ahlswede & Winter may produce an unnecessary factor of the dimension d in the exponent. See [, §§3.7, 4.8] for details.

<!-- chunk {"id": "body-0203", "role": "body", "section": "Subadditivity of Cumulants", "weight": 1.0} -->

The first major technical advance beyond the original argument of Ahlswede & Winter appeared in a paper of Oliveira. He developed a more effective way to deploy the GoldenThompson inequality, and he used this technique to establish a matrix version of Freedman's inequality. In the scalar setting, Freedman's inequality extends the Bernstein concentration inequality to martingales; Oliveira obtained the analogous extension of Bernstein's inequality for matrix-valued martingales. When specialized to independent sums, his result is quite similar with the matrix Bernstein inequality, Theorem 1.6.2, apart from the precise values of the constants. Oliveira's method, however, does not seem to deliver the full spectrum of matrix concentration inequalities that we discuss in these notes.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Subadditivity of Cumulants", "weight": 1.0} -->

The approach here, based on Lieb's Theorem, was introduced in the article by the author of these notes. This paper was apparently the first to recognize that Lieb's Theorem has probabilistic content, as stated in Corollary 3.4.2. This idea leads to Lemma 3.5.1, on the subadditivity of cumulants, along with the master tail bounds from Theorem 3.6.1. Note that the two articles are independent works.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Subadditivity of Cumulants", "weight": 1.0} -->

For a detailed discussion of the benefits of Lieb's Theorem over the Golden-Thompson inequality, see [, §4]. In summary, to get the sharpest concentration results for random matrices, Lieb's Theorem appears to be indispensible. The approach of Ahlswede & Winter seems intrinsically weaker. Oliveira's argument has certain advantages, however, in that it extends from matrices to the fully noncommutative setting.

<!-- chunk {"id": "body-0206", "role": "body", "section": "Subadditivity of Cumulants", "weight": 1.0} -->

Subsequent research on the underpinnings of the matrix Laplace transform method has led to a martingale version of the subadditivity of cumulants; these works also depend on Lieb's Theorem. The technical report shows how to use a related result, called the Lieb-Seiringer Theorem, to obtain upper and lower tail bounds for all eigenvalues of a sum of independent random Hermitian matrices.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Noncommutative Moment Inequalities", "weight": 1.0} -->

There is a closely related, and much older, line of research on noncommutative moment inequalities. These results provide information about the expected trace of a power of a sum of independent random matrices. The matrix Laplace transform method, as encapsulated in Theorem 3.6.1, gives analogous bounds for the exponential moments.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Noncommutative Moment Inequalities", "weight": 1.0} -->

Research on noncommutative moment inequalities dates to an important paper of Françoise Lust-Piquard, which contains an operator extension of the Khintchine inequality. Her result, now called the noncommutative Khintchine inequality, controls the trace moments of a sum of fixed matrices, each modulated by an independent Rademacher random variable; see Section 4.7.2 for more details.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Noncommutative Moment Inequalities", "weight": 1.0} -->

In recent years, researchers have generalized many other moment inequalities for a sum of scalar random variables to matrices (and beyond). For instance, the Rosenthal-Pinelis inequality for a sum of independent zero-mean random variables admits a matrix version [, MJC ⊕ 14, ]. We present a variant of the latter result below in (6.1.6). See the paper for a good overview of some other noncommutative moment inequalities.

<!-- chunk {"id": "body-0210", "role": "body", "section": "Noncommutative Moment Inequalities", "weight": 1.0} -->

Finally, and tangentially, we mention that a different notion of matrix moments and cumulants plays a central role in the theory of free probability.

<!-- chunk {"id": "body-0211", "role": "body", "section": "QuantumStatistical Mechanics", "weight": 1.0} -->

A curious feature of the theory of matrix concentration inequalities is that the most powerful tools come from the mathematical theory of quantum statistical mechanics. This field studies the bulk statistical properties of interacting quantum systems, and it would seem quite distant from the field of random matrix theory. The connection between these two areas has emerged because of research on quantum information theory, which studies how information can be encoded, operated upon, and transmitted via quantum mechanical systems.

<!-- chunk {"id": "body-0212", "role": "body", "section": "QuantumStatistical Mechanics", "weight": 1.0} -->

TheGolden-Thompsoninequalityisamajorresultfromquantumstatisticalmechanics. Bhatia's book [, Sec. IX.3] contains a detailed treatment of this result from the perspective of matrix theory. For an account with more physical content, see the book of Thirring. The fact that the Golden-Thompson inequality fails for three matrices can be obtained from simple examples, such as combinations of Pauli spin matrices [, Exer. IX.8.4].

<!-- chunk {"id": "body-0213", "role": "body", "section": "QuantumStatistical Mechanics", "weight": 1.0} -->

Lieb's Theorem [, Thm. 6] was first established in an important paper of Elliott Lieb on the convexity of trace functions. His main goal was to establish concavity properties for a function that measures the amount of information in a quantum system. See the notes in Chapter 8 for a more detailed discussion.

<!-- chunk {"id": "body-0214", "role": "body", "section": "Matrix Gaussian Series & Matrix Rademacher Series", "weight": 1.0} -->

In this chapter, we present our first set of matrix concentration inequalities. These results provide spectral information about a sum of fixed matrices, each modulated by an independent scalar random variable. This type of formulation is surprisingly versatile, and it captures a range of interesting examples. Our main goal, however, is to introduce matrix concentration in the simplest setting possible.

<!-- chunk {"id": "body-0215", "role": "body", "section": "Matrix Gaussian Series & Matrix Rademacher Series", "weight": 1.0} -->

To be more precise about our scope, let us introduce the concept of a matrix Gaussian series. Consider a finite sequence { B k } of fixed matrices with the same dimension, along with a finite sequence { k } of independent standard normal random variables. We will study the spectral norm of the random matrix This expression looks abstract, but it has concrete modeling power. For example, we can express aGaussianWignermatrix, one of the classical random matrices, in this fashion. But the real value of this approach is that we can use matrix Gaussian series to represent many kinds of random matrices built from Gaussian random variables. This technique allows us to attack problems that classical methods do not handle gracefully. For instance, we can easily study a Toeplitz matrix with Gaussian entries.

<!-- chunk {"id": "body-0216", "role": "body", "section": "Matrix Gaussian Series & Matrix Rademacher Series", "weight": 1.0} -->

Similar ideas allow us to treat a matrix Rademacher series, a sum of fixed matrices modulated by random signs. (Recall that a Rademacher random variable takes the values ♣ 1 with equal probability.) The results in this case are almost identical with the results for matrix Gaussian series, but they allow us to consider new problems. As an example, we can study the expected spectral norm of a fixed real matrix after flipping the signs of the entries at random.

<!-- chunk {"id": "body-0217", "role": "body", "section": "Overview", "weight": 1.0} -->

In §4.1, we begin with an overview of our results for matrix Gaussian series; very similar results also hold for matrix Rademacher series. Afterward, we discuss the accuracy of the theoretical bounds. The subsequent sections, §§4.2-4.4, describe what the matrix concentration inequalities tell us about some classical and not-so-classical examples of random matrices. Section 4.5 includes an overview of a more substantial application in combinatorial optimization. The final part §4.6 contains detailed proofs of the bounds. We conclude with bibliographical notes.

<!-- chunk {"id": "body-0218", "role": "body", "section": "ANormBoundforRandomSeries with Matrix Coefficients", "weight": 1.0} -->

Consider a finite sequence { bk } of real numbers and a finite sequence { k } of independent standard normal random variables. Form the random series Z ∅ P k k b k. A routine invocation of the scalar Laplace transform method demonstrates that It turns out that the inequality (4.1.1) extends directly to the matrix setting.

<!-- chunk {"id": "body-0219", "role": "body", "section": "ANormBoundforRandomSeries with Matrix Coefficients", "weight": 1.0} -->

Theorem 4.1.1 (Matrix Gaussian & Rademacher Series). Consider a finite sequence { B k } of fixed complexmatrices with dimension d 1 ≤ d 2, and let { k } be a finite sequence of independent standard normal variables. Introduce the matrix Gaussian series Let v (Z) be the matrix variance statistic of the sum: The same bounds hold when we replace { k } by a finite sequence { % k } of independent Rademacher random variables.

<!-- chunk {"id": "body-0220", "role": "body", "section": "ANormBoundforRandomSeries with Matrix Coefficients", "weight": 1.0} -->

The proof of Theorem 4.1.1 appears below in §4.6.

<!-- chunk {"id": "body-0221", "role": "body", "section": "Discussion", "weight": 1.5} -->

Let us take a moment to discuss the content of Theorem 4.1.1. The main message is that the expectation of κ Z κ is controlled by the matrix variance statistic v ( Z ). Furthermore, κ Z κ has a subgaussian tail whose decay rate depends on v ( Z ).

<!-- chunk {"id": "body-0222", "role": "body", "section": "Discussion", "weight": 1.5} -->

Thematrixvariancestatistic v ( Z ) defined in (4.1.3) specializes the general formulation (2.2.8). The second expression (4.1.4) follows from the additivity property (2.2.11) for the variance of an independent sum. When the summands are Hermitian, observe that the two terms in the maximumcoincide. The formulas (4.1.3) and (4.1.4) are a direct extension of the variance that arises in the scalar bound (4.1.1).

<!-- chunk {"id": "body-0223", "role": "body", "section": "Discussion", "weight": 1.5} -->

Furthermore, for all t ÷ 0, As compared with (4.1.1), a new feature of the bound (4.1.6) is the dimensional factor d 1 ⊕ d 2. When d 1 ∅ d 2 ∅ 1, the matrix bound reduces to the scalar result (4.1.1). In this case, at least, we have lost nothing by lifting the Laplace transform method to matrices. The behavior of the matrix tail bound (4.1.6) is more subtle than the behavior of the scalar tail bound (4.1.1). See Figure 4.1 for an illustration.

<!-- chunk {"id": "body-0224", "role": "body", "section": "Optimality of the Bounds for Matrix Gaussian Series", "weight": 1.0} -->

One may wonder whether Theorem 4.1.1 provides accurate information about the behavior of a matrix Gaussian series. The answer turns out to be complicated. Here is the executive summary: the expectation bound (4.1.5) is always quite good, but the tail bound (4.1.6) is sometimes quite bad. The rest of this section expands on these claims.

<!-- chunk {"id": "body-0225", "role": "body", "section": "The Expectation Bound", "weight": 1.0} -->

Let Z be a matrix Gaussian series of the form (4.1.2). We will argue that In other words, the matrix variance v (Z) is roughly the correct scale for κ Z κ 2. This pair of estimates is a significant achievement because it is quite challenging to compute the norm of a matrix Gaussian series in general. Indeed, the literature contains very few examples where explicit estimates are available, especially if one desires reasonable constants.

<!-- chunk {"id": "body-0226", "role": "body", "section": "The Expectation Bound", "weight": 1.0} -->

We begin with the lower bound in (4.1.7), which is elementary. Indeed, since the spectral norm is convex, Jensen's inequality ensures that The first identity follows from (2.1.24), and the last is the definition (2.2.8) of the matrix variance. The upper bound in (4.1.7) is a consequence of the tail bound (4.1.6): In the first step, rewrite the expectation using integration by parts, and then split the integral at a positive number E. In the first term, we bound the probability by one, while the second term results from the tail bound (4.1.6). Afterward, we compute the integrals explicitly. Finally, select E 2 ∅ 2 v (Z)log(d 1 ⊕ d 2) to complete the proof of (4.1.7).

<!-- chunk {"id": "body-0227", "role": "body", "section": "About the Dimensional Factor", "weight": 1.0} -->

At this point, one may ask whether it is possible to improve either side of the inequality (4.1.7). The answer is negative unless we have additional information about the Gaussian series beyond the matrix variance statistic v ( Z ).

<!-- chunk {"id": "body-0228", "role": "body", "section": "About the Dimensional Factor", "weight": 1.0} -->

Indeed, for arbitrarily large dimensions d 1 and d 2, we can exhibit a matrix Gaussian series where the left-hand inequality in (4.1.7) is correct. That is, E κ Z κ 2 … v ( Z ) with no additional dependence on the dimensions d 1 or d 2. One such example appears below in §4.2.2.

<!-- chunk {"id": "body-0229", "role": "body", "section": "About the Dimensional Factor", "weight": 1.0} -->

At the same time, for arbitrarily large dimensions d 1 and d 2, we can construct a matrix Gaussian series where the right-hand inequality in (4.1.7) is correct. That is, E κ Z κ 2 … v ( Z )log( d 1 ⊕ d 2). See §4.4 for an example.

<!-- chunk {"id": "body-0230", "role": "body", "section": "About the Dimensional Factor", "weight": 1.0} -->

We can offer a rough intuition about how these two situations differ from each other. The presence or absence of the dimensional factor log( d 1 ⊕ d 2) depends on how much the coefficients B k in the matrix Gaussian series Z commute with each other. More commutativity leads to a logarithm, while less commutativity can sometimes result in cancelations that obliterate the logarithm. It remains a major open question to find a simple quantity, computable from the coefficients B k, that decides whether E κ Z κ 2 contains a dimensional factor or not.

<!-- chunk {"id": "body-0231", "role": "body", "section": "About the Dimensional Factor", "weight": 1.0} -->

In Chapter 7, we will describe a technique that allows us to moderate the dimensional factor in (4.1.7) for some types of matrix series. But we cannot remove the dimensional factor entirely with current technology.

<!-- chunk {"id": "body-0232", "role": "body", "section": "The Tail Bound", "weight": 1.0} -->

What about the tail bound (4.1.6) for the norm of the Gaussian series? Here, our results are less impressive. It turns out that the large-deviation behavior of the spectral norm of a matrix Gaussian series Z is controlled by a statistic v ? (Z) called the weak variance: The best general inequalities between the matrix variance statistic and the weak variance are There are examples of matrix Gaussian series that saturate the lower or the upper inequality.

<!-- chunk {"id": "body-0233", "role": "body", "section": "The Tail Bound", "weight": 1.0} -->

Theclassical concentration inequality [, Thm. 5.6] for a function of independent Gaussian random variables implies that Let us emphasize that the bound (4.1.8) provides no information about E κ Z κ; it only tells us about the probability that κ Z κ is larger than its mean.

<!-- chunk {"id": "body-0234", "role": "body", "section": "The Tail Bound", "weight": 1.0} -->

Together, the last two displays indicate that the exponent in the tail bound (4.1.6) is sometimes too big by a factor min{ d 1, d 2}. Therefore, a direct application of Theorem 4.1.1 can badly overestimate the tail probability P { κ Z κ ∪ t } when the level t is large. Fortunately, this problem is less pronounced with the matrix Chernoff inequalities of Chapter 5 and the matrix Bernstein inequalities of Chapter 6.

<!-- chunk {"id": "body-0235", "role": "body", "section": "Expectations and Tails", "weight": 1.0} -->

When studying concentration of random variables, it is quite common that we need to use one method to assess the expected value of the random variable and a separate technique to determine the probability of a large deviation.

<!-- chunk {"id": "body-0236", "role": "body", "section": "Expectations and Tails", "weight": 1.0} -->

The primary value of matrix concentration inequalities inheres in the estimates that they provide for the expectation of the spectral norm (or maximum eigenvalue or minimum eigenvalue) of a random matrix.

<!-- chunk {"id": "body-0237", "role": "body", "section": "Expectations and Tails", "weight": 1.0} -->

In many cases, matrix concentration bounds provide reasonable information about the tail decay, but there are other situations where the tail bounds are feeble. In this event, we recommend applying a scalar concentration inequality to control the tails.

<!-- chunk {"id": "body-0238", "role": "body", "section": "Example: Some Gaussian Matrices", "weight": 1.0} -->

Let us try out our methods on two types of Gaussian matrices that have been studied extensively in the classical literature on random matrix theory. In these cases, precise information about the spectral distribution is available, which provides a benchmark for assessing our results. We find that bounds based on Theorem 4.1.1 lead to very reasonable estimates, but they are not sharp. The advantage of our approach is that it applies to every example, whereas we are making comparisons with specialized techniques that only illuminate individual cases. Similar conclusions hold for matrices with independent Rademacher entries.

<!-- chunk {"id": "body-0239", "role": "body", "section": "Gaussian Wigner Matrices", "weight": 1.0} -->

We begin with a family of Gaussian Wigner matrices. A d ≤ d matrix W d from this ensemble is real-symmetric with a zero diagonal; the entries above the diagonal are independent normal variables with mean zero and variance one: where { j k: 1 · j ∩ k · d } is an independent family of standard normal variables. We can represent this matrix compactly as a Gaussian series: The norm of a Wigner matrix satisfies For example, see [, Thm. 5.1]. To make (4.2.2) precise, we assume that { W d } is an independent sequence of Gaussian Wigner matrices, indexed by the dimension d.

<!-- chunk {"id": "body-0240", "role": "body", "section": "Gaussian Wigner Matrices", "weight": 1.0} -->

Theorem 4.6.1 provides a simple way to bound the norm of a Gaussian Wigner matrix. We just need to compute the matrix variance statistic v (W d). The formula (4.1.4) for v (W d) asks us to form the sum of the squared coefficients from the representation (4.2.1): Since the terms in (4.2.1) are Hermitian, we have only one sum of squares to consider. We have also used the facts that E j k E k j ∅ E j j while E j k E j k ∅ 0 because of the condition j ∩ k in the limits of summation. We see that The bound (4.1.5) for the expectation of the norm gives In conclusion, our techniques overestimate κ W d κ byafactor of about p 0.5log d. The result (4.2.3) is not perfect, but it only takes two lines of work. In contrast, the classical result (4.2.2) depends on a long moment calculation that involves challenging combinatorial arguments.

<!-- chunk {"id": "body-0241", "role": "body", "section": "Rectangular Gaussian Matrices", "weight": 1.0} -->

Next, we consider a d 1 ≤ d 2 rectangular matrix with independent standard normal entries: where { j k } is an independent family of standard normal variables. We can express this matrix efficiently using a Gaussian series: There is an elegant estimate [, Thm. 2.13] for the norm of this matrix: The inequality (4.2.5) is sharp when d 1 and d 2 tend to infinity while the ratio d 1/ d 2 ! const. See [, Thm. 5.8] for details.

<!-- chunk {"id": "body-0242", "role": "body", "section": "Rectangular Gaussian Matrices", "weight": 1.0} -->

Theorem 4.1.1 yields another bound on the expected norm of the matrix G. In order to compute the matrix variance statistic v (G), we calculate the sums of the squared coefficients from the representation (4.2.4): The matrix variance statistic (4.1.3) satisfies The leading term is roughly correct because The logarithmic factor in (4.2.6) does not belong, but it is rather small in comparison with the leading terms. Once again, we have produced a reasonable result with a short argument based on general principles.

<!-- chunk {"id": "body-0243", "role": "body", "section": "Example: Matrices with Randomly Signed Entries", "weight": 1.0} -->

Next, we turn to an example that is superficially similar with the matrix discussed in §4.2.2 but is less understood. Consider a fixed d 1 ≤ d 2 matrix B with real entries, and let { % j k } be an independent family of Rademacher random variables. Consider the d 1 ≤ d 2 random matrix In other words, we obtain the random matrix B ♣ by randomly flipping the sign of each entry of B. The expected norm of this matrix satisfies the bound where the leading factor v 1/2 satisfies We have written b j: for the j th row of B and b: k for the k th column of B. In other words, the expected norm of a matrix with randomly signed entries is comparable with the maximum ' 2 normachievedbyanyroworcolumn. Therearecaseswherethebound(4.3.1)admitsamatching lower bound. These results appear in [, Thms. 3.1, 3.2] and [, Cor. 4.7].

<!-- chunk {"id": "body-0244", "role": "body", "section": "Example: Matrices with Randomly Signed Entries", "weight": 1.0} -->

Theorem 4.1.1 leads to a quick proof of a slightly weaker result. We simply need to compute the matrix variance statistic v (B ♣). To that end, note that Therefore, using the formula (4.1.4), we find that We see that v (B ♣) coincides with v, the leading term (4.3.2) in the established estimate (4.3.1)! Now, Theorem 4.1.1 delivers the bound Observe that the estimate (4.3.3) for the norm matches the correct bound (4.3.1) up to the logarithmic factor. Yet again, we obtain a result that is respectably close to the optimal one, even though it is not quite sharp.

<!-- chunk {"id": "body-0245", "role": "body", "section": "Example: Matrices with Randomly Signed Entries", "weight": 1.0} -->

The main advantage of using results like Theorem 4.1.1 to analyze this random matrix is that we can obtain a good result with a minimal amount of arithmetic. The analysis that leads to (4.3.1) involves a specialized combinatorial argument.

<!-- chunk {"id": "body-0246", "role": "body", "section": "Example: Gaussian Toeplitz Matrices", "weight": 1.0} -->

Matrix concentration inequalities offer an effective tool for analyzing random matrices whose dependency structures are more complicated than those of the classical ensembles. In this section, we consider Gaussian Toeplitz matrices, which have applications in signal processing.

<!-- chunk {"id": "body-0247", "role": "body", "section": "Example: Gaussian Toeplitz Matrices", "weight": 1.0} -->

Weconstruct an (unsymmetric) d ≤ d Gaussian Toeplitz matrix ¡ d by populating the first row and first column of the matrix with independent standard normal variables; the entries along each diagonal of the matrix take the same value: where { k } is an independent family of standard normal variables. As usual, we represent the Gaussian Toeplitz matrix as a matrix Gaussian series: where C 2 M d denotes the shift-up operator acting on d -dimensional column vectors: It follows that C k shifts a vector up by k places, introducing zeros at the bottom, while (C k) / shifts a vector down by k places, introducing zeros at the top.

<!-- chunk {"id": "body-0248", "role": "body", "section": "Example: Gaussian Toeplitz Matrices", "weight": 1.0} -->

Wecan analyze this example quickly using Theorem 4.1.1. First, note that To obtain the matrix variance statistic (4.1.4), we calculate the sum of the squares of the coefficient matrices that appear in (4.4.1). In this instance, the two terms in the variance are the same. Wefind that In the second line, we (carefully) switch the order of summation and rewrite the identity matrix as a sum of diagonal standard basis matrices. We reach An application of Theorem 4.1.1 leads us to conclude that It turns out that the inequality (4.4.3) is correct up to the precise value of the constant, which does not seem to be known. Nevertheless, the limiting value is available for the top eigenvalue of a (scaled) symmetric Toeplitz matrix whose first row contains independent standard normal variables [, Thm. 1]. From this result, we may conclude that Here, we take { ¡ d } to be a sequence of unsymmetric Gaussian Toeplitz matrices, indexed by the ambient dimension d.

<!-- chunk {"id": "body-0249", "role": "body", "section": "Example: Gaussian Toeplitz Matrices", "weight": 1.0} -->

Our simple argument gives the right scaling for this problem, and our estimate for the constant lies within 21% of the optimal value!

<!-- chunk {"id": "body-0250", "role": "body", "section": "Application: Rounding for the MaxQP Relaxation", "weight": 1.0} -->

Our final application involves a more substantial question from combinatorial optimization. One of the methods that has been proposed for solving a certain optimization problem leads to a matrix Rademacher series, and the analysis of this method requires the spectral norm bounds from Theorem 4.1.1. A detailed treatment would take us too far afield, so we just sketch the context and indicate how the random matrix arises.

<!-- chunk {"id": "body-0251", "role": "body", "section": "Application: Rounding for the MaxQP Relaxation", "weight": 1.0} -->

There are many types of optimization problems that are computationally difficult to solve exactly. One approach to solving these problems is to enlarge the constraint set in such a way that the problem becomes tractable, a process called 'relaxation.' After solving the relaxed problem, we can use a randomized 'rounding' procedure to map the solution back to the constraint set for the original problem. If we can perform the rounding step without changing the value of the objective function substantially, then the rounded solution is also a decent solution to the original optimization problem.

<!-- chunk {"id": "body-0252", "role": "body", "section": "Application: Rounding for the MaxQP Relaxation", "weight": 1.0} -->

One difficult class of optimization problems has a matrix decision variable, and it requires us to maximize a quadratic form in the matrix variable subject to a set of convex quadratic constraints and a spectral norm constraint. This problem is referred to as MAXQP. The desired solution B to this problem is a d 1 ≤ d 2 matrix. The solution needs to satisfy several different requirements, but we focus on the condition that κ B κ · 1.

<!-- chunk {"id": "body-0253", "role": "body", "section": "Application: Rounding for the MaxQP Relaxation", "weight": 1.0} -->

There is a natural relaxation of the MAXQP problem. When we solve the relaxation, we obtain a family { B k: k ∅ 1,2,..., n } of d 1 ≤ d 2 matrices that satisfy the constraints In fact, these two bounds are part of the specification of the relaxed problem. To round the family of matrices back to a solution of the original problem, we form the random matrix where { % k } is an independent family of Rademacher random variables. The scaling factor fi ∪ 0 can be adjusted to guarantee that the norm constraint κ Z κ · 1 holds with high probability.

<!-- chunk {"id": "body-0254", "role": "body", "section": "Application: Rounding for the MaxQP Relaxation", "weight": 1.0} -->

What is the expected norm of Z ? Theorem 4.1.1 yields Here, the matrix variance statistic satisfies owing to the constraint (4.5.1) on the matrices B 1,..., B n. It follows that the scaling parameter fi should satisfy to ensure that E κ Z κ · 1. For this choice of fi, the rounded solution Z obeys the spectral norm constraint on average. By using the tail bound (4.1.6), we can even obtain high-probability estimates for the norm of the rounded solution Z.

<!-- chunk {"id": "body-0255", "role": "body", "section": "Application: Rounding for the MaxQP Relaxation", "weight": 1.0} -->

The important fact here is that the scaling parameter fi is usually small as compared with the other parameters of the problem ( d 1, d 2, n, and so forth). Therefore, the scaling does not have a massive effect on the value of the objective function. Ultimately, this approach leads to a technique for solving the MAXQP problem that produces a feasible point whose objective value is within a factor of p 2log( d 1 ⊕ d 2) of the maximum objective value possible.

<!-- chunk {"id": "body-0256", "role": "body", "section": "Analysis of Matrix Gaussian & Rademacher Series", "weight": 1.0} -->

We began this chapter with a concentration inequality, Theorem 4.1.1, for the norm of a matrix Gaussian series, and we have explored a number of different applications of this result. This section contains a proof of this theorem.

<!-- chunk {"id": "body-0257", "role": "body", "section": "RandomSeries with Hermitian Coefficients", "weight": 1.0} -->

As the development in Chapter 3 suggests, random Hermitian matrices provide the natural setting for establishing matrix concentration inequalities. Therefore, we begin our treatment with a detailed statement of the matrix concentration inequality for a Gaussian series with Hermitian matrix coefficients.

<!-- chunk {"id": "body-0258", "role": "body", "section": "RandomSeries with Hermitian Coefficients", "weight": 1.0} -->

Theorem 4.6.1 (Matrix Gaussian & Rademacher Series: The Hermitian Case). Consider a finite sequence { A k } of fixed Hermitian matrices with dimension d, and let { k } be a finite sequence of independent standard normal variables. Introduce the matrix Gaussian series Let v (Y) be the matrix variance statistic of the sum: The same bounds hold when we replace { k } by a finite sequence of independent Rademacher random variables.

<!-- chunk {"id": "body-0259", "role": "body", "section": "RandomSeries with Hermitian Coefficients", "weight": 1.0} -->

Furthermore, for all t ÷ 0, The proof of this result occupies the rest of the section.

<!-- chunk {"id": "body-0260", "role": "body", "section": "Discussion", "weight": 1.5} -->

Before we proceed to the analysis, let us take a moment to compare Theorem 4.6.1 with the result for general matrix series, Theorem 4.1.1.

<!-- chunk {"id": "body-0261", "role": "body", "section": "Discussion", "weight": 1.5} -->

First, we consider the matrix variance statistic v ( Y ) defined in (4.6.1). Since Y has zero mean, this definition coincides with the general formula (2.2.4). The second expression, in terms of the coefficient matrices, follows from the additivity property (2.2.6) for the variance of a sum of independent, random Hermitian matrices.

<!-- chunk {"id": "body-0262", "role": "body", "section": "Discussion", "weight": 1.5} -->

Next, bounds for the minimum eigenvalue, min(Y) follow from the results for the maximum eigenvalue because ϒ Y has the same distribution as Y. Therefore, The second identity holds because of the relationship (2.1.5) between minimum and maximum eigenvalues. Similar considerations lead to a lower tail bound for the minimum eigenvalue: This result follows directly from the upper tail bound (4.6.3).

<!-- chunk {"id": "body-0263", "role": "body", "section": "Discussion", "weight": 1.5} -->

This observation points to the most important difference between the Hermitian case and the general case. Indeed, Theorem 4.6.1 concerns the extreme eigenvalues of the random series Y instead of the norm. This change amounts to producing one-sided tail bounds instead of twosided tail bounds. For Gaussian and Rademacher series, this improvement is not really useful, but there are random Hermitian matrices whose minimum and maximum eigenvalues exhibit different types of behavior. For these problems, it can be extremely valuable to examine the two tails separately. See Chapter 5 and 6 for some results of this type.

<!-- chunk {"id": "body-0264", "role": "body", "section": "Analysis for Hermitian Gaussian Series", "weight": 1.0} -->

We continue with the proof that matrix Gaussian series exhibit the behavior described in Theorem 4.6.1. Afterward, we show how to adapt the argument to address matrix Rademacher series. Our main tool is Theorem 3.6.1, the set of master bounds for independent sums. To use this result, we must identify the cgf of a fixed matrix modulated by a Gaussian random variable.

<!-- chunk {"id": "body-0265", "role": "body", "section": "Analysis for Hermitian Gaussian Series", "weight": 1.0} -->

Lemma4.6.2 (Gaussian ≤ Matrix: Mgf and Cgf). Suppose that A is a fixed Hermitian matrix, and let be a standard normal random variable. Then Proof. Wemayassume ∅ 1 by absorbing into the matrix A. It is well known that the moments of a standard normal variable satisfy The formula for the odd moments holds because a standard normal variable is symmetric. One way to establish the formula for the even moments is to use integration by parts to obtain a recursion for the (2 q)th moment in terms of the (2 q ϒ 2)th moment.

<!-- chunk {"id": "body-0266", "role": "body", "section": "Analysis for Hermitian Gaussian Series", "weight": 1.0} -->

Therefore, the matrix mgf satisfies The first identity holds because the odd terms vanish from the series representation (2.1.15) of the matrix exponential when we take the expectation. To compute the cgf, we extract the logarithm of the mgf and recall (2.1.17), which states that the matrix logarithm is the functional inverse of the matrix exponential.

<!-- chunk {"id": "body-0267", "role": "body", "section": "Analysis for Hermitian Gaussian Series", "weight": 1.0} -->

We quickly reach results on the maximum eigenvalue of a matrix Gaussian series with Hermitian coefficients.

<!-- chunk {"id": "body-0268", "role": "body", "section": "Analysis for Hermitian Gaussian Series", "weight": 1.0} -->

Proof of Theorem 4.6.1: Gaussian Case. Consider a finite sequence { A k } of Hermitian matrices with dimension d, and let { k } be a finite sequence of independent standard normal variables. Define the matrix Gaussian series Webegin with the upper bound (4.6.2) for E, max(Y). The master expectation bound (3.6.1) from Theorem 3.6.1 implies that The second line follows when we introduce the cgf from Lemma 4.6.2. To reach the third inequality, we bound the trace by the dimension times the maximum eigenvalue. The fourth line is the Spectral Mapping Theorem, Proposition 2.1.3. Use the formula (4.6.1) to identify the matrix variance statistic v (Y) in the exponent. The infimum is attained at ∅ p 2 v (Y) ϒ 1 log d. This choice leads to (4.6.2).

<!-- chunk {"id": "body-0269", "role": "body", "section": "Analysis for Hermitian Gaussian Series", "weight": 1.0} -->

Next, we turn to the proof of the upper tail bound (4.6.3), max(Y). Invoke the master tail bound (3.6.3) from Theorem 3.6.1, and calculate that The steps here are the same as in the previous calculation. The infimum is achieved at ∅ t / v (Y), which yields (4.6.3).

<!-- chunk {"id": "body-0270", "role": "body", "section": "Analysis for Hermitian Rademacher Series", "weight": 1.0} -->

The inequalities for matrix Rademacher series involve arguments closely related to the proofs for matrix Gaussian series, but we require one additional piece of reasoning to obtain the simplest results. First, let us compute bounds for the matrix mgf and cgf of a Hermitian matrix modulated by a Rademacher random variable.

<!-- chunk {"id": "body-0271", "role": "body", "section": "Analysis for Hermitian Rademacher Series", "weight": 1.0} -->

Lemma4.6.3 (Rademacher ≤ Matrix: Mgf and Cgf). Suppose that A is a fixed Hermitian matrix, and let % be a Rademacher random variable. Then Proof. First, we establish a scalar inequality. Comparing Taylor series, The inequality holds because (2 q)! ÷ (2 q)(2 q ϒ 2) ′ ′ ′ ∅ 2 q q !.

<!-- chunk {"id": "body-0272", "role": "body", "section": "Analysis for Hermitian Rademacher Series", "weight": 1.0} -->

To compute the matrix mgf, we may assume ∅ 1. By direct calculation, Thesemidefinite bound follows when we apply the Transfer Rule (2.1.14) to the inequality (4.6.6). To determine the matrix cgf, observe that The semidefinite bound follows when we apply the Transfer Rule (2.1.14) to the scalar inequality logcosh(a) · a 2 /2 for a 2 R, which is a consequence of (4.6.6).

<!-- chunk {"id": "body-0273", "role": "body", "section": "Analysis for Hermitian Rademacher Series", "weight": 1.0} -->

We are prepared to develop some probability inequalities for the maximum eigenvalue of a Rademacher series with Hermitian coefficients.

<!-- chunk {"id": "body-0274", "role": "body", "section": "Analysis for Hermitian Rademacher Series", "weight": 1.0} -->

Proof of Theorem 4.6.1: Rademacher Case. Consider a finite sequence { A k } of Hermitian matrices, and let { % k } be a finite sequence of independent Rademacher variables. Define the matrix Rademacher series The bounds for the extreme eigenvalues of Y follow from an argument almost identical with the proof in the Gaussian case. The only point that requires justification is the inequality To obtain this result, we introduce the semidefinite bound, Lemma 4.6.3, for the Rademacher cgf into the trace exponential. The left-hand side increases after this substitution because of the fact (2.1.16) that the trace exponential function is monotone with respect to the semidefinite order.

<!-- chunk {"id": "body-0275", "role": "body", "section": "Analysis of Matrix Series with Rectangular Coefficients", "weight": 1.0} -->

Finally, we consider a series with non-Hermitian matrix coefficients modulated by independent Gaussian or Rademacher random variables. The bounds for the norm of a rectangular series follow instantly from the bounds for the norm of an Hermitian series because of a formal device. Wesimply apply the Hermitian results to the Hermitian dilation (2.1.26) of the series.

<!-- chunk {"id": "body-0276", "role": "body", "section": "Analysis of Matrix Series with Rectangular Coefficients", "weight": 1.0} -->

Proof of Theorem 4.1.1. Consider a finite sequence { B k } of d 1 ≤ d 2 complex matrices, and let { ‡ k } be a finite sequence of independent random variables, either standard normal or Rademacher.

<!-- chunk {"id": "body-0277", "role": "body", "section": "Analysis of Matrix Series with Rectangular Coefficients", "weight": 1.0} -->

Recall from Definition 2.1.5 that the Hermitian dilation is the map This leads us to form the two series The second expression for Y holds because the Hermitian dilation is real-linear. Since we have written Y as a matrix series with Hermitian coefficients, we may analyze it using Theorem 4.6.1. Wejust need to express the conclusions in terms of the random matrix Z.

<!-- chunk {"id": "body-0278", "role": "body", "section": "Analysis of Matrix Series with Rectangular Coefficients", "weight": 1.0} -->

First, we employ the fact (2.1.28) that the Hermitian dilation preserves spectral information: Therefore, bounds, max(Y) deliver bounds on κ Z κ. In view of the calculation (2.2.10) for the variance statistic of a dilation, we have Recall that the matrix variance statistic v (Z) defined in (4.1.3) coincides with the general definition from (2.2.8). Now, invoke Theorem 4.6.1 to obtain Theorem 4.1.1.

<!-- chunk {"id": "body-0279", "role": "body", "section": "Notes", "weight": 1.0} -->

We give an overview of research related to matrix Gaussian series, along with references for the specific random matrices that we have analyzed.

<!-- chunk {"id": "body-0280", "role": "body", "section": "Matrix Gaussian and Rademacher Series", "weight": 1.0} -->

The main results, Theorem 4.1.1 and Theorem 4.6.1, have an interesting history. In the precise form presented here, these two statements first appeared, but we can trace them back more than two decades.

<!-- chunk {"id": "body-0281", "role": "body", "section": "Matrix Gaussian and Rademacher Series", "weight": 1.0} -->

In his work [, Thm. 1], Oliveira established the mgf bounds presented in Lemma 4.6.2 and Lemma 4.6.3. He also developed an ingenious improvement on the arguments of Ahlswede & Winter [, App.], and he obtained a bound similar with Theorem 4.6.1. The constants in Oliveira's result are worse, but the dependence on the dimension is better because it depends on the number of summands. We do not believe that the approach Ahlswede & Winter describe can deliver any of these results.

<!-- chunk {"id": "body-0282", "role": "body", "section": "Matrix Gaussian and Rademacher Series", "weight": 1.0} -->

Recently, there have been some minor improvements to the dimensional factor that appears in Theorem 4.6.1. We discuss these results and give citations in Chapter 7.

<!-- chunk {"id": "body-0283", "role": "body", "section": "The Noncommutative Khintchine Inequality", "weight": 1.0} -->

Our theory about matrix Rademacher and Gaussian series should be compared with a classic result, called the noncommutative Khintchine inequality, that was originally due to LustPiquard; see also the follow-up work. In its simplest form, this inequality concerns a matrix Rademacher series with Hermitian coefficients: The noncommutative Khintchine inequality states that The minimum value of the constant C 2 q ∅ (2 q)!/(2 q q !) was obtained in the two papers. Traditional proofs of the noncommutative Khintchine inequality are quite involved, but there is now an elementary argument available [MJC ⊕ 14, Cor. 7.3].

<!-- chunk {"id": "body-0284", "role": "body", "section": "The Noncommutative Khintchine Inequality", "weight": 1.0} -->

Theorem 4.6.1 is the exponential moment analog of the polynomial moment bound (4.7.1). The polynomial moment inequality is somewhat stronger than the exponential moment inequality. Nevertheless, the exponential results are often more useful in practice. For a more thorough exploration of the relationships between Theorem 4.6.1 and noncommutative moment inequalities, such as (4.7.1), see the discussion in [, §4].

<!-- chunk {"id": "body-0285", "role": "body", "section": "Application to Random Matrices", "weight": 1.0} -->

It has also been known for a long time that results such as Theorem 4.6.1 and inequality (4.7.1) can be used to study random matrices.

<!-- chunk {"id": "body-0286", "role": "body", "section": "Application to Random Matrices", "weight": 1.0} -->

Webelieve that the geometric functional analysis literature contains the earliest applications of matrix concentration results to analyze random matrices. In a well-known paper, Mark Rudelson-acting on a suggestion of Gilles Pisier-showed how to use the noncommutative Khintchine inequality (4.7.1) to study covariance estimation. This work led to a significant amount of activity in which researchers used variants of Rudelson's argument to prove other types of results. See, for example, the paper. This approach is powerful, but it tends to require some effort to use.

<!-- chunk {"id": "body-0287", "role": "body", "section": "Application to Random Matrices", "weight": 1.0} -->

In parallel, other researchers in noncommutative probability theory also came to recognize the power of noncommutative moment inequalities in random matrix theory. The paper contains a specific example. Unfortunately, this literature is technically formidable, which makes it difficult for outsiders to appreciate its achievements.

<!-- chunk {"id": "body-0288", "role": "body", "section": "Application to Random Matrices", "weight": 1.0} -->

The work of Ahlswede & Winter led to the first 'packaged' matrix concentration inequalities of the type that we describe in these lecture notes. For the first few years after this work, most of the applications concerned quantum information theory and random graph theory. The paper introduced the method of Ahlswede & Winter to researchers in mathematical signal processing and statistics, and it served to popularize matrix concentration bounds.

<!-- chunk {"id": "body-0289", "role": "body", "section": "Application to Random Matrices", "weight": 1.0} -->

At this point, the available matrix concentration inequalities were still significantly suboptimal. The main advances led to optimal matrix concentration results of the kind that we present in these lecture notes. These results allow researchers to obtain reasonably accurate analyses of a wide variety of random matrices with very little effort.

<!-- chunk {"id": "body-0290", "role": "body", "section": "Wigner and Marˇ cenko-Pastur", "weight": 1.0} -->

Wigner matrices first emerged in the literature on nuclear physics, where they were used to modeltheHamiltoniansofreactionsinvolvingheavyatoms[, §1.1]. Wigner showed that the limiting spectral distribution of a certain type of Wigner matrix follows the semicircle law. See the book [, §2.4] of Tao for an overview and the book [, Chap. 2] of Bai & Silverstein for a complete treatment. The Bai-Yin law states that, up to scaling, the maximum eigenvalue of a Wigner matrix converges almost surely to two. See [, §2.3] or [, Chap. 5] for more information. The analysis of the Gaussian Wigner matrix that we present here, using Theorem 4.6.1, is drawn from [, §4].

<!-- chunk {"id": "body-0291", "role": "body", "section": "Wigner and Marˇ cenko-Pastur", "weight": 1.0} -->

Thefirst rigorous work on a rectangular Gaussian matrix is due to Marˇ cenko & Pastur, who established that the limiting distribution of the squared singular values follows a distribution that now bears their names. The Bai-Yin law gives an almost-sure limit for the largest singular value of a rectangular Gaussian matrix. The expectation bound (4.2.5) appears in a survey article by Davidson & Szarek. The latter result is ultimately derived from a comparison theorem for Gaussian processes due to Férnique and amplified by Gordon. Our approach, using Theorem 4.1.1, is based on [, §4].

<!-- chunk {"id": "body-0292", "role": "body", "section": "Randomly Signed Matrices", "weight": 1.0} -->

Matrices with randomly signed entries have not received much attention in the literature. The result (4.3.1) is due to Yoav Seginer. There is also a well-known paper by Rafał Latała that provides a bound for the expected norm of a Gaussian matrix whose entries have nonuniform variance. Riemer & Schütt have extended the earlier results. The very recent paper of Afonso Bandeira and Ramon Van Handel contains an elegant new proof of Seginer's result based on a general theorem for random matrices with independent entries. The analysis here, using Theorem 4.1.1, is drawn from [, §4].

<!-- chunk {"id": "body-0293", "role": "body", "section": "Gaussian Toeplitz Matrices", "weight": 1.0} -->

Research on random Toeplitz matrices is surprisingly recent, but there are now a number of papers available. Bryc, Dembo, & Jiang obtained the limiting spectral distribution of a symmetric Toeplitz matrix based on independent and identically distributed (iid) random variables. Later, Mark Meckes established the first bound for the expected norm of a random Toeplitz matrix based on iid random variables. More recently, Sen & Virág computed the limiting value of the expected norm of a random, symmetric Toeplitz matrix whose entries have identical second-order statistics. See the latter paper for additional references. The analysis here, based on Theorem 4.1.1, is new. Our lower bound for the value of E κ ¡ d κ follows from the results of Sen & Virág. We are not aware of any analysis for a random Toeplitz matrix whose entries have different variances, but this type of result would follow from a simple modification of the argument in §4.4.

<!-- chunk {"id": "body-0294", "role": "body", "section": "Relaxation and Rounding of MAXQP", "weight": 1.0} -->

The idea of using semidefinite relaxation and rounding to solve the MAXQP problem is due to Arkadi Nemirovski. He obtained nontrivial results on the performance of his method using some matrix moment calculations, but he was unable to reach the sharpest possible bound.

<!-- chunk {"id": "body-0295", "role": "body", "section": "Relaxation and Rounding of MAXQP", "weight": 1.0} -->

Anthony So pointed out that matrix moment inequalities imply an optimal result; he also showed that matrix concentration inequalities have applications to robust optimization. The presentation here, using Theorem 4.1.1, is essentially equivalent with the approach, but we have achieved slightly better bounds for the constants.

<!-- chunk {"id": "body-0296", "role": "body", "section": "ASumofRandom Positive-Semidefinite Matrices", "weight": 1.0} -->

This chapter presents matrix concentration inequalities that are analogous with the classical Chernoff bounds. In the matrix setting, Chernoff-type inequalities allow us to control the extreme eigenvalues of a sum of independent, random, positive-semidefinite matrices.

<!-- chunk {"id": "body-0297", "role": "body", "section": "ASumofRandom Positive-Semidefinite Matrices", "weight": 1.0} -->

More formally, we consider a finite sequence { X k } of independent, random Hermitian matrices that satisfy Introduce the sum Y ∅ P k X k. Our goal is to study the expectation and tail behavior of, max(Y) and, min(Y). Bounds on the maximum eigenvalue, max(Y) give us information about the norm of the matrix Y, a measure of how much the action of the matrix can dilate a vector. Bounds for the minimum eigenvalue, min(Y) tell us when the matrix Y is nonsingular; they also provide evidence about the norm of the inverse Y ϒ 1, when it exists.

<!-- chunk {"id": "body-0298", "role": "body", "section": "ASumofRandom Positive-Semidefinite Matrices", "weight": 1.0} -->

The matrix Chernoff inequalities are quite powerful, and they have numerous applications. We demonstrate the relevance of this theory by considering two examples. First, we show how to study the norm of a random submatrix drawn from a fixed matrix, and we explain how to check when the random submatrix has full rank. Second, we develop an analysis to determine when a random graph is likely to be connected. These two problems are closely related to basic questions in statistics and in combinatorics.

<!-- chunk {"id": "body-0299", "role": "body", "section": "ASumofRandom Positive-Semidefinite Matrices", "weight": 1.0} -->

In contrast, the matrix Bernstein inequalities, appearing in Chapter 6, describe how much a random matrix deviates from its mean value. As such, the matrix Bernstein bounds are more suitable than the matrix Chernoff bounds for problems that concern matrix approximations. Matrix Bernstein inequalities are also more appropriate when the variance v ( Y ) is small in comparison with the upper bound L on the summands.

<!-- chunk {"id": "body-0300", "role": "body", "section": "Overview", "weight": 1.0} -->

Section 5.1 presents the main results on the expectations and the tails of the extreme eigenvalues of a sum of independent, random, positive-semidefinite matrices. Section 5.2 explains how the matrix Chernoff bounds provide spectral information about a random submatrix drawn from a fixed matrix. In §5.3, we use the matrix Chernoff bounds to study when a random graph is connected. Afterward, in §5.4 we explain how to prove the main results.

<!-- chunk {"id": "body-0301", "role": "body", "section": "The Matrix Chernoff Inequalities", "weight": 1.0} -->

In the scalar setting, the Chernoff inequalities describe the behavior of a sum of independent, nonnegative random variables that are subject to a uniform upper bound. These results are often applied to study the number Y of successes in a sequence of independent-but not necessarily identical-Bernoulli trials with small probabilities of success. In this case, the Chernoff bounds show that Y behaves like a Poisson random variable. The random variable Y concentrates near the expected number of successes. Its lower tail has Gaussian decay, while its upper tail drops off faster than that of an exponential random variable. See [, §2.2] for more background.

<!-- chunk {"id": "body-0302", "role": "body", "section": "The Matrix Chernoff Inequalities", "weight": 1.0} -->

In the matrix setting, we encounter similar phenomena when we consider a sum of independent, random, positive-semidefinite matrices whose eigenvalues meet a uniform upper bound. This behavior emerges from the next theorem, which closely parallels the scalar Chernoff theorem.

<!-- chunk {"id": "body-0303", "role": "body", "section": "The Matrix Chernoff Inequalities", "weight": 1.0} -->

Theorem 5.1.1 (Matrix Chernoff). Consider a finite sequence { X k } of independent, random, Hermitian matrices with common dimension d. Assume that Introduce the random matrix Define the minimum eigenvalue ' min and maximum eigenvalue ' max of the expectation E Y: The proof of Theorem 5.1.1 appears below in §5.4.

<!-- chunk {"id": "body-0304", "role": "body", "section": "Discussion", "weight": 1.5} -->

Let us consider some facets of Theorem 5.1.1.

<!-- chunk {"id": "body-0305", "role": "body", "section": "Aspects of the Matrix Chernoff Inequality", "weight": 1.0} -->

In many situations, it is easier to work with streamlined versions of the expectation bounds: Weobtain these results by selecting ∅ 1 in both (5.1.3) and (5.1.4) and evaluating the numerical constants.

<!-- chunk {"id": "body-0306", "role": "body", "section": "Aspects of the Matrix Chernoff Inequality", "weight": 1.0} -->

These simplifications also help to clarify the meaning of Theorem 5.1.1. On average min( Y ) is not much smaller than, min( E Y ), minus a fluctuation term that reflects the maximum size L of a summand and the ambient dimension d. Similarly, the average value of, max( Y ) is close to, max( E Y ), plus the same fluctuation term.

<!-- chunk {"id": "body-0307", "role": "body", "section": "Aspects of the Matrix Chernoff Inequality", "weight": 1.0} -->

Wecan also weaken the tail bounds (5.1.5) and (5.1.6) to reach The first bound shows that the lower tail of, min(Y) decays at a subgaussian rate with variance L / ' min. The second bound manifests that the upper tail of, max(Y) decays faster than that of an exponential random variable with mean L / ' max. This is the same type of prediction we receive from the scalar Chernoff inequalities.

<!-- chunk {"id": "body-0308", "role": "body", "section": "Aspects of the Matrix Chernoff Inequality", "weight": 1.0} -->

As with other matrix concentration results, the tail bounds (5.1.5) and (5.1.6) can overestimate the actual tail probabilities for the extreme eigenvalues of Y, especially at large deviations from the mean. The value of the matrix Chernoff theorem derives from the estimates (5.1.3) and (5.1.4) for the expectation of the minimum and maximum eigenvalue of Y. Scalar concentration inequalities may provide better estimates for tail probabilities.

<!-- chunk {"id": "body-0309", "role": "body", "section": "Related Results", "weight": 1.0} -->

Wecan moderate the dimensional factor d in the bounds, max( Y ) from Theorem 5.1.1 when the random matrix Y has limited spectral content in most directions. We take up this analysis in Chapter 7.

<!-- chunk {"id": "body-0310", "role": "body", "section": "Related Results", "weight": 1.0} -->

Next, let us present an important refinement [, Thm. A.1] of the bound (5.1.8) that can be very useful in practice: This estimate may be regarded as a matrix version of Rosenthal's inequality. Observe that the uniform bound L appearing in (5.1.8) always exceeds the large parenthesis on the right-hand side of (5.1.9). Therefore, the estimate (5.1.9) is valuable when the summands are unbounded and, especially, when they have heavy tails. See the notes at the end of the chapter for more information.

<!-- chunk {"id": "body-0311", "role": "body", "section": "Optimality of the Matrix Chernoff Bounds", "weight": 1.0} -->

In this section, we explore how well bounds such as Theorem 5.1.1 and inequality (5.1.9) describe the behavior of a random matrix Y formed as a sum of independent, random positivesemidefinite matrices.

<!-- chunk {"id": "body-0312", "role": "body", "section": "The Upper Chernoff Bounds", "weight": 1.0} -->

We will demonstrate that both terms in the matrix Rosenthal inequality (5.1.9) are necessary. More precisely, Therefore, we have identified appropriate parameters for bounding E, max(Y), although the constants and the logarithm may not be sharp in every case.

<!-- chunk {"id": "body-0313", "role": "body", "section": "The Upper Chernoff Bounds", "weight": 1.0} -->

The appearance of ' max on the left-hand side of (5.1.10) is a consequence of Jensen's inequality. Indeed, the maximum eigenvalue is convex, so To justify the other term, apply the fact that the summands X k are positive semidefinite to conclude that We have used the fact that, max(A ⊕ H) ÷, max(A) whenever H is positive semidefinite. Average the last two displays to develop the left-hand side of (5.1.10). The right-hand side of (5.1.10) is obviously just (5.1.9).

<!-- chunk {"id": "body-0314", "role": "body", "section": "The Upper Chernoff Bounds", "weight": 1.0} -->

A simple example suffices to show that the logarithm cannot always be removed from the second term in (5.1.8) or from (5.1.9). For each natural number n, consider the d ≤ d random matrix where ' -(n) i k ' is an independent family of BERNOULLI(n ϒ 1) random variables and E kk is the d ≤ d matrix with a one in the (k, k) entry an zeros elsewhere. An easy application of (5.1.8) delivers Using the Poisson limit of a binomial random variable and the Skorokhod representation, we can construct an independent family { Qk } of POISSON random variables for which Therefore, the logarithm on the second term in (5.1.8) cannot be reduced by a factor larger than the iterated logarithm loglog d. This modest loss comes from approximations we make when developing the estimate for the mean. The tail bound (5.1.6) accurately predicts the order of, max(Y n) in this example.

<!-- chunk {"id": "body-0315", "role": "body", "section": "The Upper Chernoff Bounds", "weight": 1.0} -->

Thelatter example depends on the commutativity of the summands and the infinite divisibility of the Poisson distribution, so it may seem rather special. Nevertheless, the logarithm really does belong in many (but not all!) examples that arise in practice. In particular, it is necessary in the application to random submatrices in §5.2.

<!-- chunk {"id": "body-0316", "role": "body", "section": "The Lower Chernoff Bounds", "weight": 1.0} -->

The upper expectation bound (5.1.4) is quite satisfactory, but the situation is murkier for the lower expectation bound (5.1.3). The mean term appears naturally in the lower bound: This estimate is a consequence of Jensen's inequality and the concavity of the minimum eigenvalue. On the other hand, it is not clear what the correct form of the second term in (5.1.3) should be for a general sum of random positive-semidefinite matrices.

<!-- chunk {"id": "body-0317", "role": "body", "section": "The Lower Chernoff Bounds", "weight": 1.0} -->

Nevertheless, a simple example demonstrates that the lower Chernoff bound (5.1.3) is numerically sharp in some situations. Let X be a d ≤ d random positive-semidefinite matrix that satisfies It is clear that E X ∅ I d. Form the random matrix The lower Chernoff bound (5.1.3) implies that The parameter ∪ 0 is at our disposal. This analysis predicts that E, min(Y n) ∪ 0 precisely when n ∪ d log d.

<!-- chunk {"id": "body-0318", "role": "body", "section": "The Lower Chernoff Bounds", "weight": 1.0} -->

Ontheotherhand max( Y n ) ∪ 0 if and only if each diagonal matrix d E i i appears at least once amongthesummands X 1,..., X n. To determine the probability that this event occurs, notice that this question is an instance of the coupon collector problem [, §3.6]. The probability of collecting all d coupons within n draws undergoes a phase transition from about zero to about one at n ∅ d log d. By refining this argument, we can verify that both lower Chernoff bounds (5.1.3) and (5.1.5) provide a numerically sharp lower bound for the value of n where the phase transition occurs. In other words, the lower matrix Chernoff bounds are themselves sharp.

<!-- chunk {"id": "body-0319", "role": "body", "section": "Example: A Random Submatrix of a Fixed Matrix", "weight": 1.0} -->

The matrix Chernoff inequality can be used to bound the extreme singular values of a random submatrix drawn from a fixed matrix. Theorem 5.1.1 might not seem suitable for this purpose because it deals with eigenvalues, but we can connect the method with the problem via a simple transformation. The results in this section have found applications in randomized linear algebra, sparse approximation, machine learning, and other fields. See the notes at the end of the chapter for some additional discussion and references.

<!-- chunk {"id": "body-0320", "role": "body", "section": "ARandomColumnSubmatrix", "weight": 1.0} -->

Let B be a fixed d ≤ n matrix, and let b: k denote the k th column of this matrix. The matrix can be expressed as the sum of its columns: The symbol e k refers to the standard basis (column) vector with a one in the k th component and zeros elsewhere; the length of the vector e k is determined by context.

<!-- chunk {"id": "body-0321", "role": "body", "section": "ARandomColumnSubmatrix", "weight": 1.0} -->

We consider a simple model for a random column submatrix. Let { -k } be an independent sequence of BERNOULLI(p / n) random variables. Define the random matrix That is, we include each column independently with probability p / n, which means that there are typically about p nonzero columns in the matrix. We do not remove the other columns; we just zero them out.

<!-- chunk {"id": "body-0322", "role": "body", "section": "ARandomColumnSubmatrix", "weight": 1.0} -->

In this section, we will obtain bounds on the expectation of the extreme singular values 1(Z) and d (Z) of the d ≤ n random matrix Z. More precisely, That is, the random submatrix Z gets its 'fair share' of the squared singular values of the original matrix B. There is a fluctuation term that depends on largest norm of a column of B and the logarithm of the number d of rows in B. This result is very useful because a positive lower bound on d (Z) ensures that the rows of the random submatrix Z are linearly independent.

<!-- chunk {"id": "body-0323", "role": "body", "section": "The Analysis", "weight": 1.0} -->

To study the singular values of Z, it is convenient to define a d ≤ d random, positive-semidefinite matrix Note that -2 k ∅ -k because -k only takes the values zero and one. The eigenvalues of Y determine the singular values of Z, and vice versa. In particular, where we arrange the singular values of Z in weakly decreasing order 1(Z) ÷′′′ ÷ d (Z).

<!-- chunk {"id": "body-0324", "role": "body", "section": "The Analysis", "weight": 1.0} -->

The matrix Chernoff inequality provides bounds for the expectations of the eigenvalues of Y. To apply the result, first calculate Define L ∅ max k κ b: k κ 2, and observe that κ -k b: k b /: k κ · L for each index k. The simplified matrix Chernoff bounds (5.1.7) and (5.1.8) now deliver the result (5.2.1).

<!-- chunk {"id": "body-0325", "role": "body", "section": "ARandomRowandColumnSubmatrix", "weight": 1.0} -->

Next, we consider a model for a random set of rows and columns drawn from a fixed d ≤ n matrix B. In this case, it is helpful to use matrix notation to represent the extraction of a submatrix. Define independent random projectors where { -k } is an independent family of BERNOULLI(p / d) random variables and { » k } is an independent family of BERNOULLI(r / n) random variables. Then is a random submatrix of B with about p nonzero rows and r nonzero columns.

<!-- chunk {"id": "body-0326", "role": "body", "section": "ARandomRowandColumnSubmatrix", "weight": 1.0} -->

In this section, we will show that The notations b j: and b: k refer to the j th row and k th column of the matrix B, while bjk is the (j, k) entry of the matrix. In other words, the random submatrix Z gets its share of the total squared norm of the matrix B. The fluctuation terms reflect the maximum row norm and the maximum column norm of B, as well as the size of the largest entry. There is also a weak dependence on the ambient dimensions d and n.

<!-- chunk {"id": "body-0327", "role": "body", "section": "The Analysis", "weight": 1.0} -->

The argument has much in common with the calculations for a random column submatrix, but we need to do some extra work to handle the interaction between the random row sampling and the random column sampling.

<!-- chunk {"id": "body-0328", "role": "body", "section": "The Analysis", "weight": 1.0} -->

To begin, we express the squared norm κ Z κ 2 in terms of the maximum eigenvalue of a randompositive-semidefinite matrix: We have used the fact that RR / ∅ R, and the notation (PB): k refers to the k th column of the matrix PB. Observe that the random positive-semidefinite matrix on the right-hand side has dimension d. Invoking the matrix Chernoff inequality (5.1.8), conditional on the choice of P, we obtain The required calculation is analogous with the one in the Section 5.2.1, so we omit the details. To reach a deterministic bound, we still have two more expectations to control.

<!-- chunk {"id": "body-0329", "role": "body", "section": "The Analysis", "weight": 1.0} -->

Next, we examine the term in (5.2.3) that involves the maximum eigenvalue: Thefirst identity holds because, max(CC /) ∅, max(C / C) for any matrix C, and PP / ∅ P. Observe that the random positive-semidefinite matrix on the right-hand side has dimension n, and apply the matrix Chernoff inequality (5.1.8) again to reach Recall that, max(B / B) ∅κ B κ 2 to simplify this expression slightly.

<!-- chunk {"id": "body-0330", "role": "body", "section": "The Analysis", "weight": 1.0} -->

Last, we develop a bound on the maximum column norm in (5.2.3). This result also follows from the matrix Chernoff inequality, but we need to do a little work to see why. There are more direct proofs, but this approach is closer in spirit to the rest of our proof.

<!-- chunk {"id": "body-0331", "role": "body", "section": "The Analysis", "weight": 1.0} -->

We are going to treat the maximum column norm as the maximum eigenvalue of a sum of independent, random diagonal matrices. Observe that Using this representation, we see that To activate the matrix Chernoff bound, we need to compute the two parameters that appear in (5.1.8). First, the uniform upper bound L satisfies Second, to compute ' max, note that Take the maximum eigenvalue of this expression to reach Therefore, the matrix Chernoff inequality implies Onaverage, the maximum squared column norm of a random submatrix PB with approximately p nonzero rows gets its share p / d of the maximum squared column norm of B, plus a fluctuation term that depends on the magnitude of the largest entry of B and the logarithm of the number n of columns.

<!-- chunk {"id": "body-0332", "role": "body", "section": "The Analysis", "weight": 1.0} -->

Combine the three bounds (5.2.3), (5.2.4), and (5.2.5) to reach the result (5.2.2). We have simplified numerical constants to make the expression more compact.

<!-- chunk {"id": "body-0333", "role": "body", "section": "Application: When is an Erd˝ os-Rényi Graph Connected?", "weight": 1.0} -->

Random graph theory concerns probabilistic models for the interactions between pairs of objects. One basic question about a random graph is to ask whether there is a path connecting every pair of vertices or whether there are vertices segregated in different parts of the graph. It is possible to address this problem by studying the eigenvalues of random matrices, a challenge that we take up in this section.

<!-- chunk {"id": "body-0334", "role": "body", "section": "The Model of Erd˝ os & Rényi", "weight": 1.0} -->

The simplest possible example of a random graph is the independent model G (n, p) of Erd˝ os and Rényi. The number n is the number of vertices in the graph, and p 2 is the probability that two vertices are connected. More precisely, here is how to construct a random graph in G (n, p). Between each pair of distinct vertices, we place an edge independently at random with probability p. In other words, the adjacency matrix takes the form Figure 5.1: The adjacency matrix of an Erd˝ os-Rényi graph. This figure shows the pattern of nonzero entries in the adjacency matrix A of a random graph drawn from G (100,0.1). Out of a possible 4,950 edges, there are 486 edges present. A basic question is whether the graph is connected. The graph is dis connected if and only if there is a permutation of the vertices so that the adjacency matrix is block diagonal. This property is reflected in the second-smallest eigenvalue of the Laplacian matrix ¢.

<!-- chunk {"id": "body-0335", "role": "body", "section": "The Model of Erd˝ os & Rényi", "weight": 1.0} -->

The family { » j k: 1 · j ∩ k · n } consists of mutually independent BERNOULLI( p ) random variables. Figure 5.3.2 shows one realization of the adjacency matrix of an Erd˝ os-Rényi graph.

<!-- chunk {"id": "body-0336", "role": "body", "section": "The Model of Erd˝ os & Rényi", "weight": 1.0} -->

Let us explain how to represent the adjacency matrix and Laplacian matrix of an Erd˝ os-Rényi graph as a sum of independent random matrices. The adjacency matrix A of a random graph in G (n, p) can be written as This expression is a straightforward translation of the definition (5.3.1) into matrix form. Similarly, the Laplacian matrix ¢ of the random graph can be expressed as To verify the formula (5.3.3), observe that the presence of an edge between the vertices j and k increases the degree of j and k by one. Therefore, when » j k ∅ 1, we augment the (j, j) and (k, k) entries of ¢ to reflect the change in degree, and we mark the (j, k) and (k, j) entries with ϒ 1 to reflect the presence of the edge between j and k.

<!-- chunk {"id": "body-0337", "role": "body", "section": "Connectivity of an Erd˝ os-Rényi Graph", "weight": 1.0} -->

We will obtain a near-optimal bound for the range of parameters where an Erd˝ os-Rényi graph G ( n, p ) is likely to be connected. We can accomplish this goal by showing that the second smallest eigenvalue of the n ≤ n random Laplacian matrix ¢ ∅ D ϒ A is strictly positive. We will solve the problem by using the matrix Chernoff inequality to study the second-smallest eigenvalue of the random Laplacian ¢.

<!-- chunk {"id": "body-0338", "role": "body", "section": "Connectivity of an Erd˝ os-Rényi Graph", "weight": 1.0} -->

Weneedtoformarandommatrix Y that consists of independent positive-semidefinite terms and whose minimum eigenvalue coincides with the second-smallest eigenvalue of ¢. Our approach is to compress the matrix Y to the orthogonal complement of the vector e of ones. To that end, we introduce an (n ϒ 1) ≤ n partial isometry R that satisfies Now, consider the (n ϒ 1) ≤ (n ϒ 1) random matrix Recall that { » j k } is an independent family of BERNOULLI(p) random variables, so the summands are mutually independent. The Conjugation Rule (2.1.12) ensures that each summand remains positive semidefinite. Furthermore, the Courant-Fischer theorem implies that the minimum eigenvalue of Y coincides with the second-smallest eigenvalue of ¢ because the smallest eigenvalue of ¢ has eigenvector e.

<!-- chunk {"id": "body-0339", "role": "body", "section": "Connectivity of an Erd˝ os-Rényi Graph", "weight": 1.0} -->

To apply the matrix Chernoff inequality, we show that L ∅ 2 is an upper bound for the eigenvalues of each summand in (5.3.4). We have The first bound follows from the submultiplicativity of the spectral norm. To obtain the second bound, note that » j k takes 0-1 values. The matrix R is a partial isometry so its norm equals one. Finally, a direct calculation shows that T ∅ E j j ⊕ E kk ϒ E j k ϒ E k j satisfies the polynomial T 2 ∅ 2 T, so each eigenvalue of T must equal zero or two.

<!-- chunk {"id": "body-0340", "role": "body", "section": "Connectivity of an Erd˝ os-Rényi Graph", "weight": 1.0} -->

Next, we compute the expectation of the matrix Y.

<!-- chunk {"id": "body-0341", "role": "body", "section": "Connectivity of an Erd˝ os-Rényi Graph", "weight": 1.0} -->

The first identity follows when we apply linearity of expectation to (5.3.5) and then use linearity of matrix multiplication to draw the sum inside the conjugation by R. Theterm(n ϒ 1) I n emerges whenwesumthediagonalmatrices. The term ee / ϒ I n comesfromthe off-diagonal matrix units, once we note that the matrix ee / has one in each component. The last identity holds because of the properties of R displayed in (5.3.4). We conclude that This is all the information we need.

<!-- chunk {"id": "body-0342", "role": "body", "section": "Connectivity of an Erd˝ os-Rényi Graph", "weight": 1.0} -->

To arrive at a probability inequality for the second-smallest eigenvalue, ∀ 2 (¢) of the matrix ¢, we apply the tail bound (5.1.5) to the matrix Y. Weobtain, for t 2, To appreciate what this means, we may think about the situation where t ! 0. Then the bracket tends to e ϒ 1, and we see that the second-smallest eigenvalue of ¢ is unlikely to be zero when log(n ϒ 1) ϒ pn /2 ∩ 0. Rearranging this expression, we obtain a sufficient condition for an Erd˝ os-Rényi graph G (n, p) to be connected with high probability as n !1. This bound is quite close to the optimal result, which lacks the factor two on the right-hand side. It is possible to make this reasoning more precise, but it does not seem worth the fuss.

<!-- chunk {"id": "body-0343", "role": "body", "section": "Notes", "weight": 1.0} -->

As usual, we continue with an overview of background references and related work.

<!-- chunk {"id": "body-0344", "role": "body", "section": "Matrix Chernoff Inequalities", "weight": 1.0} -->

Scalar Chernoff inequalities date to the paper [, Thm. 1] by Herman Chernoff. The original result provides probability bounds for the number of successes in a sequence of independent but non-identical Bernoulli trials. Chernoff's proof combines the scalar Laplace transform method with refined bounds on the mgf of a Bernoulli random variable. It is very common to encounter simplified versions of Chernoff's result, such as [, Exer. 8] or [, §4.1].

<!-- chunk {"id": "body-0345", "role": "body", "section": "Matrix Chernoff Inequalities", "weight": 1.0} -->

In their paper, Ahlswede & Winter developed a matrix version of the Chernoff inequality. The matrix mgf bound, Lemma 5.4.1, essentially appears in their work. Ahlswede & Winter focus on the case of independent and identically distributed random matrices, in which case their results are roughly equivalent with Theorem 5.1.1. For the general case, their approach leads to matrix expectation statistics of the form It is clear that their ' AW min may be substantially smaller than the quantity ' min we defined in Theorem 5.1.1. Similarly, their ' AW max may be substantially larger than the quantity ' max that drives the upper Chernoff bounds.

<!-- chunk {"id": "body-0346", "role": "body", "section": "Matrix Chernoff Inequalities", "weight": 1.0} -->

The tail bounds from Theorem 5.1.1 are drawn from [, §5], but the expectation bounds we present are new. The technical report extends the matrix Chernoff inequality to provide upper and lower tail bounds for all eigenvalues of a sum of random, positive-semidefinite matrices. Chapter 7 contains a slight improvement of the bounds for the maximum eigenvalue in Theorem 5.1.1.

<!-- chunk {"id": "body-0347", "role": "body", "section": "Matrix Chernoff Inequalities", "weight": 1.0} -->

Let us mention a few other results that are related to the matrix Chernoff inequality. First, Theorem 5.1.1 has a lovely information-theoretic formulation where the tail bounds are stated in terms of an information divergence. To establish this result, we must restructure the proof and eliminate some of the approximations. See [, Thm. 19] or [, Thm. 5.1].

<!-- chunk {"id": "body-0348", "role": "body", "section": "Matrix Chernoff Inequalities", "weight": 1.0} -->

Second, the problem of bounding the minimum eigenvalue of a sum of random, positivesemidefinite matrices has a special character. The reason, roughly, is that a sum of independent, nonnegative random variables cannot easily take the value zero. A closely related phenomenon holds in the matrix setting, and it is possible to develop estimates that exploit this observation. See [, Thm. 3.1] and [, Thm. 1.3] for two wildly different approaches.

<!-- chunk {"id": "body-0349", "role": "body", "section": "The Matrix Rosenthal Inequality", "weight": 1.0} -->

The matrix Rosenthal inequality (5.1.9) is one of the earliest matrix concentration bounds. In his paper, Rudelson used the noncommutative Khintchine inequality (4.7.1) to establish a specialization of (5.1.9) to rank-one summands. A refinement appears, and explicit constants were first derived. We believe that the paper contains the first complete statement of the moment bound (5.1.9) for general positive-semidefinite summands; see also the work. The constants in [, Thm. A.1], and hence in (5.1.9), can be improved slightly by using the sharp version of the noncommutative Khintchine inequality. Let us stress that all of these results follow from easy variations of Rudelson's argument.

<!-- chunk {"id": "body-0350", "role": "body", "section": "The Matrix Rosenthal Inequality", "weight": 1.0} -->

The work [MJC ⊕ 14, Cor. 7.4] provides a self-contained and completely elementary proof of a matrix Rosenthal inequality that is closely related to (5.1.9). This result depends on different principles from the works mentioned in the last paragraph.

<!-- chunk {"id": "body-0351", "role": "body", "section": "RandomSubmatrices", "weight": 1.0} -->

The problem of studying a random submatrix drawn from a fixed matrix has a long history. An early example is the paving problem from operator theory, which asks for a maximal wellconditioned set of columns (or a well-conditioned submatrix) inside a fixed matrix. Random selection provides a natural way to approach this question. The papers of Bourgain & Tzafriri and Kashin & Tzafriri study random paving using sophisticated tools from functional analysis. See the paper for a summary of research on randomized methods for constructing pavings. Very recently, Adam Marcus, Dan Spielman, & Nikhil Srivastava have solved the paving problem completely.

<!-- chunk {"id": "body-0352", "role": "body", "section": "RandomSubmatrices", "weight": 1.0} -->

Later, Rudelson and Vershynin showed that the noncommutative Khintchine inequality provides a clean way to bound the norm of a random column submatrix (or a random row and column submatrix) drawn from a fixed matrix. Their ideas have found many applications in the mathematical signal processing literature. For example, the paper uses similar techniques to analyze the perfomance of ' 1 minimization for recovering a random sparse signal. The same methods support the paper, which contains a modern proof of the random paving result [, Thm. 2.1] of Bourgain & Tzafriri.

<!-- chunk {"id": "body-0353", "role": "body", "section": "RandomSubmatrices", "weight": 1.0} -->

The article contains the observation that the matrix Chernoff inequality is an ideal tool for studying random submatrices. It applies this technique to study a random matrix that arises in numerical linear algebra, and it achieves an optimal estimate for the minimum singular value of the random matrix that arises in this setting. Our analysis of a random column submatrix is based on this work. The analysis of a random row and column submatrix is new. The paper, by Chrétien and Darses, uses matrix Chernoff bounds in a more sophisticated way to develop tail bounds for the norm of a random row and column submatrix.

<!-- chunk {"id": "body-0354", "role": "body", "section": "RandomGraphs", "weight": 1.0} -->

The analysis of random graphs and random hypergraphs appeared as one of the earliest applications of matrix concentration inequalities. Christofides and Markström developed a matrix Hoeffding inequality to aid in this purpose. Later, Oliveira wrote two papers on random graph theory based on matrix concentration. We recommend these works for further information.

<!-- chunk {"id": "body-0355", "role": "body", "section": "RandomGraphs", "weight": 1.0} -->

To analyze the random graph Laplacian, we compressed the Laplacian to a subspace so that the minimum eigenvalue of the compression coincides with the second-smallest eigenvalue of the original Laplacian. This device can be extended to obtain tail bounds for all the eigenvalues of a sum of independent random matrices. See the technical report for a development of this idea.

<!-- chunk {"id": "body-0356", "role": "body", "section": "ASumofBounded RandomMatrices", "weight": 1.0} -->

In this chapter, we describe matrix concentration inequalities that generalize the classical Bernstein bound. The matrix Bernstein inequalities concern a random matrix formed as a sum of independent, random matrices that are bounded in spectral norm. The results allow us to study how much this type of random matrix deviates from its mean value in the spectral norm.

<!-- chunk {"id": "body-0357", "role": "body", "section": "ASumofBounded RandomMatrices", "weight": 1.0} -->

Formally, we consider an finite sequence { S k } of random matrices of the same dimension. Assume that the matrices satisfy the conditions E S k ∅ 0 and κ S k κ · L for each index k.

<!-- chunk {"id": "body-0358", "role": "body", "section": "ASumofBounded RandomMatrices", "weight": 1.0} -->

Form the sum Z ∅ P k S k. The matrix Bernstein inequality controls the expectation and tail behavior of κ Z κ in terms of the matrix variance statistic v ( Z ) and the uniform bound L.

<!-- chunk {"id": "body-0359", "role": "body", "section": "ASumofBounded RandomMatrices", "weight": 1.0} -->

The matrix Bernstein inequality is a powerful tool with a huge number of applications. In these pages, we can only give a coarse indication of how researchers have used this result, so we have chosen to focus on problems that use random sampling to approximate a specified matrix. This model applies to the sample covariance matrix in the introduction. In this chapter, we outline several additional examples. First, we consider the technique of randomized sparsification, in which we replace a dense matrix with a sparse proxy that has similar spectral behavior. Second, we explain how to develop a randomized algorithm for approximate matrix multiplication, and we establish an error bound for this method. Third, we develop an analysis of random features, a method for approximating kernel matrices that has become popular in contemporary machine learning.

<!-- chunk {"id": "body-0360", "role": "body", "section": "ASumofBounded RandomMatrices", "weight": 1.0} -->

As these examples suggest, the matrix Bernstein inequality is very effective for studying randomized approximations of a given matrix. Nevertheless, when the matrix Chernoff inequality, Theorem 5.1.1, happens to apply to a problem, it often delivers better results.

<!-- chunk {"id": "body-0361", "role": "body", "section": "Overview", "weight": 1.0} -->

Section 6.1 describes the matrix Bernstein inequality. Section 6.2 explains how to use the Bernstein inequality to study randomized methods for matrix approximation. In §§6.3, 6.4, and 6.5, we apply the latter result to three matrix approximation problems. We conclude with the proof of the matrix Bernstein inequality in §6.6.

<!-- chunk {"id": "body-0362", "role": "body", "section": "ASumofBoundedRandomMatrices", "weight": 1.0} -->

In the scalar setting, the label 'Bernstein inequality' applies to a very large number of concentration results. Most of these bounds have extensions to matrices. For simplicity, we focus on the most famous of the scalar results, a tail bound for the sum Z of independent, zero-mean random variables that are subject to a uniform bound. In this case, the Bernstein inequality shows that Z concentrates around zero. The tails of Z make a transition from subgaussian decay at moderate deviations to subexponential decay at large deviations. See [, §2.7] for more information about Bernstein's inequality.

<!-- chunk {"id": "body-0363", "role": "body", "section": "ASumofBoundedRandomMatrices", "weight": 1.0} -->

In analogy, the simplest matrix Bernstein inequality concerns a sum of independent, zeromean random matrices whose norms are bounded above. The theorem demonstrates that the norm of the sum acts much like the scalar random variable Z that we discussed in the last paragraph.

<!-- chunk {"id": "body-0364", "role": "body", "section": "ASumofBoundedRandomMatrices", "weight": 1.0} -->

Theorem 6.1.1 (Matrix Bernstein). Consider a finite sequence { S k } of independent, random matrices with common dimension d 1 ≤ d 2. Assume that Introduce the random matrix Let v (Z) be the matrix variance statistic of the sum: Furthermore, for all t ÷ 0, The proof of Theorem 6.1.1 appears in §6.6.

<!-- chunk {"id": "body-0365", "role": "body", "section": "Discussion", "weight": 1.5} -->

Let us spend a few moments to discuss the matrix Bernstein inequality, Theorem 6.1.1, its consequences, and some of the improvements that are available.

<!-- chunk {"id": "body-0366", "role": "body", "section": "Aspects of the Matrix Bernstein Inequality", "weight": 1.0} -->

First, observe that the matrix variance statistic v (Z) appearing in (6.1.1) coincides with the general definition (2.2.8) because Z has zero mean. To reach (6.1.2), we have used the additivity law (2.2.11) for an independent sum to express the matrix variance statistic in terms of the summands. Observe that, when the summands S k are Hermitian, the two terms in the maximum coincide. π The expectation bound (6.1.3) shows that E κ Z κ is on the same scale as the root v (Z) of the matrix variance statistic and the upper bound L for the summands; there is also a weak dependence on the ambient dimension d. In general, all three of these features are necessary. Nevertheless, the bound may not be very tight for particular examples. See Section 6.1.2 for some evidence.

<!-- chunk {"id": "body-0367", "role": "body", "section": "Aspects of the Matrix Bernstein Inequality", "weight": 1.0} -->

Next, let us explain how to interpret the tail bound (6.1.4). The main difference between this result and the scalar Bernstein bound is the appearance of the dimensional factor d 1 ⊕ d 2, which reduces the range of t where the inequality is informative. To get a better idea of what this result means, it is helpful to make a further estimate: In other words, for moderate values of t, the tail probability decays as fast as the tail of a Gaussian random variable whose variance is comparable with v (Z). For larger values of t, the tail probability decays at least as fast as that of an exponential random variable whose mean is comparable with L. As usual, we insert a warning that the tail behavior reported by the matrix Bernstein inequality can overestimate the actual tail behavior.

<!-- chunk {"id": "body-0368", "role": "body", "section": "Aspects of the Matrix Bernstein Inequality", "weight": 1.0} -->

Last, it is helpful to remember that the matrix Bernstein inequality extends to a sum of uncentered random matrices. In this case, the result describes the spectral-norm deviation of the random sum from its mean value. For reference, we include the statement here.

<!-- chunk {"id": "body-0369", "role": "body", "section": "Aspects of the Matrix Bernstein Inequality", "weight": 1.0} -->

Corollary 6.1.2 (Matrix Bernstein: Uncentered Summands). Consider a finite sequence { S k } of independent random matrices with common dimension d 1 ≤ d 2. Assume that each matrix has uniformly bounded deviation from its mean: and let v (Z) denote the matrix variance statistic of the sum: Furthermore, for all t ÷ 0, This result follows as an immediate corollary of Theorem 6.1.1.

<!-- chunk {"id": "body-0370", "role": "body", "section": "Related Results", "weight": 1.0} -->

The bounds in Theorem 6.1.1 are stated in terms of the ambient dimensions d 1 and d 2 of the random matrix Z. The dependence on the ambient dimension is not completely natural. For example, consider embedding the random matrix Z into the top corner of a much larger matrix which is zero everywhere else. It turns out that we can achieve results that reflect only the 'intrinsic dimension' of Z. Weturn to this analysis in Chapter 7.

<!-- chunk {"id": "body-0371", "role": "body", "section": "Related Results", "weight": 1.0} -->

In addition, there are many circumstances where the uniform upper bound L that appears in (6.1.3) does not accurately reflect the tail behavior of the random matrix. For instance, the summands themselves may have very heavy tails. In such emergencies, the following expectation bound [, Thm. A.1] can be a lifesaver.

<!-- chunk {"id": "body-0372", "role": "body", "section": "Related Results", "weight": 1.0} -->

This result is a matrix formulation of the Rosenthal-Pinelis inequality [, Thm. 4.1].

<!-- chunk {"id": "body-0373", "role": "body", "section": "Related Results", "weight": 1.0} -->

Finally, let us reiterate that there are other types of matrix Bernstein inequalities. For example, we can sharpen the tail bound (6.1.4) to obtain a matrix Bennett inequality. We can also relax the boundedness assumption to a weaker hypothesis on the growth of the moments of each summand S k. In the Hermitian setting, the result can also discriminate the behavior of the upper and lower tails, which is a consequence of Theorem 6.6.1 below. See the notes at the end of this chapter and the annotated bibliography for more information.

<!-- chunk {"id": "body-0374", "role": "body", "section": "Optimality of the Matrix Bernstein Inequality", "weight": 1.0} -->

To use the matrix Bernstein inequality, Theorem 6.1.1, and its relatives with intelligence, one must appreciate their strengths and weaknesses. We will focus on the matrix Rosenthal-Pinelis inequality (6.1.6). Nevertheless, similar insights are relevant to the estimate (6.1.3).

<!-- chunk {"id": "body-0375", "role": "body", "section": "The Expectation Bound", "weight": 1.0} -->

Let us present lower bounds to demonstrate that the matrix Rosenthal-Pinelis inequality (6.1.6) requires both terms that appear. First, the quantity v (Z) cannot be omitted because Jensen's inequality implies that Under a natural hypothesis, the second term on the right-hand side of (6.1.6) also is essential. Suppose that each summand S k is a symmetric random variable; that is, S k and ϒ S k have the same distribution. In this case, an involved argument [, Prop. 6.10] leads to the bound There are examples where the right-hand side of (6.1.7) is comparable with the uniform upper bound L on the summands, but this is not always so.

<!-- chunk {"id": "body-0376", "role": "body", "section": "The Expectation Bound", "weight": 1.0} -->

In summary, when the summands S k are symmetric, we have matching estimates We see that the bound (6.1.6) must include some version of each term that appears, but the logarithms are not always necessary.

<!-- chunk {"id": "body-0377", "role": "body", "section": "Examples where the Logarithms Appear", "weight": 1.0} -->

First, let us show that the variance term in (6.1.6) must contain a logarithm. For each natural number n, consider the d ≤ d random matrix Z of the form where { % i k } is an independent family of Rademacher random variables. An easy application of the bound (6.1.6) implies that Using the central limit theorem and the Skorokhod representation, we can construct an independent family { k } of standard normal random variables for which But this fact ensures that Therefore, we cannot remove the logarithm from the variance term in (6.1.6).

<!-- chunk {"id": "body-0378", "role": "body", "section": "Examples where the Logarithms Appear", "weight": 1.0} -->

Next, let us justify the logarithm on the norm of the summands in (6.1.6). For each natural number n, consider a d ≤ d random matrix Z of the form where ' -(n) i k ' is an independent family of BERNOULLI(n ϒ 1) random variables. The matrix RosenthalPinelis inequality (6.1.6) ensures that Using the Poisson limit of a binomial random variable and the Skorohod representation, we can construct an independent family { Qk } of POISSON random variables for which In short, the bound we derived from (6.1.6) requires the logarithm on the second term, but it is suboptimal by a loglog factor. The upper matrix Chernoff inequality (5.1.6) correctly predicts the appearance of the iterated logarithm in this example, as does the matrix Bennett inequality.

<!-- chunk {"id": "body-0379", "role": "body", "section": "Examples where the Logarithms Appear", "weight": 1.0} -->

The last two examples rely heavily on the commutativity of the summands as well as the infinite divisibility of the normal and Poisson distributions. As a consequence, it may appear that the logarithms only appear in very special contexts. In fact, many (but not all!) examples that arise in practice do require the logarithms that appear in the matrix Bernstein inequality. It is a subject of ongoing research to obtain a simple criterion for deciding when the logarithms belong.

<!-- chunk {"id": "body-0380", "role": "body", "section": "Example: Matrix Approximation by Random Sampling", "weight": 1.0} -->

In applied mathematics, we often need to approximate a complicated target object by a more structured object. In some situations, we can solve this problem using a beautiful probabilistic approach called empirical approximation. The basic idea is to construct a 'simple' random object whose expectation equals the target. We obtain the approximation by averaging several independent copies of the simple random object. As the number of terms in this average increases, the approximation becomes more complex, but it represents the target more faithfully. The challenge is to quantify this tradeoff.

<!-- chunk {"id": "body-0381", "role": "body", "section": "Example: Matrix Approximation by Random Sampling", "weight": 1.0} -->

In particular, we often encounter problems where we need to approximate a matrix by a more structured matrix. For example, we may wish to find a sparse matrix that is close to a given matrix, or we may need to construct a low-rank matrix that is close to a given matrix. Empirical approximation provides a mechanism for obtaining these approximations. The matrix Bernstein inequality offers a natural tool for assessing the quality of the randomized approximation.

<!-- chunk {"id": "body-0382", "role": "body", "section": "Example: Matrix Approximation by Random Sampling", "weight": 1.0} -->

This section develops a general framework for empirical approximation of matrices. Subsequent sections explain how this technique applies to specific examples from the fields of randomized linear algebra and machine learning.

<!-- chunk {"id": "body-0383", "role": "body", "section": "Setup", "weight": 1.0} -->

Let B be a target matrix that we hope to approximate by a more structured matrix. To that end, let us represent the target as a sum of 'simple' matrices: The idea is to identify summands with desirable properties that we want our approximation to inherit. The examples in this chapter depend on decompositions of the form (6.2.1).

<!-- chunk {"id": "body-0384", "role": "body", "section": "Setup", "weight": 1.0} -->

Along with the decomposition (6.2.1), we need a set of sampling probabilities: We want to ascribe larger probabilities to 'more important' summands. Quantifying what 'important' means is the most difficult aspect of randomized matrix approximation. Choosing the right sampling distribution for a specific problem requires insight and ingenuity.

<!-- chunk {"id": "body-0385", "role": "body", "section": "Setup", "weight": 1.0} -->

Given the data (6.2.1) and (6.2.2), we may construct a 'simple' random matrix R by sampling: This construction ensures that R is an unbiased estimator of the target: E R ∅ B. Even so, the random matrix R offers a poor approximation of the target B because it has a lot more structure.

<!-- chunk {"id": "body-0386", "role": "body", "section": "Setup", "weight": 1.0} -->

To improve the quality of the approximation, we average n independent copies of the random matrix R. Weobtain an estimator of the form By linearity of expectation, this estimator is also unbiased: E ¯ R n ∅ B. The approximation ¯ R n remains structured when the number n of terms in the approximation is small as compared with the number N of terms in the decomposition (6.2.1).

<!-- chunk {"id": "body-0387", "role": "body", "section": "Setup", "weight": 1.0} -->

Our goal is to quantify the approximation error as a function of the complexity n of the approximation: There is a tension between the total number n of terms in the approximation and the error error(n) the approximation incurs. In applications, it is essential to achieve the right balance.

<!-- chunk {"id": "body-0388", "role": "body", "section": "Error Estimate for Matrix Sampling Estimators", "weight": 1.0} -->

We can obtain an error estimate for the approximation scheme described in Section 6.2.1 as an immediate corollary of the matrix Bernstein inequality, Theorem 6.1.1.

<!-- chunk {"id": "body-0389", "role": "body", "section": "Error Estimate for Matrix Sampling Estimators", "weight": 1.0} -->

Corollary 6.2.1 (Matrix Approximation by Random Sampling). Let B be a fixed d 1 ≤ d 2 matrix. Construct a d 1 ≤ d 2 random matrix R that satisfies Compute the per-sample second moment: Form the matrix sampling estimator Then the estimator satisfies Furthermore, for all t ÷ 0, Proof. Since R is an unbiased estimator of the target matrix B, we can write We have defined the summands S k ∅ n ϒ 1 (R k ϒ E R). These random matrices form an independent and identically distributed family, and each S k has mean zero.

<!-- chunk {"id": "body-0390", "role": "body", "section": "Error Estimate for Matrix Sampling Estimators", "weight": 1.0} -->

Now, each of the summands is subject to an upper bound: The first relation is the triangle inequality; the second is Jensen's inequality. The last estimate follows from our assumption that κ R κ · L.

<!-- chunk {"id": "body-0391", "role": "body", "section": "Error Estimate for Matrix Sampling Estimators", "weight": 1.0} -->

To control the matrix variance statistic v (Z), first note that The first identity follows from the expression (6.1.2) for the matrix variance statistic, and the second holds because the summands S k are identically distributed. We may calculate that Thefirst relation holds because the expectation of the random positive-semidefinite matrix S 1 S / 1 is positive semidefinite. The first identity follows from the definition of S 1 and the fact that R 1 has the same distribution as R. The second identity is a direct calculation. The last relation holds because (E R)(E R) / is positive semidefinite. As a consequence, The last line follows from the definition (6.2.4) of m 2(R).

<!-- chunk {"id": "body-0392", "role": "body", "section": "Error Estimate for Matrix Sampling Estimators", "weight": 1.0} -->

Weare prepared to apply the matrix Bernstein inequality, Theorem 6.1.1, to the random matrix Z ∅ P k S k. This operation results in the statement of the corollary.

<!-- chunk {"id": "body-0393", "role": "body", "section": "Discussion", "weight": 1.5} -->

One of the most common applications of the matrix Bernstein inequality is to analyze empirical matrix approximations. As a consequence, Corollary 6.2.1 is one of the most useful forms of the matrix Bernstein inequality. Let us discuss some of the important aspects of this result.

<!-- chunk {"id": "body-0394", "role": "body", "section": "Understanding the Bound on the Approximation Error", "weight": 1.0} -->

First, let us examine how many samples n suffice to bring the approximation error bound in Corollary 6.2.1 below a specified positive tolerance ". Examining inequality (7.3.5), we find that In summary, Roughly, the number n of samples should be on the scale of the per-sample second moment m 2(R) and the uniform upper bound L.

<!-- chunk {"id": "body-0395", "role": "body", "section": "Understanding the Bound on the Approximation Error", "weight": 1.0} -->

The bound (6.2.7) also reveals an unfortunate aspect of empirical matrix approximation. To make the tolerance " small, the number n of samples must increase proportional with " ϒ 2. In other words, it takes many samples to achieve a highly accurate approximation. We cannot avoid this phenomenon, which ultimately is a consequence of the central limit theorem.

<!-- chunk {"id": "body-0396", "role": "body", "section": "Understanding the Bound on the Approximation Error", "weight": 1.0} -->

On a more positive note, it is quite valuable that the error bounds (7.3.5) and (7.3.6) involve the spectral norm. This type of estimate simultaneously controls the error in every linear function of the approximation: The Schatten 1-norm κ′κ S 1 is defined in (2.1.29). These bounds also control the error in each singular value j (¯ R n) of the approximation: Whenthere is a gap between two singular values of B, we can also obtain bounds for the discrepancy between the associated singular vectors of ¯ R n and B using perturbation theory.

<!-- chunk {"id": "body-0397", "role": "body", "section": "Understanding the Bound on the Approximation Error", "weight": 1.0} -->

To construct a good sampling estimator R, we ought to control both m 2( R ) and L. In practice, this demands considerable creativity. This observation hints at the possibility of achieving a bias-variance tradeoff when approximating B. To do so, we can drop all of the 'unimportant' terms in the representation (6.2.1), i.e., those whose sampling probabilities are small. Then we construct a random approximation R only for the 'important' terms that remain. Properly executed, this process may decrease both the per-sample second moment m 2( R ) and the upper bound L. The idea is analogous with shrinkage in statistical estimation.

<!-- chunk {"id": "body-0398", "role": "body", "section": "AGeneral Sampling Model", "weight": 1.0} -->

Corollary 6.2.1 extends beyond the sampling model based on the finite expansion (6.2.1). Indeed, we can consider a more general decomposition of the target matrix B: where ' is a probability measure on a sample space ›. As before, the idea is to represent the target matrix B as an average of 'simple' matrices B (!). The main difference is that the family of simple matrices may now be infinite. In this setting, we construct the random approximation R so that In particular, it follows that As we will discuss, this abstraction is important for applications in machine learning.

<!-- chunk {"id": "body-0399", "role": "body", "section": "Suboptimality of Sampling Estimators", "weight": 1.0} -->

Another fundamental point about sampling estimators is that they are usually suboptimal. In other words, the matrix sampling estimator may incur an error substantially worse than the error in the best structured approximation of the target matrix.

<!-- chunk {"id": "body-0400", "role": "body", "section": "Suboptimality of Sampling Estimators", "weight": 1.0} -->

To see why, let us consider a simple form of low-rank approximation by random sampling. The method here does not have practical value, but it highlights the reason that sampling estimators usually do not achieve ideal results. Suppose that B has singular value decomposition Given the SVD, we can construct a random rank-one approximation R of the form Per Corollary 6.2.1, the error in the associated sampling estimator ¯ R n of B satisfies On the other hand, a best rankn approximation of B takes the form B n ∅ P n j ∅ 1 j u j v / j, and it incurs error The second relation is Markov's inequality, which provides an accurate estimate only when the singular values 1,..., n ⊕ 1 are comparable. In that case, the sampling estimator arrives within a logarithmic factor of the optimal error. But there are many matrices whose singular values decay quickly, so that n ⊕ 1 ↵ (n ⊕ 1) ϒ 1. In the latter situation, the error in the sampling estimator is much worse than the optimal error.

<!-- chunk {"id": "body-0401", "role": "body", "section": "Warning: Frobenius-Norm Bounds", "weight": 1.0} -->

We often encounter papers that develop Frobenius-norm error bounds for matrix approximations, perhaps because the analysis is more elementary.

<!-- chunk {"id": "body-0402", "role": "body", "section": "Frobenius-norm error bounds are typically vacuous", "weight": 1.0} -->

In particular, this phenomenon occurs in data analysis whenever we try to approximate a matrix that contains white or pink noise.

<!-- chunk {"id": "body-0403", "role": "body", "section": "Frobenius-norm error bounds are typically vacuous", "weight": 1.0} -->

To illustrate this point, let us consider the ubiquitous problem of approximating a low-rank matrix corrupted by additive white Gaussian noise: The desired approximation of the matrix B is the rank-one matrix B opt ∅ xx /. For modeling purposes, we assume that E has independent NORMAL(0, d ϒ 1) entries. As a consequence, Now, the spectral-norm error in the desired approximation satisfies Onthe other hand, the Frobenius-norm error in the desired approximation satisfies We see that the Frobenius-norm error can be quite large, even when we find the required approximation.

<!-- chunk {"id": "body-0404", "role": "body", "section": "Frobenius-norm error bounds are typically vacuous", "weight": 1.0} -->

Here is another way to look at the same fact. Suppose we construct an approximation b B of the matrix B from (6.2.8) whose Frobenius-norm error is comparable with the optimal error: There is no reason for the approximation b B to have any relationship with the desired approximation B opt. For example, the approximation b B ∅ fi E satisfies this error bound with " ∅ d ϒ 1/2 even though b B consists only of noise.

<!-- chunk {"id": "body-0405", "role": "body", "section": "Application: Randomized Sparsification of a Matrix", "weight": 1.0} -->

Many tasks in data analysis involve large, dense matrices that contain a lot of redundant information. For example, an experiment that tabulates many variables about a large number of subjects typically results in a low-rank data matrix because subjects are often similar with each other. Many questions that we pose about these data matrices can be addressed by spectral computations. In particular, factor analysis involves a singular value decomposition.

<!-- chunk {"id": "body-0406", "role": "body", "section": "Application: Randomized Sparsification of a Matrix", "weight": 1.0} -->

When the data matrix is approximately low rank, it has fewer degrees of freedom than its ambient dimension. Therefore, we can construct a simpler approximation that still captures most of the information in the matrix. One method for finding this approximation is to replace the dense target matrix by a sparse matrix that is close in spectral-norm distance. An elegant wayto identify this sparse proxy is to randomly select a small number of entries from the original matrix to retain. This is a type of empirical approximation.

<!-- chunk {"id": "body-0407", "role": "body", "section": "Application: Randomized Sparsification of a Matrix", "weight": 1.0} -->

Sparsification has several potential advantages. First, it is considerably less expensive to store a sparse matrix than a dense matrix. Second, many algorithms for spectral computation operate more efficiently on sparse matrices.

<!-- chunk {"id": "body-0408", "role": "body", "section": "Application: Randomized Sparsification of a Matrix", "weight": 1.0} -->

In this section, we examine a very recent approach to randomized sparsification due to Kundu &Drineas. The analysis is an immediate consequence of Corollary 6.2.1. See the notes at the end of the chapter for history and references.

<!-- chunk {"id": "body-0409", "role": "body", "section": "Problem Formulation & Randomized Algorithm", "weight": 1.0} -->

Let B be a fixed d 1 ≤ d 2 complex matrix. The sparsification problem requires us to find a sparse matrix b B that has small distance from B with respect to the spectral norm. We can achieve this goal using an empirical approximation strategy.

<!-- chunk {"id": "body-0410", "role": "body", "section": "Problem Formulation & Randomized Algorithm", "weight": 1.0} -->

First, let us express the target matrix as a sum of its entries: Introduce sampling probabilities The Frobenius norm is defined in (2.1.2), and the entrywise ' 1 norm is defined in (2.1.30). It is easy to check that the numbers pi j form a probability distribution. Let us emphasize that the non-obvious form of the distribution (6.3.1) represents a decade of research.

<!-- chunk {"id": "body-0411", "role": "body", "section": "Problem Formulation & Randomized Algorithm", "weight": 1.0} -->

Now, we introduce a d 1 ≤ d 2 random matrix R that has exactly one nonzero entry: We use the convention that 0/0 ∅ 0 so that we do not need to treat zero entries separately. It is immediate that Therefore, R is an unbiased estimate of B.

<!-- chunk {"id": "body-0412", "role": "body", "section": "Problem Formulation & Randomized Algorithm", "weight": 1.0} -->

Although the expectation of R is correct, its variance is quite high. Indeed, R has only one nonzero entry, while B typically has many nonzero entries. To reduce the variance, we combine several independent copies of the simple estimator: By linearity of expectation, E ¯ R n ∅ B. Therefore, the matrix ¯ R n has at most n nonzero entries, and its also provides an unbiased estimate of the target. The challenge is to quantify the error κ ¯ R n ϒ B κ as a function of the sparsity level n.

<!-- chunk {"id": "body-0413", "role": "body", "section": "Performance of Randomized Sparsification", "weight": 1.0} -->

The randomized sparsification method is clearly a type of empirical approximation, so we can use Corollary 6.2.1 to perform the analysis. We will establish the following error bound.

<!-- chunk {"id": "body-0414", "role": "body", "section": "Performance of Randomized Sparsification", "weight": 1.0} -->

The short proof of (6.3.2) appears below in Section 6.3.3.

<!-- chunk {"id": "body-0415", "role": "body", "section": "Performance of Randomized Sparsification", "weight": 1.0} -->

Let us explain the content of the estimate (6.3.2). First, the bound (2.1.31) allows us to replace the ' 1 norm by the Frobenius norm: Placing the error (6.3.2) on a relative scale, we see that The stable rank srank(B), defined in (2.1.25), emerges naturally as a quantity of interest.

<!-- chunk {"id": "body-0416", "role": "body", "section": "Performance of Randomized Sparsification", "weight": 1.0} -->

Now, suppose that the sparsity level n satisfies where the tolerance " 2 (0,1]. We determine that Since the stable rank always exceeds one and we have assumed that " · 1, this estimate implies that Wediscover that it is possible to replace the matrix B by a matrix with at most n nonzero entries while achieving a small relative error in the spectral norm. When srank(B) ↵ min{ d 1, d 2}, we can achieve a dramatic reduction in the number of nonzero entries needed to carry the spectral information in the matrix B.

<!-- chunk {"id": "body-0417", "role": "body", "section": "Analysis of Randomized Sparsification", "weight": 1.0} -->

Let us proceed with the analysis of randomized sparsification. To apply Corollary 6.2.1, we need to obtain bounds for the per-sample variance m 2(R) and the uniform upper bound L. The key to both calculations is to obtain appropriate lower bounds on the sampling probabilities pi j. Indeed, Each estimate follows by neglecting one term in (6.3.3).

<!-- chunk {"id": "body-0418", "role": "body", "section": "Analysis of Randomized Sparsification", "weight": 1.0} -->

First, we turn to the uniform bound on the random matrix R. Wehave The last inequality depends on the first bound in (6.3.3). Therefore, we may take L ∅ 2 κ B κ ' 1. Second, we turn to the computation of the per-sample second moment m 2(R). We have The semidefinite inequality holds because each matrix ϕ bi j ϕ 2 E i i is positive semidefinite and because of the second bound in (6.3.3). Similarly, This is the required estimate for the per-sample second moment.

<!-- chunk {"id": "body-0419", "role": "body", "section": "Analysis of Randomized Sparsification", "weight": 1.0} -->

Finally, to reach the advertised error bound (6.3.2), we invoke Corollary 6.2.1 with the parameters L ∅κ B κ ' 1 and m 2( R ) · 2max{ d 1, d 2}.

<!-- chunk {"id": "body-0420", "role": "body", "section": "Application: Randomized Matrix Multiplication", "weight": 1.0} -->

Numerical linear algebra (NLA) is a well-established and important part of computer science. Some of the basic problems in this area include multiplying matrices, solving linear systems, computing eigenvalues and eigenvectors, and solving linear least-squares problems. Historically, the NLA community has focused on developing highly accurate deterministic methods that require as few floating-point operations as possible. Unfortunately, contemporary applications can strain standard NLA methods because problems have continued to become larger. Furthermore, on modern computer architectures, computational costs depend heavily on communication and other resources that the standard algorithms do not manage very well.

<!-- chunk {"id": "body-0421", "role": "body", "section": "Application: Randomized Matrix Multiplication", "weight": 1.0} -->

In response to these challenges, researchers have started to develop randomized algorithms for core problems in NLA. In contrast to the classical algorithms, these new methods make random choices during execution to achieve computational efficiencies. These randomized algorithms can also be useful for large problems or for modern computer architectures. On the other hand, randomized methods can fail with some probability, and in some cases they are less accurate than their classical competitors.

<!-- chunk {"id": "body-0422", "role": "body", "section": "Application: Randomized Matrix Multiplication", "weight": 1.0} -->

Matrix concentration inequalities are one of the key tools used to design and analyze randomized algorithms for NLA problems. In this section, we will describe a randomized method for matrix multiplication developed by Magen & Zouzias. We will analyze this algorithm using Corollary 6.2.1. Turn to the notes at the end of the chapter for more information about the history.

<!-- chunk {"id": "body-0423", "role": "body", "section": "Problem Formulation & Randomized Algorithm", "weight": 1.0} -->

One of the basic tasks in numerical linear algebra is to multiply two matrices with compatible dimensions. Suppose that B is a d 1 ≤ N complex matrix and that C is an N ≤ d 2 complex matrix, andwewishtocomputetheproduct BC. Thestraightforward algorithm forms the product entry by entry: This approach takes O(N ′ d 1 d 2) arithmetic operations. There are algorithms, such as Strassen's divide-and-conquer method, that can reduce the cost, but these approaches are not considered practical for most applications.

<!-- chunk {"id": "body-0424", "role": "body", "section": "Problem Formulation & Randomized Algorithm", "weight": 1.0} -->

Suppose that the inner dimension N is substantially larger than the outer dimensions d 1 and d 2. In this setting, both matrices B and C are rank-deficient, so the columns of B contain a lot of linear dependencies, as do the rows of C. As a consequence, a random sample of columns from B (or rows from C) can be used as a proxy for the full matrix. Formally, the key to this approach is to view the matrix product as a sum of outer products: Asusual, b: j denotes the j th column of B, while c j: denotes the j th row of C. We can approximate this sum using the empirical method.

<!-- chunk {"id": "body-0425", "role": "body", "section": "Problem Formulation & Randomized Algorithm", "weight": 1.0} -->

To develop an algorithm, the first step is to construct a simple random matrix R that provides an unbiased estimate for the matrix product. To that end, we pick a random index and form a rank-one matrix from the associated columns of B and row of C. More precisely, define The Frobenius norm is defined in (2.1.2). Using the properties of the norms, we can easily check that (p 1, p 2, p 3,..., pN) forms a bonafide probability distribution. The cost of computing these probabilities is at most O (N ′ (d 1 ⊕ d 2)) arithmetic operations, which is much smaller than the cost of forming the product BC when d 1 and d 2 are large.

<!-- chunk {"id": "body-0426", "role": "body", "section": "Problem Formulation & Randomized Algorithm", "weight": 1.0} -->

Wenowdefine a d 1 ≤ d 2 random matrix R by the expression Weuse the convention that 0/0 ∅ 0 so we do not have to treat zero rows and columns separately. It is straightforward to compute the expectation of R: As required, R is an unbiased estimator for the product BC.

<!-- chunk {"id": "body-0427", "role": "body", "section": "Problem Formulation & Randomized Algorithm", "weight": 1.0} -->

Although the expectation of R is correct, its variance is quite high. Indeed, R has rank one, while the rank of BC is usually larger! To reduce the variance, we combine several independent copies of the simple estimator: By linearity of expectation, E ¯ R n ∅ BC, so we imagine that ¯ R n approximates the product well.

<!-- chunk {"id": "body-0428", "role": "body", "section": "Problem Formulation & Randomized Algorithm", "weight": 1.0} -->

To see whether this heuristic holds true, we need to understand how the error E κ ¯ R n ϒ BC κ depends on the number n of samples. It costs O ( n ′ d 1 d 2) floating-point operations to determine all the entries of ¯ R n. Therefore, when the number n of samples is much smaller than the inner dimension N of the matrices, we can achieve significant economies over the naïve matrix multiplication algorithm.

<!-- chunk {"id": "body-0429", "role": "body", "section": "Problem Formulation & Randomized Algorithm", "weight": 1.0} -->

In fact, it requires no computation beyond sampling the row/column indices to express ¯ R n in the form (6.4.4). This approach gives an inexpensive way to represent the product approximately.

<!-- chunk {"id": "body-0430", "role": "body", "section": "Performance of Randomized Matrix Multiplication", "weight": 1.0} -->

To simplify our presentation, we will assume that both matrices have been scaled so that their spectral norms are equal to one: It is relatively inexpensive to compute the spectral norm of a matrix accurately, so this preprocessing step is reasonable.

<!-- chunk {"id": "body-0431", "role": "body", "section": "Performance of Randomized Matrix Multiplication", "weight": 1.0} -->

Let asr ∅ 1 2 (srank(B) ⊕ srank(C)) be the average stable rank of the two factors; see (2.1.25) for the definition of the stable rank. In §6.4.3, we will prove that To appreciate what this estimate means, suppose that the number n of samples satisfies where " is a positive tolerance. Then we obtain a relative error bound for the randomized matrix multiplication method This expression depends on the normalization of B and C. The computational cost of forming the approximation is In other words, when the average stable rank asr is substantially smaller than the inner dimension N of the two matrices B and C, the random estimate ¯ R n for the product BC achieves a small error relative to the scale of the factors.

<!-- chunk {"id": "body-0432", "role": "body", "section": "Analysis of Randomized Matrix Multiplication", "weight": 1.0} -->

The randomized matrix multiplication method is just a specific example of empirical approximation, and the error bound (6.4.5) is an immediate consequence of Corollary 6.2.1.

<!-- chunk {"id": "body-0433", "role": "body", "section": "Analysis of Randomized Matrix Multiplication", "weight": 1.0} -->

To pursue this approach, we need to establish a uniform bound on the norm of the estimator R for the product. Observe that To obtain a bound, recall the value (6.4.3) of the probability pj, and invoke the inequality between geometric and arithmetic means: Since the matrices B and C have unit spectral norm, we can express this inequality in terms of the average stable rank: This is the exactly kind of bound that we need.

<!-- chunk {"id": "body-0434", "role": "body", "section": "Analysis of Randomized Matrix Multiplication", "weight": 1.0} -->

Next, we need an estimate for the per-sample second moment m 2(R). By direct calculation, The semidefinite relation holds because each fraction lies between zero and one, and each matrix b: j b /: j is positive semidefinite. Therefore, increasing the fraction to one only increases in the matrix in the semidefinite order. Similarly, The penultimate line depends on the identity (2.1.24) and our assumption that both matrices B and C have norm one.

<!-- chunk {"id": "body-0435", "role": "body", "section": "Analysis of Randomized Matrix Multiplication", "weight": 1.0} -->

Finally, to reach the stated estimate (6.4.5), we apply Corollary 6.2.1 with the parameters L ∅ asr and m 2( R ) · 2 ′ asr.

<!-- chunk {"id": "body-0436", "role": "body", "section": "Application: Random Features", "weight": 1.0} -->

As a final application of empirical matrix approximation, let us discuss a contemporary idea from machine learning called random features. Although this technique may appear more sophisticated than randomized sparsification or randomized matrix multiplication, it depends on exactly the same principles. Random feature maps were proposed by Ali Rahimi and Ben Recht. The analysis in this section is due to David Lopez-Paz et al. [LPSS ⊕ 14].

<!-- chunk {"id": "body-0437", "role": "body", "section": "Kernel Matrices", "weight": 1.0} -->

Let X be a set. We think about the elements of the set X as (potential) observations that we would like to use to perform learning and inference tasks. Let us introduce a bounded measure ' of similarity between pairs of points in the set: The similarity measure ' is often called a kernel. Weassume that the kernel returns the value ⊕ 1 whenits arguments are identical, and it returns smaller values when its arguments are dissimilar. Wealso assume that the kernel is symmetric; that is, ' (x, y) ∅ ' (y, x) for all arguments x, y 2 X.

<!-- chunk {"id": "body-0438", "role": "body", "section": "Kernel Matrices", "weight": 1.0} -->

In summary, A simple example of a kernel is the angular similarity between a pair of points in a Euclidean space: We write ∡ (′, ′) for the planar angle between two vectors, measured in radians. As usual, we instate the convention that 0/0 ∅ 0. See Figure 6.1 for an illustration.

<!-- chunk {"id": "body-0439", "role": "body", "section": "Kernel Matrices", "weight": 1.0} -->

Supposethat x 1,..., x N 2 X are observations. The kernel matrix G ∅ [gi j] 2 M N just tabulates the values of the kernel function for each pair of data points: It may be helpful to think about the kernel matrix G as a generalization of the Gram matrix of a family of points in a Euclidean space. We say that the kernel ' is positive definite if the kernel matrix G is positive semidefinite for any choice of observations { x i }  X. We will be concerned only with positive-definite kernels in this discussion.

<!-- chunk {"id": "body-0440", "role": "body", "section": "Kernel Matrices", "weight": 1.0} -->

In the Euclidean setting, there are statistical learning methods that only require the inner product between each pair of observations. These algorithms can be extended to the kernel setting by replacing each inner product with a kernel evaluation. As a consequence, kernel matrices can be used for classification, regression, and feature selection. In these applications, kernels are advantageous because they work outside the Euclidean domain, and they allow task-specific measures of similarity. This idea, sometimes called the kernel trick, is one of the major insights in modern machine learning.

<!-- chunk {"id": "body-0441", "role": "body", "section": "Kernel Matrices", "weight": 1.0} -->

A significant challenge for algorithms based on kernels is that the kernel matrix is big. Indeed, G contains O ( N 2 ) entries, where N is the number of data points. Furthermore, the cost of constructing the kernel matrix is O ( dN 2 ) where d is the number of parameters required to specify a point in the universe X.

<!-- chunk {"id": "body-0442", "role": "body", "section": "Kernel Matrices", "weight": 1.0} -->

Nevertheless, there is an opportunity. Large data sets tend to be redundant, so the kernel matrix also tends to be redundant. This manifests in the kernel matrix being close to a low-rank matrix. As a consequence, we may try to replace the kernel matrix by a low-rank proxy. For some similarity measures, we can accomplish this task using empirical approximation.

<!-- chunk {"id": "body-0443", "role": "body", "section": "RandomFeatures and Low-Rank Approximation of the Kernel Matrix", "weight": 1.0} -->

In certain cases, a positive-definite kernel can be written as an expectation, and we can take advantage of this representation to construct an empirical approximation of the kernel matrix. Let us begin with the general construction, and then we will present a few examples in Section 6.5.3.

<!-- chunk {"id": "body-0444", "role": "body", "section": "RandomFeatures and Low-Rank Approximation of the Kernel Matrix", "weight": 1.0} -->

Let W be a sample space equipped with a sigma-algebra and a probability measure '. Introduce a bounded feature map: Consider a random variable w taking values in W and distributed according to the measure '. Weassume that this random variable satisfies the reproducing property The pair (ˆ, w) is called a random feature map for the kernel '.

<!-- chunk {"id": "body-0445", "role": "body", "section": "RandomFeatures and Low-Rank Approximation of the Kernel Matrix", "weight": 1.0} -->

We want to approximate the kernel matrix with a set { x 1,..., x N }  X of observations. To do so, we draw a random vector w 2 W distributed according to '. Form a random vector z 2 R N by applying the feature map to each data point with the same choice of the random vector w. That is, The vector z is sometimes called a random feature. By the reproducing property (6.5.2) for the random feature map, Wecan write this relation in matrix form as G ∅ E (zz /). Therefore, the random matrix R ∅ zz / is an unbiased rank-one estimator for the kernel matrix G. This representation demonstrates that random feature maps, as defined here, only exist for positive-definite kernels.

<!-- chunk {"id": "body-0446", "role": "body", "section": "RandomFeatures and Low-Rank Approximation of the Kernel Matrix", "weight": 1.0} -->

As usual, we construct a better empirical approximation of the kernel matrix G by averaging several realizations of the simple estimator R: In other words, we are using n independent random features z 1,..., z n to approximate the kernel matrix. The question is how many random features are needed before our estimator is accurate.

<!-- chunk {"id": "body-0447", "role": "body", "section": "Examples of Random Feature Maps", "weight": 1.0} -->

Before we continue with the analysis, let us describe some random feature maps. This discussion is tangential to our theme of matrix concentration, but it is valuable to understand why random feature maps exist.

<!-- chunk {"id": "body-0448", "role": "body", "section": "Examples of Random Feature Maps", "weight": 1.0} -->

First, let us consider the angular similarity (6.5.1) defined on R d. Wecan construct a random feature map using a classical result from plane geometry. If we draw w uniformly from the unit sphere S d ϒ 1  R d, then The easy proof of this relation should be visible from the diagram in Figure 6.1. In light of the formula (6.5.4), we set W ∅ S d ϒ 1 with the uniform measure, and we define the feature map The reproducing property (6.5.2) follows immediately from (6.5.4). Therefore, the pair (ˆ, w) is a random feature map for the angular similarity kernel.

<!-- chunk {"id": "body-0449", "role": "body", "section": "Examples of Random Feature Maps", "weight": 1.0} -->

Next, let us describe an important class of kernels that can be expressed using random feature maps. A kernel on R d is translation invariant if there is a function ': R d ! R for which Figure 6.1: The angular similarity between two vectors. Let x and y be nonzero vectors in R 2 with angle ∡ (x, y). The red region contains the directions u where the product sgn η x, u ι ′ sgn η y, u ι equals ⊕ 1, and the blue region contains the directions u where the same product equals ϒ 1. The blue region subtends a total angle of 2 ∡ (x, y), and the red region subtends a total angle of 2 … ϒ 2 ∡ (x, y).

<!-- chunk {"id": "body-0450", "role": "body", "section": "Examples of Random Feature Maps", "weight": 1.0} -->

Bôchner's Theorem, a classical result from harmonic analysis, gives a representation for each continuous, positive-definite, translation-invariant kernel: In this expression, the positive scale factor c and the probability measure ' depend only on the function '. The formula (6.5.5) yields a (complex-valued) random feature map: This map satisfies a complex variant of the reproducing property (6.5.2): where we have written / for complex conjugation.

<!-- chunk {"id": "body-0451", "role": "body", "section": "Examples of Random Feature Maps", "weight": 1.0} -->

With a little more work, we can construct a real-valued random feature map. Recall that the kernel ' is symmetric, so the complex exponentials in (6.5.5) can be written in terms of cosines. This observation leads to the random feature map To verify that (ˆ, (w, U)) reproduces the kernel ', as required by (6.5.2), we just make a short calculation using the angle-sum formula for the cosine.

<!-- chunk {"id": "body-0452", "role": "body", "section": "Examples of Random Feature Maps", "weight": 1.0} -->

We conclude this section with the most important example of a random feature map from the class we have just described. Consider the Gaussian radial basis function kernel: The positive parameter fi reflects how close two points must be before they are regarded as 'similar.' For the Gaussian kernel, Bôchner's Theorem (6.5.5) holds with the scaling factor c ∅ 1 and the probability measure ' ∅ NORMAL(0, fi I d). In summary, we define This random feature map reproduces the Gaussian radial basis function kernel.

<!-- chunk {"id": "body-0453", "role": "body", "section": "Performance of the Random Feature Approximation", "weight": 1.0} -->

We will demonstrate that the approximation ¯ R n of the N ≤ N kernel matrix G using n random features, constructed in (6.5.3), leads to an estimate of the form In this expression, b is the uniform bound on the magnitude of the feature map ˆ. The short proof of (6.5.7) appears in §6.5.5.

<!-- chunk {"id": "body-0454", "role": "body", "section": "Performance of the Random Feature Approximation", "weight": 1.0} -->

To clarify what this result means, we introduce the intrinsic dimension of the N ≤ N kernel matrix G: The stable rank is defined in Section 2.1.15. We have used the assumption that the similarity measure is positive definite to justify the computation of the square root of the kernel matrix, and tr G ∅ N because of the requirement that ' (x, x) ∅ ⊕ 1 for all x 2 X. See §7.1 for further discussion of the intrinsic dimension Now, assume that the number n of random features satisfies the bound In view of (6.5.7), the relative error in the empirical approximation of the kernel matrix satisfies Welearn that the randomized approximation of the kernel matrix G is accurate when its intrinsic dimension is much smaller than the number of data points. That is, intdim(G) ↵ N.

<!-- chunk {"id": "body-0455", "role": "body", "section": "Analysis of the Random Feature Approximation", "weight": 1.0} -->

The analysis of random features is based on Corollary 6.2.1. To apply this result, we need the per-sample second-moment m 2( R ) and the uniform upper bound L. Both are easy to come.

<!-- chunk {"id": "body-0456", "role": "body", "section": "Analysis of the Random Feature Approximation", "weight": 1.0} -->

First, observe that Recall that b is the uniform bound on the feature map ˆ, and N is the number of components in the random feature vector z.

<!-- chunk {"id": "body-0457", "role": "body", "section": "Analysis of the Random Feature Approximation", "weight": 1.0} -->

Second, we calculate that Each random matrix zz / is positive semidefinite, so we can introduce the upper bound κ z κ 2 · bN. The last identity holds because R is an unbiased estimator of the kernel matrix G. It follows that This is our bound for the per-sample second moment.

<!-- chunk {"id": "body-0458", "role": "body", "section": "Analysis of the Random Feature Approximation", "weight": 1.0} -->

Finally, we invoke Corollary 6.2.1 with parameters L ∅ bN and m 2( R ) · bN κ G κ to arrive at the estimate (6.5.7).

<!-- chunk {"id": "body-0459", "role": "body", "section": "ASumofBoundedRandomHermitianMatrices", "weight": 1.0} -->

The first result is a Bernstein inequality for a sum of independent, random Hermitian matrices whose eigenvalues are bounded above.

<!-- chunk {"id": "body-0460", "role": "body", "section": "ASumofBoundedRandomHermitianMatrices", "weight": 1.0} -->

Theorem 6.6.1 (Matrix Bernstein: Hermitian Case). Consider a finite sequence { X k } of independent, random, Hermitian matrices with dimension d. Assume that Introduce the random matrix Furthermore, for all t ÷ 0.

<!-- chunk {"id": "body-0461", "role": "body", "section": "ASumofBoundedRandomHermitianMatrices", "weight": 1.0} -->

Let v (Y) be the matrix variance statistic of the sum: The proof of Theorem 6.6.1 appears below in §6.6.

<!-- chunk {"id": "body-0462", "role": "body", "section": "Discussion", "weight": 1.5} -->

Theorem 6.6.1 also yields information about the minimum eigenvalue of an independent sum of d -dimensional Hermitian matrices. Suppose that the independent random matrices satisfy Applying the expectation bound (6.6.2) to ϒ Y, we obtain Wecan use (6.6.3) to develop a tail bound. For t ÷ 0, Let us emphasize that the bounds, max(Y) and, min(Y) may diverge because the two parameters L and L can take sharply different values. This fact indicates that the maximum eigenvalue bound in Theorem 6.6.1 is a less strict assumption than the spectral norm bound in Theorem 6.1.1.

<!-- chunk {"id": "body-0463", "role": "body", "section": "Bounds for the Matrix Mgf and Cgf", "weight": 1.0} -->

In establishing the matrix Bernstein inequality, the main challenge is to obtain an appropriate bound for the matrix mgf and cgf of a zero-mean random matrix whose norm satisfies a uniform bound. We do not present the sharpest estimate possible, but rather the one that leads most directly to the useful results stated in Theorem 6.6.1.

<!-- chunk {"id": "body-0464", "role": "body", "section": "Bounds for the Matrix Mgf and Cgf", "weight": 1.0} -->

Lemma 6.6.2 (Matrix Bernstein: Mgf and Cgf Bound). Suppose that X is a random Hermitian matrix that satisfies Proof. Fix the parameter ∪ 0. In the exponential e X, we would like to expose the random matrix X and its square X 2 so that we can exploit information about the mean and variance. To that end, we write where f is a function on the real line: The function f is increasing because its derivative is positive. Therefore, f (x) · f (L) when x · L. By assumption, the eigenvalues of X do not exceed L, so the Transfer Rule (2.1.14) implies that TheConjugationRule(2.1.12) allows us to introduce the relation (6.6.6) into our expansion (6.6.5) of the matrix exponential: This relation is the basis for our matrix mgf bound.

<!-- chunk {"id": "body-0465", "role": "body", "section": "Bounds for the Matrix Mgf and Cgf", "weight": 1.0} -->

To obtain the desired result, we develop a further estimate for f (L). This argument involves a clever application of Taylor series: The second expression is simply the Taylor expansion of the fraction, viewed as a function of. We obtain the inequality by factoring out (L) 2 /2 from each term in the series and invoking the bound q ! ÷ 2 ′ 3 q ϒ 2, valid for each q ∅ 2,3,4,.... Sum the geometric series to obtain the final identity.

<!-- chunk {"id": "body-0466", "role": "body", "section": "Bounds for the Matrix Mgf and Cgf", "weight": 1.0} -->

To complete the proof of the mgf bound, we combine the last two displays: This estimate is valid because X 2 is positive semidefinite. Expectation preserves the semidefinite order, so We have used the assumption that X has zero mean. The second semidefinite relation follows when we apply the Transfer Rule (2.1.14) to the inequality 1 ⊕ a · e a, which holds for a 2 R.

<!-- chunk {"id": "body-0467", "role": "body", "section": "Bounds for the Matrix Mgf and Cgf", "weight": 1.0} -->

To obtain the semidefinite bound for the cgf, we extract the logarithm of the mgf bound using the fact (2.1.18) that the logarithm is operator monotone.

<!-- chunk {"id": "body-0468", "role": "body", "section": "Notes", "weight": 1.0} -->

The literature contains a wide variety of Bernstein-type inequalities in the scalar case, and the matrix case is no different. The applications of the matrix Bernstein inequality are also numerous. We only give a brief summary here.

<!-- chunk {"id": "body-0469", "role": "body", "section": "Matrix Bernstein Inequalities", "weight": 1.0} -->

David Gross and Ben Recht used the approach of Ahlswede & Winter to develop two different versions of the matrix Bernstein inequality. These papers helped to popularize the use matrix concentration inequalities in mathematical signal processing and statistics. Nevertheless, their results involve a suboptimal variance parameter of the form This parameter can be significantly larger than the matrix variance statistic (6.6.1) that appears in Theorem 6.6.1. They do coincide in some special cases, such as when the summands are independent and identically distributed.

<!-- chunk {"id": "body-0470", "role": "body", "section": "Matrix Bernstein Inequalities", "weight": 1.0} -->

Oliveira established the first version of the matrix Bernstein inequality that yields the correct matrix variance statistic (6.6.1). He accomplished this task with an elegant application of the Golden-Thompson inequality (3.3.3). His method even gives a result, called the matrix Freedman inequality, that holds for matrix-valued martingales. His bound is roughly equivalent with Theorem 6.6.1, up to the precise value of the constants.

<!-- chunk {"id": "body-0471", "role": "body", "section": "Matrix Bernstein Inequalities", "weight": 1.0} -->

The matrix Bernstein inequality we have stated here, Theorem 6.6.1, first appeared in the paper [, §6] by the author of these notes. The bounds for the expectation are new. The argument is based on Lieb's Theorem, and it also delivers a matrix Bennett inequality. This paper also describes how to establish matrix Bernstein inequalities for sums of unbounded random matrices, given some control over the matrix moments.

<!-- chunk {"id": "body-0472", "role": "body", "section": "Matrix Bernstein Inequalities", "weight": 1.0} -->

The research is independent from Oliveira's work, although Oliveira's paper motivated the subsequent article and the technical report, which explain how to use Lieb's Theorem to study matrix martingales. The technical report develops a Bernstein inequality for interior eigenvalues using the Lieb-Seiringer Theorem.

<!-- chunk {"id": "body-0473", "role": "body", "section": "Matrix Bernstein Inequalities", "weight": 1.0} -->

For more versions of the matrix Bernstein inequality, see Vladimir Koltchinskii's lecture notes from Saint-Flour. In Chapter 7, we present another extension of the matrix Bernstein inequality that involves a smaller dimensional parameter.

<!-- chunk {"id": "body-0474", "role": "body", "section": "The Matrix Rosenthal-Pinelis Inequality", "weight": 1.0} -->

The matrix Rosenthal-Pinelis inequality (6.1.6) is a close cousin of the matrix Rosenthal inequality (5.1.9). Both results are derived from the noncommutative Khintchine inequality (4.7.1) using the same pattern of argument [, Thm. A.1]. We believe that is the first paper to recognize and state the result (6.1.6), even though it is similar in spirit with the work. A self-contained, elementary proof of a related matrix Rosenthal-Pinelis inequality appears in [MJC ⊕ 14, Cor. 7.4].

<!-- chunk {"id": "body-0475", "role": "body", "section": "The Matrix Rosenthal-Pinelis Inequality", "weight": 1.0} -->

Versions of the matrix Rosenthal-Pinelis inequality first appeared in the literature on noncommutative martingales, where they were called noncommutative Burkholder inequalities. For an application to random matrices, see the follow-up work by the same authors. Subsequent papers contain related noncommutative martingale inequalities inspired by the research.

<!-- chunk {"id": "body-0476", "role": "body", "section": "Empirical Approximation", "weight": 1.0} -->

Matrix approximation by random sampling is a special case of a general method that Bernard Maurey developed to compute entropy numbers of convex hulls. Let us give a short presentation of the original context, along with references to some other applications.

<!-- chunk {"id": "body-0477", "role": "body", "section": "Empirical Bounds for Covering Numbers", "weight": 1.0} -->

Suppose that X is a Banach space. Consider the convex hull E ∅ conv{ e 1,..., e N } of a set of N points in X, and assume that κ e k κ · L. We would like to give an upper bound for the number of balls of radius " it takes to cover this set.

<!-- chunk {"id": "body-0478", "role": "body", "section": "Empirical Bounds for Covering Numbers", "weight": 1.0} -->

Fix a point u 2 E, and express u as a convex combination: Let x be the random vector in X that takes value e k with probability pk. Wecanapproximate the point u as an average ¯ x ∅ n ϒ 1 P n k ∅ 1 x k of independent copies x 1,..., x n of the random vector x. Then The family { % k } consists of independent Rademacher random variables. The first inequality depends on the symmetrization procedure [, Lem. 6.3], and the second is Hölder's. In certain Banach spaces, a Khintchine-type inequality holds: The last inequality depends on the uniform bound κ e k κ · L. This estimate controls the expected error in approximating an arbitrary point in E by randomized sampling.

<!-- chunk {"id": "body-0479", "role": "body", "section": "Empirical Bounds for Covering Numbers", "weight": 1.0} -->

The number T 2(X) is called the type two constant of the Banach space X, and it can be estimated in many concrete instances; see [, Chap. 9] or [, Chap. 11]. For our purposes, the most relevant example is the Banach space M d 1 ≤ d 2 consisting of d 1 ≤ d 2 matrices equipped with the spectral norm. Its type two constant satisfies This result follows from work of Tomczak-Jaegermann [, Thm. 3.1(ii)]. In fact, the space M d 1 ≤ d 2 enjoys an even stronger property with respect to averages, namely the noncommutative Khintchine inequality (4.7.1).

<!-- chunk {"id": "body-0480", "role": "body", "section": "Empirical Bounds for Covering Numbers", "weight": 1.0} -->

Now, suppose that the number n of samples in our empirical approximation ¯ x n of the point u 2 E satisfies Then the probabilistic method ensures that there is a some collection of u 1,..., u n of points drawn with repetition from the set { e 1,..., e N } that satisfies There are at most N n different ways to select the points u k. It follows that we can cover the convex hull E ∅ conv{ e 1,..., e N } in X with at most N n norm balls of radius ".

<!-- chunk {"id": "body-0481", "role": "body", "section": "History and Applications of Empirical Approximation", "weight": 1.0} -->

Maurey did not publish his ideas, and the method was first broadcast in a paper of Pisier [, Lem. 1]. Another early reference is the work of Carl [, Lem. 1]. More recently, this covering argument has been used to study the restricted isomorphism behavior of a random set of rows drawn from a discrete Fourier transform matrix.

<!-- chunk {"id": "body-0482", "role": "body", "section": "History and Applications of Empirical Approximation", "weight": 1.0} -->

By now, empirical approximation has appeared in a wide range of applied contexts, although many papers do not recognize the provenance of the method. Let us mention some examples in machine learning. Empirical approximation has been used to study what functions can be approximated by neural networks. The same idea appears in papers on sparse modeling, such as, and it supports the method of random features. Empirical approximation also stands at the core of a recent algorithm for constructing approximate Nash equilibria.

<!-- chunk {"id": "body-0483", "role": "body", "section": "History and Applications of Empirical Approximation", "weight": 1.0} -->

It is difficult to identify the earliest work in computational mathematics that invoked the empirical method to approximate matrices. The paper of Achlioptas & McSherry on randomized sparsification is one possible candidate.

<!-- chunk {"id": "body-0484", "role": "body", "section": "History and Applications of Empirical Approximation", "weight": 1.0} -->

Corollary 6.2.1, which we use to perform the analysis of matrix approximation by sampling, does not require the full power of the matrix Bernstein inequality, Theorem 6.1.1. Indeed, Corollary 6.2.1 can be derived from the weaker methods of Ahlswede & Winter; for example, see the papers.

<!-- chunk {"id": "body-0485", "role": "body", "section": "Randomized Sparsification", "weight": 1.0} -->

The idea of using randomized sparsification to accelerate spectral computations appears in a paper of Achlioptas & McSherry. d'Asprémont [d'A11] proposed to use sparsification to accelerate algorithms for semidefinite programming. The paper by Achlioptas, Karnin, & Liberty recommends sparsification as a mechanism for data compression.

<!-- chunk {"id": "body-0486", "role": "body", "section": "Randomized Sparsification", "weight": 1.0} -->

After the initial paper, several other researchers developed sampling schemes for randomized sparsification. Later, Drineas & Zouzias pointed out that matrix concentration inequalities can be used to analyze this type of algorithm. The paper refined this analysis to obtain sharper bounds. The simple analysis here is drawn from a recent note by Kundu & Drineas.

<!-- chunk {"id": "body-0487", "role": "body", "section": "Randomized Matrix Multiplication", "weight": 1.0} -->

Theideaofusingrandomsamplingtoaccelerate matrix multiplication appeared in nascent form in a paper of Frieze, Kannan, & Vempala. The paper of Drineas & Kannan develops this idea in full generality, and the article of Drineas, Kannan, & Mahoney contains a more detailed treatment. Subsequently, Tamás Sarlós obtained a significant improvement in the performance of this algorithm. Rudelson & Vershynin obtained the first error bound for approximate matrix multiplication with respect to the spectral norm. The analysis that we presented is adapted from the dissertation of Tassos Zouzias, which refines an earlier treatment by Magen & Zouzias. See the monographs of Mahoney and Woodruff for a more extensive discussion.

<!-- chunk {"id": "body-0488", "role": "body", "section": "RandomFeatures", "weight": 1.0} -->

Our discussion of kernel methods is adapted from the book. The papers of Ali Rahimi and Ben Recht proposed the idea of using random features to summarize data for large-scale kernel machines. The construction (6.5.6) of a random feature map for a translationinvariant, positive-definite kernel appears in their work. This approach has received a significant amountof attention over the last few years, and there has been a lot of subsequent development. For example, the paper of Kar & Karnick shows how to construct random features for inner-product kernels, and the paper of Hamid et al. develops random features for polynomial kernels. Our analysis of random features using the matrix Bernstein inequality is drawn from the recent article [LPSS ⊕ 14] of Lopez-Paz et al. The presentation here is adapted from the author's tutorial on randomized matrix approximation, given at ICML 2014 in Beijing. Werecommend the two papers [, LPSS ⊕ 14] for an up-to-date bibliography.

<!-- chunk {"id": "body-0489", "role": "body", "section": "Results Involving the Intrinsic Dimension", "weight": 1.0} -->

A minor shortcoming of our matrix concentration results is the dependence on the ambient dimension of the matrix. In this chapter, we show how to obtain a dependence on an intrinsic dimension parameter, which occasionally is much smaller than the ambient dimension. In many cases, intrinsic dimension bounds offer only a modest improvement. Nevertheless, there are examples where the benefits are significant enough that we can obtain nontrivial results for infinite-dimensional random matrices.

<!-- chunk {"id": "body-0490", "role": "body", "section": "Results Involving the Intrinsic Dimension", "weight": 1.0} -->

In this chapter, present a version of the matrix Chernoff inequality that involves an intrinsic dimension parameter. We also describe a version of the matrix Bernstein inequality that involves an intrinsic dimension parameter. The intrinsic Bernstein result usually improves on Theorem 6.1.1. These results depend on a new argument that distills ideas from a paper of Stanislav Minsker. We omit intrinsic dimension bounds for matrix series, which the reader may wish to develop as an exercise.

<!-- chunk {"id": "body-0491", "role": "body", "section": "Results Involving the Intrinsic Dimension", "weight": 1.0} -->

To give a sense of what these new results accomplish, we revisit some of the examples from earlier chapters. We apply the intrinsic Chernoff bound to study a random column submatrix of a fixed matrix. We also reconsider the randomized matrix multiplication algorithm in light of the intrinsic Bernstein bound. In each case, the intrinsic dimension parameters have an attractive interpretation in terms of the problem data.

<!-- chunk {"id": "body-0492", "role": "body", "section": "Overview", "weight": 1.0} -->

We begin our development in §7.1 with the definition of the intrinsic dimension of a matrix. In §7.2, we present the intrinsic Chernoff bound and some of its consequences. In §7.3, we describe the intrinsic Bernstein inequality and its applications. Afterward, we describe the new ingredients that are required in the proofs. Section 7.4 explains how to extend the matrix Laplace transform method beyond the exponential function, and §7.5 describes a simple but powerful lemma that allows us to obtain the dependence on the intrinsic dimension. Section 7.6 contains the proof of the intrinsic Chernoff bound, and §7.7 develops the proof of the intrinsic Bernstein bound.

<!-- chunk {"id": "body-0493", "role": "body", "section": "The Intrinsic Dimension of a Matrix", "weight": 1.0} -->

Some types of random matrices are concentrated in a small number of dimensions, while they have little content in other dimensions. So far, our bounds do not account for the difference. We need to introduce a more refined notion of dimension that will help us to discriminate among these examples.

<!-- chunk {"id": "body-0494", "role": "body", "section": "The Intrinsic Dimension of a Matrix", "weight": 1.0} -->

Definition 7.1.1 (Intrinsic Dimension). For a positive-semidefinite matrix A, the intrinsic dimension is the quantity We interpret the intrinsic dimension as a measure of the number of dimensions where A has significant spectral content.

<!-- chunk {"id": "body-0495", "role": "body", "section": "The Intrinsic Dimension of a Matrix", "weight": 1.0} -->

Let us make a few observations that support this view. By expressing the trace and the norm in terms of the eigenvalues, we can verify that 1 · intdim(A) · rank(A) · dim(A).

<!-- chunk {"id": "body-0496", "role": "body", "section": "The Intrinsic Dimension of a Matrix", "weight": 1.0} -->

The first inequality is attained precisely when A has rank one, while the second inequality is attained precisely when A is a multiple of the identity. The intrinsic dimension is 0-homogeneous, so it is insensitive to changes in the scale of the matrix A. The intrinsic dimension is not monotone with respect to the semidefinite order. Indeed, we can drive the intrinsic dimension to one by increasing one eigenvalue of A substantially.

<!-- chunk {"id": "body-0497", "role": "body", "section": "Matrix Chernoff with Intrinsic Dimension", "weight": 1.0} -->

Let us present an extension of the matrix Chernoff inequality. This result controls the maximum eigenvalue of a sum of random, positive-semidefinite matrices in terms of the intrinsic dimension of the expectation of the sum.

<!-- chunk {"id": "body-0498", "role": "body", "section": "Matrix Chernoff with Intrinsic Dimension", "weight": 1.0} -->

Theorem 7.2.1 (Matrix Chernoff: Intrinsic Dimension). Consider a finite sequence { X k } of random, Hermitian matrices of the same size, and assume that Introduce the random matrix Suppose that we have a semidefinite upper bound M for the expectation E Y: Define an intrinsic dimension bound and a mean bound: The proof of this result appears below in §7.6.

<!-- chunk {"id": "body-0499", "role": "body", "section": "Discussion", "weight": 1.5} -->

Theorem 7.2.1 is almost identical with the parts of the basic matrix Chernoff inequality that concern the maximum eigenvalue, max( Y ). Let us call attention to the differences. The key advantage is that the current result depends on the intrinsic dimension of the matrix M instead of the ambient dimension. When the eigenvalues of M decay, the improvement can be dramatic. We do suffer a small cost in the extra factor of two, and the tail bound is restricted to a smaller range of the parameter ". Neither of these limitations is particularly significant.

<!-- chunk {"id": "body-0500", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have chosen to frame the result in terms of the upper bound M because it can be challenging to calculate the mean E Y exactly. The statement here allows us to draw conclusions directly from the upper bound M. These estimates do not follow formally from a result stated for E Y because the intrinsic dimension is not monotone with respect to the semidefinite order.

<!-- chunk {"id": "body-0501", "role": "body", "section": "Discussion", "weight": 1.5} -->

A shortcoming of Theorem 7.2.1 is that it does not provide any information about, min( Y ). Curiously, the approach we use to prove the result just does not work for the minimum eigenvalue.

<!-- chunk {"id": "body-0502", "role": "body", "section": "Example: A Random Column Submatrix", "weight": 1.0} -->

To demonstrate the value of Theorem 7.2.1, let us return to one of the problems we studied in §5.2. We can now develop a refined estimate for the expected norm of a random column submatrix drawn from a fixed matrix.

<!-- chunk {"id": "body-0503", "role": "body", "section": "Example: A Random Column Submatrix", "weight": 1.0} -->

In this example, we consider a fixed m ≤ n matrix B, and we let { -k } be an independent family of BERNOULLI(p / n) random variables. We form the random submatrix where b: k is the k th column of B. This random submatrix contains an average of p nonzero columns from B. To study the norm of Z, we consider the positive-semidefinite random matrix This time, we invoke Theorem 7.2.1 to obtain a new estimate for the maximum eigenvalue of Y.

<!-- chunk {"id": "body-0504", "role": "body", "section": "Example: A Random Column Submatrix", "weight": 1.0} -->

We need a semidefinite bound M for the mean E Y of the random matrix. In this case, the exact value is available: Wecan easily calculate the intrinsic dimension of this matrix: The second identity holds because the intrinsic dimension is scale invariant. The last relation is simply the definition (2.1.25) of the stable rank. The maximum eigenvalue of M verifies The maximum norm L of any term in the sum Y satisfies L ∅ max k κ b: k κ 2.

<!-- chunk {"id": "body-0505", "role": "body", "section": "Example: A Random Column Submatrix", "weight": 1.0} -->

Wemaynowapplytheintrinsic Chernoff inequality. The expectation bound (7.2.1) with ∅ 1 delivers In the earlier analysis, we obtained a similar bound (5.2.1). The new result depends on the logarithm of the stable rank instead of log m, the logarithm of the number of rows of B. When the stable rank of B is small-meaning that many rows are almost collinear-then the revised estimate can result in a substantial improvement.

<!-- chunk {"id": "body-0506", "role": "body", "section": "Matrix Bernstein with Intrinsic Dimension", "weight": 1.0} -->

Next, we present an extension of the matrix Bernstein inequality. These results provide tail bounds for an independent sum of bounded random matrices that depend on the intrinsic dimension of the variance. This theorem is essentially due to Stanislav Minsker.

<!-- chunk {"id": "body-0507", "role": "body", "section": "Matrix Bernstein with Intrinsic Dimension", "weight": 1.0} -->

Theorem 7.3.1 (Intrinsic Matrix Bernstein). Consider a finite sequence { S k } of random complex matrices with the same size, and assume that Let V 1 and V 2 be semidefinite upper bounds for the matrix-valued variances Var 1(Z) and Var 2(Z): Define an intrinsic dimension bound and a variance bound Introduce the random matrix The proof of this result appears below in §7.7.

<!-- chunk {"id": "body-0508", "role": "body", "section": "Discussion", "weight": 1.5} -->

Theorem 7.3.1 is quite similar to Theorem 6.1.1, so we focus on the differences. Although the statement of Theorem 7.3.1 may seem circumspect, it is important to present the result in terms of upper bounds V 1 and V 2 for the matrix-valued variances. Indeed, it can be challenging to calculate the matrix-valued variances exactly. The fact that the intrinsic dimension is not monotone interferes with our ability to use a simpler result.

<!-- chunk {"id": "body-0509", "role": "body", "section": "Discussion", "weight": 1.5} -->

Notethatthetail bound (7.3.2) now depends on the intrinsic dimension of the block-diagonal matrix diag( V 1, V 2). This intrinsic dimension quantity never exceeds the total of the two side lengths of the random matrix Z. As a consequence, the new tail bound always has a better dimensional dependence than the earlier result. The costs of this improvement are small: We pay an extra factor of four in the probability bound, and we must restrict our attention to a more limited range of the parameter t. Neither of these changes is significant.

<!-- chunk {"id": "body-0510", "role": "body", "section": "Discussion", "weight": 1.5} -->

The result does not contain an explicit estimate for E κ Z κ, but we can obtain such a bound by integrating the tail inequality (7.3.2). This estimate is similar with the earlier bound (6.1.3), but it depends on the intrinsic dimension instead of the ambient dimension.

<!-- chunk {"id": "body-0511", "role": "body", "section": "Discussion", "weight": 1.5} -->

Corollary 7.3.2 (Intrinsic Matrix Bernstein: Expectation Bound). Instate the notation and hypotheses of Theorem 7.3.1. Then See §7.7.4 for the proof.

<!-- chunk {"id": "body-0512", "role": "body", "section": "Discussion", "weight": 1.5} -->

Next, let us have a closer look at the intrinsic dimension quantity defined in (7.3.1).

<!-- chunk {"id": "body-0513", "role": "body", "section": "Discussion", "weight": 1.5} -->

Wecanmakeafurther bound on the denominator to obtain an estimate in terms of the intrinsic dimensions of the two blocks: This bound reflects a curious phenomenon: the intrinsic dimension parameter d is not necessarily comparable with the larger of intdim(V 1) or intdim(V 2).

<!-- chunk {"id": "body-0514", "role": "body", "section": "Discussion", "weight": 1.5} -->

The other commentary about the original matrix Bernstein inequality, Theorem 6.1.1, also applies to the intrinsic dimension result. For example, we can adapt the result to a sum of uncentered, independent, random, bounded matrices. In addition, the theorem becomes somewhat simpler for a Hermitian random matrix because there is only one matrix-valued variance to deal. The modifications required in these cases are straightforward.

<!-- chunk {"id": "body-0515", "role": "body", "section": "Example: Matrix Approximation by Random Sampling", "weight": 1.0} -->

Wecanapply the intrinsic Bernstein inequality to study the behavior of randomized methods for matrix approximation. The following result is an immediate consequence of Theorem 7.3.1 and Corollary 7.3.2.

<!-- chunk {"id": "body-0516", "role": "body", "section": "Example: Matrix Approximation by Random Sampling", "weight": 1.0} -->

Corollary 7.3.3 (Matrix Approximation by Random Sampling: Intrinsic Dimension Bounds). Let B be a fixed d 1 ≤ d 2 matrix. Construct a d 1 ≤ d 2 random matrix R that satisfies Let M 1 and M 2 be semidefinite upper bounds for the expected squares: Define the quantities Form the matrix sampling estimator Then the estimator satisfies Furthermore, for all t ÷ π m ⊕ L /3, The proof is similar with that of Corollary 6.2.1, so we omit the details.

<!-- chunk {"id": "body-0517", "role": "body", "section": "Application: Randomized Matrix Multiplication", "weight": 1.0} -->

Wewill apply Corollary 7.3.3 to study the randomized matrix multiplication algorithm from §6.4. This method results in a small, but very appealing, improvement in the number of samples that are required. This argument is essentially due to Tassos Zouzias.

<!-- chunk {"id": "body-0518", "role": "body", "section": "Application: Randomized Matrix Multiplication", "weight": 1.0} -->

Our goal is to approximate the product of a d 1 ≤ N matrix B and an N ≤ d 2 matrix C. We assume that both matrices B and C have unit spectral norm. The results are stated in terms of the average stable rank The stable rank was introduced in (2.1.25). To approximate the product BC, we constructed a simple random matrix R whose mean E R ∅ BC, and then we formed the estimator The challenge is to bound the error κ ¯ R n ϒ BC κ.

<!-- chunk {"id": "body-0519", "role": "body", "section": "Application: Randomized Matrix Multiplication", "weight": 1.0} -->

To do so, let us refer back to our calculations from §6.4. We find that Starting from this point, we can quickly improve on our earlier analysis by incorporating the intrinsic dimension bounds.

<!-- chunk {"id": "body-0520", "role": "body", "section": "Application: Randomized Matrix Multiplication", "weight": 1.0} -->

It is natural to set M 1 ∅ 2 ′ asr ′ BB / and M 2 ∅ 2 ′ asr ′ C / C. We may now bound the intrinsic dimension parameter ∅ srank(B) ⊕ srank(C) ∅ 2 ′ asr.

<!-- chunk {"id": "body-0521", "role": "body", "section": "Application: Randomized Matrix Multiplication", "weight": 1.0} -->

Thefirst inequality follows from (7.3.4), and the second is Definition 7.1.1, of the intrinsic dimension. The third relation depends on the norm identities (2.1.8) and (2.1.24). Finally, we identify the stable ranks of B and C and the average stable rank. The calculation of the quantity m proceeds from the same considerations as in §6.4. Thus, This is all the information we need to collect.

<!-- chunk {"id": "body-0522", "role": "body", "section": "Application: Randomized Matrix Multiplication", "weight": 1.0} -->

Corollary 7.3.3 now implies that In other words, if the number n of samples satisfies In the original analysis from §6.4, our estimate for the number n of samples contained the term log(d 1 ⊕ d 2) instead of log(1 ⊕ asr). We have replaced the dependence on the ambient dimension of the product BC by a measure of the stable rank of the two factors. When the average stable rank is small in comparison with the dimension of the product, the analysis based on the intrinsic dimension offers an improvement in the bound on the number of samples required to approximate the product.

<!-- chunk {"id": "body-0523", "role": "body", "section": "Revisiting the Matrix Laplace Transform Bound", "weight": 1.0} -->

Let us proceed with the proofs of the matrix concentration inequalities based on intrinsic dimension. The challenge is to identify and remedy the weak points in the arguments from Chapter 3.

<!-- chunk {"id": "body-0524", "role": "body", "section": "Revisiting the Matrix Laplace Transform Bound", "weight": 1.0} -->

After some reflection, we can trace the dependence on the ambient dimension in our earlier results to the proof of Proposition 3.2.1. In the original argument, we used an exponential function to transform the tail event before applying Markov's inequality. This approach leads to trouble for the simple reason that the exponential function does not pass through the origin, which gives undue weight to eigenvalues that are close to zero. then the error satisfies We can resolve this problem by using other types of maps to transform the tail event. The functions we have in mind are adjusted versions of the exponential. In particular, for fixed ∪ 0, we can consider Both functions are nonnegative and convex, and they are nondecreasing on the positive real line. In each case, ˆ i ∅ 0. At the same time, the presence of the exponential function allows us to exploit our bounds for the trace mgf.

<!-- chunk {"id": "body-0525", "role": "body", "section": "Revisiting the Matrix Laplace Transform Bound", "weight": 1.0} -->

Proposition 7.4.1 (Generalized Matrix Laplace Transform Bound). Let Y be a random Hermitian matrix. Let ˆ: R ! R ⊕ be a nonnegative function that is nondecreasing on [0, 1). For each t ÷ 0, Proof. The proof follows the same lines as the proof of Proposition 3.2.1, but it requires some additional finesse. Since ˆ is nondecreasing on [0, 1), the bound a ÷ t implies that ˆ (a) ÷ ˆ (t). As a consequence, Indeed, on the tail event, max(Y) ÷ t, we must have ˆ (, max(Y)) ÷ ˆ (t). The Spectral Mapping Theorem, Proposition 2.1.3, indicates that the number ˆ (, max(Y)) is one of the eigenvalues of the matrix ˆ (Y), so we determine that, max(ˆ (Y)) also exceeds ˆ (t).

<!-- chunk {"id": "body-0526", "role": "body", "section": "Revisiting the Matrix Laplace Transform Bound", "weight": 1.0} -->

Returning to the tail probability, we discover that ThesecondboundisMarkov'sinequality (2.2.1), which is valid because ˆ is nonnegative. Finally, The inequality holds because of the fact (2.1.13) that the trace of ˆ (Y), a positive-semidefinite matrix, must be at least as large as its maximum eigenvalue.

<!-- chunk {"id": "body-0527", "role": "body", "section": "The Intrinsic Dimension Lemma", "weight": 1.0} -->

The other new ingredient is a simple observation that allows us to control a trace function applied to a positive-semidefinite matrix in terms of the intrinsic dimension of the matrix.

<!-- chunk {"id": "body-0528", "role": "body", "section": "The Intrinsic Dimension Lemma", "weight": 1.0} -->

Lemma7.5.1 (Intrinsic Dimension). Let ' be a convex function on the interval [0, 1), and assume that ' ∅ 0. For any positive-semidefinite matrix A, it holds that Proof. Since the function a 7! ' (a) is convex on the interval [0, L], it is bounded above by the chord connecting the graph at the endpoints. That is, for a 2 [0, L], The eigenvalues of A fall in the interval [0, L], where L ∅κ A κ. As an immediate consequence of the Transfer Rule (2.1.14), we find that Identify the intrinsic dimension of A to complete the argument.

<!-- chunk {"id": "body-0529", "role": "body", "section": "The Hermitian Case", "weight": 1.0} -->

As usual, Hermitian matrices provide the natural setting for matrix concentration. We begin with an explicit statement and proof of a bound for the Hermitian case.

<!-- chunk {"id": "body-0530", "role": "body", "section": "The Hermitian Case", "weight": 1.0} -->

Theorem 7.7.1 (Matrix Bernstein: Hermitian Case with Intrinsic Dimension). Consider a finite sequence { X k } of random Hermitian matrices of the same size, and assume that Introduce the random matrix Let V be a semidefinite upper bound for the matrix-valued variance Var (Y): Define the intrinsic dimension bound and variance bound The proof of this result appears in the next section.

<!-- chunk {"id": "body-0531", "role": "body", "section": "Notes", "weight": 1.0} -->

At present, there are two different ways to improve the dimensional factor that appears in matrix concentration inequalities.

<!-- chunk {"id": "body-0532", "role": "body", "section": "Notes", "weight": 1.0} -->

First, there is a sequence of matrix concentration results where the dimensional parameter is bounded by the maximum rank of the random matrix. The first bound of this type is due to Rudelson. Oliveira's results also exhibit this reduced dimensional dependence. A subsequent paper by Magen & Zouzias contains a related argument that gives similar results. We do not discuss this class of bounds here.

<!-- chunk {"id": "body-0533", "role": "body", "section": "Notes", "weight": 1.0} -->

The idea that the dimensional factor should depend on metric properties of the random matrix appears in a paper of Hsu, Kakade, & Zhang. They obtain a bound that is similar with Theorem 7.7.1. Unfortunately, their argument is complicated, and the results it delivers are suboptimal.

<!-- chunk {"id": "body-0534", "role": "body", "section": "Notes", "weight": 1.0} -->

Theorem 7.7.1 is essentially due to Stanislav Minsker. His approach leads to somewhat sharper bounds than the approach in the paper of Hsu, Kakade, & Zhang, and his method is easier to understand.

<!-- chunk {"id": "body-0535", "role": "body", "section": "Notes", "weight": 1.0} -->

These notes contain another approach to intrinsic dimension bounds. The intrinsic Chernoff bounds that emerge from our framework are new. The proof of the intrinsic Bernstein bound, Theorem 7.7.1, can be interpreted as a distillation of Minsker's argument. Indeed, many of the specific calculations already appear in Minsker's paper. We have obtained constants that are marginally better.

<!-- chunk {"id": "body-0536", "role": "body", "section": "AProof of Lieb's Theorem", "weight": 1.0} -->

Ourapproach to random matrices depends on some sophisticated ideas that are not usually presented in linear algebra courses. This chapter contains a complete derivation of the results that undergird our matrix concentration inequalities. We begin with a short argument that explains how Lieb's Theorem follows from deep facts about a function called the matrix relative entropy. The balance of the chapter is devoted to an analysis of the matrix relative entropy. Along the way, weestablish the core properties of the trace exponential function and the matrix logarithm. This discussion may serve as an introduction to the advanced techniques of matrix analysis.

<!-- chunk {"id": "body-0537", "role": "body", "section": "Lieb's Theorem", "weight": 1.0} -->

In his 1973 paper on trace functions, Lieb established an important concavity theorem [, Thm. 6] for the trace exponential function. As we saw in Chapter 3, this result animates all of our matrix concentration inequalities.

<!-- chunk {"id": "body-0538", "role": "body", "section": "Lieb's Theorem", "weight": 1.0} -->

Theorem 8.1.1 (Lieb). Let H be a fixed Hermitian matrix with dimension d. The map is concave on the convex cone of d ≤ d positive-definite Hermitian matrices.

<!-- chunk {"id": "body-0539", "role": "body", "section": "Lieb's Theorem", "weight": 1.0} -->

Section 8.1 contains an overview of the proof of Theorem 8.1.1. First, we state the background material that we require, and then we show how the theorem follows. Some of the supporting results are major theorems in their own right, and the details of their proofs will consume the rest of the chapter.

<!-- chunk {"id": "body-0540", "role": "body", "section": "Conventions", "weight": 1.0} -->

The symbol R ⊕⊕ refers to the set of positive real numbers. We remind the reader of our convention that bold capital letters that are symmetric about the vertical axis ( A, H, M, T, U, ' ) always refer to Hermitian matrices. We reserve the letter I for the identity matrix, while the letter Q always refers to a unitary matrix. Other bold capital letters ( B, K, L ) denote rectangular matrices.

<!-- chunk {"id": "body-0541", "role": "body", "section": "Conventions", "weight": 1.0} -->

Unless stated otherwise, the results in this chapter hold for all matrices whose dimensions are compatible. For example, any result that involves a sum A ⊕ H includes the implicit constraint that the two matrices are the same size.

<!-- chunk {"id": "body-0542", "role": "body", "section": "Conventions", "weight": 1.0} -->

Throughout this chapter, we assume that the parameter ¿ 2, and we use the shorthand ¯ ¿ ∅ 1 ϒ ¿ to make formulas involving convex combinations more legible.

<!-- chunk {"id": "body-0543", "role": "body", "section": "Matrix Relative Entropy", "weight": 1.0} -->

The proof of Lieb's Theorem depends on the properties of a bivariate function called the matrix relative entropy.

<!-- chunk {"id": "body-0544", "role": "body", "section": "Matrix Relative Entropy", "weight": 1.0} -->

Definition 8.1.2 (Matrix Relative Entropy). Let A and H be positive-definite matrices of the same size. The entropy of A relative to H is The relative entropy can be viewed as a measure of the difference between the matrix A and the matrix H, but it is not a metric. Related functions arise in quantum statistical mechanics and quantum information theory.

<!-- chunk {"id": "body-0545", "role": "body", "section": "Matrix Relative Entropy", "weight": 1.0} -->

Weneed two facts about the matrix relative entropy.

<!-- chunk {"id": "body-0546", "role": "body", "section": "Matrix Relative Entropy", "weight": 1.0} -->

Proposition 8.1.3 (Matrix Relative Entropy is Nonnegative). For positive-definite matrices A and H of the same size, the matrix relative entropy D( A; H ) ÷ 0.

<!-- chunk {"id": "body-0547", "role": "body", "section": "Matrix Relative Entropy", "weight": 1.0} -->

Proposition 8.1.3 is easy to prove; see Section 8.3.5 for the short argument.

<!-- chunk {"id": "body-0548", "role": "body", "section": "Matrix Relative Entropy", "weight": 1.0} -->

Theorem 8.1.4 (The Matrix Relative Entropy is Convex). The map (A, H) 7! D(A; H) is convex. That is, for positive-definite A i and H i of the same size, Theorem 8.1.4 is one of the crown jewels of matrix analysis. The supporting material for this result occupies the bulk of this chapter; the argument culminates in Section 8.8.

<!-- chunk {"id": "body-0549", "role": "body", "section": "Partial Maximization", "weight": 1.0} -->

We also require a basic fact from convex analysis which states that partial maximization of a concave function produces a concave function. We include the simple proof.

<!-- chunk {"id": "body-0550", "role": "body", "section": "Partial Maximization", "weight": 1.0} -->

Fact 8.1.5 (Partial Maximization). Let f be a concave function of two variables. Then the function y 7! sup x f ( x; y ) obtained by partial maximization is concave.

<!-- chunk {"id": "body-0551", "role": "body", "section": "Partial Maximization", "weight": 1.0} -->

Proof. Fix " ∪ 0. For each pair of points y 1 and y 2, there are points x 1 and x 2 that satisfy For each ¿ 2, the concavity of f implies that Take the limit as " # 0 to see that the partial supremum is a concave function of y.

<!-- chunk {"id": "body-0552", "role": "body", "section": "AProof of Lieb's Theorem", "weight": 1.0} -->

Taking the results about the matrix relative entropy for granted, it is not hard to prove Lieb's Theorem. We begin with a variational representation of the trace, which restates the fact that matrix relative entropy is nonnegative.

<!-- chunk {"id": "body-0553", "role": "body", "section": "AProof of Lieb's Theorem", "weight": 1.0} -->

Lemma8.1.6 (Variational Formula for Trace). Let M be a positive-definite matrix. Then Proof. Proposition (8.1.3) states that D(T; M) ÷ 0. Introduce the definition of the matrix relative entropy, and rearrange to reach When T ∅ M, both sides are equal, which yields the advertised identity.

<!-- chunk {"id": "body-0554", "role": "body", "section": "AProof of Lieb's Theorem", "weight": 1.0} -->

To establish Lieb's Theorem, we use the variational formula to represent the trace exponential. Then we use the partial maximization result to condense the desired concavity property from the convexity of the matrix relative entropy.

<!-- chunk {"id": "body-0555", "role": "body", "section": "AProof of Lieb's Theorem", "weight": 1.0} -->

Proof of Theorem 8.1.1. In the variational formula, Lemma 8.1.6, select M ∅ exp(H ⊕ log A) to obtain The latter expression can be written compactly using the matrix relative entropy: For each Hermitian matrix H, the bracket is a concave function of the pair (T, A) because of Theorem 8.1.4. We see that the right-hand side of (8.1.2) is the partial maximum of a concave function, and Fact 8.1.5 ensures that this expression defines a concave function of A. This observation establishes the theorem.

<!-- chunk {"id": "body-0556", "role": "body", "section": "Analysis of the Relative Entropy for Vectors", "weight": 1.0} -->

Many deep theorems about matrices have analogies for vectors. This observation is valuable because we can usually adapt an analysis from the vector setting to establish the parallel result for matrices. In the matrix setting, however, it may be necessary to install a significant amount of extra machinery. If we keep the simpler structure of the vector argument in mind, we can avoid being crushed in the gears.

<!-- chunk {"id": "body-0557", "role": "body", "section": "The Relative Entropy for Vectors", "weight": 1.0} -->

The goal of §8.2 is to introduce the relative entropy function for positive vectors and to derive some key properties of this function. Later we will analyze the matrix relative entropy by emulating these arguments.

<!-- chunk {"id": "body-0558", "role": "body", "section": "The Relative Entropy for Vectors", "weight": 1.0} -->

Definition 8.2.1 (Relative Entropy). Let a and h be positive vectors of the same size. The entropy of a relative to h is defined as A variant of the relative entropy arises in information theory and statistics as a measure of the discrepancy between two probability distributions on a finite set. We will show that the relative entropy is nonnegative and convex.

<!-- chunk {"id": "body-0559", "role": "body", "section": "The Relative Entropy for Vectors", "weight": 1.0} -->

It may seem abusive to recycle the notation for the relative entropy on matrices. To justify this decision, we observe that where diag(′) maps a vector to a diagonal matrix in the natural way. In other words, the vector relative entropy is a special case of the matrix relative entropy. Ultimately, the vector case is easier to understand because diagonal matrices commute.

<!-- chunk {"id": "body-0560", "role": "body", "section": "Relative Entropy is Nonnegative", "weight": 1.0} -->

As we have noted, the relative entropy measures the difference between two positive vectors. This interpretation is supported by the fact that the relative entropy is nonnegative.

<!-- chunk {"id": "body-0561", "role": "body", "section": "Relative Entropy is Nonnegative", "weight": 1.0} -->

Proposition 8.2.2 (Relative Entropy is Nonnegative). For positive vectors a and h of the same size, the relative entropy D( a; h ) ÷ 0.

<!-- chunk {"id": "body-0562", "role": "body", "section": "Relative Entropy is Nonnegative", "weight": 1.0} -->

Proof. Let f: R ⊕⊕ ! R be a differentiable convex function on the positive real line. The function f lies above its tangent lines, so Instantiate this result for the convex function f (a) ∅ a log a ϒ a, and rearrange to obtain the numerical inequality Sumthis expression over the components of the vectors a and h to complete the argument.

<!-- chunk {"id": "body-0563", "role": "body", "section": "Relative Entropy is Nonnegative", "weight": 1.0} -->

Proposition 8.1.3 states that the matrix relative entropy satisfies the same nonnegativity property as the vector relative entropy. The argument for matrices relies on the same ideas as Proposition 8.2.2, and it is hardly more difficult. See §8.3.5 for the details.

<!-- chunk {"id": "body-0564", "role": "body", "section": "The Perspective Transformation", "weight": 1.0} -->

Our next goal is to prove that the relative entropy is a convex function. To establish this claim, we use an elegant technique from convex analysis. The approach depends on the perspective transformation, a method for constructing a bivariate convex function from a univariate convex function.

<!-- chunk {"id": "body-0565", "role": "body", "section": "The Perspective Transformation", "weight": 1.0} -->

Definition 8.2.3 (Perspective Transformation). Let f: R ⊕⊕ ! R be a convex function on the positive real line. The perspective ˆ f of the function f is defined as The perspective transformation has an interesting geometric interpretation. If we trace the ray from the origin in R 3 through the point (a, h, ˆ f (a; h)), it pierces the plane (1, ′, ′) at the point (1, h / a, f (h / a)). Equivalently, for each positive a, the epigraph of f is the 'shadow' of the epigraph of ˆ f (a, ′) on the plane (1, ′, ′).

<!-- chunk {"id": "body-0566", "role": "body", "section": "The Perspective Transformation", "weight": 1.0} -->

The key fact is that the perspective of a convex function is convex. This point follows from the geometric reasoning in the last paragraph; we also include an analytic proof.

<!-- chunk {"id": "body-0567", "role": "body", "section": "The Perspective Transformation", "weight": 1.0} -->

Fact 8.2.4 (Perspectives are Convex). Let f: R ⊕⊕ ! R be a convex function. Then the perspective ˆ f is convex. That is, for positive numbers ai and hi, Proof. Fix two pairs (a 1, h 1) and (a 2, h 2) of positive numbers and an interpolation parameter ¿ 2. Form the convex combinations Weneed to bound the perspective ˆ f (a; h) as the convex combination of its values at ˆ f (a 1; h 1) and ˆ f (a 2; h 2). The trick is to introduce another pair of interpolation parameters: By construction, s 2 and ¯ s ∅ 1 ϒ s. Wequickly determine that To obtain the second identity, we write h as a convex combination. The third identity follows from the definitions of s and ¯ s. The inequality depends on the fact that f is convex. Afterward, we invoke the definitions of s and ¯ s again. We conclude that ˆ f is convex.

<!-- chunk {"id": "body-0568", "role": "body", "section": "The Perspective Transformation", "weight": 1.0} -->

When we study standard matrix functions, it is sometimes necessary to replace a convexity assumption by a stricter property called operator convexity. There is a remarkable extension of the perspective transform that constructs a bivariate matrix function from an operator convex function. The matrix perspective has a powerful convexity property analogous with the result in Fact 8.2.4. The analysis of the matrix perspective depends on a far-reaching generalization of the Jensen inequality for operator convex functions. We develop these ideas in §§8.4.5, 8.5, and 8.6.

<!-- chunk {"id": "body-0569", "role": "body", "section": "The Relative Entropy is Convex", "weight": 1.0} -->

To establish that the relative entropy is convex, we simply need to represent it as the perspective of a convex function.

<!-- chunk {"id": "body-0570", "role": "body", "section": "The Relative Entropy is Convex", "weight": 1.0} -->

Proposition 8.2.5 (Relative Entropy is Convex). The map (a, h) 7! D(a; h) is convex. That is, for positive vectors a i and h i of the same size, Proof. Consider the convex function f (a) ∅ a ϒ 1 ϒ log a, defined on the positive real line. By direct calculation, the perspective transformation satisfies Fact 8.2.4 states that ˆ f is a convex function. For positive vectors a and h, we can express the relative entropy as It follows that the relative entropy is convex.

<!-- chunk {"id": "body-0571", "role": "body", "section": "The Relative Entropy is Convex", "weight": 1.0} -->

Similarly, we can express the matrix relative entropy using the matrix perspective transformation. The analysis for matrices is substantially more involved. But, as we will see in §8.8, the argument ultimately follows the same pattern as the proof of Proposition 8.2.5.

<!-- chunk {"id": "body-0572", "role": "body", "section": "Elementary Trace Inequalities", "weight": 1.0} -->

It is time to begin our investigation into the properties of matrix functions. This section contains somesimple inequalities for the trace of a matrix function that we can establish by manipulating eigenvalues and eigenvalue decompositions. These techniques are adequate to explain why the matrix relative entropy is nonnegative. In contrast, we will need more subtle arguments to study the convexity properties of the matrix relative entropy.

<!-- chunk {"id": "body-0573", "role": "body", "section": "Trace Functions", "weight": 1.0} -->

We can construct a real-valued function on Hermitian matrices by composing the trace with a standard matrix function. This type of map is called a trace function.

<!-- chunk {"id": "body-0574", "role": "body", "section": "Trace Functions", "weight": 1.0} -->

Definition 8.3.1 (Trace function). Let f: I ! R be a function on an interval I of the real line, and let A be an Hermitian matrix whose eigenvalues are contained in I. We define the trace function tr f by the rule where, i (A) denotes the ith largest eigenvalue of A. This formula gives the same result as composing the trace with the standard matrix function f.

<!-- chunk {"id": "body-0575", "role": "body", "section": "Trace Functions", "weight": 1.0} -->

Our first goal is to demonstrate that a trace function tr f inherits a monotonicity property from the underlying scalar function f.

<!-- chunk {"id": "body-0576", "role": "body", "section": "Monotone Trace Functions", "weight": 1.0} -->

Let us demonstrate that the trace of a weakly increasing scalar function induces a trace function that preserves the semidefinite order. To that end, recall that the relation A ≼ H implies that each eigenvalue of A is dominated by the corresponding eigenvalue of H.

<!-- chunk {"id": "body-0577", "role": "body", "section": "Monotone Trace Functions", "weight": 1.0} -->

Fact 8.3.2 (Semidefinite Order implies Eigenvalue Order). For Hermitian matrices A and H, Proof. This result follows instantly from the Courant-Fischer Theorem: The maximum ranges over all i -dimensional linear subspaces L in the domain of A, and we use the convention that 0/0 ∅ 0. The inequality follows from the definition (2.1.11) of the semidefinite order ≼.

<!-- chunk {"id": "body-0578", "role": "body", "section": "Monotone Trace Functions", "weight": 1.0} -->

With this fact at hand, the claim follows quickly.

<!-- chunk {"id": "body-0579", "role": "body", "section": "Monotone Trace Functions", "weight": 1.0} -->

Proposition 8.3.3 (Monotone Trace Functions). Let f: I ! R be a weakly increasing function on an interval I of the real line, and let A and H be Hermitian matrices whose eigenvalues are contained in I. Then Proof. In view of Fact 8.3.2, The inequality depends on the assumption that f is weakly increasing.

<!-- chunk {"id": "body-0580", "role": "body", "section": "Monotone Trace Functions", "weight": 1.0} -->

Our approach to matrix concentration relies on a special case of Proposition 8.3.3.

<!-- chunk {"id": "body-0581", "role": "body", "section": "Monotone Trace Functions", "weight": 1.0} -->

Example 8.3.4 (Trace Exponential is Monotone). The trace exponential map is monotone: for all Hermitian matrices A and H.

<!-- chunk {"id": "body-0582", "role": "body", "section": "Eigenvalue Decompositions, Redux", "weight": 1.0} -->

Before we continue, let us introduce a style for writing eigenvalue decompositions that will make the next argument more transparent. Each d ≤ d Hermitian matrix A can be expressed as Theeigenvalues, 1 ÷′′′ ÷, d of A are real numbers, listed in weakly decreasing order. The family { u 1,..., u d } of eigenvectors of A forms an orthonormal basis for C d with respect to the standard inner product.

<!-- chunk {"id": "body-0583", "role": "body", "section": "ATrace Inequality for Bivariate Functions", "weight": 1.0} -->

In general, it is challenging to study functions of two or more matrices because the eigenvectors can interact in complicated ways. Nevertheless, there is one type of relation that always transfers from the scalar setting to the matrix setting.

<!-- chunk {"id": "body-0584", "role": "body", "section": "ATrace Inequality for Bivariate Functions", "weight": 1.0} -->

Proposition 8.3.5 (Generalized Klein Inequality). Let fi: I ! R and gi: I ! R be functions on an interval I of the real line, and suppose that If A and H are Hermitian matrices whose eigenvalues are contained in I, then Proof. Consider eigenvalue decompositions A ∅ P j, j u j u / j and H ∅ P k ' k v k v / k. Then We use the definition of a standard matrix function, we apply linearity of the trace to reorder the sums, and we identify the trace as a squared inner product. The inequality follows from our assumption on the scalar functions.

<!-- chunk {"id": "body-0585", "role": "body", "section": "The Matrix Relative Entropy is Nonnegative", "weight": 1.0} -->

Using the generalized Klein inequality, it is easy to prove Proposition 8.1.3, which states that the matrix relative entropy is nonnegative. The argument echoes the analysis in Proposition 8.2.2 for the vector case.

<!-- chunk {"id": "body-0586", "role": "body", "section": "The Matrix Relative Entropy is Nonnegative", "weight": 1.0} -->

Proof of Proposition 8.1.3. Suppose that f: R ⊕⊕ ! R is a differentiable, convex function on the positive real line. Since f is convex, the graph of f lies above its tangents: Using the generalized Klein inequality, Proposition 8.3.5, we can lift this relation to matrices: This formula is sometimes called the (ungeneralized) Klein inequality.

<!-- chunk {"id": "body-0587", "role": "body", "section": "The Matrix Relative Entropy is Nonnegative", "weight": 1.0} -->

Instantiate the latter result for the function f (a) ∅ a log a ϒ a, and rearrange to see that In other words, the matrix relative entropy is nonnegative.

<!-- chunk {"id": "body-0588", "role": "body", "section": "The Logarithm of a Matrix", "weight": 1.0} -->

In this section, we commence our journey toward the proof that the matrix relative entropy is convex. The proof of Proposition 8.2.5 indicates that the convexity of the logarithm plays an important role in the convexity of the vector relative entropy. As a first step, we will demonstrate that the matrix logarithm has a striking convexity property with respect to the semidefinite order. Along the way, we will also develop a monotonicity property of the matrix logarithm.

<!-- chunk {"id": "body-0589", "role": "body", "section": "AnIntegral Representation of the Logarithm", "weight": 1.0} -->

Initially, we defined the logarithm of a d ≤ d positive-definite matrix A using an eigenvalue decomposition: To study how the matrix logarithm interacts with the semidefinite order, we will work with an alternative presentation based on an integral formula.

<!-- chunk {"id": "body-0590", "role": "body", "section": "AnIntegral Representation of the Logarithm", "weight": 1.0} -->

Proposition 8.4.1 (Integral Representation of the Logarithm). The logarithm of a positive number a is given by the integral Similarly, the logarithm of a positive-definite matrix A is given by the integral Proof. To verify the scalar formula, we simply use the definition of the improper integral: We obtain the matrix formula by applying the scalar formula to each eigenvalue of A and then expressing the result in terms of the original matrix.

<!-- chunk {"id": "body-0591", "role": "body", "section": "AnIntegral Representation of the Logarithm", "weight": 1.0} -->

The integral formula from Proposition 8.4.1 is powerful because it expresses the logarithm in terms of the matrix inverse, which is much easier to analyze. Although it may seem that we have pulled this representation from thin air, the approach is motivated by a wonderful theory of matrix functions initiated by Löwner in the 1930s.

<!-- chunk {"id": "body-0592", "role": "body", "section": "Operator Monotone Functions", "weight": 1.0} -->

Our next goal is to study the monotonicity properties of the matrix logarithm. To frame this discussion properly, we need to introduce an abstract definition.

<!-- chunk {"id": "body-0593", "role": "body", "section": "Operator Monotone Functions", "weight": 1.0} -->

Definition 8.4.2 (Operator Monotone Function). Let f: I ! R be a function on an interval I of the real line. The function f is operator monotone on I when for all Hermitian matrices A and H whose eigenvalues are contained in I.

<!-- chunk {"id": "body-0594", "role": "body", "section": "Operator Monotone Functions", "weight": 1.0} -->

Let us state some basic facts about operator monotone functions. Many of these points follow easily from the definition.

<!-- chunk {"id": "body-0595", "role": "body", "section": "Operator Monotone Functions", "weight": 1.0} -->

- Whenfl ÷ 0, the weakly increasing affine function t 7!fi ⊕ fl t is operator monotone on each interval I of the real line. - The quadratic function t 7! t 2 is not operator monotone on the positive real line. - The exponential map t 7! e t is not operator monotone on the real line. - Whenfi ÷ 0 and f is operator monotone on I, the function fi f is operator monotone on I. - If f and g are operator monotone on an interval I, then f ⊕ g is operator monotone on I.

<!-- chunk {"id": "body-0596", "role": "body", "section": "Operator Monotone Functions", "weight": 1.0} -->

These properties imply that the operator monotone functions form a convex cone. It also warns us that the class of operator monotone functions is somewhat smaller than the class of weakly increasing functions.

<!-- chunk {"id": "body-0597", "role": "body", "section": "The Negative Inverse is Operator Monotone", "weight": 1.0} -->

Fortunately, interesting operator monotone functions do exist. Let us present an important example related to the matrix inverse.

<!-- chunk {"id": "body-0598", "role": "body", "section": "The Negative Inverse is Operator Monotone", "weight": 1.0} -->

Proposition 8.4.3 (Negative Inverse is Operator Monotone). For each number u ÷ 0, the function a 7!ϒ (a ⊕ u) ϒ 1 is operator monotone on the positive real line. That is, for positive-definite matrices A and H, Proof. Define the matrices A u ∅ A ⊕ u I and H u ∅ H ⊕ u I. Thesemidefinite relation A ≼ H implies that A u ≼ H u. Apply the Conjugation Rule (2.1.12) to see that Whenapositive-definite matrix has eigenvalues bounded above by one, its inverse has eigenvalues bounded below by one. Therefore, Another application of the Conjugation Rule (2.1.12) delivers the inequality H ϒ 1 u ≼ A ϒ 1 u. Finally, we negate this semidefinite relation, which reverses its direction.

<!-- chunk {"id": "body-0599", "role": "body", "section": "The Logarithm is Operator Monotone", "weight": 1.0} -->

Now, we are prepared to demonstrate that the logarithm is an operator monotone function. The argument combines the integral representation from Proposition 8.4.1 with the monotonicity of the inverse map from Proposition 8.4.3.

<!-- chunk {"id": "body-0600", "role": "body", "section": "The Logarithm is Operator Monotone", "weight": 1.0} -->

Proposition 8.4.4 (Logarithm is Operator Monotone). The logarithm is an operator monotone function on the positive real line. That is, for positive-definite matrices A and H, A ≼ H implies log A ≼ log H.

<!-- chunk {"id": "body-0601", "role": "body", "section": "The Logarithm is Operator Monotone", "weight": 1.0} -->

Proof. For each u ÷ 0, Proposition 8.4.3 demonstrates that The integral representation of the logarithm, Proposition 8.4.1, allows us to calculate that We have used the fact that the semidefinite order is preserved by integration against a positive measure.

<!-- chunk {"id": "body-0602", "role": "body", "section": "Operator Convex Functions", "weight": 1.0} -->

Next, let us investigate the convexity properties of the matrix logarithm. As before, we start with an abstract definition.

<!-- chunk {"id": "body-0603", "role": "body", "section": "Operator Convex Functions", "weight": 1.0} -->

Definition 8.4.5 (Operator Convex Function). Let f: I ! R be a function on an interval I of the real line. The function f is operator convex on I when andfor all Hermitian matrices A and H whose eigenvalues are contained in I. A function g: I ! R is operator concave when ϒ g is operator convex on I.

<!-- chunk {"id": "body-0604", "role": "body", "section": "Operator Convex Functions", "weight": 1.0} -->

We continue with some important facts about operator convex functions. Most of these claims can be derived easily.

<!-- chunk {"id": "body-0605", "role": "body", "section": "Operator Convex Functions", "weight": 1.0} -->

- When ÷ 0, the quadratic function t 7!fi ⊕ fl t ⊕ t 2 is operator convex on the real line. - The exponential map t 7! e t is not operator convex on the real line. - When fi ÷ 0 and f is operator convex on I, the function fi f is operator convex in I. - If f and g are operator convex on I, then f ⊕ g is operator convex on I.

<!-- chunk {"id": "body-0606", "role": "body", "section": "Operator Convex Functions", "weight": 1.0} -->

The operator monotone functions form a convex cone. We also learn that the family of operator convex functions is somewhat smaller than the family of convex functions.

<!-- chunk {"id": "body-0607", "role": "body", "section": "The Inverse is Operator Convex", "weight": 1.0} -->

The inverse provides a very important example of an operator convex function.

<!-- chunk {"id": "body-0608", "role": "body", "section": "The Inverse is Operator Convex", "weight": 1.0} -->

Proposition 8.4.6 (Inverse is Operator Convex). For each u ÷ 0, the function a 7! (a ⊕ u) ϒ 1 is operator convex on the positive real line. That is, for positive-definite matrices A and H, To establish Proposition 8.4.6, we use an argument based on the Schur complement lemma. For completeness, let us state and prove this important fact.

<!-- chunk {"id": "body-0609", "role": "body", "section": "The Inverse is Operator Convex", "weight": 1.0} -->

Fact 8.4.7 (Schur Complements). Suppose that T is a positive-definite matrix. Then Proof of Fact 8.4.7. To see why this is true, just calculate that In essence, we are performing block Gaussian elimination to bring the original matrix into blockdiagonal form. Now, the Conjugation Rule (2.1.12) ensures that the central matrix on the left is positive semidefinite together with the matrix on the right. From this equivalence, we extract the result (8.4.1).

<!-- chunk {"id": "body-0610", "role": "body", "section": "The Inverse is Operator Convex", "weight": 1.0} -->

Wecontinue with the proof that the inverse is operator convex.

<!-- chunk {"id": "body-0611", "role": "body", "section": "The Inverse is Operator Convex", "weight": 1.0} -->

Proof of Proposition 8.4.6. The Schur complement lemma, Fact 8.4.7, provides that Applying this observation to the positive-definite matrices A ⊕ u I and H ⊕ u I, we see that Since the top-left block of the latter matrix is positive definite, another application of Fact 8.4.7 delivers the relation This is the advertised conclusion.

<!-- chunk {"id": "body-0612", "role": "body", "section": "The Logarithm is Operator Concave", "weight": 1.0} -->

We are finally prepared to verify that the logarithm is operator concave. The argument is based on the integral representation from Proposition 8.4.4 and the convexity of the inverse map from Proposition 8.4.6.

<!-- chunk {"id": "body-0613", "role": "body", "section": "The Logarithm is Operator Concave", "weight": 1.0} -->

Proposition 8.4.8 (Logarithm is Operator Concave). The logarithm is operator concave on the positive real line. That is, for positive-definite matrices A and H, Proof. For each u ÷ 0, Proposition 8.4.6 demonstrates that Invoke the integral representation of the logarithm from Proposition 8.4.1 to see that Once again, we have used the fact that integration preserves the semidefinite order.

<!-- chunk {"id": "body-0614", "role": "body", "section": "The Operator Jensen Inequality", "weight": 1.0} -->

Convexity is a statement about how a function interacts with averages. By definition, a function f: I ! R is convex when The convexity inequality (8.5.1) automatically extends from an average involving two terms to an arbitrary average. This is the content of Jensen's inequality.

<!-- chunk {"id": "body-0615", "role": "body", "section": "The Operator Jensen Inequality", "weight": 1.0} -->

Definition 8.4.5, of an operator convex function f: I ! R, is similar in spirit: and all Hermitian matrices A and H whose eigenvalues are contained in I. Surprisingly, the semidefinite relation (8.5.2) automatically extends to a large family of matrix averaging operations. This remarkable property is called the operator Jensen inequality.

<!-- chunk {"id": "body-0616", "role": "body", "section": "Matrix Convex Combinations", "weight": 1.0} -->

In a vector space, convex combinations provide a natural method of averaging. But matrices have a richer structure, so we can consider a more general class of averages.

<!-- chunk {"id": "body-0617", "role": "body", "section": "Matrix Convex Combinations", "weight": 1.0} -->

Definition 8.5.1 (Matrix Convex Combination). Let A 1 and A 2 be Hermitian matrices. Consider a decomposition of the identity of the form is called a matrix convex combination of A 1 and A 2.

<!-- chunk {"id": "body-0618", "role": "body", "section": "Matrix Convex Combinations", "weight": 1.0} -->

To see why it is reasonable to call (8.5.3) an averaging operation on Hermitian matrices, let us note a few of its properties.

<!-- chunk {"id": "body-0619", "role": "body", "section": "Matrix Convex Combinations", "weight": 1.0} -->

- Definition 8.5.1 encompasses scalar convex combinations because we can take K 1 ∅ ¿ 1/2 I and K 2 ∅ ¯ ¿ 1/2 I. - The matrix convex combination preserves the identity matrix: K / 1 I K 1 ⊕ K / 2 I K 2 ∅ I.

<!-- chunk {"id": "body-0620", "role": "body", "section": "Matrix Convex Combinations", "weight": 1.0} -->

- If the eigenvalues of A 1 and A 2 are contained in an interval I, then the eigenvalues of the matrix convex combination (8.5.3) are also contained in I.

<!-- chunk {"id": "body-0621", "role": "body", "section": "Matrix Convex Combinations", "weight": 1.0} -->

Wewill encounter a concrete example of a matrix convex combination later when we prove Theorem 8.6.2.

<!-- chunk {"id": "body-0622", "role": "body", "section": "Jensen's Inequality for Matrix Convex Combinations", "weight": 1.0} -->

Operator convexity is a self-improving property. Even though the definition of an operator convex function only involves a scalar convex combination, it actually contains an inequality for matrix convex combinations. This is the content of the operator Jensen inequality.

<!-- chunk {"id": "body-0623", "role": "body", "section": "Jensen's Inequality for Matrix Convex Combinations", "weight": 1.0} -->

Theorem8.5.2 (Operator Jensen Inequality). Let f be an operator convex function on an interval I of the real line, and let A 1 and A 2 be Hermitian matrices with eigenvalues in I. Consider a decomposition of the identity Proof. Let us introduce a block-diagonal matrix: Indeed, the matrix A lies in the domain of f because its eigenvalues fall in the interval I. Wecan apply a standard matrix function to a block-diagonal matrix by applying the function to each block.

<!-- chunk {"id": "body-0624", "role": "body", "section": "Jensen's Inequality for Matrix Convex Combinations", "weight": 1.0} -->

There are two main ingredients in the argument. The first idea is to realize the matrix convex combination of A 1 and A 2 by conjugating the block-diagonal matrix A with an appropriate unitary matrix. To that end, let us construct a unitary matrix To see why this is possible, note that the first block of columns is orthonormal: As a consequence, we can choose L 1 and L 2 to complete the unitary matrix Q. By direct computation, we find that Wehave omitted the precise values of the entries labeled / because they do not play a role in our argument.

<!-- chunk {"id": "body-0625", "role": "body", "section": "Jensen's Inequality for Matrix Convex Combinations", "weight": 1.0} -->

Then The second idea is to restrict the block matrix in (8.5.5) to its diagonal. To perform this maneuver, we express the diagonalizing operation as a scalar convex combination of two unitary conjugations, which gives us access to the operator convexity of f. Let us see how this works. Define the unitary matrix The key observation is that, for any block matrix, Another advantage of this construction is that we can easily apply a standard matrix function to the block-diagonal matrix.

<!-- chunk {"id": "body-0626", "role": "body", "section": "Jensen's Inequality for Matrix Convex Combinations", "weight": 1.0} -->

Together, these two ideas lead to a succinct proof of the operator Jensen inequality. Write [′]11 for the operation that returns the block of a block matrix. We may calculate that The first identity depends on the representation (8.5.5) of the matrix convex combination as the block of Q / AQ. The second line follows because the averaging operation presented in (8.5.6) does not alter the block of the matrix. In view of (8.5.6), we are looking at the block of the matrix obtained by applying f to a block-diagonal matrix. This is equivalent to applying the function f inside the block, which gives the third line. Last, the semidefinite relation follows from the operator convexity of f on the interval I.

<!-- chunk {"id": "body-0627", "role": "body", "section": "Jensen's Inequality for Matrix Convex Combinations", "weight": 1.0} -->

Wecomplete the argument by reversing the steps we have taken so far.

<!-- chunk {"id": "body-0628", "role": "body", "section": "Jensen's Inequality for Matrix Convex Combinations", "weight": 1.0} -->

To obtain the first relation, recall that a standard matrix function commutes with unitary conjugation. The second identity follows from the formula (8.5.6) because diagonalization preserves the block. Finally, we identify the block of Q / f ( A ) Q just as we did in (8.5.5). This step depends on the fact that the diagonal blocks of f ( A ) are simply f ( A 1) and f ( A 2).

<!-- chunk {"id": "body-0629", "role": "body", "section": "The Matrix Perspective Transformation", "weight": 1.0} -->

To show that the vector relative entropy is convex, we represented it as the perspective of a convex function. To demonstrate that the matrix relative entropy is convex, we are going to perform a similar maneuver. This section develops an extension of the perspective transformation that applies to operator convex functions. Then we demonstrate that this matrix perspective has a strong convexity property with respect to the semidefinite order.

<!-- chunk {"id": "body-0630", "role": "body", "section": "The Matrix Perspective", "weight": 1.0} -->

In the scalar setting, the perspective transformation converts a convex function into a bivariate convex function. There is a related construction that applies to an operator convex function.

<!-- chunk {"id": "body-0631", "role": "body", "section": "The Matrix Perspective", "weight": 1.0} -->

Definition 8.6.1 (Matrix Perspective). Let f: R ⊕⊕ ! R be an operator convex function, and let A and H be positive-definite matrices of the same size. Define the perspective map The notation A 1/2 refers to the unique positive-definite square root of A, and A ϒ 1/2 denotes the inverse of this square root.

<!-- chunk {"id": "body-0632", "role": "body", "section": "The Matrix Perspective", "weight": 1.0} -->

The Conjugation Rule (2.1.12) ensures that all the matrices involved remain positive definite, so this definition makes sense. To see why the matrix perspective extends the scalar perspective, notice that This formula is valid because commuting matrices are simultaneously diagonalizable. We will use the matrix perspective in a case where the matrices commute, but it is no harder to analyze the perspective without this assumption.

<!-- chunk {"id": "body-0633", "role": "body", "section": "The Matrix Perspective is Operator Convex", "weight": 1.0} -->

The key result is that the matrix perspective is an operator convex map on a pair of positivedefinite matrices. This theorem follows from the operator Jensen inequality in much the same way that Fact 8.2.4 follows from scalar convexity.

<!-- chunk {"id": "body-0634", "role": "body", "section": "The Matrix Perspective is Operator Convex", "weight": 1.0} -->

Theorem 8.6.2 (Matrix Perspective is Operator Convex). Let f: R ⊕⊕ ! R be an operator convex function. Let A i and H i be positive-definite matrices of the same size. Then Proof. Let f be an operator convex function, and let ' f be its perspective transform. Fix pairs (A 1, H 1) and (A 2, H 2) of positive-definite matrices, and choose an interpolation parameter ¿ 2. Form the scalar convex combinations Our goal is to bound the perspective ' f (A; H) as a scalar convex combination of its values ' f (A 1; H 1) and ' f (A 2; H 2). The idea is to introduce matrix interpolation parameters: Observe that these two matrices decompose the identity: This construction allows us to express the perspective using a matrix convex combination, which gives us access to the operator Jensen inequality.

<!-- chunk {"id": "body-0635", "role": "body", "section": "The Matrix Perspective is Operator Convex", "weight": 1.0} -->

The first line is simply the definition of the matrix perspective. In the second line, we use the definition of H as a scalar convex combination. Third, we introduce the matrix interpolation parameters through the expressions ¿ 1/2 A ϒ 1/2 ∅ A 1/2 1 K 1 and ¯ ¿ 1/2 A ϒ 1/2 ∅ A 1/2 2 K 2 and their conjugate transposes. To continue the calculation, we apply the operator Jensen inequality, Theorem 8.5.2, to reach We have also used the Conjugation Rule (2.1.12) to support the first relation. Finally, we recall the definitions of K 1 and K 2, and we identify the two matrix perspectives.

<!-- chunk {"id": "body-0636", "role": "body", "section": "The Kronecker Product", "weight": 1.0} -->

The matrix relative entropy is a function of two matrices. One of the difficulties of analyzing this type of function is that the two matrix arguments do not generally commute with each other. As a consequence, the behavior of the matrix relative entropy depends on the interactions between the eigenvectors of the two matrices. To avoid this problem, we will build matrices that do commute with each other, which simplifies our task considerably.

<!-- chunk {"id": "body-0637", "role": "body", "section": "The Kronecker Product", "weight": 1.0} -->

Our approach is based on an fundamental object from linear algebra. We restrict our attention to the simplest version here.

<!-- chunk {"id": "body-0638", "role": "body", "section": "The Kronecker Product", "weight": 1.0} -->

Definition 8.7.1 (Kronecker Product). Let A and H be Hermitian matrices with dimension d ≤ d. The Kronecker product A ↑ H is the d 2 ≤ d 2 Hermitian matrix At first sight, the definition of the Kronecker product may seem strange, but it has many delightful properties. The rest of the section develops the basic facts about this construction.

<!-- chunk {"id": "body-0639", "role": "body", "section": "Linearity Properties", "weight": 1.0} -->

First of all, a Kronecker product with the zero matrix is always zero: Next, the Kronecker product is homogeneous in each factor: Furthermore, the Kronecker product is additive in each coordinate: In other words, the Kronecker product is a bilinear operation.

<!-- chunk {"id": "body-0640", "role": "body", "section": "Mixed Products", "weight": 1.0} -->

The Kronecker product interacts beautifully with the usual product of matrices. By direct calculation, we obtain a simple rule for mixed products: Since I ↑ I is the identity matrix, the identity (8.7.1) leads to a formula for the inverse of a Kronecker product: Another important consequence of the rule (8.7.1) is the following commutativity relation: This simple fact has great importance for us.

<!-- chunk {"id": "body-0641", "role": "body", "section": "The Kronecker Product of Positive Matrices", "weight": 1.0} -->

As we have noted, the Kronecker product of two Hermitian matrices is itself an Hermitian matrix. In fact, the Kronecker product preserves positivity as well.

<!-- chunk {"id": "body-0642", "role": "body", "section": "The Kronecker Product of Positive Matrices", "weight": 1.0} -->

Fact 8.7.2 (Kronecker Product Preserves Positivity). Let A and H be positive-definite matrices. Then A ↑ H is positive definite.

<!-- chunk {"id": "body-0643", "role": "body", "section": "The Kronecker Product of Positive Matrices", "weight": 1.0} -->

Proof. To see why, observe that As usual, A 1/2 refers to the unique positive-definite square root of the positive-definite matrix A. We have expressed A ↑ H as the square of an Hermitian matrix, so it must be a positivesemidefinite matrix. To see that it is actually positive definite, we simply apply the inversion formula (8.7.2) to discover that A ↑ H is invertible.

<!-- chunk {"id": "body-0644", "role": "body", "section": "The Logarithm of a Kronecker Product", "weight": 1.0} -->

Aswehavediscussed, the matrix logarithm plays a central role in our analysis. There is an elegant formula for the logarithm of a Kronecker product that will be valuable to us.

<!-- chunk {"id": "body-0645", "role": "body", "section": "The Logarithm of a Kronecker Product", "weight": 1.0} -->

Fact 8.7.3 (Logarithm of a Kronecker Product). Let A and H be positive-definite matrices. Then Proof. Theargumentisbasedonthefactthatthematrixlogarithmisthefunctionalinverseofthe matrix exponential. Since the exponential of a sum of commuting matrices equals the product of the exponentials, we have This formula relies on the commutativity relation (8.7.3). Applying the power series representation of the exponential, we determine that The second identity depends on the rule (8.7.1) for mixed products, and the last identity follows from the linearity of the Kronecker product. A similar calculation shows that exp(I ↑ T) ∅ I ↑ e T. In summary, Wehaveusedtheproduct rule (8.7.1) again. To complete the argument, simply choose M ∅ log A and T ∅ log H and take the logarithm of the last identity.

<!-- chunk {"id": "body-0646", "role": "body", "section": "ALinear Map", "weight": 1.0} -->

Finally, we claim that there is a linear map ' that extracts the trace of the matrix product from the Kronecker product. Let A and H be d ≤ d Hermitian matrices. Then we define The map ' is linear because the Kronecker product A ↑ H tabulates all the pairwise products of the entries of A and H, and tr(AH) is a sum of certain of these pairwise products. For our purposes, the key fact is that the map ' preserves the semidefinite order: This formula is valid for all Hermitian matrices A i and H i. To see why (8.7.5) holds, simply note that the map can be represented as an inner product: The vec operation stacks the columns of a d ≤ d matrix on top of each other, moving from left to right, to form a column vector of length d 2.

<!-- chunk {"id": "body-0647", "role": "body", "section": "The Matrix Relative Entropy is Convex", "weight": 1.0} -->

We are finally prepared to establish Theorem 8.1.4, which states that the matrix relative entropy is a convex function. This argument draws on almost all of the ideas we have developed over the course of this chapter.

<!-- chunk {"id": "body-0648", "role": "body", "section": "The Matrix Relative Entropy is Convex", "weight": 1.0} -->

Consider the function f ( a ) ∅ a ϒ 1 ϒ log a, defined on the positive real line. This function is operator convex because it is the sum of the affine function a 7! a ϒ 1 and the operator convex function a 7!ϒ log a. The negative logarithm is operator convex because of Proposition 8.4.8.

<!-- chunk {"id": "body-0649", "role": "body", "section": "The Matrix Relative Entropy is Convex", "weight": 1.0} -->

Let A and H be positive-definite matrices. Consider the matrix perspective ' f evaluated at the commuting positive-definite matrices A ↑ I and I ↑ H: Wehaveusedthesimplified definition (8.6.1) of the perspective for commuting matrices, and we haveinvokedtherules (8.7.1) and (8.7.2) for arithmetic with Kronecker products. Introducing the definition of the function f, we find that To reach the second line, we use more Kronecker product arithmetic, along with Fact 8.7.3, the law for calculating the logarithm of the Kronecker product. The last line depends on the property that log ¡ A ϒ 1 ¢ ∅ϒ log A. Applying the linear map ' from (8.7.4) to both sides, we reach Wehave represented the matrix relative entropy in terms of a matrix perspective.

<!-- chunk {"id": "body-0650", "role": "body", "section": "The Matrix Relative Entropy is Convex", "weight": 1.0} -->

Let A i and H i be positive-definite matrices, and fix a parameter ¿ 2. Theorem 8.6.2 tells us that the matrix perspective is operator convex: The inequality (8.7.5) states that the linear map ' preserves the semidefinite order.

<!-- chunk {"id": "body-0651", "role": "body", "section": "The Matrix Relative Entropy is Convex", "weight": 1.0} -->

Introducing the formula (8.8.1), we conclude that The matrix relative entropy is convex.

<!-- chunk {"id": "body-0652", "role": "body", "section": "Notes", "weight": 1.0} -->

The material in this chapter is drawn from a variety of sources, ranging from textbooks to lecture notes to contemporary research articles. The best general sources include the books on matrix analysis by Bhatia and by Hiai & Petz. We also recommend a set of notes by Eric Carlen. More specific references appear below.

<!-- chunk {"id": "body-0653", "role": "body", "section": "Lieb's Theorem", "weight": 1.0} -->

Theorem 8.1.1 is one of the major results in the important paper of Elliott Lieb on convex trace functions. Lieb wrote this paper to resolve a conjecture of Wigner, Yanase, & Dyson about the concavity properties of a certain measure of information in a quantum system. He was also motivated by a conjecture that quantum mechanical entropy satisfies a strong subadditivity property. The latter result states that our uncertainty about a partitioned quantum system is controlled by the uncertainty about smaller parts of the system. See Carlen's notes for a modern presentation of these ideas.

<!-- chunk {"id": "body-0654", "role": "body", "section": "Lieb's Theorem", "weight": 1.0} -->

Lieb derived Theorem 8.1.1 as a corollary of another difficult concavity theorem that he developed [, Thm. 1]. The most direct proof of Lieb's Theorem is probably Epstein's argument, which is based on methods from complex analysis; see Ruskai's papers for a condensed version of Epstein's approach. The proof that appears in Section 8.1 is due to the author of these notes; this technique depends on ideas developed by Carlen & Lieb to prove some other convexity theorems [, §5].

<!-- chunk {"id": "body-0655", "role": "body", "section": "Lieb's Theorem", "weight": 1.0} -->

In fact, many deep convexity and concavity theorems for trace functions are equivalent with each other, in the sense that the mutual implications follow from relatively easy arguments. See [, §5] and [, §5] for discussion of this point.

<!-- chunk {"id": "body-0656", "role": "body", "section": "The Matrix Relative Entropy", "weight": 1.0} -->

Our definition of matrix relative entropy differs slightly from the usual definition in the literature on quantum statistical mechanics and quantum information theory because we have included an additional linear term. This alteration does not lead to substantive changes in the analysis.

<!-- chunk {"id": "body-0657", "role": "body", "section": "The Matrix Relative Entropy", "weight": 1.0} -->

The fact that matrix relative entropy is nonnegative is a classical result attributed to Klein. See [, §2] or [, §2.3].

<!-- chunk {"id": "body-0658", "role": "body", "section": "The Matrix Relative Entropy", "weight": 1.0} -->

Lindblad is credited with the result that matrix relative entropy is convex, as stated in Theorem 8.1.4. Lindblad derived this theorem as a corollary of Lieb's results. Bhatia [, Chap. IX] gives two alternative proofs, one due to Connes & Størmer and another due to Petz. There is also a remarkable proof due to Ando [, Thm. 7].

<!-- chunk {"id": "body-0659", "role": "body", "section": "The Matrix Relative Entropy", "weight": 1.0} -->

Our approach to Theorem 8.1.4 is adapted directly from a recent paper of Effros. Nevertheless, many of the ideas date back to the works cited in the last paragraph.

<!-- chunk {"id": "body-0660", "role": "body", "section": "The Relative Entropy for Vectors", "weight": 1.0} -->

The treatment of the relative entropy for vectors in Section 8.2 is based on two classical methods for constructing divergences. To show that the relative entropy is nonnegative, we represent it as a Bregman divergence [Brè67]. To show that the relative entropy is convex, we represent it as an f -divergence. Let us say a few more words about these constructions.

<!-- chunk {"id": "body-0661", "role": "body", "section": "The Relative Entropy for Vectors", "weight": 1.0} -->

Suppose that f is a differentiable convex function on R d. Bregman considered divergences of the form Since f is convex, the Bregman divergence B f is always nonnegative. In the vector setting, there are two main examples of Bregman divergences. The function f (a) ∅ 1 2 κ a κ 2 2 leads to the squared Euclidean distance, and the function f (a) ∅ P i (ai log ai ϒ ai) leads to the vector relative entropy. Bregmandivergences have many geometric properties in common with these two functions. For an introduction to Bregman divergences for matrices, see.

<!-- chunk {"id": "body-0662", "role": "body", "section": "The Relative Entropy for Vectors", "weight": 1.0} -->

Suppose that f: R ⊕⊕ ! R is a convex function. Ali & Silvey and Csiszár considered divergences of the form We recognize this expression as a perspective transformation, so the f -divergence C f is always convex. The main example is based on the Shannon entropy f (a) ∅ a log a, which leads to a cousin of the vector relative entropy. The paper contains a recent discussion of f -divergences and their applications in machine learning. Petz has studied functions related to f -divergences in the matrix setting.

<!-- chunk {"id": "body-0663", "role": "body", "section": "Elementary Trace Inequalities", "weight": 1.0} -->

The material in Section 8.3 on trace functions is based on classical results in quantum statistical mechanics. We have drawn the arguments in this section from Petz's survey [, Sec. 2] and Carlen's lecture notes [, Sec. 2.2].

<!-- chunk {"id": "body-0664", "role": "body", "section": "Operator Monotone & Operator Convex Functions", "weight": 1.0} -->

The theory of operator monotone functions was initiated by Löwner [Löw34]. He developed a characterization of an operator monotone function in terms of divided differences. For a function f, the fi rst divided difference is the quantity Löwner proved that f is operator monotone on an interval I if and only we have the semidefinite relation This result is analogous with the fact that a smooth, monotone scalar function has a nonnegative derivative. Löwner also established a connection between operator monotone functions and Pick functions from the theory of complex variables. A few years later, Kraus introduced the concept of an operator convex function, and he developed some results that parallel Löwner's theory for operator monotone functions.

<!-- chunk {"id": "body-0665", "role": "body", "section": "Operator Monotone & Operator Convex Functions", "weight": 1.0} -->

Somewhat later, Bendat & Sherman developed characterizations of operator monotone and operator convex functions based on integral formulas. For example, f is an operator monotone function on if and only if it can be written in the form Similarly, f is an operator convex function on [0, 1) if and only if it can be written in the form In both cases, d ‰ is a nonnegative measure. The integral representation of the logarithm in Proposition 8.4.1 is closely related to these formulas.

<!-- chunk {"id": "body-0666", "role": "body", "section": "Operator Monotone & Operator Convex Functions", "weight": 1.0} -->

We have taken the proof that the matrix inverse is monotone from Bhatia's book [, Prop. V.1.6]. The proof that the matrix inverse is convex appears in Ando's paper. Our treatment of the matrix logarithm was motivated by a conversation with Eric Carlen at an IPAM workshop at Lake Arrowhead in December 2010.

<!-- chunk {"id": "body-0667", "role": "body", "section": "Operator Monotone & Operator Convex Functions", "weight": 1.0} -->

For more information about operator monotonicity and operator convexity, we recommend Bhatia's books, Carlen's lecture notes, and the book of Hiai & Petz.

<!-- chunk {"id": "body-0668", "role": "body", "section": "The Operator Jensen Inequality", "weight": 1.0} -->

The paper of Hansen & Pedersen contains another treatment of operator monotone and operator convex functions. The highlight of this work is a version of the operator Jensen inequality. Theorem 8.5.2 is a refinement of this result that was established by the same authors two decades later. Our proof of the operator Jensen inequality is drawn from Petz's book [, Thm. 8.4]; see also Carlen's lecture notes [, Thm. 4.20].

<!-- chunk {"id": "body-0669", "role": "body", "section": "The Matrix Perspective & the Kronecker Product", "weight": 1.0} -->

Wehavebeenunabletoidentifytheprecisesourceoftheideathatabivariate matrix function can be represented in terms of a matrix perspective. Two important results in this direction appear in Ando's paper [, Thms. 6 and 7]. f positive and operator concave on implies f operator monotone on implies (A, H) 7! (A ↑ I) ′ f ¡ A ↑ H ¢ is operator convex ϒ 1 on pairs of positive-definite matrices. Similarly, ϒ 1 on pairs of positive-definite matrices. Ando proves that the matrix relative entropy is convex by applying the latter result to the matrix logarithm. We believe that Ando was the first author to appreciate the value of framing results of this type in terms of the Kronecker product, and we have followed his strategy here. On the other hand, Ando's analysis is different in spirit because he relies on integral representations of operator monotone and convex functions.

<!-- chunk {"id": "body-0670", "role": "body", "section": "The Matrix Perspective & the Kronecker Product", "weight": 1.0} -->

In a subsequent paper, Kubo & Ando constructed operator means using a related approach. They show that f positive and operator monotone on implies on pairs of positive-definite matrices. Kubo & Ando point out that particular cases of this construction appear in the work of Pusz & Woronowicz. This is the earliest citation where we have seen the matrix perspective black-on-white.

<!-- chunk {"id": "body-0671", "role": "body", "section": "The Matrix Perspective & the Kronecker Product", "weight": 1.0} -->

A few years later, Petz introduced a class of quasi-entropies for matrices. These functions also involve a perspective-like construction, and Petz was clearly influenced by Csiszár's work on f -divergences. See for a contemporary treatment.

<!-- chunk {"id": "body-0672", "role": "body", "section": "The Matrix Perspective & the Kronecker Product", "weight": 1.0} -->

The presentation in these notes is based on a recent paper of Effros. He showed that convexity properties of the matrix perspective follow from the operator Jensen inequality, and he derived the convexity of the matrix relative entropy as a consequence. Our analysis of the matrix perspective in Theorem 8.6.2 is drawn from a subsequent paper, which removes some commutativity assumptions from Effros's argument.

<!-- chunk {"id": "body-0673", "role": "body", "section": "The Matrix Perspective & the Kronecker Product", "weight": 1.0} -->

The proof in §8.8 that the matrix relative entropy is convex, Theorem 8.1.4, recasts Effros's argument [, Cor. 2.2] in the language of Kronecker products. In his paper, Effros works with left- and right-multiplication operators. To appreciate the connection, simply note the identities In other words, the matrix A ↑ I can be interpreted as right-multiplication by A, while the matrix I ↑ H can be interpreted as left-multiplication by H. (The change in sense is an unfortunate consequence of the definition of the Kronecker product.)

<!-- chunk {"id": "body-0674", "role": "body", "section": "Matrix Concentration: Resources", "weight": 1.0} -->

This annotated bibliography describes some papers that involve matrix concentration inequalities. Right now, this presentation is heavily skewed toward theoretical results, rather than applications of matrix concentration.

<!-- chunk {"id": "body-0675", "role": "body", "section": "Exponential Matrix Concentration Inequalities", "weight": 1.0} -->

Webegin with papers that contain the most current results on matrix concentration.

<!-- chunk {"id": "body-0676", "role": "body", "section": "Exponential Matrix Concentration Inequalities", "weight": 1.0} -->

-. These lecture notes are based heavily on the research described in this paper. This work identifies Lieb's Theorem [, Thm. 6] as the key result that animates exponential moment bounds for random matrices. Using this technique, the paper develops the bounds for matrix Gaussian and Rademacher series, the matrix Chernoff inequalities, and several versions of the matrix Bernstein inequality. In addition, it contains a matrix Hoeffding inequality (for sums of bounded random matrices), a matrix Azuma inequality (for matrix martingales with bounded differences), and a matrix bounded difference inequality (for matrix-valued functions of independent random variables). -. This note describes a simple proof of Lieb's Theorem that is based on the joint convexity of quantum relative entropy. This reduction, however, still involves a deep convexity theorem. Chapter 8 contains an explication of this paper. -. Oliveira's paper uses an ingenious argument, based on the Golden-Thompson inequality (3.3.3), to establish a matrix version of Freedman's inequality. This result is, roughly, a martingale version of Bernstein's inequality.

<!-- chunk {"id": "body-0677", "role": "body", "section": "Exponential Matrix Concentration Inequalities", "weight": 1.0} -->

This approach has the advantage that it extends to the fully noncommutative setting. Oliveira applies his results to study some problems in random graph theory. -. This paper shows that Lieb's Theorem leads to a Freedman-type inequality for matrix-valued martingales. The associated technical report describes additional results for matrix-valued martingales. -. This article explains how to use the Lieb-Seiringer Theorem to develop tail bounds for the interior eigenvalues of a sum of independent random matrices. It contains a Chernoff-type bound for a sum of positive-semidefinite matrices, as well as several Bernstein-type bounds for sums of bounded random matrices. - [MJC ⊕ 14]. This paper contains a strikingly different method for establishing matrix concentration inequalities. The argument is based on work of Sourav Chatterjee that shows how Stein's method of exchangeable pairs leads to probability inequalities. This technique has two main advantages. First, it gives results for random matrices that are based on dependent random variables. As a special case, the results apply to sums of independentrandommatrices.

<!-- chunk {"id": "body-0678", "role": "body", "section": "Exponential Matrix Concentration Inequalities", "weight": 1.0} -->

Second, it delivers both exponential moment bounds and polynomial moment bounds for random matrices. Indeed, the paper describes a Bernsteintype exponential inequality and also a Rosenthal-type polynomial moment bound. Furthermore, this work contains what is arguably the simplest known proof of the noncommutative Khintchine inequality.

<!-- chunk {"id": "body-0679", "role": "body", "section": "Exponential Matrix Concentration Inequalities", "weight": 1.0} -->

-. This paper improves on the work in [MJC ⊕ 14] by extending an argument, based on Markov chains, that was developed in Chatterjee's thesis. This analysis leads to satisfactory matrix analogs of scalar concentration inequalities based on logarithmic Sobolev inequalities. In particular, it is possible to develop a matrix version of the exponential Efron-Stein inequality in this fashion. -. The primary focus of this paper is to analyze a specific type of procedure for covariance estimation. The appendix contains a new matrix moment inequality that is, roughly, the polynomial moment bound associated with the matrix Bernstein inequality. -. These lecture notes use matrix concentration inequalities as a tool to study some estimation problems in statistics. They also contain some matrix Bernstein inequalities for unbounded random matrices. - [GN]. Gross and Nesme show how to extend Hoeffding's method for analyzing sampling without replacement to the matrix setting. This result can be combined with a variety of matrix concentration inequalities. -.

<!-- chunk {"id": "body-0680", "role": "body", "section": "Exponential Matrix Concentration Inequalities", "weight": 1.0} -->

This paper combines the matrix Chernoff inequality, Theorem 5.1.1, with the argument from [GN] to obtain a matrix Chernoff bound for a sum of random positivesemidefinite matrices sampled without replacement from a fixed collection. The result is applied to a random matrix that plays a role in numerical linear algebra. -. This paper establishes logarithmic Sobolev inequalities for random matrices, and it derives some matrix concentration inequalities as a consequence. The methods in the paper have applications in quantum information theory, although the matrix concentration bounds are inferior to related results derived using Stein's method.

<!-- chunk {"id": "body-0681", "role": "body", "section": "Bounds with Intrinsic Dimension Parameters", "weight": 1.0} -->

The following works contain matrix concentration bounds that depend on a dimension parameter that may be smaller than the ambient dimension of the matrix.

<!-- chunk {"id": "body-0682", "role": "body", "section": "Bounds with Intrinsic Dimension Parameters", "weight": 1.0} -->

-. Oliveira shows how to develop a version of Rudelson's inequality using a variant of the argument of Ahlswede & Winter. Oliveira's paper is notable because the dimensional factor is controlled by the maximum rank of the random matrix, rather than the ambient dimension.

<!-- chunk {"id": "body-0683", "role": "body", "section": "Bounds with Intrinsic Dimension Parameters", "weight": 1.0} -->

-. This work contains a matrix Chernoff bound for a sum of independent positivesemidefinite random matrices where the dimensional dependence is controlled by the maximum rank of the random matrix. The approach is, essentially, the same as the argument in Rudelson's paper. The paper applies these results to study randomized matrix multiplication algorithms. -. This paper describes a method for proving matrix concentration inequalities where the ambient dimension is replaced by the intrinsic dimension of the matrix variance. The argument is based on an adaptation of the proof. The authors give several examples in statistics and machine learning. -. This work presents a more refined technique for obtaining matrix concentration inequalities that depend on the intrinsic dimension, rather than the ambient dimension. This paper motivated the results in Chapter 7.

<!-- chunk {"id": "body-0684", "role": "body", "section": "The Method of Ahlswede & Winter", "weight": 1.0} -->

Next, we list some papers that use the ideas from the work of Ahslwede & Winter to obtain matrix concentration inequalities. In general, these results have suboptimal parameters, but they played an important role in the development of this field.

<!-- chunk {"id": "body-0685", "role": "body", "section": "The Method of Ahlswede & Winter", "weight": 1.0} -->

-. The original paper of Ahlswede & Winter describes the matrix Laplace transform method, along with a number of other foundational results. They show how to use the Golden-Thompsoninequality to bound the trace of the matrix mgf, and they use this technique to prove a matrix Chernoff inequality for sums of independent and identically distributed random variables. Their main application concerns quantum information theory. -. Christofides and Markström develop a Hoeffding-type inequality for sums of bounded random matrices using the approach of Ahlswede & Winter. They apply this result to study random graphs. -. Gross presents a matrix Bernstein inequality based on the method of Ahlswede & Winter, and he uses it to study algorithms for matrix completion. -. Recht describes a different version of the matrix Bernstein inequality, which also follows from the technique of Ahlswede & Winter. His paper also concerns algorithms for matrix completion.

<!-- chunk {"id": "body-0686", "role": "body", "section": "Noncommutative Moment Inequalities", "weight": 1.0} -->

We conclude with an overview of some major works on bounds for the polynomial moments of a noncommutative martingale. Sums of independent random matrices provide one concrete example where these results apply. The results in this literature are as strong, or stronger, than the exponential moment inequalities that we have described in these notes. Unfortunately, the proofs are typically quite abstract and difficult, and they do not usually lead to explicit constants. Recently there has been some cross-fertilization between noncommutative probability and the field of matrix concentration inequalities.

<!-- chunk {"id": "body-0687", "role": "body", "section": "Noncommutative Moment Inequalities", "weight": 1.0} -->

Note that 'noncommutative' is not synonymous with 'matrix' in that there are noncommutative von Neumann algebras much stranger than the familiar algebra of finite-dimensional matrices equipped with the operator norm.

<!-- chunk {"id": "body-0688", "role": "body", "section": "Noncommutative Moment Inequalities", "weight": 1.0} -->

-. This classic paper gives a bound for the expected trace of an even power of a matrix Rademacher series. These results are important, but they do not give the optimal bounds. -. This paper gives the first noncommutative Khintchine inequality, a bound for the expected trace of an even power of a matrix Rademacher series that depends on the matrix variance. -. This work establishes dual versions of the noncommutative Khintchine inequality. -. These papers prove optimal noncommutative Khintchine inequalities in more general settings, and they obtain sharp constants. -. These papers establish noncommutative versions of the Burkholder-DavisGundy inequality for martingales. They also give an application of these results to random matrix theory. -. This paper contains an overview of noncommutative moment results, along with information about the optimal rate of growth in the constants. -. This paper describes a fully noncommutative version of the Bennett inequality. The proof is based on the method of Ahlswede & Winter. -. This work shows how to use Oliveira's argument to obtain some results for fully noncommutative martingales.

<!-- chunk {"id": "body-0689", "role": "body", "section": "Noncommutative Moment Inequalities", "weight": 1.0} -->

- [MJC ⊕ 14]. This work, described above, includes a section on matrix moment inequalities. This paper contains what are probably the simplest available proofs of these results. -. The appendix of this paper contains a polynomial inequality for sums of independent random matrices.
