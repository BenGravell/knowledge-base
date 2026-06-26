<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

User-friendly Tail Bounds for Sums of Random Matrices

Topics include Matrix concentration, Random matrices, Tail bounds, Probability inequalities, Martingales, Spectral norm.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents accessible matrix concentration inequalities for sums of independent random self-adjoint matrices, including matrix analogues of classical scalar bounds. The paper became a standard reference because it packages powerful noncommutative tail tools in user-friendly forms.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents new probability inequalities for sums of independent, random, self-adjoint matrices. These results place simple and easily verifiable hypotheses on the summands, and they deliver strong conclusions about the large-deviation behavior of the maximum eigenvalue of the sum. Tail bounds for the norm of a sum of random rectangular matrices follow as an immediate corollary. The proof techniques also yield some information about matrix-valued martingales. In other words, this paper provides noncommutative generalizations of the classical bounds associated with the names Azuma, Bennett, Bernstein, Chernoff, Hoeffding, and McDiarmid. The matrix inequalities promise the same diversity of application, ease of use, and strength of conclusion that have made the scalar inequalities so valuable.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Random matrices have come to play a significant role in computational mathematics. This line of research has advanced by using established methods from random matrix theory, but it has also generated difficult questions that cannot be addressed without new tools. Let us summarize some of the challenges that arise in numerical applications.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Research has extended well beyond the classical ensembles (e.g., Wishart matrices and Wigner matrices) to encompass many other classes of random matrices. For instance, it is now common to study the properties of a sparse matrix sampled from a fixed matrix or a random submatrix drawn from a fixed matrix.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We also encounter highly structured matrices that involve a limited amount of randomness. One important example is the randomized DFT, which consists of a diagonal matrix of random signs multiplied by a discrete Fourier transform matrix.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Questions about the spectral properties of random matrices remain fundamental, but modern problems can also involve other considerations. For example, we might need to estimate the cut norm of a random adjacency matrix. Or we might want to study the action of a random operator on a class of vectors or matrices.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most problems in numerical mathematics concern matrices of finite order. Asymptotic theory is less relevant in practice.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We often require explicit large-deviation theorems for statistics of random matrices so that we can study rates of convergence.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Results with effective constants are essential to ensure that algorithms are provably correct.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We have encountered these issues in a wide range of problems from computational mathematics: smoothed analysis of Gaussian elimination; semidefinite relaxation and rounding of quadratic maximization problems; construction of maps for dimensionality reduction; matrix approximation by sparsification and by sampling submatrices; analysis of sparse approximation and compressive sampling algorithms; randomized schemes for low-rank matrix factorization; and analysis of algorithms for completion of low-rank matrices. And this list is by no means comprehensive!

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

In most of these applications, the methods currently invoked to study random matrices require a substantial amount of practice to use effectively. Even so, the final results tend to be a little disappointing: the constants are usually poor and the predictions are sometimes coarser than we might like. These frustrations have led us to search for simpler techniques that still yield detailed quantitative information about finite random matrices.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Technical Overview", "weight": 1.0} -->

We consider a finite sequence $\{{\mathbf{X}}_{k}\}$ of random, self-adjoint matrices with dimension $d$. Our goal is to harness basic properties of these matrices to bound the probability Here and elsewhere, $\lambda_{\max}$ denotes the algebraically largest eigenvalue of a self-adjoint matrix. This formulation is more general than it may appear because we can exploit the same ideas to explore several related problems: We can study the smallest eigenvalue of the sum.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Technical Overview", "weight": 1.0} -->

We can bound the largest singular value of a sum of random rectangular matrices.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Technical Overview", "weight": 1.0} -->

Related arguments apply to matrix martingales and other adapted sequences.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Technical Overview", "weight": 1.0} -->

Indeed, the expression (1.1) captures the essence of many questions that arise in numerical applications of random matrix theory, including most of the research cited above.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Technical Overview", "weight": 1.0} -->

Observe that (1.1) formally resembles the probability that a sum of real random variables exceeds a certain level. The *Laplace transform method*, attributed to Bernstein, is a particularly elegant system for producing tail bounds for sums of scalar random variables; see for accessible discussions. In a remarkable paper, Ahlswede and Winter show how to transport the Laplace transform method to the matrix setting. They establish that In words, the probability (1.1) is controlled by a matrix version of the moment generating function (mgf). See Proposition 3.1. ‣ 3.2. The Laplace Transform Method for Matrices ‣ 3. Tail Bounds via the Laplace Transform Method ‣ User-Friendly Tail Bounds for Sums of Random Matrices") for an easy proof of (1.2) that is due to Oliveira.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Technical Overview", "weight": 1.0} -->

The matrix Laplace transform estimate (1.2) presents a serious technical challenge. We must control the trace of the matrix mgf using information about the summands ${\mathbf{X}}_{1},{\mathbf{X}}_{2},{\mathbf{X}}_{3},\ldots$. This estimate requires powerful tools, and it stands as the major impediment to bounding the tail probability (1.1).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Technical Overview", "weight": 1.0} -->

The true significance of the Ahlswede--Winter argument \[, App.\] consists in their technique for computing the required bounds on the matrix mgf. We describe their method in §3.7. The following probability inequality for a matrix Gaussian series is typical of the results that emerge from their approach. Let $\{{\mathbf{A}}_{k}\}$ be a family of fixed self-adjoint matrices with dimension $d$, and let $\{\gamma_{k}\}$ be a sequence of independent standard normal variables. Then The Ahlswede--Winter apparatus leads to a collection of other interesting probability inequalities; see §1.3 for references. Nevertheless, tail bounds developed in this fashion, including (1.3), are usually very far from optimal. See §3.7 and §4.8 for further discussion of this point.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Technical Overview", "weight": 1.0} -->

This paper describes a more satisfactory framework for completing the bound on the matrix mgf. The crucial new ingredient in our argument is a deep theorem \[, Thm. 6\] of Lieb from his seminal paper on convex trace functions. We introduce Lieb's theorem in §3.4, and we explain how to combine this result with the matrix Laplace transform technique. We use this scheme to obtain a large family of probability inequalities that are essentially sharp in a wide variety of situations.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Technical Overview", "weight": 1.0} -->

Our approach represents a dramatic advance beyond the Ahlswede--Winter technique. For example, our method delivers the following bound for a matrix Gaussian series: The estimate (1.4) offers a fundamental advantage over (1.3) because the variance parameter $\sigma^{2}$ is often $d$ times smaller than $\sigma_{AW}^{2}$. Furthermore, the discussion in §4 demonstrates that the inequality (1.4) cannot be sharpened without changing its structure. This improvement is typical of results constructed from our blueprint.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Index of Inequalities", "weight": 1.0} -->

This work contains a large number of bounds for the probability (1.1). The precise form of each inequality depends on prior information about the summands. As a service to the reader, we have collected the most useful results in this section. We have also included a short qualitative discussion of each bound, along with the location in the paper where the full treatment appears.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Main Results for Positive-Semidefinite Matrices", "weight": 1.0} -->

In classical probability theory, one of the most famous concentration results concerns the number of successes in a sequence of independent random trials. This quantity can be expressed as a sum of independent, bounded random variables. Chernoff's large-deviation theorem provides explicit estimates on the probability that this type of series is greater than (or smaller than) a specified level.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Main Results for Positive-Semidefinite Matrices", "weight": 1.0} -->

In the matrix setting, the analogous theorem concerns a sum of positive-semidefinite random matrices subject to a uniform eigenvalue bound. The matrix Chernoff inequality shows that the extreme eigenvalues of the matrix series have the same binomial-type behavior that occurs in the scalar case.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Main Results for Self-Adjoint Matrices", "weight": 1.0} -->

Another basic example of concentration is provided by a sum of real numbers modulated by independent standard normal variables or, alternatively, by independent Rademacher^11^1A Rademacher random variable is uniformly distributed on $\{{\pm 1}\}$. random variables. A classical result shows that this type of random series exhibits subgaussian tails. When we replace the real numbers by self-adjoint random matrices, we discover that the maximum and minimum eigenvalue of the matrix sum retain this normal tail behavior.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Main Results for Rectangular Matrices", "weight": 1.0} -->

As an immediate corollary of our results for self-adjoint random matrices, we can also establish a collection of inequalities for the maximum singular value of a sum of random rectangular matrices. In each case, we extend the result to rectangular matrices by using a device from operator theory called the *self-adjoint dilation* (§2.6). Remark 3.11. ‣ 3.6. Tail Bounds for Independent Sums ‣ 3. Tail Bounds via the Laplace Transform Method ‣ User-Friendly Tail Bounds for Sums of Random Matrices") and §4.2 offer some discussion of this technique. This section presents two of the most important inequalities for sums of random rectangular matrices.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Main Results for Rectangular Matrices", "weight": 1.0} -->

As in the self-adjoint case, the norm of a Gaussian or Rademacher series with rectangular matrix coefficients has subgaussian tails. This result follows directly from Theorem 1.2. ‣ 1.2.3. Main Results for Self-Adjoint Matrices ‣ 1.2. Index of Inequalities ‣ 1. Introduction ‣ User-Friendly Tail Bounds for Sums of Random Matrices"); see §4.2 for a complete proof. Observe that the variance parameter changes to reflect the fact that the row and column spaces of a general matrix are independent from each other; the variance can be viewed as a noncommutative "sum of squares."

<!-- chunk {"id": "body-0028", "role": "body", "section": "Inequalities for Matrix Martingales", "weight": 1.0} -->

The techniques in this paper also lead directly to some simple results for matrix martingales. This material appears in §7.: The Azuma inequality is the martingale extension of the Hoeffding inequality.: The McDiarmid bounded difference inequality concerns matrix-valued functions of a family of independent random variables. It demonstrates that the extreme eigenvalues of the matrix-valued function exhibit normal concentration.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Inequalities for Matrix Martingales", "weight": 1.0} -->

For more refined martingale inequalities, see the papers and the technical report.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Summary of Related Work", "weight": 1.0} -->

We continue with an overview of some related work on finite-dimensional random matrices. The first group of papers relies on the matrix extension of the Laplace transform method; the second group uses noncommutative moment inequalities.

<!-- chunk {"id": "body-0031", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

The most important precedent for our work is the influential paper of Ahlswede and Winter. They are responsible for developing the matrix version of the Laplace transform method, which shows that the tail probability (1.1) is controlled by a matrix generalization of the mgf. They describe an iterative argument, based on the Golden--Thompson inequality, (2.6) below, that allows them to provide a weak bound for the mgf of a sum of independent random matrices in terms of mgf bounds for the individual summands. In particular, they apply this technique to obtain an extension of the Chernoff inequality \[, Thm. 19\].

<!-- chunk {"id": "body-0032", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

The Ahlswede--Winter method for bounding the matrix mgf is quite general. Several other authors have exploited their technique to obtain matrix extensions of classical probability inequalities. Christofides and Markström establish a matrix version of the Azuma and Hoeffding inequalities. Gross \[, Thm. 6\] and Recht \[, Thm. 3.2\] develop two different matrix extensions of Bernstein's inequality. We also refer the reader to Vershynin's note, which offers a self-contained introduction to the Ahlswede--Winter circle of ideas.

<!-- chunk {"id": "body-0033", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

Results established within the Ahlswede--Winter framework are often sharp for sums of i.i.d. random matrices, but the inequalities are far less accurate when applied to other types of sums. Roughly speaking, the tail bounds have the correct shape, but the method often leads to poor estimates for the quantity that controls the scale of large deviations. For a specific example, compare the variance parameter in (1.3) with the (correct) variance parameter appearing in (1.4). All the results we have mentioned so far have this shortcoming. See §3.7 for technical details.

<!-- chunk {"id": "body-0034", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

Very recently, Oliveira has developed two notable variations on the Ahlswede--Winter method for bounding the matrix mgf. These techniques can sometimes identify the correct matrix generalization of the scale parameter. In particular, the approach can be used to prove Theorem 1.2. ‣ 1.2.3. Main Results for Self-Adjoint Matrices ‣ 1.2. Index of Inequalities ‣ 1. Introduction ‣ User-Friendly Tail Bounds for Sums of Random Matrices"). Oliveira has also developed a version of the matrix Bernstein inequality \[, Thm. 1.2\] that is similar to Theorem 1.4. ‣ 1.2.3. Main Results for Self-Adjoint Matrices ‣ 1.2. Index of Inequalities ‣ 1. Introduction ‣ User-Friendly Tail Bounds for Sums of Random Matrices"); his proof involves a matrix extension of the martingale techniques.

<!-- chunk {"id": "body-0035", "role": "body", "section": "The Matrix Laplace Transform Method", "weight": 1.0} -->

The current article was inspired by the work of Ahlswede--Winter and Oliveira. Our results were obtained independently from Oliveira's paper.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Noncommutative Moment Inequalities", "weight": 1.0} -->

There is another contemporary line of research that uses noncommutative (nc) moment inequalities to study random matrices. In a significant article, Rudelson obtains an optimal estimate for the sample complexity of approximating the covariance matrix of a general isotropic distribution. The argument in his paper, which is due to Pisier, depends on a version of the nc Khintchine inequality.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Noncommutative Moment Inequalities", "weight": 1.0} -->

Rudelson's technique has been applied widely over the last ten years, and it has emerged as a valuable tool for studying discrete random matrices. For example, the method can be used to provide bounds on the norm of a random submatrix \[, Thm. 1.8\] drawn from a fixed matrix. It seems likely, however, that matrix probability inequalities will replace the nc Khintchine inequality for many applications because they are easier to use and often produce better results.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Noncommutative Moment Inequalities", "weight": 1.0} -->

By now, there is a substantial literature on other nc moment inequalities. The article contains a reasonably accessible and comprehensive discussion. Some of these results have been applied to the study of random matrices; see for an example. As we discuss in §4.7, nc moment bounds can also be combined with the matrix Laplace transform method because they sometimes provide an alternative way to control the matrix mgf.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Roadmap", "weight": 1.0} -->

The rest of the paper is organized as follows. Section 2 introduces the background results required for our proofs. Section 3 proves the main technical results that lead to probability inequalities for sums of independent random matrices. Section 4 uses Gaussian series as a case study to illustrate the main features of matrix probability inequalities and to argue that the bounds in this paper are structurally optimal. We develop the matrix Chernoff and Bernstein inequalities in §§5--6. Finally, we establish some simple martingale results in §7.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Algebra, Analysis, and Probability with Matrices", "weight": 1.0} -->

This section provides a short introduction to the background we require for our proofs. The proofs contain detailed cross-references to this material, so the reader may wish to proceed directly to the main thread of argument in §3.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Algebra, Analysis, and Probability with Matrices", "weight": 1.0} -->

Most of these results can be located in Bhatia's books on matrix analysis. The works of Horn and Johnson also serve as good general references. Higham's book is an excellent source for information about matrix functions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conventions on Matrices", "weight": 1.0} -->

A *matrix* is a finite, two-dimensional array of complex numbers. *In this paper, all matrices are square unless otherwise noted*. We add the qualification *rectangular* when we need to refer to a general array, which may be square or nonsquare. Many parts of the discussion do not depend on the size of a matrix, so we specify dimensions only when it matters. In particular, we usually do not state the size of a matrix when it is determined by the context.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conventions on Matrices", "weight": 1.0} -->

Several abbreviations are ubiquitous. Instead of self-adjoint, we often write *s.a.* Positive semidefinite becomes *psd*, and we shorten positive definite to *pd*.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conventions on Matrices", "weight": 1.0} -->

We write $\mathbf{0}$ for the zero matrix and $\mathbf{I}$ for the identity matrix. The matrix $\mathbf{E}_{ij}$ has a unit entry in the $(i,j)$ position and zeros elsewhere. The symbol $\mathbf{Q}$ is reserved for a unitary matrix. We adopt Parlett's convention that bold capital letters symmetric about the vertical axis (${\mathbf{A}},\ldots,{\mathbf{Y}}$ and $\mathbf{\Delta},\ldots,\mathbf{\Omega}$) refer to s.a. matrices.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conventions on Matrices", "weight": 1.0} -->

The symbols $\lambda_{\min}$ and $\lambda_{\max}$ refer to the algebraic minimum and maximum eigenvalues of a s.a. matrix. We use curly inequalities to denote the semidefinite ordering: ${\mathbf{A}} \succcurlyeq \mathbf{0}$ means that $\mathbf{A}$ is psd. The symbol $\left. \parallel \cdot \parallel \right.$ always refers to the $\ell_{2}$ vector norm or the associated operator norm, which is called the *spectral norm* because it returns the maximum singular value of its argument.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conventions on Probability", "weight": 1.0} -->

We prefer to avoid unnecessary abstraction and technical detail, so we frame the standing assumption that all random variables are sufficiently regular that we are justified in computing expectations, interchanging limits, and so forth. Furthermore, we often state that a random variable satisfies some relation and omit the qualification "almost surely." We reserve the symbols ${\mathbf{X}},{\mathbf{Y}}$ for random s.a. matrices.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Matrix Functions", "weight": 1.0} -->

Consider a function $f:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$. We define a map on diagonal matrices by applying the function to each diagonal entry. We then extend $f$ to a function on s.a. matrices using the eigenvalue decomposition: The *spectral mapping theorem* states that each eigenvalue of $f{({\mathbf{A}})}$ is equal to $f{(\lambda)}$ for some eigenvalue $\lambda$ of $\mathbf{A}$. This point is obvious from our definition.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Matrix Functions", "weight": 1.0} -->

Standard inequalities for real functions typically *do not* have parallel versions that hold for the semidefinite ordering. Nevertheless, there is one type of relation for real functions that always extends to the semidefinite setting: We sometimes refer to (2.2) as the *transfer rule*.

<!-- chunk {"id": "body-0049", "role": "body", "section": "The Matrix Exponential", "weight": 1.0} -->

The exponential of an s.a. matrix $\mathbf{A}$ can be defined by applying (2.1) with the function ${f{(x)}} = e^{x}$. Alternatively, we may use the power series expansion The exponential of an s.a. matrix is always pd because of the spectral mapping theorem. On account of the transfer rule (2.2), the matrix exponential satisfies some simple semidefinite relations that we collect here. For each s.a. matrix $\mathbf{A}$, it holds that We often work with the trace of the matrix exponential, ${{tr}\exp}:{{\mathbf{A}}\mapsto{{tr}e^{\mathbf{A}}}}$. The trace exponential function is convex. It is also monotone with respect to the semidefinite order: See \[, Sec. 2\] for short proofs of these facts.

<!-- chunk {"id": "body-0050", "role": "body", "section": "The Matrix Exponential", "weight": 1.0} -->

The matrix exponential *does not* convert sums into products, but the trace exponential has a related property that serves as a limited substitute. The Golden--Thompson inequality \[, Sec. IX.3\] states that The obvious generalization of the bound (2.6) to three matrices is false \[, Prob. IX.8.4\].

<!-- chunk {"id": "body-0051", "role": "body", "section": "The Matrix Logarithm", "weight": 1.0} -->

We define the matrix logarithm as the functional inverse of the matrix exponential: This formula determines the logarithm on the pd cone, which is adequate for our purposes.

<!-- chunk {"id": "body-0052", "role": "body", "section": "The Matrix Logarithm", "weight": 1.0} -->

The matrix logarithm interacts beautifully with the semidefinite order \[, Exer. 4.2.5\]. Indeed, the logarithm is operator monotone: The logarithm is also operator concave: Caveat lector: Operator monotone functions and operator convex functions are depressingly rare. In particular, the matrix exponential does not belong to either class \[, Ch. V\].

<!-- chunk {"id": "body-0053", "role": "body", "section": "Dilations", "weight": 1.0} -->

An extraordinarily fruitful idea from operator theory is to embed matrices within larger block matrices, called *dilations*. The *s.a. dilation* of a rectangular matrix $\mathbf{B}$ is Evidently, $\mathcal{S}{({\mathbf{B}})}$ is always s.a. A short calculation yields the important identity It can also be verified that the s.a. dilation preserves spectral information: We use dilations to extend results for s.a. matrices to rectangular matrices. See Remark 3.11. ‣ 3.6. Tail Bounds for Independent Sums ‣ 3. Tail Bounds via the Laplace Transform Method ‣ User-Friendly Tail Bounds for Sums of Random Matrices") and §4.2 for more information about this technique.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Expectation and the Semidefinite Order", "weight": 1.0} -->

Since the expectation of a random matrix can be viewed as a convex combination and the psd cone is convex, expectation preserves the semidefinite order: Every operator convex function admits an operator Jensen's inequality. In particular, the matrix square is operator convex, which implies that The relation (2.14) is also a specific instance of Kadison's inequality \[, Thm. 2.3.2\].

<!-- chunk {"id": "body-0055", "role": "body", "section": "Tail Bounds via the Laplace Transform Method", "weight": 1.0} -->

This section develops some general probability inequalities for the maximum eigenvalue of a sum of independent random matrices. The main argument can be viewed as a matrix extension of the Laplace transform method for sums of independent real random variables. In the matrix setting, however, it requires great care to execute this technique successfully.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Matrix Moments and Cumulants", "weight": 1.0} -->

Consider a random s.a. matrix $\mathbf{X}$ that has moments of all orders. By analogy with the classical scalar definitions, we may construct matrix extensions of the moment generating function (mgf) and the cumulant generating function (cgf): We admit the possibility that these expectations do not exist for all values of $\theta$. The matrix cgf can be viewed as an *exponential mean*, a weighted average that emphasizes large deviations (with the same sign as $\theta$). The matrix mgf and cgf have formal power series expansions: The coefficients ${\mathbb{E}}{({\mathbf{X}}^{p})}$ are called *matrix moments*, and we refer to $\mathbf{\Psi}_{p}$ as a *matrix cumulant*. The matrix cumulant $\mathbf{\Psi}_{p}$ has a formal expression as a (noncommutative) polynomial in the matrix moments up to order $p$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Matrix Moments and Cumulants", "weight": 1.0} -->

In particular, the first cumulant is the mean and the second cumulant is the variance: Higher-order cumulants are harder to write down and interpret.

<!-- chunk {"id": "body-0058", "role": "body", "section": "The Laplace Transform Method for Matrices", "weight": 1.0} -->

We begin our main development with a striking idea drawn from the influential paper of Ahlswede and Winter. Their work contains a matrix analog of the classical Laplace transform bound. We need the following variant, which is due to Oliveira.

<!-- chunk {"id": "body-0059", "role": "body", "section": "The Failure of the Matrix mgf", "weight": 1.0} -->

In the scalar setting, the Laplace transform method is very effective for studying sums of independent random variables because the mgf decomposes. Consider an independent sequence $\{ X_{k}\}$ of real random variables. Operating formally, we see that the (scalar) mgf of the sum satisfies a multiplication rule: This calculation relies on the fact that the scalar exponential function converts sums to products, a property the matrix exponential does not share. As a consequence, there is no immediate analog of (3.2) in the matrix setting.

<!-- chunk {"id": "body-0060", "role": "body", "section": "The Failure of the Matrix mgf", "weight": 1.0} -->

Ahlswede and Winter attempt to imitate the multiplication rule (3.2) using the following observation. When ${\mathbf{X}}_{1}$ and ${\mathbf{X}}_{2}$ are independent random matrices, The first relation is the Golden--Thompson trace inequality (2.6). Unfortunately, we cannot extend the bound (3.3) to include additional matrices. This cold fact suggests that the Golden--Thompson inequality may not be the natural way to proceed. In §3.7, we map out the route Ahlswede and Winter pursue, but we continue along a different path.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Concave Trace Function", "weight": 1.0} -->

For inspiration, we turn to the literature on matrix analysis. Some of the most beautiful and profound results in this domain concern the convexity of trace functions. We have observed that this theory has incredible implications for the study of random matrices. This paper demonstrates that a large class of matrix probability inequalities follows from a deep theorem \[, Thm. 6\] of Lieb that appears in his seminal work on convex trace functions.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Subadditivity of the Matrix cgf", "weight": 1.0} -->

Let us return to the problem of bounding the matrix mgf of an independent sum. Although the multiplication rule (3.2) is a dead end in the matrix case, the scalar cgf has a related property that submits to generalization. For an independent family $\{ X_{k}\}$ of real random variables, the scalar cgf is additive: where the second identity follows from (3.2) when we take logarithms.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Subadditivity of the Matrix cgf", "weight": 1.0} -->

Our key insight is that Corollary 3.3 offers a completely satisfactory way to extend the addition rule (3.4) for scalar cgfs to the matrix setting. We have the following result.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 3.5", "weight": 1.0} -->

To make the parallel with the addition rule (3.4) clearer, we can rewrite the conclusion of Lemma 3.4. ‣ 3.5. Subadditivity of the Matrix cgf ‣ 3. Tail Bounds via the Laplace Transform Method ‣ User-Friendly Tail Bounds for Sums of Random Matrices") in the form by applying the definition (3.1) of the matrix cgf.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Tail Bounds for Independent Sums", "weight": 1.0} -->

This section contains abstract tail bounds for the sum of independent random matrices. Later, we will specialize these results to some specific situations. We begin with a very general inequality, which is the progenitor of our other results.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 3.8", "weight": 1.0} -->

An alternative expression of the result (3.7) is that In words, the exponent in the tail bound can be written in terms of the perspective transformation of the Fenchel--Legendre conjugate of the function $g$. This inequality parallels the upper estimate in Cramér's classical result for large deviations \[, Thm. 2.2.3\].

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 3.8", "weight": 1.0} -->

It is also worthwhile to state another consequence of Theorem 3.6. ‣ 3.6. Tail Bounds for Independent Sums ‣ 3. Tail Bounds via the Laplace Transform Method ‣ User-Friendly Tail Bounds for Sums of Random Matrices"). This bound is sometimes more useful than Corollary 3.7 because it combines the mgfs of the random matrices together under a single logarithm.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 3.10 (Minimum Eigenvalue)", "weight": 1.0} -->

We can study the minimum eigenvalue of a sum of random s.a. matrices because ${{\lambda_{\min}{({\mathbf{X}})}} = {- {\lambda_{\max}{({- {\mathbf{X}}})}}}}.$ As a result, In §5, we apply this observation to develop lower Chernoff bounds.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 3.11 (Maximum Singular Value)", "weight": 1.0} -->

We can also analyze the maximum singular value of a sum of random rectangular matrices by applying these results to the s.a. dilation (2.10). For a finite sequence $\{{\mathbf{Z}}_{k}\}$ of independent, random, rectangular matrices, we have on account of (2.12) and the property that the dilation is real-linear. This device allows us to extend most of the tail bounds in this paper to rectangular matrices. See §4 for an application to Gaussian and Rademacher series.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Remark 3.12 (Martingales)", "weight": 1.0} -->

It is possible to combine the proofs of Lemma 3.4. ‣ 3.5. Subadditivity of the Matrix cgf ‣ 3. Tail Bounds via the Laplace Transform Method ‣ User-Friendly Tail Bounds for Sums of Random Matrices") and Theorem 3.6. ‣ 3.6. Tail Bounds for Independent Sums ‣ 3. Tail Bounds via the Laplace Transform Method ‣ User-Friendly Tail Bounds for Sums of Random Matrices") to obtain some simple results for matrix martingales. See the demonstration of the matrix Azuma inequality in §7 for an example of this approach. To reach fully detailed results for martingales, one must use a fundamentally different style of argument.

<!-- chunk {"id": "body-0071", "role": "body", "section": "The Ahlswede--Winter Method", "weight": 1.0} -->

Ahlswede and Winter use a different approach to bound the matrix mgf, which exploits the multiplicative bound (3.3) for the trace exponential of a sum of two independent, random, s.a. matrices. The reader may find their argument interesting.

<!-- chunk {"id": "body-0072", "role": "body", "section": "The Ahlswede--Winter Method", "weight": 1.0} -->

Consider a sequence $\{{\mathbf{X}}_{k}:{k = {1,2,\ldots,n}}\}$ of independent, random, s.a. matrices with dimension $d$, and let ${\mathbf{Y}} = {\sum_{k}{\mathbf{X}}_{k}}$. The trace inequality (3.3) implies that Iterating this procedure leads to the relation The bound (3.10) is the key to the Ahlswede--Winter method for producing probability inequalities. As a consequence, their approach generally leads to tail bounds that depend on a scale parameter involving "the sum of eigenvalues." See, for example, the bound (1.3) or the matrix probability inequalities presented in the papers.

<!-- chunk {"id": "body-0073", "role": "body", "section": "The Ahlswede--Winter Method", "weight": 1.0} -->

In contrast, our result on the subadditivity of cumulants, Lemma 3.4. ‣ 3.5. Subadditivity of the Matrix cgf ‣ 3. Tail Bounds via the Laplace Transform Method ‣ User-Friendly Tail Bounds for Sums of Random Matrices"), implies that Probability inequalities developed with (3.11) contain a scale parameter that involves the "eigenvalue of a sum." See, for example, the bound (1.4). The exponent in (3.10) often exceeds the exponent in (3.11) by a factor of $d$, the ambient dimension, which is a serious loss. Section 4.8 describes concrete situations where this discrepancy occurs.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Case Study: Matrix Gaussian Series", "weight": 1.0} -->

A matrix Gaussian series stands among the simplest instances of a sum of independent random matrices. Nevertheless, this example already exhibits several new phenomena that arise when we translate scalar tail bounds to the matrix setting. Consequently, we explore this fundamental case in depth as a way to develop insights about other matrix probability inequalities.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Main Results", "weight": 1.0} -->

We begin with the scalar case. Consider a finite sequence $\{ a_{k}\}$ of real numbers and a finite sequence $\{\gamma_{k}\}$ of independent standard Gaussian variables. We have the probability inequality This result testifies that a Gaussian series with real coefficients satisfies a normal-type tail bound where the variance is controlled by the sum of the squared coefficients. The relation (4.1) follows easily from the scalar Laplace transform method. An alternative proof proceeds using the rotational invariance of a standard normal vector along with basic estimates on the error function.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Main Results", "weight": 1.0} -->

The inequality (4.1) generalizes directly to the noncommutative setting, as do many other scalar tail bounds. The matrix Laplace transform method, Proposition 3.1. ‣ 3.2. The Laplace Transform Method for Matrices ‣ 3. Tail Bounds via the Laplace Transform Method ‣ User-Friendly Tail Bounds for Sums of Random Matrices"), delivers the following result on the tail behavior of a matrix Gaussian series.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Proofs", "weight": 1.0} -->

We continue with a short demonstration of the main results for matrix Gaussian and Rademacher series. The first step is to obtain a semidefinite bound for the mgf of a fixed matrix modulated by a Gaussian variable or a Rademacher variable. This mgf bound essentially appears in Oliveira's work \[, Lem. 2\].

<!-- chunk {"id": "body-0078", "role": "body", "section": "Application: A Gaussian Matrix with Nonuniform Variances", "weight": 1.0} -->

It may not be immediately clear why abstract probability inequalities, such as Theorem 4.1. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices") and Corollary 4.2. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices"), deliver information about interesting random matrices that arise in practice. Let us describe a simple application that speaks to this concern.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Application: A Gaussian Matrix with Nonuniform Variances", "weight": 1.0} -->

Fix a $d_{1} \times d_{2}$ matrix $\mathbf{B}$, and draw a random $d_{1} \times d_{2}$ matrix $\mathbf{\Gamma}$ whose entries are independent standard normal variables. Let $\odot$ denote the componentwise (i.e., Schur or Hadamard) product of matrices. Construct the random matrix $\mathbf{\Gamma} \odot {\mathbf{B}}$, and observe that its $(j,k)$ component is a Gaussian variable with mean zero and variance $\left| b_{jk} \right|^{2}$. We claim that The symbols ${\mathbf{b}}_{j:}$ and ${\mathbf{b}}_{:k}$ represent the $j$th row and $k$th column of the matrix $\mathbf{B}$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Application: A Gaussian Matrix with Nonuniform Variances", "weight": 1.0} -->

An immediate consequence of (4.6) is that the median of the norm satisfies There are nonuniform Gaussian matrices where the estimate (4.7) for the median has the correct order and other examples where the logarithmic factor is parasitic; see §§4.4--4.5 below. The reader may also wish to juxtapose (4.7) with the work of Seginer \[, Thm. 3.1\] and Latała \[, Thm. 1\] although these results are not fully comparable.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Application: A Gaussian Matrix with Nonuniform Variances", "weight": 1.0} -->

To establish (4.6), we first decompose the matrix of interest as a Gaussian series: Next, we must determine the variance parameter. Note that An application of Corollary 4.2. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices") yields the tail bound (4.6).

<!-- chunk {"id": "body-0082", "role": "body", "section": "Controlling the Expectation", "weight": 1.0} -->

A remarkable feature of Theorem 4.1. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices") is that it always allows us to obtain reasonably accurate estimates for the expected norm of the s.a. Gaussian series To establish this point, we first compute upper and lower bounds for the second moment of $\left\| {\mathbf{Y}} \right\|$. Theorem 4.1. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices") yields Jensen's inequality furnishes the lower estimate: The (homogeneous) first and second moment of the norm of a Gaussian series are equivalent up to a universal constant \[, Cor. 3.2\], so we conclude that This argument demonstrates that the matrix variance parameter $\sigma^{2}$ controls the expected norm ${\mathbb{E}}\left\| {\mathbf{Y}} \right\|$ up to a factor that depends very weakly on the dimension.

<!-- chunk {"id": "body-0083", "role": "body", "section": "The Dimensional Factor", "weight": 1.0} -->

In the inequality (4.9), the gap between the upper and lower bounds for ${\mathbb{E}}\left\| {\mathbf{Y}} \right\|$ arises because of the dimensional factor $d$ in the statement (4.4. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices")). This dimensional dependence is a new feature of probability inequalities in the matrix setting. The extra term appears in each of our main results, and it is usually possible to identify a simple case where it is necessary.

<!-- chunk {"id": "body-0084", "role": "body", "section": "The Dimensional Factor", "weight": 1.0} -->

In particular, we cannot remove the factor $d$ from the probability bound in Theorem 4.1. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices"). Observe that the norm of a diagonal Gaussian matrix is typically bounded below: Theorem 4.1. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices") delivers the following tail bound for this series.

<!-- chunk {"id": "body-0085", "role": "body", "section": "The Dimensional Factor", "weight": 1.0} -->

The factor $2d$ ensures that this probability inequality does not become effective until $t \geq \sqrt{2{\log{({2d})}}}$, comme il faut.

<!-- chunk {"id": "body-0086", "role": "body", "section": "The Dimensional Factor", "weight": 1.0} -->

We can also identify situations where the dimensional term produces an overestimate of the expected norm. For instance, consider a $d$-dimensional matrix drawn from the unnormalized Gaussian orthogonal ensemble (GOE): The literature contains a sharp bound for the expected norm of this matrix: The result (4.10) follows from ideas of Gordon elaborated in \[, Thm. 2.11\]. Meanwhile, integrating the tail bound (4.4. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices")) from Theorem 4.1. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices") yields the weaker result The estimate (4.11) is too large by a factor of about $\sqrt{\log d}$, which is the worst possible discrepancy in view of (4.9).

<!-- chunk {"id": "body-0087", "role": "body", "section": "Remark 4.4 (Effective Dimension)", "weight": 1.0} -->

Let us stress that the *nominal* dimension of the matrices does not play a role in Theorem 4.1. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices"). If the ranges of the matrices ${\mathbf{A}}_{1},{\mathbf{A}}_{2},\ldots$ are contained within a fixed $r$-dimensional subspace, we can replace the ambient dimension $d$ with the effective dimension $r$. A similar remark applies to our other results.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Comparison with Concentration Inequalities", "weight": 1.0} -->

It is fruitful to think about Theorem 4.1. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices") as a statement that the matrix Gaussian series (4.8) typically falls near its expectation *as a random matrix* when we measure the size of deviations using the operator norm: In contrast, the classical concentration inequality \[, Thm. 1.7.6\] concerns the variation of *the norm* about its mean value: where the scale for deviations depends on the *weak variance* parameter It can be shown \[, Cor. 3.2\] that the bound (4.13) is asymptotically sharp as $t\rightarrow\infty$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Comparison with Concentration Inequalities", "weight": 1.0} -->

Let us elaborate on the relationship between the matrix variance $\sigma^{2}$ defined in (4.2. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices")) and the weak variance $\sigma_{\ast}^{2}$ appearing in (4.14). First, note that Equality holds in (4.15) when, for example, the family $\{{\mathbf{A}}_{k}\}$ commutes. We can also establish a reverse inequality. where $\{\mathbf{e}_{j}:{j = {1,\ldots,d}}\}$ is the standard basis for ${\mathbb{R}}^{d}$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Comparison with Concentration Inequalities", "weight": 1.0} -->

In the worst case^22^2A worst-case example occurs with high probability when the sequence $\{{\mathbf{A}}_{k}:{k = {1,\ldots,d}}\}$ consists of independent matrices drawn from the $d$-dimensional GOE, but the proof seems to be complicated., the bound (4.16) has roughly the correct order.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Comparison with Concentration Inequalities", "weight": 1.0} -->

In summary, the matrix concentration inequality (4.12) always leads to a good estimate for the expected norm ${\mathbb{E}}\left\| {\mathbf{Y}} \right\|$. Nevertheless, the presence of the parameter $\sigma^{2}$ in the tail bound can lead to a significant overestimate of the probability that $\left\| {\mathbf{Y}} \right\|$ is large. On the other hand, the classical inequality (4.13) contains no information about the mean, but it always produces a sharp large-deviation bound. Therefore, the two results complement each other well.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Noncommutative Moment Inequalities", "weight": 1.0} -->

The matrix Laplace transform bound, Proposition 3.1. ‣ 3.2. The Laplace Transform Method for Matrices ‣ 3. Tail Bounds via the Laplace Transform Method ‣ User-Friendly Tail Bounds for Sums of Random Matrices") demonstrates that we can bound tail probabilities for the norm of a random series by controlling the matrix mgf. In certain special cases, it is possible to bound the matrix mgf using noncommutative (nc) moment inequalities. Let us describe how to establish Theorem 4.1. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices") in this fashion. This material is unrelated to the main development, so the reader may skip it with impunity.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Noncommutative Moment Inequalities", "weight": 1.0} -->

The nc Khintchine inequality provides an estimate for the expectation of the $({2p})$th moment of the Schatten $2p$-norm of a matrix Gaussian series. The most elementary formulation of this result states that Buchholz \[, Thm. 5\] has shown that the optimal constant in (4.17) satisfies The bound (4.17) also holds with the same constant when we replace $\{\gamma_{k}\}$ by a sequence of independent Rademacher variables \[, Thm. 5\].

<!-- chunk {"id": "body-0094", "role": "body", "section": "Noncommutative Moment Inequalities", "weight": 1.0} -->

The family (4.17) of inequalities allows us to develop a short proof of the tail bound for matrix Gaussian and Rademacher series.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Alternative Proof of Theorem 4.1. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices\")", "weight": 1.0} -->

Proposition 3.1. ‣ 3.2. The Laplace Transform Method for Matrices ‣ 3. Tail Bounds via the Laplace Transform Method ‣ User-Friendly Tail Bounds for Sums of Random Matrices") yields We may use (4.17) to bound the Taylor series for the matrix mgf term by term: Substitute (4.7) into (4.18), and select $\theta = {t/\sigma^{2}}$ to complete the minimization. ∎ We may regard the mgf bound (4.7) as an "exponential generating function" for the family of nc Khintchine inequalities (4.17), but---unfortunately---the nc Khintchine inequalities *do not* follow as a consequence of this mgf bound. Recall that Lieb's result, Theorem 3.2. ‣ 3.4. A Concave Trace Function ‣ 3. Tail Bounds via the Laplace Transform Method ‣ User-Friendly Tail Bounds for Sums of Random Matrices"), also delivers a proof of the inequality (4.7).

<!-- chunk {"id": "body-0096", "role": "body", "section": "Alternative Proof of Theorem 4.1. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices\")", "weight": 1.0} -->

This observation suggests that it might be possible to use Lieb's theorem to prove the nc Khintchine inequalities (4.17). We regard this as a tantalizing open question.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Comparison with the Ahlswede--Winter Bound", "weight": 1.0} -->

In §3.7, we describe how Ahlswede and Winter go about bounding the matrix mgf \[, App.\]. It is natural to ask how inequalities developed using their approach compare with the results in this paper.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Comparison with the Ahlswede--Winter Bound", "weight": 1.0} -->

Gaussian series provide an excellent illustration of the discrepancy between the two techniques. In this case, the Ahlswede--Winter method yields the probability inequality The estimate (4.20) should be compared with our bound (4.4. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices")). The Ahlswede--Winter variance parameter $\sigma_{AW}^{2}$ always dominates the matrix variance parameter (4.2. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices")) because The two variance parameters rarely coincide, and the best reverse inequality is This worst-case behavior is typical. For instance, consider the two Gaussian matrices presented in §4.5. The Ahlswede--Winter tail bound (4.20) provides essentially no information about the norm of either matrix.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Remark 4.5 (Moment Inequalities)", "weight": 1.0} -->

There is an alternative approach to establishing the result (4.20) that parallels the method presented in §4.7. We simply bound the Taylor series of the matrix mgf term by term using an appropriate family of moment inequalities: These estimates follow from a result of Tomczak--Jaegermann \[, Thm. 3.1\] for Rademacher series together with the central limit theorem.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Sums of Random Positive-Semidefinite Matrices", "weight": 1.0} -->

The classical Chernoff bounds concern the sum of independent, nonnegative, and uniformly bounded random variables. In sympathy, matrix Chernoff bounds describe the extreme eigenvalues of a sum of independent, psd random matrices whose maximum eigenvalues are subject to a uniform bound. These probability inequalities demonstrate that the upper and lower tails of the sum exhibit binomial-type behavior.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Sums of Random Positive-Semidefinite Matrices", "weight": 1.0} -->

Our first result parallels the strongest versions of the scalar Chernoff inequality for the proportion of successes in a sequence of independent (but not identical) Bernoulli trials \[, Exer. 7\].

<!-- chunk {"id": "body-0102", "role": "body", "section": "Remark 5.3 (Related Inequalities)", "weight": 1.0} -->

The following standard simplification of Corollary 5.2. ‣ 5. Sums of Random Positive-Semidefinite Matrices ‣ User-Friendly Tail Bounds for Sums of Random Matrices") is useful.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Remark 5.3 (Related Inequalities)", "weight": 1.0} -->

These inequalities manifest that the minimum eigenvalue has normal-type behavior and the maximum eigenvalue exhibits Poisson-type decay.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Remark 5.4 (Applications)", "weight": 1.0} -->

Matrix Chernoff inequalities are very effective for studying random matrices with independent columns. Consider a rectangular random matrix where $\{{\mathbf{z}}_{k}\}$ is a family of independent random vectors in ${\mathbb{C}}^{m}$. The norm of $\mathbf{Z}$ satisfies Similarly, the minimum singular value $s_{m}$ of the matrix satisfies In each case, the summands are stochastically independent and psd, so the matrix Chernoff bounds apply. See for a problem where this method applies.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Remark 5.5 (Expectations)", "weight": 1.0} -->

Corollary 5.2. ‣ 5. Sums of Random Positive-Semidefinite Matrices ‣ User-Friendly Tail Bounds for Sums of Random Matrices") produces accurate estimates for the expectation of the maximum eigenvalue: The lower bound is Jensen's inequality; the upper bound follows from a messy---but standard---calculation. Observe that the dimensional dependence vanishes when the mean $\mu_{\max}$ is sufficiently large in comparison with the upper bound $R$!

<!-- chunk {"id": "body-0106", "role": "body", "section": "Remark 5.6 (Dimensional Factor)", "weight": 1.0} -->

The factor $d$ in the Chernoff bounds cannot be omitted because of the coupon collector's problem \[, §3.6\]. Consider a $d$-dimensional random matrix $\mathbf{X}$ with the distribution If $\{{\mathbf{X}}_{k}\}$ is a sequence of independent random matrices with the same distribution as $\mathbf{X}$, then The dimensional factor in the lower Chernoff bound reflects this fact. The same example shows that the upper Chernoff bound must also exhibit a dimensional dependence. We have extracted this idea from \[, Sec. 3.5\].

<!-- chunk {"id": "body-0107", "role": "body", "section": "Remark 5.7 (Previous Work)", "weight": 1.0} -->

Theorem 5.1. ‣ 5. Sums of Random Positive-Semidefinite Matrices ‣ User-Friendly Tail Bounds for Sums of Random Matrices") is a considerable strengthening of the matrix Chernoff bound established by Ahlswede and Winter \[, Thm. 19\]. Their proof requires the extra assumption that the summands are identically distributed, in which case their result matches Theorem 5.1. ‣ 5. Sums of Random Positive-Semidefinite Matrices ‣ User-Friendly Tail Bounds for Sums of Random Matrices").

<!-- chunk {"id": "body-0108", "role": "body", "section": "Proofs", "weight": 1.0} -->

To establish the matrix Chernoff inequalities, we commence with a semidefinite bound for the matrix mgf of a random psd contraction.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Remark 5.9 (Alternative Proof)", "weight": 1.0} -->

Corollary 5.2. ‣ 5. Sums of Random Positive-Semidefinite Matrices ‣ User-Friendly Tail Bounds for Sums of Random Matrices") can also be established directly using Corollary 3.7 instead of Corollary 3.9. In this case, we use the mgf bound which follows instantly from Lemma 5.8. ‣ 5.1. Proofs ‣ 5. Sums of Random Positive-Semidefinite Matrices ‣ User-Friendly Tail Bounds for Sums of Random Matrices") and the semidefinite relation (2.3). The remaining details mirror the arguments here.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Matrix Bennett and Bernstein Inequalities", "weight": 1.0} -->

In the scalar setting, Bennett and Bernstein inequalities describe the upper tail of a sum of independent, zero-mean random variables that are either bounded or subexponential. In the matrix case, the analogous results concern a sum of zero-mean random matrices.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Matrix Bennett and Bernstein Inequalities", "weight": 1.0} -->

Our first result describes the case where the maximum eigenvalue of each summand satisfies a uniform bound.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Remark 6.3 (Rectangular Versions)", "weight": 1.0} -->

The matrix Bernstein inequalities admit rectangular variants. For example, consider a sequence $\{{\mathbf{Z}}_{k}\}$ of $d_{1} \times d_{2}$ random matrices that satisfy the assumptions We can apply Theorem 6.1. ‣ 6. Matrix Bennett and Bernstein Inequalities ‣ User-Friendly Tail Bounds for Sums of Random Matrices") to the s.a. dilation (2.10) of the sum of these random matrices to see that the probability where $d:={d_{1} + d_{2}}$ and where the variance parameter This argument leads to Theorem 1.6. ‣ 1.2.4. Main Results for Rectangular Matrices ‣ 1.2. Index of Inequalities ‣ 1. Introduction ‣ User-Friendly Tail Bounds for Sums of Random Matrices"), stated in the introduction. There is also a rectangular extension of Theorem 6.2. ‣ 6. Matrix Bennett and Bernstein Inequalities ‣ User-Friendly Tail Bounds for Sums of Random Matrices"), but the hypotheses are messier.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Remark 6.4 (Related Inequalities)", "weight": 1.0} -->

There are too many variants of the scalar Bernstein inequality to present the matrix generalization of each one. Let us just mention a few of the possibilities.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Remark 6.4 (Related Inequalities)", "weight": 1.0} -->

Theorem 6.2. ‣ 6. Matrix Bennett and Bernstein Inequalities ‣ User-Friendly Tail Bounds for Sums of Random Matrices") can be sharpened using an idea of Rio that appears in \[, Sec. 2.2.3\].

<!-- chunk {"id": "body-0115", "role": "body", "section": "Remark 6.4 (Related Inequalities)", "weight": 1.0} -->

When the random matrices exhibit moment growth of the form ${{\mathbb{E}}{({\mathbf{X}}_{k}^{p})}} \preccurlyeq {R^{p - 2}{\mathbf{A}}_{k}^{2}}$, we recover the Poissonian tail behavior captured in Theorem 6.1. ‣ 6. Matrix Bennett and Bernstein Inequalities ‣ User-Friendly Tail Bounds for Sums of Random Matrices")(i).

<!-- chunk {"id": "body-0116", "role": "body", "section": "Remark 6.5 (Expectations)", "weight": 1.0} -->

We can use the matrix Bernstein inequality to bound the mean of the maximum eigenvalue of the random sum. For example, assume that the hypotheses of Theorem 6.1. ‣ 6. Matrix Bennett and Bernstein Inequalities ‣ User-Friendly Tail Bounds for Sums of Random Matrices") or 6.2. ‣ 6. Matrix Bennett and Bernstein Inequalities ‣ User-Friendly Tail Bounds for Sums of Random Matrices") are in force. Then The upper bound follows by integrating Theorem 6.1. ‣ 6. Matrix Bennett and Bernstein Inequalities ‣ User-Friendly Tail Bounds for Sums of Random Matrices")(ii) or Theorem 6.2. ‣ 6. Matrix Bennett and Bernstein Inequalities ‣ User-Friendly Tail Bounds for Sums of Random Matrices")(i). Lower bounds seem to require additional assumptions.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Remark 6.6 (Previous Work)", "weight": 1.0} -->

Oliveira's results are quite similar to the bounds presented here. In particular, Oliveira's martingale inequality \[, Thm. 1.2\] implies a weaker version of Theorem 6.1. ‣ 6. Matrix Bennett and Bernstein Inequalities ‣ User-Friendly Tail Bounds for Sums of Random Matrices")(ii). The main result has a similar flavor.

<!-- chunk {"id": "body-0118", "role": "body", "section": "The Matrix Hoeffding, Azuma, and McDiarmid Inequalities", "weight": 1.0} -->

In this section, we prove some simple martingale deviation bounds by modifying the approach that we have used to study sums of independent random matrices. More sophisticated martingale results require additional machinery.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Matrix Martingales", "weight": 1.0} -->

We begin with the required definitions. Let $(\Omega,\mathcal{F},{\mathbb{P}})$ be a master probability space. Consider a filtration $\{\mathcal{F}_{k}\}$ contained in the master sigma algebra: Given such a filtration, we define the conditional expectation ${\mathbb{E}}_{k}{\lbrack \cdot \rbrack}:={\mathbb{E}}{\lbrack \cdot |\mathcal{F}_{k}\rbrack}.$ A sequence $\{{\mathbf{X}}_{k}\}$ of random matrices is *adapted* to the filtration when each ${\mathbf{X}}_{k}$ is measurable with respect to $\mathcal{F}_{k}$. Loosely speaking, an adapted sequence is one where the present depends only upon the past.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Matrix Martingales", "weight": 1.0} -->

An adapted sequence $\{{\mathbf{Y}}_{k}\}$ of s.a. matrices is called a *matrix martingale* when We obtain a scalar martingale if we track any fixed coordinate of a matrix martingale $\{{\mathbf{Y}}_{k}\}$. Given a matrix martingale $\{{\mathbf{Y}}_{k}\}$, we can construct the *difference sequence* Note that the difference sequence is conditionally zero mean: ${{\mathbb{E}}_{k - 1}{\mathbf{X}}_{k}} = \mathbf{0}$.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Main Results", "weight": 1.0} -->

The scalar version of Azuma's inequality states that a scalar martingale exhibits normal concentration about its mean value, and the scale for deviations is controlled by the total maximum squared range of the difference sequence. Here is a matrix extension.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Remark 7.3 (Rectangular Version)", "weight": 1.0} -->

The matrix Azuma inequality has a rectangular version, which we obtain by applying Theorem 7.1. ‣ 7.2. Main Results ‣ 7. The Matrix Hoeffding, Azuma, and McDiarmid Inequalities ‣ User-Friendly Tail Bounds for Sums of Random Matrices") to the s.a. dilation (2.10) of the adapted sequence.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Remark 7.4 (Related Inequalities)", "weight": 1.0} -->

There are several situations where the constant 1/8 in the bound (7.2. ‣ 7.2. Main Results ‣ 7. The Matrix Hoeffding, Azuma, and McDiarmid Inequalities ‣ User-Friendly Tail Bounds for Sums of Random Matrices")) can be improved to 1/2. One case occurs when each summand ${\mathbf{X}}_{k}$ is conditionally symmetric; see Remark 7.8. Another example requires the assumption that ${\mathbf{X}}_{k}$ commutes almost surely with ${\mathbf{A}}_{k}$, which allows us to generalize the classical proof \[, Lem. 2.6\] of the Azuma inequality to the matrix setting.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Remark 7.4 (Related Inequalities)", "weight": 1.0} -->

If we place the additional assumption that the summands are independent, Theorem 7.1. ‣ 7.2. Main Results ‣ 7. The Matrix Hoeffding, Azuma, and McDiarmid Inequalities ‣ User-Friendly Tail Bounds for Sums of Random Matrices") gives a matrix extension of one of Hoeffding's inequalities, which we have presented as Theorem 1.3. ‣ 1.2.3. Main Results for Self-Adjoint Matrices ‣ 1.2. Index of Inequalities ‣ 1. Introduction ‣ User-Friendly Tail Bounds for Sums of Random Matrices") in the introduction.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Remark 7.4 (Related Inequalities)", "weight": 1.0} -->

In the scalar setting, one of the most useful corollaries of Azuma's inequality is the bounded differences inequality of McDiarmid \[, Thm. 3.1\]. This result states that a function of independent random variables exhibits normal concentration about its mean, and the variance depends on how much a change in a single variable can alter the value of the function. A version of the bounded differences inequality holds in the matrix setting.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Remark 7.8", "weight": 1.0} -->

Suppose that the sequence $\{{\mathbf{X}}_{k}\}$ is conditionally symmetric: When we execute the proof of Theorem 7.1. ‣ 7.2. Main Results ‣ 7. The Matrix Hoeffding, Azuma, and McDiarmid Inequalities ‣ User-Friendly Tail Bounds for Sums of Random Matrices") under this assumption, we can symmetrize each term in the sum without suffering an extra factor of two. For example, where $\varepsilon$ is independent from $\mathcal{F}_{n}$. The rest of the proof remains the same, but the analog of the bound (7.2. ‣ 7.2. Main Results ‣ 7. The Matrix Hoeffding, Azuma, and McDiarmid Inequalities ‣ User-Friendly Tail Bounds for Sums of Random Matrices")) has a constant of 1/2 instead of 1/8 in the exponent.
