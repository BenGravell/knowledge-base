## Abstract

Low-rank matrix approximations, such as the truncated singular value decomposition and the rank-revealing QR decomposition, play a central role in data analysis and scientific computing. This work surveys and extends recent research which demonstrates that *randomization* offers a powerful tool for performing low-rank matrix approximation. These techniques exploit modern computational architectures more fully than classical methods and open the possibility of dealing with truly massive data sets.

This paper presents a modular framework for constructing randomized algorithms that compute partial matrix decompositions. These methods use random sampling to identify a subspace that captures most of the action of a matrix. The input matrix is then compressed---either explicitly or implicitly---to this subspace, and the reduced matrix is manipulated deterministically to obtain the desired low-rank factorization. In many cases, this approach beats its classical competitors in terms of accuracy, speed, and robustness. These claims are supported by extensive numerical experiments and a detailed error analysis.

The specific benefits of randomized techniques depend on the computational environment. Consider the model problem of finding the $k$ dominant components of the singular value decomposition of an $m \times n$ matrix. (i) For a dense input matrix, randomized algorithms require $O{({mn{\log{(k)}}})}$ floating-point operations (flops) in contrast with $O{({mnk})}$ for classical algorithms. (ii) For a sparse input matrix, the flop count matches classical Krylov subspace methods, but the randomized approach is more robust and can easily be reorganized to exploit multi-processor architectures. (iii) For a matrix that is too large to fit in fast memory, the randomized techniques require only a constant number of passes over the data, as opposed to $O{(k)}$ passes for classical algorithms. In fact, it is sometimes possible to perform matrix approximation with a *single pass* over the data.

### keywords

Dimension reduction, eigenvalue decomposition, interpolative decomposition, Johnson--Lindenstrauss lemma, matrix approximation, parallel algorithm, pass-efficient algorithm, principal component analysis, randomized algorithm, random matrix, rank-revealing QR factorization, singular value decomposition, streaming algorithm.

### AMS

\[MSC2010\] Primary: 65F30. Secondary: 68W20, 60B20.

## Overview

On a well-known list of the "Top 10 Algorithms" that have influenced the practice of science and engineering during the 20th century, we find an entry that is not really an algorithm: the *idea* of using matrix factorizations to accomplish basic tasks in numerical linear algebra. In the accompanying article, Stewart explains that > The underlying principle of the decompositional approach to matrix computation is that it is not the business of the matrix algorithmicists to solve particular problems but to construct computational platforms from which a variety of problems can be solved.

Stewart goes on to argue that this point of view has had many fruitful consequences, including the development of robust software for performing these factorizations in a highly accurate and provably correct manner.

The decompositional approach to matrix computation remains fundamental, but developments in computer hardware and the emergence of new applications in the information sciences have rendered the classical algorithms for this task inadequate in many situations: A salient feature of modern applications, especially in data mining, is that the matrices are stupendously big. Classical algorithms are not always well adapted to solving the type of large-scale problems that now arise.

In the information sciences, it is common that data are missing or inaccurate. Classical algorithms are designed to produce highly accurate matrix decompositions, but it seems profligate to spend extra computational resources when the imprecision of the data inherently limits the resolution of the output.

Data transfer now plays a major role in the computational cost of numerical algorithms. Techniques that require few passes over the data may be substantially faster in practice, even if they require as many---or more---floating-point operations.

As the structure of computer processors continues to evolve, it becomes increasingly important for numerical algorithms to adapt to a range of novel architectures, such as graphics processing units.

The purpose of this paper is make the case that *randomized* algorithms provide a powerful tool for constructing approximate matrix factorizations. These techniques are simple and effective, sometimes impressively so. Compared with standard deterministic algorithms, the randomized methods are often faster and---perhaps surprisingly---more robust. Furthermore, they can produce factorizations that are accurate to any specified tolerance above machine precision, which allows the user to trade accuracy for speed if desired. We present numerical evidence that these algorithms succeed for real computational problems.

In short, our goal is to demonstrate how randomized methods interact with classical techniques to yield effective, modern algorithms supported by detailed theoretical guarantees. We have made a special effort to help practitioners identify situations where randomized techniques may outperform established methods.

Throughout this article, we provide detailed citations to previous work on randomized techniques for computing low-rank approximations. The primary sources that inform our presentation include.

### Remark 1.1

Our experience suggests that many practitioners of scientific computing view randomized algorithms as a desperate and final resort. Let us address this concern immediately. Classical Monte Carlo methods are highly sensitive to the random number generator and typically produce output with low and uncertain accuracy. In contrast, the algorithms discussed herein are relatively insensitive to the quality of randomness and produce highly accurate results. The probability of failure is a user-specified parameter that can be rendered negligible (say, less than $10^{- 15}$) with a nominal impact on the computational resources required.

### Approximation by low-rank matrices

The roster of standard matrix decompositions includes the pivoted QR factorization, the eigenvalue decomposition, and the singular value decomposition (SVD), all of which expose the (numerical) range of a matrix. Truncated versions of these factorizations are often used to express a *low-rank approximation* of a given matrix: The inner dimension $k$ is sometimes called the *numerical rank* of the matrix. When the numerical rank is much smaller than either dimension $m$ or $n$, a factorization such as allows the matrix to be stored inexpensively and to be multiplied rapidly with vectors or other matrices. The factorizations can also be used for data interpretation or to solve computational problems, such as least squares.

Matrices with low numerical rank appear in a wide variety of scientific applications. We list only a few: A basic method in statistics and data mining is to compute the directions of maximal variance in vector-valued data by performing *principal component analysis* (PCA) on the data matrix. PCA is nothing other than a low-rank matrix approximation \[71, §14.5\].

Another standard technique in data analysis is to perform low-dimensional embedding of data under the assumption that there are fewer degrees of freedom than the ambient dimension would suggest. In many cases, the method reduces to computing a partial SVD of a matrix derived from the data. See \[71, §§14.8--14.9\] or.

The problem of estimating parameters from measured data via least-squares fitting often leads to very large systems of linear equations that are close to linearly dependent. Effective techniques for factoring the coefficient matrix lead to efficient techniques for solving the least-squares problem,.

Many fast numerical algorithms for solving PDEs and for rapidly evaluating potential fields such as the fast multipole method and $\mathcal{H}$-matrices, rely on low-rank approximations of continuum operators.

Models of multiscale physical phenomena often involve PDEs with rapidly oscillating coefficients. Techniques for *model reduction* or *coarse graining* in such environments are often based on the observation that the linear transform that maps the input data to the requested output data can be approximated by an operator of low rank.

### Matrix approximation framework

The task of computing a low-rank approximation to a given matrix can be split naturally into two computational stages. The first is to construct a low-dimensional subspace that captures the action of the matrix. The second is to restrict the matrix to the subspace and then compute a standard factorization (QR, SVD, etc.) of the reduced matrix. To be slightly more formal, we subdivide the computation as follows.

Stage A: Compute an approximate basis for the range of the input matrix $\mathbf{A}$. In other words, we require a matrix $\mathbf{Q}$ for which We would like the basis matrix $\mathbf{Q}$ to contain as few columns as possible, but it is even more important to have an accurate approximation of the input matrix.

Stage B: Given a matrix $\mathbf{Q}$ that satisfies, we use $\mathbf{Q}$ to help compute a standard factorization (QR, SVD, etc.) of $\mathbf{A}$.

The task in Stage A can be executed very efficiently with random sampling methods, and these methods are the primary subject of this work. In the next subsection, we offer an overview of these ideas. The body of the paper provides details of the algorithms (§4) and a theoretical analysis of their performance (§§8--11).

Stage B can be completed with well-established deterministic methods. Section 3.3.3 contains an introduction to these techniques, and §5 shows how we apply them to produce low-rank factorizations.

At this point in the development, it may not be clear why the output from Stage A facilitates our job in Stage B. Let us illustrate by describing how to obtain an approximate SVD of the input matrix $\mathbf{A}$ given a matrix $\mathbf{Q}$ that satisfies. More precisely, we wish to compute matrices $\mathbf{U}$ and $\mathbf{V}$ with orthonormal columns and a nonnegative, diagonal matrix $\mathbf{\Sigma}$ such that ${\mathbf{A}} \approx {{\mathbf{U}}\mathbf{\Sigma}{\mathbf{V}}^{\ast}}$. This goal is achieved after three simple steps: Form ${\mathbf{B}} = {{\mathbf{Q}}^{\ast}{\mathbf{A}}}$, which yields the low-rank factorization ${\mathbf{A}} \approx {{\mathbf{Q}}{\mathbf{B}}}$.

Compute an SVD of the small matrix: ${\mathbf{B}} = {\overset{\sim}{\mathbf{U}}\mathbf{\Sigma}{\mathbf{V}}^{\ast}}$.

Set ${\mathbf{U}} = {{\mathbf{Q}}\overset{\sim}{\mathbf{U}}}$.

When $\mathbf{Q}$ has few columns, this procedure is efficient because we can easily construct the reduced matrix $\mathbf{B}$ and rapidly compute its SVD. In practice, we can often avoid forming $\mathbf{B}$ explicitly by means of subtler techniques. In some cases, it is not even necessary to revisit the input matrix $\mathbf{A}$ during Stage B. This observation allows us to develop *single-pass algorithms*, which look at each entry of $\mathbf{A}$ only once.

Similar manipulations readily yield other standard factorizations, such as the pivoted QR factorization, the eigenvalue decomposition, etc.

### Randomized algorithms

This paper describes a class of randomized algorithms for completing Stage A of the matrix approximation framework set forth in §1.2. We begin with some details about the approximation problem these algorithms target (§1.3.1). Afterward, we motivate the random sampling technique with a heuristic explanation (§1.3.2) that leads to a prototype algorithm (§1.3.3).

### Problem formulations

The basic challenge in producing low-rank matrix approximations is a primitive question that we call the *fixed-precision approximation problem*. Suppose we are given a matrix $\mathbf{A}$ and a positive error tolerance $\varepsilon$. We seek a matrix $\mathbf{Q}$ with $k = {k{(\varepsilon)}}$ orthonormal columns such that where $\left. \parallel \cdot \parallel \right.$ denotes the $\ell_{2}$ operator norm. The range of $\mathbf{Q}$ is a $k$-dimensional subspace that captures most of the action of $\mathbf{A}$, and we would like $k$ to be as small as possible.

The singular value decomposition furnishes an optimal answer to the fixed-precision problem. Let $\sigma_{j}$ denote the $j$th largest singular value of $\mathbf{A}$. For each $j \geq 0$, One way to construct a minimizer is to choose ${\mathbf{X}} = {{\mathbf{Q}}{\mathbf{Q}}^{\ast}{\mathbf{A}}}$, where the columns of $\mathbf{Q}$ are $k$ dominant left singular vectors of $\mathbf{A}$. Consequently, the minimal rank $k$ where holds equals the number of singular values of $\mathbf{A}$ that exceed the tolerance $\varepsilon$.

To simplify the development of algorithms, it is convenient to assume that the desired rank $k$ is specified in advance. We call the resulting problem the *fixed-rank approximation problem*. Given a matrix $\mathbf{A}$, a target rank $k$, and an oversampling parameter $p$, we seek to construct a matrix $\mathbf{Q}$ with $k + p$ orthonormal columns such that Although there exists a minimizer $\mathbf{Q}$ that solves the fixed rank problem for $p = 0$, the opportunity to use a small number of additional columns provides a flexibility that is crucial for the effectiveness of the computational methods we discuss.

We will demonstrate that algorithms for the fixed-rank problem can be adapted to solve the fixed-precision problem. The connection is based on the observation that we can build the basis matrix $\mathbf{Q}$ incrementally and, at any point in the computation, we can inexpensively estimate the residual error $\left\| {{\mathbf{A}} - {{\mathbf{Q}}{\mathbf{Q}}^{\ast}{\mathbf{A}}}} \right\|$. Refer to §4.4 for free ‣ 4 Stage A: Randomized schemes for approximating the range ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") for the details of this reduction.

### Intuition

To understand how randomness helps us solve the fixed-rank problem, it is helpful to consider some motivating examples.

First, suppose that we seek a basis for the range of a matrix $\mathbf{A}$ with exact rank $k$. Draw a random vector $\mathbf{ω}$, and form the product ${\mathbf{y}} = {{\mathbf{A}}{\mathbf{ω}}}$. For now, the precise distribution of the random vector is unimportant; just think of $\mathbf{y}$ as a random sample from the range of $\mathbf{A}$. Let us repeat this sampling process $k$ times: Owing to the randomness, the set $\{{\mathbf{ω}}^{(i)}:{i = {1,2,\ldots,k}}\}$ of random vectors is likely to be in general linear position. In particular, the random vectors form a linearly independent set and no linear combination falls in the null space of $\mathbf{A}$. As a result, the set $\{{\mathbf{y}}^{(i)}:{i = {1,2,\ldots,k}}\}$ of sample vectors is also linearly independent, so it spans the range of $\mathbf{A}$. Therefore, to produce an orthonormal basis for the range of $\mathbf{A}$, we just need to orthonormalize the sample vectors.

Now, imagine that ${\mathbf{A}} = {{\mathbf{B}} + {\mathbf{E}}}$ where $\mathbf{B}$ is a rank-$k$ matrix containing the information we seek and $\mathbf{E}$ is a small perturbation. Our priority is to obtain a basis that covers as much of the range of $\mathbf{B}$ as possible, rather than to minimize the number of basis vectors. Therefore, we fix a small number $p$, and we generate $k + p$ samples The perturbation $\mathbf{E}$ shifts the direction of each sample vector outside the range of $\mathbf{B}$, which can prevent the span of $\{{\mathbf{y}}^{(i)}:{i = {1,2,\ldots,k}}\}$ from covering the entire range of $\mathbf{B}$. In contrast, the enriched set $\{{\mathbf{y}}^{(i)}:{i = {1,2,\ldots,{k + p}}}\}$ of samples has a much better chance of spanning the required subspace.

Just how many extra samples do we need? Remarkably, for certain types of random sampling schemes, the failure probability decreases superexponentially with the oversampling parameter $p$; see. As a practical matter, setting $p = 5$ or $p = 10$ often gives superb results. This observation is one of the principal facts supporting the randomized approach to numerical linear algebra.

### A prototype algorithm

The intuitive approach of §1.3.2 can be applied to general matrices. Omitting computational details for now, we formalize the procedure in the figure labeled Proto-Algorithm.

Proto-Algorithm: Solving the Fixed-Rank Problem Given an m × n matrix A, a target rank k, and an oversampling parameter p, this procedure computes an m × (k + p) matrix Q whose columns are orthonormal and whose range approximates the range of A. 1 Draw a random n × (k + p) test matrix Ω. 2 Form the matrix product Y = A Ω. 3 Construct a matrix Q whose columns form an orthonormal basis for the range of Y.

This simple algorithm is by no means new. It is essentially the first step of a subspace iteration with a random initial subspace \[61, §7.3.2\]. The novelty comes from the additional observation that the initial subspace should have a slightly higher dimension than the invariant subspace we are trying to approximate. With this revision, it is often the case that *no further iteration is required* to obtain a high-quality solution to. We believe this idea can be traced to.

In order to invoke the proto-algorithm with confidence, we must address several practical and theoretical issues: What random matrix $\mathbf{\Omega}$ should we use? How much oversampling do we need?

The matrix $\mathbf{Y}$ is likely to be ill-conditioned. How do we orthonormalize its columns to form the matrix $\mathbf{Q}$?

What are the computational costs?

How can we solve the fixed-precision problem when the numerical rank of the matrix is not known in advance?

How can we use the basis $\mathbf{Q}$ to compute other matrix factorizations?

Does the randomized method work for problems of practical interest? How does its speed/accuracy/robustness compare with standard techniques?

What error bounds can we expect? With what probability?

The next few sections provide a summary of the answers to these questions. We describe several problem regimes where the proto-algorithm can be implemented efficiently, and we present a theorem that describes the performance of the most important instantiation. Finally, we elaborate on how these ideas can be applied to approximate the truncated SVD of a large data matrix. The rest of the paper contains a more exhaustive treatment---including pseudocode, numerical experiments, and a detailed theory.

### A comparison between randomized and traditional techniques

To select an appropriate computational method for finding a low-rank approximation to a matrix, the practitioner must take into account the properties of the matrix. Is it dense or sparse? Does it fit in fast memory or is it stored out of core? Does the singular spectrum decay quickly or slowly? The behavior of a numerical linear algebra algorithm may depend on all these factors. To facilitate a comparison between classical and randomized techniques, we summarize their relative performance in each of three representative environments. Section 6 contains a more in-depth treatment.

We focus on the task of computing an approximate SVD of an $m \times n$ matrix $\mathbf{A}$ with numerical rank $k$. For randomized schemes, Stage A generally dominates the cost of Stage B in our matrix approximation framework (§1.2). Within Stage A, the computational bottleneck is usually the matrix--matrix product ${\mathbf{A}}\mathbf{\Omega}$ in Step 2 of the proto-algorithm (§1.3.3). The power of randomized algorithms stems from the fact that we can reorganize this matrix multiplication for maximum efficiency in a variety of computational architectures.

### A general dense matrix that fits in fast memory

A standard deterministic technique for computing an approximate SVD is to perform a rank-revealing QR factorization of the matrix, and then to manipulate the factors to obtain the final decomposition. The cost of this approach is typically $O{({kmn})}$ floating-point operations, or *flops*, although these methods require slightly longer running times in rare cases.

In contrast, randomized schemes can produce an approximate SVD using only $O{({{mn{\log{(k)}}} + {{({m + n})}k^{2}}})}$ flops. The gain in asymptotic complexity is achieved by using a random matrix $\mathbf{\Omega}$ that has some internal structure, which allows us to evaluate the product ${\mathbf{A}}\mathbf{\Omega}$ rapidly. For example, randomizing and subsampling the discrete Fourier transform works well. Sections 4.6 and 11 contain more information on this approach.

### A matrix for which matrix--vector products can be evaluated rapidly

When the matrix $\mathbf{A}$ is sparse or structured, we may be able to apply it rapidly to a vector. In this case, the classical prescription for computing a partial SVD is to invoke a Krylov subspace method, such as the Lanczos or Arnoldi algorithm. It is difficult to summarize the computational cost of these methods because their performance depends heavily on properties of the input matrix and on the amount of effort spent to stabilize the algorithm. (Inherently, the Lanczos and Arnoldi methods are numerically unstable.) For the same reasons, the error analysis of such schemes is unsatisfactory in many important environments.

At the risk of being overly simplistic, we claim that the typical cost of a Krylov method for approximating the $k$ leading singular vectors of the input matrix is proportional to ${kT_{mult}} + {{({m + n})}k^{2}}$, where $T_{mult}$ denotes the cost of a matrix--vector multiplication with the input matrix and the constant of proportionality is small. We can also apply randomized methods using a Gaussian test matrix $\mathbf{\Omega}$ to complete the factorization at the same cost, $O{({{kT_{mult}} + {{({m + n})}k^{2}}})}$ flops.

With a given budget of floating-point operations, Krylov methods sometimes deliver a more accurate approximation than randomized algorithms. Nevertheless, the methods described in this survey have at least two powerful advantages over Krylov methods. First, the randomized schemes are inherently stable, and they come with very strong performance guarantees that do not depend on subtle spectral properties of the input matrix. Second, the matrix--vector multiplies required to form ${\mathbf{A}}\mathbf{\Omega}$ can be performed *in parallel*. This fact allows us to restructure the calculations to take full advantage of the computational platform, which can lead to dramatic accelerations in practice, especially for parallel and distributed machines.

A more detailed comparison or randomized schemes and Krylov subspace methods is given in §6.2.

### A general dense matrix stored in slow memory or streamed

When the input matrix is too large to fit in core memory, the cost of transferring the matrix from slow memory typically dominates the cost of performing the arithmetic. The standard techniques for low-rank approximation described in §1.4.1 require $O{(k)}$ passes over the matrix, which can be prohibitively expensive.

In contrast, the proto-algorithm of §1.3.3 requires only one pass over the data to produce the approximate basis $\mathbf{Q}$ for Stage A of the approximation framework. This straightforward approach, unfortunately, is not accurate enough for matrices whose singular spectrum decays slowly, but we can address this problem using very few (say, $2$ to $4$) additional passes over the data. See §1.6 or §4.5 for more discussion.

Typically, Stage B uses one additional pass over the matrix to construct the approximate SVD. With slight modifications, however, the two-stage randomized scheme can be revised so that it only makes a single pass over the data. Refer to §5.5 for information.

### Performance analysis

A principal goal of this paper is to provide a detailed analysis of the performance of the proto-algorithm described in §1.3.3. This investigation produces precise error bounds, expressed in terms of the singular values of the input matrix. Furthermore, we determine how several choices of the random matrix $\mathbf{\Omega}$ impact the behavior of the algorithm.

Let us offer a taste of this theory. The following theorem describes the average-case behavior of the proto-algorithm with a Gaussian test matrix, assuming we perform the computation in exact arithmetic. This result is a simplified version of Theorem 19. ‣ 10.2 Average-case analysis of Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions").

### Theorem 1

Suppose that $\mathbf{A}$ is a real $m \times n$ matrix. Select a target rank $k \geq 2$ and an oversampling parameter $p \geq 2$, where ${k + p} \leq {\min{\{ m,n\}}}$. Execute the proto-algorithm with a standard Gaussian test matrix to obtain an $m \times {({k + p})}$ matrix $\mathbf{Q}$ with orthonormal columns. Then where $\mathbb{E}$ denotes expectation with respect to the random test matrix and $\sigma_{k + 1}$ is the $({k + 1})$th singular value of $\mathbf{A}$.

We recall that the term $\sigma_{k + 1}$ appearing in is the smallest possible error achievable with any basis matrix $\mathbf{Q}$. The theorem asserts that, on average, the algorithm produces a basis whose error lies within a small polynomial factor of the theoretical minimum. Moreover, the error bound in the randomized algorithm is slightly sharper than comparable bounds for deterministic techniques based on rank-revealing QR algorithms.

The reader might be worried about whether the expectation provides a useful account of the approximation error. Fear not: the actual outcome of the algorithm is almost always very close to the typical outcome because of measure concentration effects. As we discuss in §10.3, the probability that the error satisfies is at least $1 - {6 \cdot p^{- p}}$ under very mild assumptions on $p$. This fact justifies the use of an oversampling term as small as $p = 5$. This simplified estimate is very similar to the major results.

The theory developed in this paper provides much more detailed information about the performance of the proto-algorithm.

When the singular values of $\mathbf{A}$ decay slightly, the error $\left\| {{\mathbf{A}} - {{\mathbf{Q}}{\mathbf{Q}}^{\ast}{\mathbf{A}}}} \right\|$ does not depend on the dimensions of the matrix (§§10.2--10.3).

We can reduce the size of the bracket in the error bound by combining the proto-algorithm with a power iteration (§10.4). For an example, see §1.6 below.

For the structured random matrices we mentioned in §1.4.1, related error bounds are in force (§11).

We can obtain inexpensive a posteriori error estimates to verify the quality of the approximation (§4.3).

### Example: Randomized SVD

We conclude this introduction with a short discussion of how these ideas allow us to perform an approximate SVD of a large data matrix, which is a compelling application of randomized matrix approximation.

The two-stage randomized method offers a natural approach to SVD computations. Unfortunately, the simplest version of this scheme is inadequate in many applications because the singular spectrum of the input matrix may decay slowly. To address this difficulty, we incorporate $q$ steps of a power iteration, where $q = 1$ or $q = 2$ usually suffices in practice. The complete scheme appears in the box labeled Prototype for Randomized SVD. For most applications, it is important to incorporate additional refinements, as we discuss in §§4--5.

Prototype for Randomized SVD Given an m × n matrix A, a target number k of singular vectors, and an exponent q (say q = 1 or q = 2), this procedure computes an approximate rank-2 k factorization U Σ V*, where U and V are orthonormal, and Σ is nonnegative and diagonal. Stage A: 1 Generate an n × 2 k Gaussian test matrix Ω. 2 Form Y = (A A*)q A Ω by multiplying alternately with A and A*. 3 Construct a matrix Q whose columns form an orthonormal basis for the range of Y. Stage B: 4 Form B = Q* A. 5 Compute an SVD of the small matrix: ${\mathbf{B}} = {\overset{\sim}{\mathbf{U}}\mathbf{\Sigma}{\mathbf{V}}^{\ast}}$. 6 Set ${\mathbf{U}} = {{\mathbf{Q}}\overset{\sim}{\mathbf{U}}}$. Note: The computation of Y in Step 2 is vulnerable to round-off errors. When high accuracy is required, we must incorporate an orthonormalization step between each application of A and A*; see Algorithm LABEL:alg:subspaceiteration.

The Randomized SVD procedure requires only $2{({q + 1})}$ passes over the matrix, so it is efficient even for matrices stored out-of-core. The flop count satisfies where $T_{mult}$ is the flop count of a matrix--vector multiply with $\mathbf{A}$ or ${\mathbf{A}}^{\ast}$. We have the following theorem on the performance of this method in exact arithmetic, which is a consequence of Corollary 23. ‣ 10.4 Analysis of the power scheme ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions").

### Theorem 2

Suppose that $\mathbf{A}$ is a real $m \times n$ matrix. Select an exponent $q$ and a target number $k$ of singular vectors, where $2 \leq k \leq {0.5{\min{\{ m,n\}}}}$. Execute the Randomized SVD algorithm to obtain a rank-$2k$ factorization $\mathbf{U}\mathbf{\Sigma}\mathbf{V}^{\ast}$. Then where $\mathbb{E}$ denotes expectation with respect to the random test matrix and $\sigma_{k + 1}$ is the $({k + 1})$th singular value of $\mathbf{A}$.

This result is new. Observe that the bracket in is essentially the same as the bracket in the basic error bound. We find that the power iteration drives the leading constant to one exponentially fast as the power $q$ increases. The rank-$k$ approximation of $\mathbf{A}$ can never achieve an error smaller than $\sigma_{k + 1}$, so the randomized procedure computes $2k$ approximate singular vectors that capture as much of the matrix as the first $k$ actual singular vectors.

In practice, we can truncate the approximate SVD, retaining only the first $k$ singular values and vectors. Equivalently, we replace the diagonal factor $\mathbf{\Sigma}$ by the matrix $\mathbf{\Sigma}_{(k)}$ formed by zeroing out all but the largest $k$ entries of $\mathbf{\Sigma}$. For this truncated SVD, we have the error bound In words, we pay no more than an additive term $\sigma_{k + 1}$ when we perform the truncation step. Our numerical experience suggests that the error bound is pessimistic. See Remark 5.1 and §9.4 for some discussion of truncation.

### Outline of paper

The paper is organized into three parts: an introduction (§§1--3), a description of the algorithms (§§4--7), and a theoretical performance analysis (§§8--11). The two latter parts commence with a short internal outline. Each part is more or less self-contained, and after a brief review of our notation in §§3.1--3.2, the reader can proceed to either the algorithms or the theory part.

## Related work and historical context

Randomness has occasionally surfaced in the numerical linear algebra literature; in particular, it is quite standard to initialize iterative algorithms for constructing invariant subspaces with a randomly chosen point. Nevertheless, we believe that sophisticated ideas from random matrix theory have not been incorporated into classical matrix factorization algorithms until very recently. We can trace this development to earlier work in computer science and---especially---to probabilistic methods in geometric analysis. This section presents an overview of the relevant work. We begin with a survey of randomized methods for matrix approximation; then we attempt to trace some of the ideas backward to their sources.

### Randomized matrix approximation

Matrices of low numerical rank contain little information relative to their apparent dimension owing to the linear dependency in their columns (or rows). As a result, it is reasonable to expect that these matrices can be approximated with far fewer degrees of freedom. A less obvious fact is that randomized schemes can be used to produce these approximations efficiently.

Several types of approximation techniques build on this idea. These methods all follow the same basic pattern: Preprocess the matrix, usually to calculate sampling probabilities.

Take random samples from the matrix, where the term *sample* refers generically to a linear function of the matrix.

Postprocess the samples to compute a final approximation, typically with classical techniques from numerical linear algebra. This step may require another look at the matrix.

We continue with a description of the most common approximation schemes.

### Sparsification

The simplest approach to matrix approximation is the method of *sparsification* or the related technique of *quantization*. The goal of sparsification is to replace the matrix by a surrogate that contains far fewer nonzero entries. Quantization produces an approximation whose components are drawn from a (small) discrete set of values. These methods can be used to limit storage requirements or to accelerate computations by reducing the cost of matrix--vector and matrix--matrix multiplies \[94, Ch. 6\]. The manuscript describes applications in optimization.

Sparsification typically involves very simple elementwise calculations. Each entry in the approximation is drawn independently at random from a distribution determined from the corresponding entry of the input matrix. The expected value of the random approximation equals the original matrix, but the distribution is designed so that a typical realization is much sparser.

The first method of this form was devised by Achlioptas and McSherry, who built on earlier work on graph sparsification due to Karger. Arora--Hazan--Kale presented a different sampling method . See for some recent work on sparsification.

### Column selection methods

A second approach to matrix approximation is based on the idea that a small set of columns describes most of the action of a numerically low-rank matrix. Indeed, classical existential results demonstrate that every $m \times n$ matrix $\mathbf{A}$ contains a $k$-column submatrix $\mathbf{C}$ for which where $k$ is a parameter, the dagger $\dagger$ denotes the pseudoinverse, and ${\mathbf{A}}_{(k)}$ is a best rank-$k$ approximation of $\mathbf{A}$. It is $\mathsf{N}\mathsf{P}$-hard to perform column selection by optimizing natural objective functions, such as the condition number of the submatrix. Nevertheless, there are efficient deterministic algorithms, such as the rank-revealing QR method of, that can nearly achieve the error bound.

There is a class of randomized algorithms that approach the fixed-rank approximation problem using this intuition. These methods first compute a sampling probability for each column, either using the squared Euclidean norms of the columns or their *leverage scores*. (Leverage scores reflect the relative importance of the columns to the action of the matrix; they can be calculated easily from the dominant $k$ right singular vectors of the matrix.) Columns are then selected randomly according to this distribution. Afterward, a postprocessing step is invoked to produce a more refined approximation of the matrix.

We believe that the earliest method of this form appeared in a 1998 paper of Frieze--Kannan--Vempala. This work was refined substantially in the papers. The basic algorithm samples columns from a distribution related to the squared $\ell_{2}$ norms of the columns. This sampling step produces a small column submatrix whose range is aligned with the range of the input matrix. The final approximation is obtained from a truncated SVD of the submatrix. Given a target rank $k$ and a parameter $\varepsilon > 0$, this approach samples $\ell = {\ell{(k,\varepsilon)}}$ columns of the matrix to produce a rank-$k$ approximation $\mathbf{B}$ that satisfies where $\left. \parallel \cdot \parallel{}_{F} \right.$ denotes the Frobenius norm. We note that the algorithm of requires only a constant number of passes over the data.

Rudelson and Vershynin later showed that the same type of column sampling method also yields spectral-norm error bounds. The techniques in their paper have been very influential; their work has found other applications in randomized regression, sparse approximation, and compressive sampling.

Deshpande et al. demonstrated that the error in the column sampling approach can be improved by iteration and adaptive volume sampling. They showed that it is possible to produce a rank-$k$ matrix $\mathbf{B}$ that satisfies using a $k$-pass algorithm. Around the same time, Har-Peled independently developed a recursive algorithm that offers the same approximation guarantees. Very recently, Desphande and Rademacher have improved the running time of volume-based sampling methods.

Drineas et al. and Boutsidis et al. have also developed randomized algorithms for the *column subset selection problem*, which requests a column submatrix $\mathbf{C}$ that achieves a bound of the form. Via the methods of Rudelson and Vershynin, they showed that sampling columns according to their leverage scores is likely to produce the required submatrix. Subsequent work showed that postprocessing the sampled columns with a rank-revealing QR algorithm can reduce the number of output columns required. The argument in explicitly decouples the linear algebraic part of the analysis from the random matrix theory. The theoretical analysis in the present work involves a very similar technique.

### Approximation by dimension reduction

A third approach to matrix approximation is based on the concept of *dimension reduction*. Since the rows of a low-rank matrix are linearly dependent, they can be embedded into a low-dimensional space without altering their geometric properties substantially. A random linear map provides an efficient, nonadaptive way to perform this embedding. (Column sampling can also be viewed as an adaptive form of dimension reduction.)

The proto-algorithm we set forth in §1.3.3 is simply a dual description of the dimension reduction approach: collecting random samples from the column space of the matrix is equivalent to reducing the dimension of the rows. No precomputation is required to obtain the sampling distribution, but the sample itself takes some work to collect. Afterward, we orthogonalize the samples as preparation for constructing various matrix approximations.

We believe that the idea of using dimension reduction for algorithmic matrix approximation first appeared in a 1998 paper of Papadimitriou et al., who described an application to latent semantic indexing (LSI). They suggested projecting the input matrix onto a random subspace and compressing the original matrix to (a subspace of) the range of the projected matrix. They established error bounds that echo the result of Frieze et al.. Although the Euclidean column selection method is a more computationally efficient way to obtain this type of error bound, dimension reduction has other advantages, e.g., in terms of accuracy.

Sarlós argued in that the computational costs of dimension reduction can be reduced substantially by means of the structured random maps proposed by Ailon--Chazelle. Sarlós used these ideas to develop efficient randomized algorithms for least-squares problems; he also studied approximate matrix multiplication and low-rank matrix approximation. The recent paper analyzes a very similar matrix approximation algorithm using Rudelson and Vershynin's methods.

The initial work of Sarlós on structured dimension reduction did not immediately yield algorithms for low-rank matrix approximation that were superior to classical techniques. Woolfe et al. showed how to obtain an improvement in asymptotic computational cost, and they applied these techniques to problems in scientific computing. Related work includes.

Martinsson--Rokhlin--Tygert have studied dimension reduction using a Gaussian transform matrix, and they demonstrated that this approach performs much better than earlier analyses had suggested. Their work highlights the importance of oversampling, and their error bounds are very similar to the estimate we presented in the introduction. They also demonstrated that dimension reduction can be used to compute an interpolative decomposition of the input matrix, which is essentially equivalent to performing column subset selection.

Rokhlin--Szlam--Tygert have shown that combining dimension reduction with a power iteration is an effective way to improve its performance. These ideas lead to very efficient randomized methods for large-scale PCA. An efficient, numerically stable version of the power iteration is discussed in §4.5, as well as. Related ideas appear in a paper of Roweis.

Very recently, Clarkson and Woodruff have developed one-pass algorithms for performing low-rank matrix approximation, and they have established lower bounds which prove that many of their algorithms have optimal or near-optimal resource guarantees, modulo constants.

### Approximation by submatrices

The matrix approximation literature contains a subgenre that discusses methods for building an approximation from a submatrix and computed coefficient matrices. For example, we can construct an approximation using a subcollection of columns (the interpolative decomposition), a subcollection of rows and a subcollection of columns (the CUR decomposition), or a square submatrix (the matrix skeleton). This type of decomposition was developed and studied in several papers, including. For data analysis applications, see the recent paper.

A number of works develop randomized algorithms for this class of matrix approximations. Drineas et al. have developed techniques for computing CUR decompositions, which express ${\mathbf{A}} \approx {{\mathbf{C}}{\mathbf{U}}{\mathbf{R}}}$, where $\mathbf{C}$ and $\mathbf{R}$ denote small column and row submatrices of $\mathbf{A}$ and where $\mathbf{U}$ is a small linkage matrix. These methods identify columns (rows) that approximate the range (corange) of the matrix; the linkage matrix is then computed by solving a small least-squares problem. A randomized algorithm for CUR approximation with controlled absolute error appears ; a relative error algorithm appears . We also mention a paper on computing a closely related factorization called the *compact matrix decomposition*.

It is also possible to produce interpolative decompositions and matrix skeletons using randomized methods, as discussed in and §5.2 of the present work.

### Other numerical problems

The literature contains a variety of other randomized algorithms for solving standard problems in and around numerical linear algebra. We list some of the basic references.: Randomized column selection methods can be used to produce CUR-type decompositions of higher-order tensors.: Column selection and dimension reduction techniques can be used to accelerate the multiplication of rank-deficient matrices. See also.

Overdetermined linear systems.: The randomized Kaczmarz algorithm is a linearly convergent iterative method that can be used to solve overdetermined linear systems.

Overdetermined least squares.: Fast dimension-reduction maps can sometimes accelerate the solution of overdetermined least-squares problems.

Nonnegative least squares.: Fast dimension reduction maps can be used to reduce the size of nonnegative least-squares problems.

Preconditioned least squares.: Randomized matrix approximations can be used to precondition conjugate gradient to solve least-squares problems.

Other regression problems.: Randomized algorithms for $\ell_{1}$ regression are described. Regression in $\ell_{p}$ for $p \in {\lbrack 1,\infty)}$ has also been considered.: The Fermat--Weber facility location problem can be viewed as matrix approximation with respect to a different discrepancy measure. Randomized algorithms for this type of problem appear.

### Compressive sampling

Although randomized matrix approximation and compressive sampling are based on some common intuitions, it is facile to consider either one as a subspecies of the other. We offer a short overview of the field of compressive sampling---especially the part connected with matrices---so we can highlight some of the differences.

The theory of compressive sampling starts with the observation that many types of vector-space data are *compressible*. That is, the data are approximated well using a short linear combination of basis functions drawn from a fixed collection. For example, natural images are well approximated in a wavelet basis; numerically low-rank matrices are well approximated as a sum of rank-one matrices. The idea behind compressive sampling is that suitably chosen random samples from this type of compressible object carry a large amount of information. Furthermore, it is possible to reconstruct the compressible object from a small set of these random samples, often by solving a convex optimization problem. The initial discovery works of Candès--Romberg--Tao and Donoho were written in 2004.

The earliest work in compressive sampling focused on vector-valued data; soon after, researchers began to study compressive sampling for matrices. In 2007, Recht--Fazel--Parillo demonstrated that it is possible to reconstruct a rank-deficient matrix from Gaussian measurements. More recently, Candès--Recht and Candès--Tao considered the problem of completing a low-rank matrix from a random sample of its entries.

The usual goals of compressive sampling are (i) to design a method for collecting informative, nonadaptive data about a compressible object and (ii) to reconstruct a compressible object given some measured data. In both cases, there is an implicit assumption that we have limited---if any---access to the underlying data.

In the problem of matrix approximation, we typically have a complete representation of the matrix at our disposal. The point is to compute a simpler representation as efficiently as possible under some operational constraints. In particular, we would like to perform as little computation as we can, but we are usually allowed to revisit the input matrix. Because of the different focus, randomized matrix approximation algorithms require fewer random samples from the matrix and use fewer computational resources than compressive sampling reconstruction algorithms.

### Origins

This section attempts to identify some of the major threads of research that ultimately led to the development of the randomized techniques we discuss in this paper.

### Random embeddings

The field of random embeddings is a major precursor to randomized matrix approximation. In a celebrated 1984 paper, Johnson and Lindenstrauss showed that the pairwise distances among a collection of $N$ points in a Euclidean space are approximately maintained when the points are mapped randomly to a Euclidean space of dimension $O{({\log N})}$. In other words, random embeddings preserve Euclidean geometry. Shortly afterward, Bourgain showed that appropriate random low-dimensional embeddings preserve the geometry of point sets in finite-dimensional $\ell_{1}$ spaces.

These observations suggest that we might be able to solve some computational problems of a geometric nature more efficiently by translating them into a lower-dimensional space and solving them there. This idea was cultivated by the theoretical computer science community beginning in the late 1980s, with research flowering in the late 1990s. In particular, nearest-neighbor search can benefit from dimension-reduction techniques. The papers were apparently the first to apply this approach to linear algebra.

Around the same time, researchers became interested in simplifying the form of dimension reduction maps and improving the computational cost of applying the map. Several researchers developed refined results on the performance of a Gaussian matrix as a linear dimension reduction map. Achlioptas demonstrated that discrete random matrices would serve nearly as well. In 2006, Ailon and Chazelle proposed the *fast Johnson--Lindenstrauss transform*, which combines the speed of the FFT with the favorable embedding properties of a Gaussian matrix. Subsequent refinements appear . Sarlós then imported these techniques to study several problems in numerical linear algebra, which has led to some of the fastest algorithms currently available.

### Data streams

Muthukrishnan argues that a distinguishing feature of modern data is the manner in which it is *presented* to us. The sheer volume of information and the speed at which it must be processed tax our ability to *transmit* the data elsewhere, to *compute* complicated functions on the data, or to *store* a substantial part of the data \[100, §3\]. As a result, computer scientists have started to develop algorithms that can address familiar computational problems under these novel constraints. The data stream phenomenon is one of the primary justifications cited by for developing pass-efficient methods for numerical linear algebra problems, and it is also the focus of the recent treatment.

One of the methods for dealing with massive data sets is to maintain *sketches*, which are small summaries that allow functions of interest to be calculated. In the simplest case, a sketch is simply a random projection of the data, but it might be a more sophisticated object \[100, §5.1\]. The idea of sketching can be traced to the work of Alon et al..

### Numerical linear algebra

Classically, the field of numerical linear algebra has focused on developing deterministic algorithms that produce highly accurate matrix approximations with provable guarantees. Nevertheless, randomized techniques have appeared in several environments.

One of the original examples is the use of random models for arithmetical errors, which was pioneered by von Neumann and Goldstine. Their papers stand among the first works to study the properties of random matrices. The earliest numerical linear algebra algorithm that depends essentially on randomized techniques is probably Dixon's method for estimating norms and condition numbers.

Another situation where randomness commonly arises is the initialization of iterative methods for computing invariant subspaces. For example, most numerical linear algebra texts advocate random selection of the starting vector for the power method because it ensures that the vector has a nonzero component in the direction of a dominant eigenvector. Woźniakowski and coauthors have analyzed the performance of the power method and the Lanczos iteration given a random starting vector.

Among other interesting applications of randomness, we mention the work by Parker and Pierce, which applies a randomized FFT to eliminate pivoting in Gaussian elimination, work by Demmel et al. who have studied randomization in connection with the stability of fast methods for linear algebra, and work by Le and Parker utilizing randomized methods for stabilizing fast linear algebraic computations based on recursive algorithms, such as Strassen's matrix multiplication.

### Scientific computing

One of the first algorithmic applications of randomness is the method of Monte Carlo integration introduced by Von Neumann and Ulam, and its extensions, such as the Metropolis algorithm for simulations in statistical physics. (See for an introduction.) The most basic technique is to estimate an integral by sampling $m$ points from the measure and computing an empirical mean of the integrand evaluated at the sample locations: where $X_{i}$ are independent and identically distributed according to the probability measure $\mu$. The law of large numbers (usually) ensures that this approach produces the correct result in the limit as $m\rightarrow\infty$. Unfortunately, the approximation error typically has a standard deviation of $m^{- {1/2}}$, and the method provides no certificate of success.

The disappointing computational profile of Monte Carlo integration seems to have inspired a distaste for randomized approaches within the scientific computing community. Fortunately, there are many other types of randomized algorithms---such as the ones in this paper---that do not suffer from the same shortcomings.

### Geometric functional analysis

There is one more character that plays a central role in our story: the probabilistic method in geometric analysis. Many of the algorithms and proof techniques ultimately come from work in this beautiful but recondite corner of mathematics.

Dvoretsky's theorem states (roughly) that every infinite-dimensional Banach space contains an $n$-dimensional subspace whose geometry is essentially the same as an $n$-dimensional Hilbert space, where $n$ is an arbitrary natural number. In 1971, V. D. Milman developed a striking proof of this result by showing that a *random* $n$-dimensional subspace of an $N$-dimensional Banach space has this property with exceedingly high probability, provided that $N$ is large enough. Milman's article debuted the *concentration of measure phenomenon*, which is a geometric interpretation of the classical idea that regular functions of independent random variables rarely deviate far from their mean. This work opened a new era in geometric analysis where the probabilistic method became a basic instrument.

Another prominent example of measure concentration is Kashin's computation of the Gel'fand widths of the $\ell_{1}$ ball, subsequently refined . This work showed that a *random* $({N - n})$-dimensional projection of the $N$-dimensional $\ell_{1}$ ball has an astonishingly small Euclidean diameter: approximately $\sqrt{{({1 + {\log{({N/n})}}})}/n}$. In contrast, a nonzero projection of the $\ell_{2}$ ball always has Euclidean diameter one. This basic geometric fact undergirds recent developments in compressive sampling.

We have already described a third class of examples: the randomized embeddings of Johnson--Lindenstrauss and of Bourgain.

Finally, we mention Maurey's technique of empirical approximation. The original work was unpublished; one of the earliest applications appears in \[24, §1\]. Although Maurey's idea has not received as much press as the examples above, it can lead to simple and efficient algorithms for sparse approximation. For some examples in machine learning, consider The importance of random constructions in the geometric analysis community has led to the development of powerful techniques for studying random matrices. Classical random matrix theory focuses on a detailed asymptotic analysis of the spectral properties of special classes of random matrices. In contrast, geometric analysts know methods for determining the approximate behavior of rather complicated finite-dimensional random matrices. See for a fairly current survey article. We also mention the works of Rudelson and Rudelson--Vershynin, which describe powerful tools for studying random matrices drawn from certain discrete distributions. Their papers are rooted deeply in the field of geometric functional analysis, but they reach out toward computational applications.

## Linear algebraic preliminaries

This section summarizes the background we need for the detailed description of randomized algorithms in §§4--6 and the analysis in §§8--11. We introduce notation in §3.1, describe some standard matrix decompositions in §3.2, and briefly review standard techniques for computing matrix factorizations in §3.3.

### Basic definitions

The standard Hermitian geometry for ${\mathbb{C}}^{n}$ is induced by the inner product The associated norm is We usually measure the magnitude of a matrix $\mathbf{A}$ with the operator norm which is often referred to as the *spectral norm*. The Frobenius norm is given by The conjugate transpose, or *adjoint*, of a matrix $\mathbf{A}$ is denoted ${\mathbf{A}}^{\ast}$. The important identities hold for each matrix $\mathbf{A}$.

We say that a matrix $\mathbf{U}$ is *orthonormal* if its columns form an orthonormal set with respect to the Hermitian inner product. An orthonormal matrix $\mathbf{U}$ preserves geometry in the sense that $\left\| {{\mathbf{U}}{\mathbf{x}}} \right\| = \left\| {\mathbf{x}} \right\|$ for every vector $\mathbf{x}$. A *unitary* matrix is a square orthonormal matrix, and an *orthogonal* matrix is a real unitary matrix. Unitary matrices satisfy the relations ${{\mathbf{U}}{\mathbf{U}}^{\ast}} = {{\mathbf{U}}^{\ast}{\mathbf{U}}} = \mathbf{I}$. Both the operator norm and the Frobenius norm are *unitarily invariant*, which means that for every matrix $\mathbf{A}$ and all orthonormal matrices $\mathbf{U}$ and $\mathbf{V}$ We use the notation of to denote submatrices. If $\mathbf{A}$ is a matrix with entries $a_{ij}$, and if $I = {\lbrack i_{1},i_{2},\ldots,i_{p}\rbrack}$ and $J = {\lbrack j_{1},j_{2},\ldots,j_{q}\rbrack}$ are two index vectors, then the associated $p \times q$ submatrix is expressed as For column- and row-submatrices, we use the standard abbreviations

### Standard matrix factorizations

This section defines three basic matrix decompositions. Methods for computing them are described in §3.3.

### The pivoted QR factorization

Each $m \times n$ matrix $\mathbf{A}$ of rank $k$ admits a decomposition where $\mathbf{Q}$ is an $m \times k$ orthonormal matrix, and $\mathbf{R}$ is a $k \times n$ *weakly upper-triangular* matrix. That is, there exists a permutation $J$ of the numbers $\{ 1,\, 2,\ldots,n\}$ such that ${\mathbf{R}}_{(:,J)}$ is upper triangular. Moreover, the diagonal entries of ${\mathbf{R}}_{(:,J)}$ are weakly decreasing. See \[61, §5.4.1\] for details.

### The singular value decomposition (SVD)

Each $m \times n$ matrix $\mathbf{A}$ of rank $k$ admits a factorization where $\mathbf{U}$ is an $m \times k$ orthonormal matrix, $\mathbf{V}$ is an $n \times k$ orthonormal matrix, and $\mathbf{\Sigma}$ is a $k \times k$ nonnegative, diagonal matrix The numbers $\sigma_{j}$ are called the *singular values* of $\mathbf{A}$. They are arranged in weakly decreasing order: The columns of $\mathbf{U}$ and $\mathbf{V}$ are called *left singular vectors* and *right singular vectors*, respectively.

Singular values are connected with the approximability of matrices. For each $j$, the number $\sigma_{j + 1}$ equals the spectral-norm discrepancy between $\mathbf{A}$ and an optimal rank-$j$ approximation. That is, In particular, $\sigma_{1} = \left\| {\mathbf{A}} \right\|$. See \[61, §2.5.3 and §5.4.5\] for additional details.

### The interpolative decomposition (ID)

Our final factorization identifies a collection of $k$ columns from a rank-$k$ matrix $\mathbf{A}$ that span the range of $\mathbf{A}$. To be precise, we can compute an index set $J = {\lbrack j_{1},\ldots,j_{k}\rbrack}$ such that where $\mathbf{X}$ is a $k \times n$ matrix that satisfies ${\mathbf{X}}_{(:,J)} = \mathbf{I}_{k}$. Furthermore, no entry of $\mathbf{X}$ has magnitude larger than two. In other words, this decomposition expresses each column of $\mathbf{A}$ using a linear combination of $k$ fixed columns with *bounded* coefficients. Stable and efficient algorithms for computing the ID appear in the papers.

It is also possible to compute a two-sided ID where $J'$ is an index set identifying $k$ of the rows of $\mathbf{A}$, and $\mathbf{W}$ is an $m \times k$ matrix that satisfies ${\mathbf{W}}_{(J',:)} = \mathbf{I}_{k}$ and whose entries are all bounded by two.

### Remark 3.1

There always exists an ID where the entries in the factor $\mathbf{X}$ have magnitude bounded by one. Known proofs of this fact are constructive, e.g., \[103, Lem. 3.3\], but they require us to find a collection of $k$ columns that has "maximum volume." It is NP-hard to identify a subset of columns with this type of extremal property. We find it remarkable that ID computations are possible as soon as the bound on $\mathbf{X}$ is relaxed.

### Techniques for computing standard factorizations

This section discusses some established deterministic techniques for computing the factorizations presented in §3.2. The material on pivoted QR and SVD can be located in any major text on numerical linear algebra, such as. References for the ID include.

### Computing the full decomposition

It is possible to compute the full QR factorization or the full SVD of an $m \times n$ matrix to double-precision accuracy with $O{({mn{\min{\{ m,n\}}}})}$ flops. Techniques for computing the SVD are iterative by necessity, but they converge so fast that we can treat them as finite for practical purposes.

### Computing partial decompositions

Suppose that an $m \times n$ matrix has numerical rank $k$, where $k$ is substantially smaller than $m$ and $n$. In this case, it is possible to produce a structured low-rank decomposition that approximates the matrix well. Sections 4 and 5 describe a set of randomized techniques for obtaining these partial decompositions. This section briefly reviews the classical techniques, which also play a role in developing randomized methods.

To compute a partial QR decomposition, the classical device is the Businger--Golub algorithm, which performs successive orthogonalization with pivoting on the columns of the matrix. The procedure halts when the Frobenius norm of the remaining columns is less than a computational tolerance $\varepsilon$. Letting $\ell$ denote the number of steps required, the process results in a partial factorization where $\mathbf{Q}$ is an $m \times \ell$ orthonormal matrix, $\mathbf{R}$ is a $\ell \times n$ weakly upper-triangular matrix, and $\mathbf{E}$ is a residual that satisfies $\left\| {\mathbf{E}} \right\|_{F} \leq \varepsilon$. The computational cost is $O{({\ellmn})}$, and the number $\ell$ of steps taken is typically close to the minimal rank $k$ for which precision $\varepsilon$ (in the Frobenius norm) is achievable. The Businger--Golub algorithm can in principle significantly overpredict the rank, but in practice this problem is very rare provided that orthonormality is maintained scrupulously.

Subsequent research has led to strong rank-revealing QR algorithms that succeed for all matrices. For example, the Gu--Eisenstat algorithm (setting their parameter $f = 2$) produces an QR decomposition of the form, where Recall that $\sigma_{k + 1}$ is the minimal error possible in a rank-$k$ approximation. The cost of the Gu--Eisenstat algorithm is typically $O{({kmn})}$, but it can be slightly higher in rare cases. The algorithm can also be used to obtain an approximate ID.

To compute an approximate SVD of a general $m \times n$ matrix, the most straightforward technique is to compute the full SVD and truncate it. This procedure is stable and accurate, but it requires $O{({mn{\min{\{ m,n\}}}})}$ flops. A more efficient approach is to compute a partial QR factorization and postprocess the factors to obtain a partial SVD using the methods described below in §3.3.3. This scheme takes only $O{({kmn})}$ flops. Krylov subspace methods can also compute partial SVDs at a comparable cost of $O{({kmn})}$, but they are less robust.

Note that all the techniques described in this section require extensive random access to the matrix, and they can be very slow when the matrix is stored out-of-core.

### Converting from one partial factorization to another

Suppose that we have obtained a partial decomposition of a matrix $\mathbf{A}$ by some means: where $\mathbf{B}$ and $\mathbf{C}$ have rank $k$. Given this information, we can efficiently compute any of the basic factorizations.

We construct a partial QR factorization using the following three steps: Compute a QR factorization of $\mathbf{C}$ so that ${\mathbf{C}} = {{\mathbf{Q}}_{1}{\mathbf{R}}_{1}}$.

Form the product ${\mathbf{D}} = {{\mathbf{R}}_{1}{\mathbf{B}}}$, and compute a QR factorization: ${\mathbf{D}} = {{\mathbf{Q}}_{2}{\mathbf{R}}}$.

Form the product ${\mathbf{Q}} = {{\mathbf{Q}}_{1}{\mathbf{Q}}_{2}}$.

The result is an orthonormal matrix $\mathbf{Q}$ and a weakly upper-triangular matrix $\mathbf{R}$ such that $\left\| {{\mathbf{A}} - {{\mathbf{Q}}{\mathbf{R}}}} \right\| \leq \varepsilon$.

An analogous technique yields a partial SVD: Compute a QR factorization of $\mathbf{C}$ so that ${\mathbf{C}} = {{\mathbf{Q}}_{1}{\mathbf{R}}_{1}}$.

Form the product ${\mathbf{D}} = {{\mathbf{R}}_{1}{\mathbf{B}}}$, and compute an SVD: ${\mathbf{D}} = {{\mathbf{U}}_{2}\mathbf{\Sigma}{\mathbf{V}}^{\ast}}$.

Form the product ${\mathbf{U}} = {{\mathbf{Q}}_{1}{\mathbf{U}}_{2}}$.

The result is a diagonal matrix $\mathbf{\Sigma}$ and orthonormal matrices $\mathbf{U}$ and $\mathbf{V}$ such that $\left\| {{\mathbf{A}} - {{\mathbf{U}}\mathbf{\Sigma}{\mathbf{V}}^{\ast}}} \right\| \leq \varepsilon$.

Converting $\mathbf{B}$ and $\mathbf{C}$ into a partial ID is a one-step process: Compute $J$ and $\mathbf{X}$ such that ${\mathbf{B}} = {{\mathbf{B}}_{(:,J)}{\mathbf{X}}}$.

Then ${\mathbf{A}} \approx {{\mathbf{A}}_{(:,J)}{\mathbf{X}}}$, but the approximation error may deteriorate from the initial estimate. For example, if we compute the ID using the Gu--Eisenstat algorithm with the parameter $f = 2$, then the error ${\parallel{{\mathbf{A}} - {{\mathbf{A}}_{(:,J)}{\mathbf{X}}}}\parallel} \leq {{({1 + \sqrt{1 + {4k{({n - k})}}}})} \cdot \varepsilon}$. Compare this bound with Lemma 4 below.

### Krylov-subspace methods

Suppose that the matrix $\mathbf{A}$ can be applied rapidly to vectors, as happens when $\mathbf{A}$ is sparse or structured. Then Krylov subspace techniques can very effectively and accurately compute partial spectral decompositions. For concreteness, assume that $\mathbf{A}$ is Hermitian. The idea of these techniques is to fix a starting vector $\mathbf{ω}$ and to seek approximations to the eigenvectors within the corresponding *Krylov subspace* Krylov methods also come in blocked versions, in which the starting vector $\mathbf{ω}$ is replaced by a starting matrix $\mathbf{\Omega}$. A common recommendation is to draw a starting vector $\mathbf{ω}$ (or starting matrix $\mathbf{\Omega}$) from a standardized Gaussian distribution, which indicates a significant overlap between Krylov methods and the methods in this paper.

The most basic versions of Krylov methods for computing spectral decompositions are numerically unstable. High-quality implementations require that we incorporate restarting strategies, techniques for maintaining high-quality bases for the Krylov subspaces, etc. The diversity and complexity of such methods make it hard to state a precise computational cost, but in the environment we consider in this paper, a typical cost for a fully stable implementation would be where $T_{mult}$ is the cost of a matrix--vector multiplication.

This part of the paper, §§4--7, provides detailed descriptions of randomized algorithms for constructing low-rank approximations to matrices. As discussed in §1.2, we split the problem into two stages. In Stage A, we construct a subspace that captures the action of the input matrix. In Stage B, we use this subspace to obtain an approximate factorization of the matrix.

Section 4 develops randomized methods for completing Stage A, and §5 describes deterministic methods for Stage B. Section 6 compares the computational costs of the resulting two-stage algorithm with the classical approaches outlined in §3. Finally, §7 illustrates the performance of the randomized schemes via numerical examples.

## Stage A: Randomized schemes for approximating the range

This section outlines techniques for constructing a subspace that captures most of the action of a matrix. We begin with a recapitulation of the proto-algorithm that we introduced in §1.3. We discuss how it can be implemented in practice (§4.1) and then consider the question of how many random samples to acquire (§4.2). Afterward, we present several ways in which the basic scheme can be improved. Sections 4.3 and 4.4 for free ‣ 4 Stage A: Randomized schemes for approximating the range ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") explain how to address the situation where the numerical rank of the input matrix is not known in advance. Section 4.5 shows how to modify the scheme to improve its accuracy when the singular spectrum of the input matrix decays slowly. Finally, §4.6 describes how the scheme can be accelerated by using a structured random matrix.

### The proto-algorithm revisited

The most natural way to implement the proto-algorithm from §1.3 is to draw a random test matrix $\mathbf{\Omega}$ from the standard Gaussian distribution. That is, each entry of $\mathbf{\Omega}$ is an independent Gaussian random variable with mean zero and variance one. For reference, we formulate the resulting scheme as Algorithm LABEL:alg:basic.

Algorithm LABEL:alg:basic: Randomized Range Finder Given an m × n matrix A, and an integer ℓ, this scheme computes an m × ℓ orthonormal matrix Q whose range approximates the range of A. 1 Draw an n × ℓ Gaussian random matrix Ω. 2 Form the m × ℓ matrix Y = A Ω. 3 Construct an m × ℓ matrix Q whose columns form an orthonormal basis for the range of Y, e.g., using the QR factorization Y = Q R.

The number $T_{basic}$ of flops required by Algorithm LABEL:alg:basic satisfies where $T_{rand}$ is the cost of generating a Gaussian random number and $T_{mult}$ is the cost of multiplying $\mathbf{A}$ by a vector. The three terms in correspond directly with the three steps of Algorithm LABEL:alg:basic.

Empirically, we have found that the performance of Algorithm LABEL:alg:basic depends very little on the quality of the random number generator used in Step 1.

The actual cost of Step 2 depends substantially on the matrix $\mathbf{A}$ and the computational environment that we are working . The estimate suggests that Algorithm LABEL:alg:basic is especially efficient when the matrix--vector product ${\mathbf{x}}\mapsto{{\mathbf{A}}{\mathbf{x}}}$ can be evaluated rapidly. In particular, the scheme is appropriate for approximating sparse or structured matrices. Turn to §6 for more details.

The most important implementation issue arises when performing the basis calculation in Step 3. Typically, the columns of the sample matrix $\mathbf{Y}$ are almost linearly dependent, so it is imperative to use stable methods for performing the orthonormalization. We have found that the Gram--Schmidt procedure, augmented with the *double orthogonalization* described , is both convenient and reliable. Methods based on Householder reflectors or Givens rotations also work very well. Note that very little is gained by pivoting because the columns of the random matrix $\mathbf{Y}$ are independent samples drawn from the same distribution.

### The number of samples required

The goal of Algorithm LABEL:alg:basic is to produce an orthonormal matrix $\mathbf{Q}$ with few columns that achieves where $\varepsilon$ is a specified tolerance. The number of columns $\ell$ that the algorithm needs to reach this threshold is usually slightly larger than the minimal rank $k$ of the smallest basis that verifies. We refer to this discrepancy $p = {\ell - k}$ as the *oversampling parameter*. The size of the oversampling parameter depends on several factors: The matrix dimensions.: Very large matrices may require more oversampling.

The singular spectrum.: The more rapid the decay of the singular values, the less oversampling is needed. In the extreme case that the matrix has exact rank $k$, it is not necessary to oversample.

The random test matrix.: Gaussian matrices succeed with very little oversampling, but are not always the most cost-effective option. The structured random matrices discussed in §4.6 may require substantial oversampling, but they still yield computational gains in certain settings.

The theoretical results in Part III provide detailed information about how the behavior of randomized schemes depends on these factors. For the moment, we limit ourselves to some general remarks on implementation issues.

For Gaussian test matrices, it is adequate to choose the oversampling parameter to be a small constant, such as $p = 5$ or $p = 10$. There is rarely any advantage to select $p > k$. This observation, first presented , demonstrates that a Gaussian test matrix results in a negligible amount of extra computation.

In practice, the target rank $k$ is rarely known in advance. Randomized algorithms are usually implemented in an adaptive fashion where the number of samples is increased until the error satisfies the desired tolerance. In other words, the user never *chooses* the oversampling parameter. Theoretical results that bound the amount of oversampling are valuable primarily as aids for designing algorithms. We develop an adaptive approach in §§4.3--4.4 for free ‣ 4 Stage A: Randomized schemes for approximating the range ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions").

The computational bottleneck in Algorithm LABEL:alg:basic is usually the formation of the product ${\mathbf{A}}\mathbf{\Omega}$. As a result, it often pays to draw a larger number $\ell$ of samples than necessary because the user can minimize the cost of the matrix multiplication with tools such as blocking of operations, high-level linear algebra subroutines, parallel processors, etc. This approach may lead to an ill-conditioned sample matrix $\mathbf{Y}$, but the orthogonalization in Step 3 of Algorithm LABEL:alg:basic can easily identify the numerical rank of the sample matrix and ignore the excess samples. Furthermore, Stage B of the matrix approximation process succeeds even when the basis matrix $\mathbf{Q}$ has a larger dimension than necessary.

### A posteriori error estimation

Algorithm LABEL:alg:basic is designed for solving the fixed-rank problem, where the target rank of the input matrix is specified in advance. To handle the fixed-precision problem, where the parameter is the computational tolerance, we need a scheme for estimating how well a putative basis matrix $\mathbf{Q}$ captures the action of the matrix $\mathbf{A}$. To do so, we develop a probabilistic error estimator. These methods are inspired by work of Dixon; our treatment follows.

The exact approximation error is $\left\| {{({\mathbf{I} - {{\mathbf{Q}}{\mathbf{Q}}^{\ast}}})}{\mathbf{A}}} \right\|$. It is intuitively plausible that we can obtain some information about this quantity by computing $\left\| {{({\mathbf{I} - {{\mathbf{Q}}{\mathbf{Q}}^{\ast}}})}{\mathbf{A}}{\mathbf{ω}}} \right\|$, where $\mathbf{ω}$ is a standard Gaussian vector. This notion leads to the following method. Draw a sequence $\{{\mathbf{ω}}^{(i)}:{i = {1,2,\ldots,r}}\}$ of standard Gaussian vectors, where $r$ is a small integer that balances computational cost and reliability. Then with probability at least $1 - 10^{- r}$. This statement follows by setting ${\mathbf{B}} = {{({\mathbf{I} - {{\mathbf{Q}}{\mathbf{Q}}^{\ast}}})}{\mathbf{A}}}$ and $\alpha = 10$ in the following lemma, whose proof appears in \[137, §3.4\].

### Lemma 3

Let $\mathbf{B}$ be a real $m \times n$ matrix. Fix a positive integer $r$ and a real number $\alpha > 1$. Draw an independent family $\{{\mathbf{ω}}^{(i)}:{i = {1,2,\ldots,r}}\}$ of standard Gaussian vectors. Then except with probability $\alpha^{- r}$.

The critical point is that the error estimate is computationally inexpensive because it requires only a small number of matrix--vector products. Therefore, we can make a lowball guess for the numerical rank of $\mathbf{A}$ and add more samples if the error estimate is too large. The asymptotic cost of Algorithm LABEL:alg:basic is preserved if we double our guess for the rank at each step. For example, we can start with 32 samples, compute another 32, then another 64, etc.

### Remark 4.1

The estimate is actually somewhat crude. We can obtain a better estimate at a similar computational cost by initializing a power iteration with a random vector and repeating the process several times.

### Error estimation (almost) for free

The error estimate described in §4.3 can be combined with any method for constructing an approximate basis for the range of a matrix. In this section, we explain how the error estimator can be incorporated into Algorithm LABEL:alg:basic at almost no additional cost.

To be precise, let us suppose that $\mathbf{A}$ is an $m \times n$ matrix and $\varepsilon$ is a computational tolerance. We seek an integer $\ell$ and an $m \times \ell$ orthonormal matrix ${\mathbf{Q}}^{(\ell)}$ such that The size $\ell$ of the basis will typically be slightly larger than the size $k$ of the smallest basis that achieves this error.

The basic observation behind the adaptive scheme is that we can generate the basis in Step 3 of Algorithm LABEL:alg:basic incrementally. Starting with an empty basis matrix ${\mathbf{Q}}^{}$, the following scheme generates an orthonormal matrix whose range captures the action of $\mathbf{A}$: How do we know when we have reached a basis ${\mathbf{Q}}^{(\ell)}$ that verifies (21 for free ‣ 4 Stage A: Randomized schemes for approximating the range ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"))? The answer becomes apparent once we observe that the vectors ${\overset{\sim}{\mathbf{q}}}^{(i)}$ are precisely the vectors that appear in the error bound. The resulting rule is that we break the loop once we observe $r$ consecutive vectors ${\overset{\sim}{\mathbf{q}}}^{(i)}$ whose norms are smaller than $\varepsilon/{({10\sqrt{2/\pi}})}$.

A formal description of the resulting algorithm appears as Algorithm LABEL:alg:adaptive2. A potential complication of the method is that the vectors ${\overset{\sim}{\mathbf{q}}}^{(i)}$ become small as the basis starts to capture most of the action of $\mathbf{A}$. In finite-precision arithmetic, their direction is extremely unreliable. To address this problem, we simply reproject the normalized vector ${\mathbf{q}}^{(i)}$ onto ${range}{({\mathbf{Q}}^{({i - 1})})}^{\perp}$ in steps 7 and 8 of Algorithm LABEL:alg:adaptive2.

The CPU time requirements of Algorithms LABEL:alg:adaptive2 and LABEL:alg:basic are essentially identical. Although Algorithm LABEL:alg:adaptive2 computes the last few samples purely to obtain the error estimate, this apparent extra cost is offset by the fact that Algorithm LABEL:alg:basic always includes an oversampling factor. The failure probability stated for Algorithm LABEL:alg:adaptive2 is pessimistic because it is derived from a simple union bound argument. In practice, the error estimator is reliable in a range of circumstances when we take $r = 10$.

Algorithm LABEL:alg:adaptive2: Adaptive Randomized Range Finder Given an m × n matrix A, a tolerance ε, and an integer r (e.g. r = 10), the following scheme computes an orthonormal matrix Q such that holds with probability at least 1 − min {m, n} 10−r. 1 Draw standard Gaussian vectors ω, …, ω(r) of length n. 2 For i = 1, 2, …, r, compute y(i) = A ω(i). 3 j = 0. 4 Q =, the m × 0 empty matrix. 5 while ${\max\left\{ {\parallel{\mathbf{y}}^{({j + 1})}\parallel},{\parallel{\mathbf{y}}^{({j + 2})}\parallel},\ldots,{\parallel{\mathbf{y}}^{({j + r})}\parallel} \right\}} > {\varepsilon/{({10\sqrt{2/\pi}})}}$, 6 j = j + 1. 7 Overwrite y(j) by (I − Q(j − 1) (Q(j − 1))*) y(j). 8 q(j) = y(j)/∥y(j)∥. 9 Q(j) = [Q(j − 1) q(j)]. 10 Draw a standard Gaussian vector ω(j + r) of length n. 11 y(j + r) = (I − Q(j) (Q(j))*) A ω(j + r). 12 for i = (j + 1), (j + 2), …, (j + r − 1), 13 Overwrite y(i) by y(i) − q(j) ⟨q(j), y(i)⟩. 14 end for 15 end while 16 Q = Q(j).

### Remark 4.2

The calculations in Algorithm LABEL:alg:adaptive2 can be organized so that each iteration processes a block of samples simultaneously. This revision can lead to dramatic improvements in speed because it allows us to exploit higher-level linear algebra subroutines (e.g., BLAS3) or parallel processors. Although blocking can lead to the generation of unnecessary samples, this outcome is generally harmless, as noted in §4.2.

### A modified scheme for matrices whose singular values decay slowly

The techniques described in §4.1 and §4.4 for free ‣ 4 Stage A: Randomized schemes for approximating the range ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") work well for matrices whose singular values exhibit some decay, but they may produce a poor basis when the input matrix has a flat singular spectrum or when the input matrix is very large. In this section, we describe techniques, originally proposed , for improving the accuracy of randomized algorithms in these situations. Related earlier work includes and the literature on classical orthogonal iteration methods \[61, p. 332\].

The intuition behind these techniques is that the singular vectors associated with small singular values interfere with the calculation, so we reduce their weight relative to the dominant singular vectors by taking powers of the matrix to be analyzed. More precisely, we wish to apply the randomized sampling scheme to the matrix ${\mathbf{B}} = {{({{\mathbf{A}}{\mathbf{A}}^{\ast}})}^{q}{\mathbf{A}}}$, where $q$ is a small integer. The matrix $\mathbf{B}$ has the same singular vectors as the input matrix $\mathbf{A}$, but its singular values decay much more quickly: We modify Algorithm LABEL:alg:basic by replacing the formula ${\mathbf{Y}} = {{\mathbf{A}}\mathbf{\Omega}}$ in Step 2 by the formula ${\mathbf{Y}} = {{\mathbf{B}}\mathbf{\Omega}} = {\left({{\mathbf{A}}{\mathbf{A}}^{\ast}} \right)^{q}{\mathbf{A}}\mathbf{\Omega}}$, and we obtain Algorithm LABEL:alg:poweriteration.

Algorithm LABEL:alg:poweriteration: Randomized Power Iteration Given an m × n matrix A and integers ℓ and q, this algorithm computes an m × ℓ orthonormal matrix Q whose range approximates the range of A. 1 Draw an n × ℓ Gaussian random matrix Ω. 2 Form the m × ℓ matrix Y = (A A*)q A Ω via alternating application of A and A*. 3 Construct an m × ℓ matrix Q whose columns form an orthonormal basis for the range of Y, e.g., via the QR factorization Y = Q R. Note: This procedure is vulnerable to round-off errors; see Remark 4.3. The recommended implementation appears as Algorithm LABEL:alg:subspaceiteration.

Algorithm LABEL:alg:poweriteration requires ${2q} + 1$ times as many matrix--vector multiplies as Algorithm LABEL:alg:basic, but is far more accurate in situations where the singular values of $\mathbf{A}$ decay slowly. A good heuristic is that when the original scheme produces a basis whose approximation error is within a factor $C$ of the optimum, the power scheme produces an approximation error within $C^{1/{({{2q} + 1})}}$ of the optimum. In other words, the power iteration drives the approximation gap to one exponentially fast. See Theorem 12. ‣ 9.3 Analysis of the power scheme ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") and §10.4 for the details.

Algorithm LABEL:alg:poweriteration targets the fixed-rank problem. To address the fixed-precision problem, we can incorporate the error estimators described in §4.3 to obtain an adaptive scheme analogous with Algorithm LABEL:alg:adaptive2. In situations where it is critical to achieve near-optimal approximation errors, one can increase the oversampling beyond our standard recommendation $\ell = {k + 5}$ all the way to $\ell = {2k}$ without changing the scaling of the asymptotic computational cost. A supporting analysis appears in Corollary 23. ‣ 10.4 Analysis of the power scheme ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions").

### Remark 4.3

Unfortunately, when Algorithm LABEL:alg:poweriteration is executed in floating point arithmetic, rounding errors will extinguish all information pertaining to singular modes associated with singular values that are small compared with $\left\| {\mathbf{A}} \right\|$. (Roughly, if machine precision is $\mu$, then all information associated with singular values smaller than $\mu^{1/{({{2q} + 1})}}\left\| {\mathbf{A}} \right\|$ is lost.) This problem can easily be remedied by orthonormalizing the columns of the sample matrix between each application of $\mathbf{A}$ and ${\mathbf{A}}^{\ast}$. The resulting scheme, summarized as Algorithm LABEL:alg:subspaceiteration, is algebraically equivalent to Algorithm LABEL:alg:poweriteration when executed in exact arithmetic. We recommend Algorithm LABEL:alg:subspaceiteration because its computational costs are similar to Algorithm LABEL:alg:poweriteration, even though the former is substantially more accurate in floating-point arithmetic.

Algorithm LABEL:alg:subspaceiteration: Randomized Subspace Iteration Given an m × n matrix A and integers ℓ and q, this algorithm computes an m × ℓ orthonormal matrix Q whose range approximates the range of A. 1 Draw an n × ℓ standard Gaussian matrix Ω. 2 Form Y0 = A Ω and compute its QR factorization Y0 = Q0 R0. 3 for j = 1, 2, …, q 4 Form ${\overset{\sim}{\mathbf{Y}}}_{j} = {{\mathbf{A}}^{\ast}{\mathbf{Q}}_{j - 1}}$ and compute its QR factorization ${\overset{\sim}{\mathbf{Y}}}_{j} = {{\overset{\sim}{\mathbf{Q}}}_{j}{\overset{\sim}{\mathbf{R}}}_{j}}$. 5 Form ${\mathbf{Y}}_{j} = {{\mathbf{A}}{\overset{\sim}{\mathbf{Q}}}_{j}}$ and compute its QR factorization Yj = Qj Rj. 6 end 7 Q = Qq.

### An accelerated technique for general dense matrices

This section describes a set of techniques that allow us to compute an approximate rank-$\ell$ factorization of a general dense $m \times n$ matrix in roughly $O{({mn{\log{(\ell)}}})}$ flops, in contrast to the asymptotic cost $O{({mn\ell})}$ required by earlier methods. We can tailor this scheme for the real or complex case, but we focus on the conceptually simpler complex case. These algorithms were introduced ; similar techniques were proposed .

The first step toward this accelerated technique is to observe that the bottleneck in Algorithm LABEL:alg:basic is the computation of the matrix product ${\mathbf{A}}\mathbf{\Omega}$. When the test matrix $\mathbf{\Omega}$ is standard Gaussian, the cost of this multiplication is $O{({mn\ell})}$, the same as a rank-revealing QR algorithm. The key idea is to use a *structured* random matrix that allows us to compute the product in $O{({mn{\log{(\ell)}}})}$ flops.

The *subsampled random Fourier transform*, or SRFT, is perhaps the simplest example of a structured random matrix that meets our goals. An SRFT is an $n \times \ell$ matrix of the form $\mathbf{D}$ is an $n \times n$ diagonal matrix whose entries are independent random variables uniformly distributed on the complex unit circle, $\mathbf{F}$ is the $n \times n$ unitary discrete Fourier transform (DFT), whose entries take the values $f_{pq} = {n^{- {1/2}}e^{- {{2\pii{({p - 1})}{({q - 1})}}/n}}}$ for ${{p,q} = 1},{2,\ldots,n}$, and $\mathbf{R}$ is an $n \times \ell$ matrix that samples $\ell$ coordinates from $n$ uniformly at random, i.e., its $\ell$ columns are drawn randomly without replacement from the columns of the $n \times n$ identity matrix.

When $\mathbf{\Omega}$ is defined, we can compute the sample matrix ${\mathbf{Y}} = {{\mathbf{A}}\mathbf{\Omega}}$ using $O{({mn{\log{(\ell)}}})}$ flops via a subsampled FFT. Then we form the basis $\mathbf{Q}$ by orthonormalizing the columns of $\mathbf{Y}$, as described in §4.1. This scheme appears as Algorithm LABEL:alg:fastbasic. The total number $T_{struct}$ of flops required by this procedure is Note that if $\ell$ is substantially larger than the numerical rank $k$ of the input matrix, we can perform the orthogonalization with $O{({k\elln})}$ flops because the columns of the sample matrix are almost linearly dependent.

The test matrix is just one choice among many possibilities. Other suggestions that appear in the literature include subsampled Hadamard transforms, chains of Givens rotations acting on randomly chosen coordinates, and many more. See and its bibliography. Empirically, we have found that the transform summarized in Remark 4.6 below performs very well in a variety of environments.

At this point, it is not well understood how to quantify and compare the behavior of structured random transforms. One reason for this uncertainty is that it has been difficult to analyze the amount of oversampling that various transforms require. Section 11 establishes that the random matrix can be used to identify a near-optimal basis for a rank-$k$ matrix using $\ell \sim {{({k + {\log{(n)}}})}{\log{(k)}}}$ samples. In practice, the transforms and typically require no more oversampling than a Gaussian test matrix requires. (For a numerical example, see §7.4.) As a consequence, setting $\ell = {k + 10}$ or $\ell = {k + 20}$ is typically more than adequate. Further research on these questions would be valuable.

Algorithm LABEL:alg:fastbasic: Fast Randomized Range Finder Given an m × n matrix A, and an integer ℓ, this scheme computes an m × ℓ orthonormal matrix Q whose range approximates the range of A. 1 Draw an n × ℓ SRFT test matrix Ω, as defined . 2 Form the m × ℓ matrix Y = A Ω using a (subsampled) FFT. 3 Construct an m × ℓ matrix Q whose columns form an orthonormal basis for the range of Y, e.g., using the QR factorization Y = Q R.

### Remark 4.4

The structured random matrices discussed in this section do not adapt readily to the fixed-precision problem, where the computational tolerance is specified, because the samples from the range are usually computed in bulk. Fortunately, these schemes are sufficiently inexpensive that we can progressively increase the number of samples computed starting with $\ell = 32$, say, and then proceeding to $\ell = {64,128,256,\ldots}$ until we achieve the desired tolerance.

### Remark 4.5

When using the SRFT for matrix approximation, we have a choice whether to use a subsampled FFT or a full FFT. The complete FFT is so inexpensive that it often pays to construct an extended sample matrix ${\mathbf{Y}}_{large} = {{\mathbf{A}}{\mathbf{D}}{\mathbf{F}}}$ and then generate the actual samples by drawing columns at random from ${\mathbf{Y}}_{large}$ and rescaling as needed. The asymptotic cost increases to $O{({mn{\log{(n)}}})}$ flops, but the full FFT is actually faster for moderate problem sizes because the constant suppressed by the big-O notation is so small. Adaptive rank determination is easy because we just examine extra samples as needed.

### Remark 4.6

Among the structured random matrices that we have tried, one of the strongest candidates involves sequences of random Givens rotations. This matrix takes the form where the prime symbol ^′^ indicates an independent realization of a random matrix. The matrices $\mathbf{R}$, $\mathbf{F}$, and $\mathbf{D}$ are defined after. The matrix $\mathbf{\Theta}$ is a chain of random Givens rotations: where $\mathbf{\Pi}$ is a random $n \times n$ permutation matrix; where $\theta_{1},\ldots,\theta_{n - 1}$ are independent random variables uniformly distributed on the interval $\lbrack 0,{2\pi}\rbrack$; and where ${\mathbf{G}}{(i,j;\theta)}$ denotes a rotation on ${\mathbb{C}}^{n}$ by the angle $\theta$ in the $(i,j)$ coordinate plane \[61, §5.1.8\].

### Remark 4.7

When the singular values of the input matrix $\mathbf{A}$ decay slowly, Algorithm LABEL:alg:fastbasic may perform poorly in terms of accuracy. When randomized sampling is used with a Gaussian random matrix, the recourse is to take a couple of steps of a power iteration; see Algorithm LABEL:alg:subspaceiteration. However, it is not currently known whether such an iterative scheme can be accelerated to $O{({mn{\log{(k)}}})}$ complexity using "fast" random transforms such as the SRFT.

## Stage B: Construction of standard factorizations

The algorithms for Stage A described in §4 produce an orthonormal matrix $\mathbf{Q}$ whose range captures the action of an input matrix $\mathbf{A}$: where $\varepsilon$ is a computational tolerance. This section describes methods for approximating standard factorizations of $\mathbf{A}$ using the information in the basis $\mathbf{Q}$.

To accomplish this task, we pursue the idea from §3.3.3 that any low-rank factorization ${\mathbf{A}} \approx {{\mathbf{C}}{\mathbf{B}}}$ can be manipulated to produce a standard decomposition. When the bound holds, the low-rank factors are simply ${\mathbf{C}} = {\mathbf{Q}}$ and ${\mathbf{B}} = {{\mathbf{Q}}^{\ast}{\mathbf{A}}}$. The simplest scheme (§5.1) computes the factor $\mathbf{B}$ directly with a matrix--matrix product to ensure a minimal error in the final approximation. An alternative approach (§5.2) constructs factors $\mathbf{B}$ and $\mathbf{C}$ without forming any matrix--matrix product. The approach of §5.2 is often faster than the approach of §5.1 but typically results in larger errors. Both schemes can be streamlined for an Hermitian input matrix (§5.3) and a positive semidefinite input matrix (§5.4). Finally, we develop single-pass algorithms that exploit other information generated in Stage A to avoid revisiting the input matrix (§5.5).

Throughout this section, $\mathbf{A}$ denotes an $m \times n$ matrix, and $\mathbf{Q}$ is an $m \times k$ orthonormal matrix that verifies. For purposes of exposition, we concentrate on methods for constructing the partial SVD.

### Factorizations based on forming ${\mathbf{Q}}^{\ast}{\mathbf{A}}$ directly

The relation implies that $\left\| {{\mathbf{A}} - {{\mathbf{Q}}{\mathbf{B}}}} \right\| \leq \varepsilon$, where ${\mathbf{B}} = {{\mathbf{Q}}^{\ast}{\mathbf{A}}}$. Once we have computed $\mathbf{B}$, we can produce any standard factorization using the methods of §3.3.3. Algorithm LABEL:alg:Atranspose illustrates how to build an approximate SVD.

Algorithm LABEL:alg:Atranspose: Direct SVD Given matrices A and Q such that holds, this procedure computes an approximate factorization A ≈ U Σ V*, where U and V are orthonormal, and Σ is a nonnegative diagonal matrix. 1 Form the matrix B = Q* A. 2 Compute an SVD of the small matrix: ${{\mathbf{B}} = {\overset{\sim}{\mathbf{U}}\mathbf{\Sigma}{\mathbf{V}}^{\ast}}}.$ 3 Form the orthonormal matrix ${{\mathbf{U}} = {{\mathbf{Q}}\overset{\sim}{\mathbf{U}}}}.$ The factors produced by Algorithm LABEL:alg:Atranspose satisfy In other words, the approximation error does not degrade.

The cost of Algorithm LABEL:alg:Atranspose is generally dominated by the cost of the product ${\mathbf{Q}}^{\ast}{\mathbf{A}}$ in Step 1, which takes $O{({kmn})}$ flops for a general dense matrix. Note that this scheme is particularly well suited to environments where we have a fast method for computing the matrix--vector product ${\mathbf{x}}\mapsto{{\mathbf{A}}^{\ast}{\mathbf{x}}}$, for example when $\mathbf{A}$ is sparse or structured. This approach retains a strong advantage over Krylov-subspace methods and rank-revealing QR because Step 1 can be accelerated using BLAS3, parallel processors, and so forth. Steps 2 and 3 require $O{({k^{2}n})}$ and $O{({k^{2}m})}$ flops respectively.

### Remark 5.1

Algorithm LABEL:alg:Atranspose produces an approximate SVD with the same rank as the basis matrix $\mathbf{Q}$. When the size of the basis exceeds the desired rank $k$ of the SVD, it may be preferable to retain only the dominant $k$ singular values and singular vectors. Equivalently, we replace the diagonal matrix $\mathbf{\Sigma}$ of computed singular values with the matrix $\mathbf{\Sigma}_{(k)}$ formed by zeroing out all but the largest $k$ entries of $\mathbf{\Sigma}$. In the worst case, this truncation step can increase the approximation error by $\sigma_{k + 1}$; see §9.4 for an analysis. Our numerical experience suggests that this error analysis is pessimistic, and the term $\sigma_{k + 1}$ often does not appear in practice.

### Postprocessing via row extraction

Given a matrix $\mathbf{Q}$ such that holds, we can obtain a rank-$k$ factorization where $\mathbf{B}$ is a $k \times n$ matrix consisting of $k$ rows extracted from $\mathbf{A}$. The approximation can be produced without computing any matrix--matrix products, which makes this approach to postprocessing very fast. The drawback comes because the error $\left\| {{\mathbf{A}} - {{\mathbf{X}}{\mathbf{B}}}} \right\|$ is usually larger than the initial error $\left\| {{\mathbf{A}} - {{\mathbf{Q}}{\mathbf{Q}}^{\ast}{\mathbf{A}}}} \right\|$, especially when the dimensions of $\mathbf{A}$ are large. See Remark 5.3 for more discussion.

To obtain the factorization, we simply construct the interpolative decomposition (§3.2.3 ‣ 3.2 Standard matrix factorizations ‣ 3 Linear algebraic preliminaries ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions")) of the matrix $\mathbf{Q}$: The index set $J$ marks $k$ rows of $\mathbf{Q}$ that span the row space of $\mathbf{Q}$, and $\mathbf{X}$ is an $m \times k$ matrix whose entries are bounded in magnitude by two and contains the $k \times k$ identity as a submatrix: ${\mathbf{X}}_{(J,:)} = \mathbf{I}_{k}$. Combining and, we reach Since ${\mathbf{X}}_{(J,:)} = \mathbf{I}_{k}$, equation implies that ${\mathbf{A}}_{(J,:)} \approx {{\mathbf{Q}}_{(J,:)}{\mathbf{Q}}^{\ast}{\mathbf{A}}}$. Therefore, follows when we put ${\mathbf{B}} = {\mathbf{A}}_{(J,:)}$.

Provided with the factorization, we can obtain any standard factorization using the techniques of §3.3.3. Algorithm LABEL:alg:extractrows illustrates an SVD calculation. This procedure requires $O{({k^{2}{({m + n})}})}$ flops. The following lemma guarantees the accuracy of the computed factors.

Algorithm LABEL:alg:extractrows: SVD via Row Extraction Given matrices A and Q such that holds, this procedure computes an approximate factorization A ≈ U Σ V*, where U and V are orthonormal, and Σ is a nonnegative diagonal matrix. 1 Compute an ID Q = X Q(J,: ). (The ID is defined in §3.2.3.) 2 Extract A(J,: ), and compute a QR factorization A(J,: ) = R* W*. 3 Form the product Z = X R*. 4 Compute an SVD ${{\mathbf{Z}} = {{\mathbf{U}}\mathbf{\Sigma}{\overset{\sim}{\mathbf{V}}}^{\ast}}}.$ 5 Form the orthonormal matrix ${{\mathbf{V}} = {{\mathbf{W}}\overset{\sim}{\mathbf{V}}}}.$ Note: Algorithm LABEL:alg:extractrows is faster than Algorithm LABEL:alg:Atranspose but less accurate. Note: It is advantageous to replace the basis Q by the sample matrix Y produced in Stage A, cf. Remark 5.2.

### Lemma 4

Let $\mathbf{A}$ be an $m \times n$ matrix and let $\mathbf{Q}$ be an $m \times k$ matrix that satisfy. Suppose that $\mathbf{U}$, $\mathbf{\Sigma}$, and $\mathbf{V}$ are the matrices constructed by Algorithm LABEL:alg:extractrows. Then

### Proof

The factors $\mathbf{U}$, $\mathbf{\Sigma}$, $\mathbf{V}$ constructed by the algorithm satisfy Define the approximation Since $\hat{\mathbf{A}} = {{\mathbf{X}}{\mathbf{Q}}_{(J,:)}{\mathbf{Q}}^{\ast}{\mathbf{A}}}$ and since ${\mathbf{X}}_{(J,:)} = \mathbf{I}_{k}$, it must be that ${\hat{\mathbf{A}}}_{(J,:)} = {{\mathbf{Q}}_{(J,:)}{\mathbf{Q}}^{\ast}{\mathbf{A}}}$. Consequently, We have the chain of relations Inequality ensures that ${\parallel{{\mathbf{A}} - \hat{\mathbf{A}}}\parallel} \leq \varepsilon$. Since ${\mathbf{A}}_{(J,:)} - {\hat{\mathbf{A}}}_{(J,:)}$ is a submatrix of ${\mathbf{A}} - \hat{\mathbf{A}}$, we must also have ${\parallel{{\mathbf{A}}_{(J,:)} - {\hat{\mathbf{A}}}_{(J,:)}}\parallel} \leq \varepsilon$. Thus, (5.2) reduces to The bound follows from after we observe that $\mathbf{X}$ contains a $k \times k$ identity matrix and that the entries of the remaining ${({n - k})} \times k$ submatrix are bounded in magnitude by two. ∎

### Remark 5.2

To maintain a unified presentation, we have formulated all the postprocessing techniques so they take an orthonormal matrix $\mathbf{Q}$ as input. Recall that, in Stage A of our framework, we construct the matrix $\mathbf{Q}$ by orthonormalizing the columns of the sample matrix $\mathbf{Y}$. With finite-precision arithmetic, it is preferable to adapt Algorithm LABEL:alg:extractrows to start directly from the sample matrix $\mathbf{Y}$. To be precise, we modify Step 1 to compute $\mathbf{X}$ and $J$ so that ${\mathbf{Y}} = {{\mathbf{X}}{\mathbf{Y}}_{(J,:)}}$. This revision is recommended even when $\mathbf{Q}$ is available from the adaptive rank determination of Algorithm LABEL:alg:adaptive2.

### Remark 5.3

As the inequality suggests, the factorization produced by Algorithm LABEL:alg:extractrows is potentially less accurate than the basis that it uses as input. This loss of accuracy is problematic when $\varepsilon$ is not so small or when $kn$ is large. In such cases, we recommend Algorithm LABEL:alg:Atranspose over Algorithm LABEL:alg:extractrows; the former is more costly, but it does not amplify the error, as shown .

### Postprocessing an Hermitian matrix

When $\mathbf{A}$ is Hermitian, the postprocessing becomes particularly elegant. In this case, the columns of $\mathbf{Q}$ form a good basis for both the column space *and* the row space of $\mathbf{A}$ so that we have ${\mathbf{A}} \approx {{\mathbf{Q}}{\mathbf{Q}}^{\ast}{\mathbf{A}}{\mathbf{Q}}{\mathbf{Q}}^{\ast}}$. More precisely, when is in force, we have The last inequality relies on the facts that $\left\| {{\mathbf{Q}}{\mathbf{Q}}^{\ast}} \right\| = 1$ and that Since ${\mathbf{A}} \approx {{\mathbf{Q}}\left({{\mathbf{Q}}^{\ast}{\mathbf{A}}{\mathbf{Q}}} \right){\mathbf{Q}}^{\ast}}$ is a low-rank approximation of $\mathbf{A}$, we can form any standard factorization using the techniques from §3.3.3.

For Hermitian $\mathbf{A}$, it is more common to compute an eigenvalue decomposition than an SVD. We can accomplish this goal using Algorithm LABEL:alg:hermeig, which adapts the scheme from §5.1. This procedure delivers a factorization that satisfies the error bound $\left\| {{\mathbf{A}} - {{\mathbf{U}}\mathbf{\Lambda}{\mathbf{U}}^{\ast}}} \right\| \leq {2\varepsilon}$. The calculation requires $O{({kn^{2}})}$ flops.

We can also pursue the row extraction approach from §5.2, which is faster but less accurate. See Algorithm LABEL:alg:hermeigrows for the details. The total cost is $O{({k^{2}n})}$ flops.

Algorithm LABEL:alg:hermeig: Direct Eigenvalue Decomposition Given an Hermitian matrix A and a basis Q such that holds, this procedure computes an approximate eigenvalue decomposition A ≈ U Λ U*, where U is orthonormal, and Λ is a real diagonal matrix. 1 Form the small matrix B = Q* A Q. 2 Compute an eigenvalue decomposition B = V Λ V*. 3 Form the orthonormal matrix U = Q V.

Algorithm LABEL:alg:hermeigrows: Eigenvalue Decomposition via Row Extraction Given an Hermitian matrix A and a basis Q such that holds, this procedure computes an approximate eigenvalue decomposition A ≈ U Λ U*, where U is orthonormal, and Λ is a real diagonal matrix. 1 Compute an ID Q = X Q(J,: ). 2 Perform a QR factorization X = V R. 3 Form the product Z = R A(J, J) R*. 4 Compute an eigenvalue decomposition Z = W Λ W*. 5 Form the orthonormal matrix U = V W. Note: Algorithm LABEL:alg:hermeigrows is faster than Algorithm LABEL:alg:hermeig but less accurate. Note: It is advantageous to replace the basis Q by the sample matrix Y produced in Stage A, cf. Remark 5.2.

### Postprocessing a positive semidefinite matrix

When the input matrix $\mathbf{A}$ is positive semidefinite, the *Nyström method* can be used to improve the quality of standard factorizations at almost no additional cost; see and its bibliography. To describe the main idea, we first recall that the direct method presented in §5.3 manipulates the approximate rank-$k$ factorization In contrast, the Nyström scheme builds a more sophisticated rank-$k$ approximation, namely where $\mathbf{F}$ is an approximate Cholesky factor of $\mathbf{A}$ with dimension $n \times k$. To compute the factor $\mathbf{F}$ numerically, first form the matrices ${\mathbf{B}}_{1} = {{\mathbf{A}}{\mathbf{Q}}}$ and ${\mathbf{B}}_{2} = {{\mathbf{Q}}^{\ast}{\mathbf{B}}_{1}}$. Then decompose the psd matrix ${\mathbf{B}}_{2} = {{\mathbf{C}}^{\ast}{\mathbf{C}}}$ into its Cholesky factors. Finally compute the factor ${\mathbf{F}} = {{\mathbf{B}}_{1}{\mathbf{C}}^{- 1}}$ by performing a triangular solve. The low-rank factorization can be converted to a standard decomposition using the techniques from §3.3.3.

The literature contains an explicit expression \[48, Lem. 4\] for the approximation error . This result implies that, in the spectral norm, the Nyström approximation error never exceeds $\left\| {{\mathbf{A}} - {{\mathbf{Q}}{\mathbf{Q}}^{\ast}{\mathbf{A}}}} \right\|$, and it is often substantially smaller. We omit a detailed discussion.

For an example of the Nyström technique, consider Algorithm LABEL:alg:nystrom, which computes an approximate eigenvalue decomposition of a positive semidefinite matrix. This method should be compared with the scheme for Hermitian matrices, Algorithm LABEL:alg:hermeig. In both cases, the dominant cost occurs when we form ${\mathbf{A}}{\mathbf{Q}}$, so the two procedures have roughly the same running time. On the other hand, Algorithm LABEL:alg:nystrom is typically much more accurate than Algorithm LABEL:alg:hermeig. In a sense, we are exploiting the fact that $\mathbf{A}$ is positive semidefinite to take one step of subspace iteration (Algorithm LABEL:alg:subspaceiteration) for free.

Algorithm LABEL:alg:nystrom: Eigenvalue Decomposition via Nyström Method Given a positive semidefinite matrix A and a basis Q such that holds, this procedure computes an approximate eigenvalue decomposition A ≈ U Λ U*, where U is orthonormal, and Λ is nonnegative and diagonal. 1 Form the matrices B1 = A Q and B2 = Q* B1. 2 Perform a Cholesky factorization B2 = C* C. 3 Form F = B1 C−1 using a triangular solve. 4 Compute an SVD F = U Σ V* and set Λ = Σ2.

### Single-pass algorithms

The techniques described in §§5.1--5.4 all require us to revisit the input matrix. This may not be feasible in environments where the matrix is too large to be stored. In this section, we develop a method that requires just one pass over the matrix to construct not only an approximate basis but also a complete factorization. Similar techniques appear in and.

For motivation, we begin with the case where $\mathbf{A}$ is Hermitian. Let us recall the proto-algorithm from §1.3.3: Draw a random test matrix $\mathbf{\Omega}$; form the sample matrix ${\mathbf{Y}} = {{\mathbf{A}}\mathbf{\Omega}}$; then construct a basis $\mathbf{Q}$ for the range of $\mathbf{Y}$. It turns out that the matrices $\mathbf{\Omega}$, $\mathbf{Y}$, and $\mathbf{Q}$ contain all the information we need to approximate $\mathbf{A}$.

To see why, define the (currently unknown) matrix $\mathbf{B}$ via ${\mathbf{B}} = {{\mathbf{Q}}^{\ast}{\mathbf{A}}{\mathbf{Q}}}$. Postmultiplying the definition by ${\mathbf{Q}}^{\ast}\mathbf{\Omega}$, we obtain the identity ${{\mathbf{B}}{\mathbf{Q}}^{\ast}\mathbf{\Omega}} = {{\mathbf{Q}}^{\ast}{\mathbf{A}}{\mathbf{Q}}{\mathbf{Q}}^{\ast}\mathbf{\Omega}}$. The relationships ${{\mathbf{A}}{\mathbf{Q}}{\mathbf{Q}}^{\ast}} \approx {\mathbf{A}}$ and ${{\mathbf{A}}\mathbf{\Omega}} = {\mathbf{Y}}$ show that $\mathbf{B}$ must satisfy All three matrices $\mathbf{\Omega}$, $\mathbf{Y}$, and $\mathbf{Q}$ are available, so we can solve to obtain the matrix $\mathbf{B}$. Then the low-rank factorization ${\mathbf{A}} \approx {{\mathbf{Q}}{\mathbf{B}}{\mathbf{Q}}^{\ast}}$ can be converted to an eigenvalue decomposition via familiar techniques. The entire procedure requires $O{({k^{2}n})}$ flops, and it is summarized as Algorithm LABEL:alg:postsym.

Algorithm LABEL:alg:postsym: Eigenvalue Decomposition in One Pass Given an Hermitian matrix A, a random test matrix Ω, a sample matrix Y = A Ω, and an orthonormal matrix Q that verifies and Y = Q Q* Y, this algorithm computes an approximate eigenvalue decomposition A ≈ U Λ U*. 1 Use a standard least-squares solver to find an Hermitian matrix Bapprox that approximately satisfies the equation Bapprox (Q* Ω) ≈ Q* Y. 2 Compute the eigenvalue decomposition Bapprox = V Λ V*. 3 Form the product U = Q V.

When $\mathbf{A}$ is not Hermitian, it is still possible to devise single-pass algorithms, but we must modify the initial Stage A of the approximation framework to simultaneously construct bases for the ranges of $\mathbf{A}$ and ${\mathbf{A}}^{\ast}$: Generate random matrices $\mathbf{\Omega}$ and $\overset{\sim}{\mathbf{\Omega}}$.

Compute ${\mathbf{Y}} = {{\mathbf{A}}\mathbf{\Omega}}$ and $\overset{\sim}{\mathbf{Y}} = {{\mathbf{A}}^{\ast}\overset{\sim}{\mathbf{\Omega}}}$ in a single pass over $\mathbf{A}$.

Compute QR factorizations ${\mathbf{Y}} = {{\mathbf{Q}}{\mathbf{R}}}$ and $\overset{\sim}{\mathbf{Y}} = {\overset{\sim}{\mathbf{Q}}\overset{\sim}{\mathbf{R}}}$.

This procedure results in matrices $\mathbf{Q}$ and $\overset{\sim}{\mathbf{Q}}$ such that ${\mathbf{A}} \approx {{\mathbf{Q}}{\mathbf{Q}}^{\ast}{\mathbf{A}}\overset{\sim}{\mathbf{Q}}{\overset{\sim}{\mathbf{Q}}}^{\ast}}$. The reduced matrix we must approximate is ${\mathbf{B}} = {{\mathbf{Q}}^{\ast}{\mathbf{A}}\overset{\sim}{\mathbf{Q}}}$. In analogy, we find that An analogous calculation shows that $\mathbf{B}$ should also satisfy Now, the reduced matrix ${\mathbf{B}}_{approx}$ can be determined by finding a minimum-residual solution to the system of relations and.

### Remark 5.4

The single-pass approaches described in this section can degrade the approximation error in the final decomposition significantly. To explain the issue, we focus on the Hermitian case. It turns out that the coefficient matrix ${\mathbf{Q}}^{\ast}\mathbf{\Omega}$ in the linear system is usually ill-conditioned. In a worst-case scenario, the error $\left\| {{\mathbf{A}} - {{\mathbf{U}}\mathbf{\Lambda}{\mathbf{U}}^{\ast}}} \right\|$ in the factorization produced by Algorithm LABEL:alg:postsym could be larger than the error resulting from the two-pass method of Section 5.3 by a factor of $1/\tau_{\min}$, where $\tau_{\min}$ is the minimal singular value of the matrix ${\mathbf{Q}}^{\ast}\mathbf{\Omega}$.

The situation can be improved by oversampling. Suppose that we seek a rank-$k$ approximate eigenvalue decomposition. Pick a small oversampling parameter $p$. Draw an $n \times {({k + p})}$ random matrix $\mathbf{\Omega}$, and form the sample matrix ${\mathbf{Y}} = {{\mathbf{A}}\mathbf{\Omega}}$. Let $\mathbf{Q}$ denote the $n \times k$ matrix formed by the $k$ leading left singular vectors of $\mathbf{Y}$. Now, the linear system has a coefficient matrix ${\mathbf{Q}}^{\ast}\mathbf{\Omega}$ of size $k \times {({k + p})}$, so it is overdetermined. An approximate solution of this system yields a $k \times k$ matrix $\mathbf{B}$.

## Computational costs

So far, we have postponed a detailed discussion of the computational cost of randomized matrix approximation algorithms because it is necessary to account for both the first stage, where we compute an approximate basis for the range (§4), and the second stage, where we postprocess the basis to complete the factorization (§5). We are now prepared to compare the cost of the two-stage scheme with the cost of traditional techniques.

Choosing an appropriate algorithm, whether classical or randomized, requires us to consider the properties of the input matrix. To draw a nuanced picture, we discuss three representative computational environments in §6.1--6.3. We close with some comments on parallel implementations in §6.4.

For concreteness, we focus on the problem of computing an approximate SVD of an $m \times n$ matrix $\mathbf{A}$ with numerical rank $k$. The costs for other factorizations are similar.

### General matrices that fit in core memory

Suppose that $\mathbf{A}$ is a general matrix presented as an array of numbers that fits in core memory. In this case, the appropriate method for Stage A is to use a structured random matrix (§4.6), which allows us to find a basis that captures the action of the matrix using $O{({{mn{\log{(k)}}} + {k^{2}m}})}$ flops. For Stage B, we apply the row-extraction technique (§5.2), which costs an additional $O{({k^{2}{({m + n})}})}$ flops. The total number of operations $T_{random}$ for this approach satisfies As a rule of thumb, the approximation error of this procedure satisfies where $\sigma_{k + 1}$ is the $({k + 1})$th singular value of $\mathbf{A}$. The estimate, which follows from Theorem 25. ‣ 11.2 Performance guarantees ‣ 11 SRFT test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") and Lemma 4, reflects the worst-case scenario; actual errors are usually smaller.

This algorithm should be compared with modern deterministic techniques, such as rank-revealing QR followed by postprocessing (§3.3.2) which typically require operations to achieve a comparable error.

In this setting, the randomized algorithm can be several times faster than classical techniques even for problems of moderate size, say ${m,n} \sim 10^{3}$ and $k \sim 10^{2}$. See §7.4 for numerical evidence.

### Remark 6.1

In case row extraction is impractical, there is an alternative $O{({mn{\log{(k)}}})}$ technique described in \[137, §5.2\]. When the error is unacceptably large, we can use the direct method (§5.1) for Stage B, which brings the total cost to $O{({kmn})}$ flops.

### Matrices for which matrix--vector products can be rapidly evaluated

In many problems in data mining and scientific computing, the cost $T_{mult}$ of performing the matrix--vector multiplication ${\mathbf{x}}\mapsto{{\mathbf{A}}{\mathbf{x}}}$ is substantially smaller than the nominal cost $O{({mn})}$ for the dense case. It is not uncommon that $O{({m + n})}$ flops suffice. Standard examples include (i) very sparse matrices; (ii) structured matrices, such as Töplitz operators, that can be applied using the FFT or other means; and (iii) matrices that arise from physical problems, such as discretized integral operators, that can be applied via, e.g., the fast multipole method.

Suppose that both $\mathbf{A}$ and ${\mathbf{A}}^{\ast}$ admit fast multiplies. The appropriate randomized approach for this scenario completes Stage A using Algorithm LABEL:alg:basic with $p$ constant (for the fixed-rank problem) or Algorithm LABEL:alg:adaptive2 (for the fixed-precision problem) at a cost of ${{({k + p})}T_{mult}} + {O{({k^{2}m})}}$ flops. For Stage B, we invoke Algorithm LABEL:alg:Atranspose, which requires ${{({k + p})}T_{mult}} + {O{({k^{2}{({m + n})}})}}$ flops. The total cost $T_{sparse}$ satisfies As a rule of thumb, the approximation error of this procedure satisfies The estimate follows from Corollary 22. ‣ 10.3 Probabilistic error bounds for Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") and the discussion in §5.1. Actual errors are usually smaller.

When the singular spectrum of $\mathbf{A}$ decays slowly, we can incorporate $q$ iterations of the power method (Algorithm LABEL:alg:poweriteration) to obtain superior solutions to the fixed-rank problem. The computational cost increases to, cf., while the error improves to The estimate takes into account the discussion in §10.4. The power scheme can also be adapted for the fixed-precision problem (§4.5).

In this setting, the classical prescription for obtaining a partial SVD is some variation of a Krylov-subspace method; see §3.3.4. These methods exhibit great diversity, so it is hard to specify a "typical" computational cost. To a first approximation, it is fair to say that in order to obtain an approximate SVD of rank $k$, the cost of a numerically stable implementation of a Krylov method is no less than the cost with $p$ set to zero. At this price, the Krylov method often obtains better accuracy than the basic randomized method obtained by combining Algorithms LABEL:alg:basic and LABEL:alg:Atranspose, especially for matrices whose singular values decay slowly. On the other hand, the randomized schemes are inherently more robust and allow much more freedom in organizing the computation to suit a particular application or a particular hardware architecture. The latter point is in practice of crucial importance because it is usually much faster to apply a matrix to $k$ vectors simultaneously than it is to execute $k$ matrix--vector multiplications consecutively. In practice, blocking and parallelism can lead to enough gain that a few steps of the power method (Algorithm LABEL:alg:poweriteration) can be performed more quickly than $k$ steps of a Krylov method.

### Remark 6.2

Any comparison between randomized sampling schemes and Krylov variants becomes complicated because of the fact that "basic" Krylov schemes such as Lanczos \[61, p. 473\] or Arnoldi \[61, p. 499\] are inherently unstable. To obtain numerical robustness, we must incorporate sophisticated modifications such as restarts, reorthogonalization procedures, etc. Constructing a high-quality implementation is sufficiently hard that the authors of a popular book on "numerical recipes" qualify their treatment of spectral computations as follows \[109, p. 567\]: > You have probably gathered by now that the solution of eigensystems is a fairly complicated business. It is. It is one of the few subjects covered in this book for which we do *not* recommend that you avoid canned routines. On the contrary, the purpose of this chapter is precisely to give you some appreciation of what is going on inside such canned routines, so that you can make intelligent choices about using them, and intelligent diagnoses when something goes wrong.

Randomized sampling does not eliminate the difficulties referred to in this quotation; however it reduces the task of computing a *partial* spectral decomposition of a very large matrix to the task of computing a *full* decomposition of a small dense matrix. (For example, in Algorithm LABEL:alg:Atranspose, the input matrix $\mathbf{A}$ is large and $\mathbf{B}$ is small.) The latter task is much better understood and is eminently suitable for using canned routines. Random sampling schemes interact with the large matrix only through matrix--matrix products, which can easily be implemented by a user in a manner appropriate to the application and to the available hardware.

The comparison is further complicated by the fact that there is significant overlap between the two sets of ideas. Algorithm LABEL:alg:poweriteration is conceptually similar to a "block Lanczos method" \[61, p. 485\] with a random starting matrix. Indeed, we believe that there are significant opportunities for cross-fertilization in this area. Hybrid schemes that combine the best ideas from both fields may perform very well.

### General matrices stored in slow memory or streamed

The traditional metric for numerical algorithms is the number of floating-point operations they require. When the data does not fit in fast memory, however, the computational time is often dominated by the cost of memory access. In this setting, a more appropriate measure of algorithmic performance is *pass-efficiency*, which counts how many times the data needs to be cycled through fast memory. Flop counts become largely irrelevant.

All the classical matrix factorization techniques that we discuss in §3.2---including dense SVD, rank-revealing QR, Krylov methods, and so forth---require at least $k$ passes over the the matrix, which is prohibitively expensive for huge data matrices. A desire to reduce the pass count of matrix approximation algorithms served as one of the early motivations for developing randomized schemes. Detailed recent work appears .

For many matrices, randomized techniques can produce an accurate approximation using just one pass over the data. For Hermitian matrices, we obtain a single-pass algorithm by combining Algorithm LABEL:alg:basic, which constructs an approximate basis, with Algorithm LABEL:alg:postsym, which produces an eigenvalue decomposition without any additional access to the matrix. Section 5.5 describes the analogous technique for general matrices.

For the huge matrices that arise in applications such as data mining, it is common that the singular spectrum decays slowly. Relevant applications include image processing (see §§7.2--7.3 for numerical examples), statistical data analysis, and network monitoring. To compute approximate factorizations in these environments, it is crucial to enhance the accuracy of the randomized approach using the power scheme, Algorithm LABEL:alg:poweriteration, or some other device. This approach increases the pass count somewhat, but in our experience it is very rare that more than five passes are required.

### Gains from parallelization

As mentioned in §§6.2--6.3, randomized methods often outperform classical techniques not because they involve fewer floating-point operations but rather because they allow us to reorganize the calculations to exploit the matrix properties and the computer architecture more fully. In addition, these methods are well suited for parallel implementation. For example, in Algorithm LABEL:alg:basic, the computational bottleneck is the evaluation of the matrix product ${\mathbf{A}}\mathbf{\Omega}$, which is embarrassingly parallelizable.

## Numerical examples

By this time, the reader has surely formulated a pointed question: Do these randomized matrix approximation algorithms actually work in practice? In this section, we attempt to address this concern by illustrating how the algorithms perform on a diverse collection of test cases.

Section 7.1 starts with two examples from the physical sciences involving discrete approximations to operators with exponentially decaying spectra. Sections 7.2 and 7.3 continue with two examples of matrices arising in "data mining." These are large matrices whose singular spectra decay slowly; one is sparse and fits in RAM, one is dense and is stored out-of-core. Finally, §7.4 investigates the performance of randomized methods based on structured random matrices.

Sections 7.1--7.3 focus on the algorithms for Stage A that we presented in §4 because we wish to isolate the performance of the randomized step.

Computational examples illustrating truly large data matrices have been reported elsewhere, for instance .

### Two matrices with rapidly decaying singular values

We first illustrate the behavior of the adaptive range approximation method, Algorithm LABEL:alg:adaptive2. We apply it to two matrices associated with the numerical analysis of differential and integral operators. The matrices in question have rapidly decaying singular values and our intent is to demonstrate that in this environment, the approximation error of a bare-bones randomized method such as Algorithm LABEL:alg:adaptive2 is *very* close to the minimal error achievable by any method. We observe that the approximation error of a randomized method is itself a random variable (it is a function of the random matrix $\mathbf{\Omega}$) so what we need to demonstrate is not only that the error is small in a typical realization, but also that it clusters tightly around the mean value.

We first consider a $200 \times 200$ matrix $\mathbf{A}$ that results from discretizing the following single-layer operator associated with the Laplace equation: where $\Gamma_{1}$ and $\Gamma_{2}$ are the two contours in ${\mathbb{R}}^{2}$ illustrated in Figure 1(a). We approximate the integral with the trapezoidal rule, which converges superalgebraically because the kernel is smooth. In the absence of floating-point errors, we estimate that the discretization error would be less than $10^{- 20}$ for a smooth source $\sigma$. The leading constant is selected so the matrix $\mathbf{A}$ has unit operator norm.

We implement Algorithm LABEL:alg:adaptive2 in Matlab v6.5. Gaussian test matrices are generated using the randn command. For each number $\ell$ of samples, we compare the following three quantities: The minimum rank-$\ell$ approximation error $\sigma_{\ell + 1}$ is determined using svd.

The actual error $e_{\ell} = \left\| {\left( {\mathbf{I} - {{\mathbf{Q}}^{(\ell)}{({\mathbf{Q}}^{(\ell)})}^{\ast}}} \right){\mathbf{A}}} \right\|$ is computed with norm.

A random estimator $f_{\ell}$ for the actual error $e_{\ell}$ is obtained , with the parameter $r$ set to $5$.

Note that any values less than $10^{- 15}$ should be considered numerical artifacts.

Figure 2 tracks a characteristic execution of Algorithm LABEL:alg:adaptive2. We make three observations: (i) The error $e_{\ell}$ incurred by the algorithm is remarkably close to the theoretical minimum $\sigma_{\ell + 1}$. (ii) The error estimate always produces an upper bound for the actual error. Without the built-in $10 \times$ safety margin, the estimate would track the actual error almost exactly. (iii) The basis constructed by the algorithm essentially reaches full double-precision accuracy.

How typical is the trial documented in Figure 2? To answer this question, we examine the empirical performance of the algorithm over 2000 independent trials. Figure 3 charts the error estimate versus the actual error at four points during the course of execution: $\ell = {25,50,75,100}$. We offer four observations: (i) The initial run detailed in Figure 2 is entirely typical. (ii) Both the actual and estimated error concentrate about their mean value. (iii) The actual error drifts slowly away from the optimal error as the number $\ell$ of samples increases. (iv) The error estimator is *always* pessimistic by a factor of about ten, which means that the algorithm *never* produces a basis with lower accuracy than requested. The only effect of selecting an unlucky sample matrix $\mathbf{\Omega}$ is that the algorithm proceeds for a few additional steps.

Fig. 1: Configurations for physical problems. (a) The contours Γ1 (red) and Γ2 (blue) for the integral operator. (b) Geometry of the lattice problem associated with matrix B in §7.1.

Fig. 2: Approximating a Laplace integral operator. One execution of Algorithm LABEL:alg:adaptive2 for the 200 × 200 input matrix A described in §7.1. The number ℓ of random samples varies along the horizontal axis; the vertical axis measures the base-10 logarithm of error magnitudes. The dashed vertical lines mark the points during execution at which Figure 3 provides additional statistics.

Fig. 3: Error statistics for approximating a Laplace integral operator. 2,000 trials of Algorithm LABEL:alg:adaptive2 applied to a 200 × 200 matrix approximating the integral operator. The panels isolate the moments at which ℓ = 25, 50, 75, 100 random samples have been drawn. Each solid point compares the estimated error fℓ versus the actual error eℓ in one trial; the open circle indicates the trial detailed in Figure 2. The dashed line identifies the minimal error σℓ + 1, and the solid line marks the contour where the error estimator would equal the actual error.

We next consider a matrix $\mathbf{B}$ which is defined implicitly in the sense that we cannot access its elements directly; we can only evaluate the map ${\mathbf{x}}\mapsto{{\mathbf{B}}{\mathbf{x}}}$ for a given vector $\mathbf{x}$. To be precise, $\mathbf{B}$ represents a transfer matrix for a network of resistors like the one shown in Figure 1(b). The vector $\mathbf{x}$ represents a set of electric potentials specified on the red nodes in the figure. These potentials induce a unique equilibrium field on the network in which the potential of each black and blue node is the average of the potentials of its three or four neighbors. The vector ${\mathbf{B}}{\mathbf{x}}$ is then the restriction of the potential to the blue exterior nodes. Given a vector $\mathbf{x}$, the vector ${\mathbf{B}}{\mathbf{x}}$ can be obtained by solving a large sparse linear system whose coefficient matrix is the classical five-point stencil approximating the 2D Laplace operator.

We applied Algorithm LABEL:alg:adaptive2 to the $1596 \times 532$ matrix $\mathbf{B}$ associated with a lattice in which there were $532$ nodes (red) on the "inner ring" and $1596$ nodes on the (blue) "outer ring." Each application of $\mathbf{B}$ to a vector requires the solution of a sparse linear system of size roughly $140\, 000 \times 140\, 000$. We implemented the scheme in Matlab using the "backslash" operator for the linear solve. The results of a typical trial appear in Figure 4. Qualitatively, the performance matches the results in Figure 3.

Fig. 4: Approximating the inverse of a discrete Laplacian. One execution of Algorithm LABEL:alg:adaptive2 for the 1596 × 532 input matrix B described in §7.1. See Figure 2 for notations.

### A large, sparse, noisy matrix arising in image processing

Our next example involves a matrix that arises in image processing. A recent line of work uses information about the local geometry of an image to develop promising new algorithms for standard tasks, such as denoising, inpainting, and so forth. These methods are based on approximating a *graph Laplacian* associated with the image. The dominant eigenvectors of this matrix provide "coordinates" that help us smooth out noisy image patches.

We begin with a $95 \times 95$ pixel grayscale image. The intensity of each pixel is represented as an integer in the range $0$ to $4095$. We form for each pixel $i$ a vector ${\mathbf{x}}^{(i)} \in {\mathbb{R}}^{25}$ by gathering the $25$ intensities of the pixels in a $5 \times 5$ neighborhood centered at pixel $i$ (with appropriate modifications near the edges). Next, we form the $9025 \times 9025$ *weight matrix* $\overset{\sim}{\mathbf{W}}$ that reflects the similarities between patches: where the parameter $\sigma = 50$ controls the level of sensitivity. We obtain a sparse weight matrix $\mathbf{W}$ by zeroing out all entries in $\overset{\sim}{\mathbf{W}}$ except the seven largest ones in each row. The object is then to construct the low frequency eigenvectors of the graph Laplacian matrix where $\mathbf{D}$ is the diagonal matrix with entries $d_{ii} = {\sum_{j}w_{ij}}$. These are the eigenvectors associated with the dominant eigenvalues of the auxiliary matrix ${\mathbf{A}} = {{\mathbf{D}}^{- {1/2}}{\mathbf{W}}{\mathbf{D}}^{- {1/2}}}$.

The matrix $\mathbf{A}$ is large, and its eigenvalues decay slowly, so we use the power scheme summarized in Algorithm LABEL:alg:poweriteration to approximate it. Figure 5\[left\] illustrates how the approximation error $e_{\ell}$ declines as the number $\ell$ of samples increases. When we set the exponent $q = 0$, which corresponds with the basic Algorithm LABEL:alg:basic, the approximation is rather poor. The graph illustrates that increasing the exponent $q$ slightly results in a tremendous improvement in the accuracy of the power scheme.

Next, we illustrate the results of using the two-stage approach to approximate the eigenvalues of $\mathbf{A}$. In Stage A, we construct a basis for $\mathbf{A}$ using Algorithm LABEL:alg:poweriteration with $\ell = 100$ samples for different values of $q$. In Stage B, we apply the Hermitian variant of Algorithm LABEL:alg:Atranspose described in §5.3 to compute an approximate eigenvalue decomposition. Figure 5\[right\] shows the approximate eigenvalues and the actual eigenvalues of $\mathbf{A}$. Once again, we see that the minimal exponent $q = 0$ produces miserable results, but the largest eigenvalues are quite accurate even for $q = 1$.

Fig. 5: Approximating a graph Laplacian. For varying exponent q, one trial of the power scheme, Algorithm LABEL:alg:poweriteration, applied to the 9025 × 9025 matrix A described in §7.2. [Left] Approximation errors as a function of the number ℓ of random samples. [Right] Estimates for the 100 largest eigenvalues given ℓ = 100 random samples compared with the 100 largest eigenvalues of A.

### Eigenfaces

Our next example involves a large, dense matrix derived from the FERET databank of face images. A simple method for performing face recognition is to identify the principal directions of the image data, which are called *eigenfaces*. Each of the original photographs can be summarized by its components along these principal directions. To identify the subject in a new picture, we compute its decomposition in this basis and use a classification technique, such as nearest neighbors, to select the closest image in the database.

We construct a data matrix $\mathbf{A}$ as follows: The FERET database contains $7254$ images, and each $384 \times 256$ image contains $98\, 304$ pixels. First, we build a $98\, 304 \times 7254$ matrix $\overset{\sim}{\mathbf{A}}$ whose columns are the images. We form $\mathbf{A}$ by centering each column of $\overset{\sim}{\mathbf{A}}$ and scaling it to unit norm, so that the images are roughly comparable. The eigenfaces are the dominant left singular vectors of this matrix.

Our goal then is to compute an approximate SVD of the matrix $\mathbf{A}$. Represented as an array of double-precision real numbers, $\mathbf{A}$ would require $5.4$ GB of storage, which does not fit within the fast memory of many machines. It is possible to compress the database down to at $57$ MB or less (in JPEG format), but then the data would have to be uncompressed with each sweep over the matrix. Furthermore, the matrix $\mathbf{A}$ has slowly decaying singular values, so we need to use the power scheme, Algorithm LABEL:alg:poweriteration, to capture the range of the matrix accurately.

To address these concerns, we implemented the power scheme to run in a pass-efficient manner. An additional difficulty arises because the size of the data makes it expensive to calculate the actual error $e_{\ell}$ incurred by the approximation or to determine the minimal error $\sigma_{\ell + 1}$. To estimate the errors, we use the technique described in Remark 4.1.

Figure 6 describes the behavior of the power scheme, which is similar to its performance for the graph Laplacian in §7.2. When the exponent $q = 0$, the approximation of the data matrix is very poor, but it improves quickly as $q$ increases. Likewise, the estimate for the spectrum of $\mathbf{A}$ appears to converge rapidly; the largest singular values are already quite accurate when $q = 1$. We see essentially no improvement in the estimates after the first 3--5 passes over the matrix.

Fig. 6: Computing eigenfaces. For varying exponent q, one trial of the power scheme, Algorithm LABEL:alg:poweriteration, applied to the 98 304 × 7254 matrix A described in §7.3. (Left) Approximation errors as a function of the number ℓ of random samples. The red line indicates the minimal errors as estimated by the singular values computed using ℓ = 100 and q = 3. (Right) Estimates for the 100 largest eigenvalues given ℓ = 100 random samples.

### Performance of structured random matrices

Our final set of experiments illustrates that the structured random matrices described in §4.6 lead to matrix approximation algorithms that are both fast and accurate.

First, we compare the computational speeds of four methods for computing an approximation to the $\ell$ dominant terms in the SVD of an $n \times n$ matrix $\mathbf{A}$. For now, we are interested in execution time only (not accuracy), so the choice of matrix is irrelevant and we have selected $\mathbf{A}$ to be a Gaussian matrix. The four methods are summarized in the following table; Remark 7.1 provides more details on the implementation.

Method Stage A Stage B Table 1 lists the measured runtime of a single execution of each algorithm for various choices of the dimension $n$ of the input matrix and the rank $\ell$ of the approximation. Of course, the cost of the full SVD does not depend on the number $\ell$ of components required. A more informative way to look at the runtime data is to compare the *relative* cost of the algorithms. The direct method is the best deterministic approach for dense matrices, so we calculate the factor by which the randomized methods improve on this benchmark. Figure 7 displays the results. We make two observations: (i) Using an SRFT often leads to a dramatic speed-up over classical techniques, even for moderate problem sizes. (ii) Using a standard Gaussian test matrix typically leads to a moderate speed-up over classical methods, primarily because performing a matrix--matrix multiplication is faster than a QR factorization.

Second, we investigate how the choice of random test matrix influences the error in approximating an input matrix. For these experiments, we return to the $200 \times 200$ matrix $\mathbf{A}$ defined in Section 7.1. Consider variations of Algorithm LABEL:alg:basic obtained when the random test matrix $\mathbf{\Omega}$ is drawn from the following four distributions: Intuitively, we expect that Ortho should provide the best performance.

For each distribution, we perform 100 000 trials of the following experiment. Apply the corresponding version of Algorithm LABEL:alg:basic to the matrix $\mathbf{A}$, and calculate the approximation error $e_{\ell} = \left\| {{\mathbf{A}} - {{\mathbf{Q}}_{\ell}{\mathbf{Q}}_{\ell}^{\ast}{\mathbf{A}}}} \right\|$. Figure 8 displays the empirical probability density function for the error $e_{\ell}$ obtained with each algorithm. We offer three observations: (i) The SRFT actually performs slightly better than a Gaussian random matrix for this example. (ii) The standard SRFT and the modified SRFT have essentially identical errors. (iii) There is almost no difference between the Gaussian random matrix and the random orthonormal matrix in the first three plots, while the fourth plot shows that the random orthonormal matrix performs better. This behavior occurs because, with high probability, a tall Gaussian matrix is well conditioned and a (nearly) square Gaussian matrix is not.

### Remark 7.1

The running times reported in Table 1 and in Figure 7 depend strongly on both the computer hardware and the coding of the algorithms. The experiments reported here were performed on a standard office desktop with a 3.2 GHz Pentium IV processor and 2 GB of RAM. The algorithms were implemented in Fortran 90 and compiled with the Lahey compiler. The Lahey versions of BLAS and LAPACK were used to accelerate all matrix--matrix multiplications, as well as the SVD computations in Algorithms LABEL:alg:Atranspose and LABEL:alg:extractrows. We used the code for the modified SRFT provided in the publicly available software package id$\underset{¯}{\ }$dist.

Table 1: Computational times for a partial SVD. The time, in seconds, required to compute the ℓ leading components in the SVD of an n × n matrix using each of the methods from §7.4. The last row indicates the time needed to obtain a full SVD.

Fig. 7: Acceleration factor. The relative cost of computing an ℓ-term partial SVD of an n × n Gaussian matrix using direct, a benchmark classical algorithm, versus each of the three competitors described in §7.4. The solid red curve shows the speedup using an SRFT test matrix, and the dotted blue curve shows the speedup with a Gaussian test matrix. The dashed green curve indicates that a full SVD computation using classical methods is substantially slower. Table 1 reports the absolute runtimes that yield the circled data points.

Fig. 8: Empirical probability density functions for the error in Algorithm LABEL:alg:basic. As described in §7.4, the algorithm is implemented with four distributions for the random test matrix and used to approximate the 200 × 200 input matrix obtained by discretizing the integral operator. The four panels capture the empirical error distribution for each version of the algorithm at the moment when ℓ = 25, 50, 75, 100 random samples have been drawn.

Part III: Theory This part of the paper, §§8--11, provides a detailed analysis of randomized sampling schemes for constructing an approximate basis for the range of a matrix, the task we refer to as Stage A in the framework of §1.2. More precisely, we assess the quality of the basis $\mathbf{Q}$ that the proto-algorithm of §1.3 produces by establishing rigorous bounds for the approximation error where $\left| \middle| \middle| \cdot \middle| \middle| \right|$ denotes either the spectral norm or the Frobenius norm. The difficulty in developing these bounds is that the matrix $\mathbf{Q}$ is random, and its distribution is a complicated nonlinear function of the input matrix $\mathbf{A}$ and the random test matrix $\mathbf{\Omega}$. Naturally, any estimate for the approximation error must depend on the properties of the input matrix and the distribution of the test matrix.

To address these challenges, we split the argument into two pieces. The first part exploits techniques from linear algebra to deliver a generic error bound that depends on the interaction between the test matrix $\mathbf{\Omega}$ and the right singular vectors of the input matrix $\mathbf{A}$, as well as the tail singular values of $\mathbf{A}$. In the second part of the argument, we take into account the distribution of the random matrix to estimate the error for specific instantiations of the proto-algorithm. This bipartite proof is common in the literature on randomized linear algebra, but our argument is most similar in spirit to.

Section 8 surveys the basic linear algebraic tools we need. Section 9 uses these methods to derive a generic error bound. Afterward, we specialize these results to the case where the test matrix is Gaussian (§10) and the case where the test matrix is a subsampled random Fourier transform (§11).

## Theoretical preliminaries

We proceed with some additional background from linear algebra. Section 8.1 sets out properties of positive-semidefinite matrices, and §8.2 offers some results for orthogonal projectors. Standard references for this material include.

### Positive semidefinite matrices

An Hermitian matrix $\mathbf{M}$ is *positive semidefinite* (briefly, *psd*) when ${{\mathbf{u}}^{\ast}{\mathbf{M}}{\mathbf{u}}} \geq 0$ for all ${\mathbf{u}} \neq \mathbf{0}$. If the inequalities are strict, $\mathbf{M}$ is *positive definite* (briefly, *pd*). The psd matrices form a convex cone, which induces a partial ordering on the linear space of Hermitian matrices: ${\mathbf{M}} \preccurlyeq {\mathbf{N}}$ if and only if ${\mathbf{N}} - {\mathbf{M}}$ is psd. This ordering allows us to write ${\mathbf{M}} \succcurlyeq \mathbf{0}$ to indicate that the matrix $\mathbf{M}$ is psd.

Alternatively, we can define a psd (resp., pd) matrix as an Hermitian matrix with nonnegative (resp., positive) eigenvalues. In particular, each psd matrix is diagonalizable, and the inverse of a pd matrix is also pd. The spectral norm of a psd matrix $\mathbf{M}$ has the variational characterization according to the Rayleigh--Ritz theorem \[72, Thm. 4.2.2\]. It follows that A fundamental fact is that conjugation preserves the psd property.

### Proposition 5 (Conjugation Rule)

Suppose that $\mathbf{M} \succcurlyeq \mathbf{0}$. For every $\mathbf{A}$, the matrix ${\mathbf{A}^{\ast}\mathbf{M}\mathbf{A}} \succcurlyeq \mathbf{0}$. In particular, Our argument invokes the conjugation rule repeatedly. As a first application, we establish a perturbation bound for the matrix inverse near the identity matrix.

### Proposition 6 (Perturbation of Inverses)

Suppose that $\mathbf{M} \succcurlyeq \mathbf{0}$. Then

### Proof

Define ${\mathbf{R}} = {\mathbf{M}}^{1/2}$, the psd square root of $\mathbf{M}$ promised by \[72, Thm. 7.2.6\]. We have the chain of relations The first equality can be verified algebraically. The second holds because rational functions of a diagonalizable matrix, such as $\mathbf{R}$, commute. The last relation follows from the conjugation rule because ${({\mathbf{I} + {\mathbf{R}}^{2}})}^{- 1} \preccurlyeq \mathbf{I}$. ∎ Next, we present a generalization of the fact that the spectral norm of a psd matrix is controlled by its trace.

### Proposition 7

We have $\left\| \mathbf{M} \right\| \leq {\left\| \mathbf{A} \right\| + \left\| \mathbf{C} \right\|}$ for each partitioned psd matrix

### Proof

The variational characterization of the spectral norm implies that The block generalization of Hadamard's psd criterion \[72, Thm. 7.7.7\] states that $\left\| {\mathbf{B}} \right\|^{2} \leq {\left\| {\mathbf{A}} \right\|\left\| {\mathbf{C}} \right\|}$. Thus, This point completes the argument. ∎

### Orthogonal projectors

An *orthogonal projector* is an Hermitian matrix $\mathbf{P}$ that satisfies the polynomial ${\mathbf{P}}^{2} = {\mathbf{P}}$. This identity implies $\mathbf{0} \preccurlyeq {\mathbf{P}} \preccurlyeq \mathbf{I}$. An orthogonal projector is completely determined by its range. For a given matrix $\mathbf{M}$, we write ${\mathbf{P}}_{\mathbf{M}}$ for the unique orthogonal projector with ${{range}{({\mathbf{P}}_{\mathbf{M}})}} = {{range}{({\mathbf{M}})}}$. When $\mathbf{M}$ has full column rank, we can express this projector explicitly: The orthogonal projector onto the complementary subspace, ${range}{({\mathbf{P}})}^{\perp}$, is the matrix $\mathbf{I} - {\mathbf{P}}$. Our argument hinges on several other facts about orthogonal projectors.

### Proposition 8

Suppose $\mathbf{U}$ is unitary. Then ${\mathbf{U}^{\ast}\mathbf{P}_{\mathbf{M}}\mathbf{U}} = \mathbf{P}_{\mathbf{U}^{\ast}\mathbf{M}}$.

### Proof

Abbreviate ${\mathbf{P}} = {{\mathbf{U}}^{\ast}{\mathbf{P}}_{\mathbf{M}}{\mathbf{U}}}$. It is clear that $\mathbf{P}$ is an orthogonal projector since it is Hermitian and ${\mathbf{P}}^{2} = {\mathbf{P}}$. Evidently, Since the range determines the orthogonal projector, we conclude ${\mathbf{P}} = {\mathbf{P}}_{{\mathbf{U}}^{\ast}{\mathbf{M}}}$. ∎

### Proposition 9

Suppose ${{range}{(\mathbf{N})}} \subset {{range}{(\mathbf{M})}}$. Then, for each matrix $\mathbf{A}$, it holds that $\left\| {\mathbf{P}_{\mathbf{N}}\mathbf{A}} \right\| \leq \left\| {\mathbf{P}_{\mathbf{M}}\mathbf{A}} \right\|$ and that $\left\| {{({\mathbf{I} - \mathbf{P}_{\mathbf{M}}})}\mathbf{A}} \right\| \leq \left\| {{({\mathbf{I} - \mathbf{P}_{\mathbf{N}}})}\mathbf{A}} \right\|$.

### Proof

The projector ${\mathbf{P}}_{\mathbf{N}} \preccurlyeq \mathbf{I}$, so the conjugation rule yields ${{\mathbf{P}}_{\mathbf{M}}{\mathbf{P}}_{\mathbf{N}}{\mathbf{P}}_{\mathbf{M}}} \preccurlyeq {\mathbf{P}}_{\mathbf{M}}$. The hypothesis ${{range}{({\mathbf{N}})}} \subset {{range}{({\mathbf{M}})}}$ implies that ${{\mathbf{P}}_{\mathbf{M}}{\mathbf{P}}_{\mathbf{N}}} = {\mathbf{P}}_{\mathbf{N}}$, which results in In summary, ${\mathbf{P}}_{\mathbf{N}} \preccurlyeq {\mathbf{P}}_{\mathbf{M}}$. The conjugation rule shows that ${{\mathbf{A}}^{\ast}{\mathbf{P}}_{\mathbf{N}}{\mathbf{A}}} \preccurlyeq {{\mathbf{A}}^{\ast}{\mathbf{P}}_{\mathbf{M}}{\mathbf{A}}}$. We conclude from that The second statement follows from the first by taking orthogonal complements. ∎ Finally, we need a generalization of the scalar inequality $\left| {px} \right|^{q} \leq {|p||x|^{q}}$, which holds when $|p| \leq 1$ and $q \geq 1$.

### Proposition 10

Let $\mathbf{P}$ be an orthogonal projector, and let $\mathbf{M}$ be a matrix. For each positive number $q$,

### Proof

Suppose that $\mathbf{R}$ is an orthogonal projector, $\mathbf{D}$ is a nonnegative diagonal matrix, and $t \geq 1$. We claim that Granted this inequality, we quickly complete the proof. Using an SVD ${\mathbf{M}} = {{\mathbf{U}}\mathbf{\Sigma}{\mathbf{V}}^{\ast}}$, we compute We have used the unitary invariance of the spectral norm in the second and fourth relations. The inequality applies because ${\mathbf{U}}^{\ast}{\mathbf{P}}{\mathbf{U}}$ is an orthogonal projector. Take a square root to finish the argument.

Now, we turn to the claim. This relation follows immediately from \[11, Thm. IX.2.10\], but we offer a direct argument based on more elementary considerations. Let $\mathbf{x}$ be a unit vector at which We must have ${{\mathbf{R}}{\mathbf{x}}} = {\mathbf{x}}$. Otherwise, $\left\| {{\mathbf{R}}{\mathbf{x}}} \right\| < 1$ because $\mathbf{R}$ is an orthogonal projector, which implies that the unit vector ${\mathbf{y}} = {{{\mathbf{R}}{\mathbf{x}}}/\left\| {{\mathbf{R}}{\mathbf{x}}} \right\|}$ verifies Writing $x_{j}$ for the entries of $\mathbf{x}$ and $d_{j}$ for the diagonal entries of $\mathbf{D}$, we find that The inequality is Jensen's, which applies because ${\sum x_{j}^{2}} = 1$ and the function $z\mapsto|z|^{t}$ is convex for $t \geq 1$. ∎

## Error bounds via linear algebra

We are now prepared to develop a deterministic error analysis for the proto-algorithm described in §1.3. To begin, we must introduce some notation. Afterward, we establish the key error bound, which strengthens a result from the literature \[17, Lem. 4.2\]. Finally, we explain why the power method can be used to improve the performance of the proto-algorithm.

### Setup

Let $\mathbf{A}$ be an $m \times n$ matrix that has a singular value decomposition ${\mathbf{A}} = {{\mathbf{U}}\mathbf{\Sigma}{\mathbf{V}}^{\ast}}$, as described in Section 3.2.2 ‣ 3.2 Standard matrix factorizations ‣ 3 Linear algebraic preliminaries ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"). Roughly speaking, the proto-algorithm tries to approximate the subspace spanned by the first $k$ left singular vectors, where $k$ is now a fixed number. To perform the analysis, it is appropriate to partition the singular value decomposition as follows.

\end{matrix}\lbrack} & \begin{matrix} \end{matrix} & \begin{matrix} \end{matrix} & {\rbrack\begin{matrix} \end{matrix}} & \begin{bmatrix} \end{bmatrix} & \begin{matrix} The matrices $\mathbf{\Sigma}_{1}$ and $\mathbf{\Sigma}_{2}$ are square. We will see that the left unitary factor $\mathbf{U}$ does not play a significant role in the analysis.

Let $\mathbf{\Omega}$ be an $n \times \ell$ test matrix, where $\ell$ denotes the number of samples. We assume only that $\ell \geq k$. Decompose the test matrix in the coordinate system determined by the right unitary factor of $\mathbf{A}$: The error bound for the proto-algorithm depends critically on the properties of the matrices $\mathbf{\Omega}_{1}$ and $\mathbf{\Omega}_{2}$. With this notation, the sample matrix $\mathbf{Y}$ can be expressed as \end{matrix}\lbrack} & \begin{matrix} {\mathbf{\Sigma}_{1}\mathbf{\Omega}_{1}} \\{\mathbf{\Sigma}_{2}\mathbf{\Omega}_{2}} \end{matrix} & {\rbrack\begin{matrix} It is a useful intuition that the block $\mathbf{\Sigma}_{1}\mathbf{\Omega}_{1}$ in (9.1) reflects the gross behavior of $\mathbf{A}$, while the block $\mathbf{\Sigma}_{2}\mathbf{\Omega}_{2}$ represents a perturbation.

### A deterministic error bound for the proto-algorithm

The proto-algorithm constructs an orthonormal basis $\mathbf{Q}$ for the range of the sample matrix $\mathbf{Y}$, and our goal is to quantify how well this basis captures the action of the input $\mathbf{A}$. Since ${{\mathbf{Q}}{\mathbf{Q}}^{\ast}} = {\mathbf{P}}_{\mathbf{Y}}$, the challenge is to obtain bounds on the approximation error The following theorem shows that the behavior of the proto-algorithm depends on the interaction between the test matrix and the right singular vectors of the input matrix, as well as the singular spectrum of the input matrix.

### Theorem 11 (Deterministic error bound)

Let $\mathbf{A}$ be an $m \times n$ matrix with singular value decomposition $\mathbf{A} = {\mathbf{U}\mathbf{\Sigma}\mathbf{V}^{\ast}}$, and fix $k \geq 0$. Choose a test matrix $\mathbf{\Omega}$, and construct the sample matrix $\mathbf{Y} = {\mathbf{A}\mathbf{\Omega}}$. Partition $\mathbf{\Sigma}$ as specified, and define $\mathbf{\Omega}_{1}$ and $\mathbf{\Omega}_{2}$ via. Assuming that $\mathbf{\Omega}_{1}$ has full row rank, the approximation error satisfies where $\left| \middle| \middle| \cdot \middle| \middle| \right|$ denotes either the spectral norm or the Frobenius norm.

Theorem 11. ‣ 9.2 A deterministic error bound for the proto-algorithm ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") sharpens the result \[17, Lem. 2\], which lacks the squares present in (55. ‣ 9.2 A deterministic error bound for the proto-algorithm ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions")). This refinement yields slightly better error estimates than the earlier bound, and it has consequences for the probabilistic behavior of the error when the test matrix $\mathbf{\Omega}$ is random. The proof here is different in spirit from the earlier analysis; our argument is inspired by the perturbation theory of orthogonal projectors.

### Proof

We establish the bound for the spectral-norm error. The bound for the Frobenius-norm error follows from an analogous argument that is slightly easier.

Let us begin with some preliminary simplifications. First, we argue that the left unitary factor $\mathbf{U}$ plays no essential role in the argument. In effect, we execute the proof for an auxiliary input matrix $\overset{\sim}{\mathbf{A}}$ and an associated sample matrix $\overset{\sim}{\mathbf{Y}}$ defined by Owing to the unitary invariance of the spectral norm and to Proposition 8, we have the identity In view of, it suffices to prove that Second, we assume that the number $k$ is chosen so the diagonal entries of $\mathbf{\Sigma}_{1}$ are strictly positive. Suppose not. Then $\mathbf{\Sigma}_{2}$ is zero because of the ordering of the singular values. As a consequence, This calculation uses the decompositions presented, as well as the fact that both ${\mathbf{V}}_{1}^{\ast}$ and $\mathbf{\Omega}_{1}$ have full row rank. We conclude that so the error bound holds trivially. (In fact, both sides are zero.)

The main argument is based on ideas from perturbation theory. To illustrate the concept, we start with a matrix related to $\overset{\sim}{\mathbf{Y}}$: \end{matrix}\lbrack} & \begin{matrix} {\mathbf{\Sigma}_{1}\mathbf{\Omega}_{1}} \\\end{matrix} & {\rbrack\begin{matrix} The matrix $\mathbf{W}$ has the same range as a related matrix formed by "flattening out" the spectrum of the top block. Indeed, since $\mathbf{\Sigma}_{1}\mathbf{\Omega}_{1}$ has full row rank, \end{matrix}\lbrack} & \begin{matrix} \end{matrix} & {\rbrack\begin{matrix} The matrix on the right-hand side has full column rank, so it is legal to apply the formula for an orthogonal projector, which immediately yields In words, the range of $\mathbf{W}$ aligns with the first $k$ coordinates, which span the same subspace as the first $k$ left singular vectors of the auxiliary input matrix $\overset{\sim}{\mathbf{A}}$. Therefore, ${range}{({\mathbf{W}})}$ captures the action of $\overset{\sim}{\mathbf{A}}$, which is what we wanted from ${range}{(\overset{\sim}{\mathbf{Y}})}$.

We treat the auxiliary sample matrix $\overset{\sim}{\mathbf{Y}}$ as a perturbation of $\mathbf{W}$, and we hope that their ranges are close to each other. To make the comparison rigorous, let us emulate the arguments outlined in the last paragraph. Referring to the display, we flatten out the top block of $\overset{\sim}{\mathbf{Y}}$ to obtain the matrix Let us return to the error bound. The construction ensures that ${{range}{({\mathbf{Z}})}} \subset {{range}{(\overset{\sim}{\mathbf{Y}})}}$, so Proposition 9 implies that the error satisfies Squaring this relation, we obtain The last identity follows from the definition $\overset{\sim}{\mathbf{A}} = {\mathbf{\Sigma}{\mathbf{V}}^{\ast}}$ and the unitary invariance of the spectral norm. Therefore, we can complete the proof of by producing a suitable bound for the right-hand side of.

To continue, we need a detailed representation of the projector $\mathbf{I} - {\mathbf{P}}_{\mathbf{Z}}$. The construction ensures that $\mathbf{Z}$ has full column rank, so we can apply the formula for an orthogonal projector to see that Expanding this expression, we determine that the complementary projector satisfies The partitioning here conforms with the partitioning of $\mathbf{\Sigma}$. When we conjugate the matrix by $\mathbf{\Sigma}$, copies of $\mathbf{\Sigma}_{1}^{- 1}$, presently hidden in the top-left block, will cancel to happy effect.

The latter point may not seem obvious, owing to the complicated form of. In reality, the block matrix is less fearsome than it looks. Proposition 6. ‣ 8.1 Positive semidefinite matrices ‣ 8 Theoretical preliminaries ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"), on the perturbation of inverses, shows that the top-left block verifies The bottom-right block satisfies because the conjugation rule guarantees that ${{\mathbf{F}}{({\mathbf{I} + {{\mathbf{F}}^{\ast}{\mathbf{F}}}})}^{- 1}{\mathbf{F}}^{\ast}} \succcurlyeq \mathbf{0}$. We abbreviate the off-diagonal blocks with the symbol ${\mathbf{B}} = {- {{({\mathbf{I} + {{\mathbf{F}}^{\ast}{\mathbf{F}}}})}^{- 1}{\mathbf{F}}^{\ast}}}$. In summary, This relation exposes the key structural properties of the projector. Compare this relation with the expression for the "ideal" projector $\mathbf{I} - {\mathbf{P}}_{\mathbf{W}}$.

Moving toward the estimate required, we conjugate the last relation by $\mathbf{\Sigma}$ to obtain The conjugation rule demonstrates that the matrix on the left-hand side is psd, so the matrix on the right-hand side is too. Proposition 7 results in the norm bound Recall that ${\mathbf{F}} = {\mathbf{\Sigma}_{2}\mathbf{\Omega}_{2}\mathbf{\Omega}_{1}^{\dagger}\mathbf{\Sigma}_{1}^{- 1}}$, so the factor $\mathbf{\Sigma}_{1}$ cancels neatly. Therefore, Finally, introduce the latter inequality into to complete the proof. ∎

### Analysis of the power scheme

Theorem 11. ‣ 9.2 A deterministic error bound for the proto-algorithm ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") suggests that the performance of the proto-algorithm depends strongly on the relationship between the large singular values of $\mathbf{A}$ listed in $\mathbf{\Sigma}_{1}$ and the small singular values listed in $\mathbf{\Sigma}_{2}$. When a substantial proportion of the mass of $\mathbf{A}$ appears in the small singular values, the constructed basis $\mathbf{Q}$ may have low accuracy. Conversely, when the large singular values dominate, it is much easier to identify a good low-rank basis.

To improve the performance of the proto-algorithm, we can run it with a closely related input matrix whose singular values decay more rapidly. Fix a positive integer $q$, and set We apply the proto-algorithm to $\mathbf{B}$, which generates a sample matrix ${\mathbf{Z}} = {{\mathbf{B}}\mathbf{\Omega}}$ and constructs a basis $\mathbf{Q}$ for the range of $\mathbf{Z}$. Section 4.5 elaborates on the implementation details, and describes a reformulation that sometimes improves the accuracy when the scheme is executed in finite-precision arithmetic. The following result describes how well we can approximate the *original* matrix $\mathbf{A}$ within the range of $\mathbf{Z}$.

### Theorem 12 (Power scheme)

Let $\mathbf{A}$ be an $m \times n$ matrix, and let $\mathbf{\Omega}$ be an $n \times \ell$ matrix. Fix a nonnegative integer $q$, form $\mathbf{B} = {{({\mathbf{A}^{\ast}\mathbf{A}})}^{q}\mathbf{A}}$, and compute the sample matrix $\mathbf{Z} = {\mathbf{B}\mathbf{\Omega}}$. Then

### Proof

as a direct consequence of Proposition 10. ∎ Let us illustrate how the power scheme interacts with the main error bound (55. ‣ 9.2 A deterministic error bound for the proto-algorithm ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions")). Let $\sigma_{k + 1}$ denote the $({k + 1})$th singular value of $\mathbf{A}$. First, suppose we approximate $\mathbf{A}$ in the range of the sample matrix ${\mathbf{Y}} = {{\mathbf{A}}\mathbf{\Omega}}$. Since $\left\| \mathbf{\Sigma}_{2} \right\| = \sigma_{k + 1}$, Theorem 11. ‣ 9.2 A deterministic error bound for the proto-algorithm ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") implies that Now, define ${\mathbf{B}} = {{({{\mathbf{A}}{\mathbf{A}}^{\ast}})}^{q}{\mathbf{A}}}$, and suppose we approximate $\mathbf{A}$ within the range of the sample matrix ${\mathbf{Z}} = {{\mathbf{B}}\mathbf{\Omega}}$. Together, Theorem 12. ‣ 9.3 Analysis of the power scheme ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") and Theorem 11. ‣ 9.2 A deterministic error bound for the proto-algorithm ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") imply that because $\sigma_{k + 1}^{{2q} + 1}$ is the $({k + 1})$th singular value of $\mathbf{B}$. In effect, the power scheme drives down the suboptimality of the bound exponentially fast as the power $q$ increases. In principle, we can make the extra factor as close to one as we like, although this increases the cost of the algorithm.

### Analysis of truncated SVD

Finally, let us study the truncated SVD described in Remark 5.1. Suppose that we approximate the input matrix $\mathbf{A}$ inside the range of the sample matrix $\mathbf{Z}$. In essence, the truncation step computes a best rank-$k$ approximation ${\hat{\mathbf{A}}}_{(k)}$ of the compressed matrix ${\mathbf{P}}_{\mathbf{Z}}{\mathbf{A}}$. The next result provides a simple error bound for this method; this argument was proposed by Ming Gu.

### Theorem 13 (Analysis of Truncated SVD)

Let $\mathbf{A}$ be an $m \times n$ matrix with singular values $\sigma_{1} \geq \sigma_{2} \geq \sigma_{3} \geq \ldots$, and let $\mathbf{Z}$ be an $m \times \ell$ matrix, where $\ell \geq k$. Suppose that ${\hat{\mathbf{A}}}_{(k)}$ is a best rank-$k$ approximation of $\mathbf{P}_{\mathbf{Z}}\mathbf{A}$ with respect to the spectral norm. Then

### Proof

Apply the triangle inequality to split the error into two components.

We have already developed a detailed theory for estimating the first term. To analyze the second term, we introduce a best rank-$k$ approximation ${\mathbf{A}}_{(k)}$ of the matrix $\mathbf{A}$. Note that because ${\hat{\mathbf{A}}}_{(k)}$ is a best rank-$k$ approximation to the matrix ${\mathbf{P}}_{\mathbf{Z}}{\mathbf{A}}$, whereas ${\mathbf{P}}_{\mathbf{Z}}{\mathbf{A}}_{(k)}$ is an undistinguished rank-$k$ matrix. It follows that The second inequality holds because the orthogonal projector is a contraction; the last identity follows from Mirsky's theorem. Combine and to reach the main result. ∎

### Remark 9.1

In the randomized setting, the truncation step appears to be less damaging than the error bound of Theorem 13. ‣ 9.4 Analysis of truncated SVD ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") suggests, but we currently lack a complete theoretical understanding of its behavior.

## Gaussian test matrices

The error bound in Theorem 11. ‣ 9.2 A deterministic error bound for the proto-algorithm ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") shows that the performance of the proto-algorithm depends on the interaction between the test matrix $\mathbf{\Omega}$ and the right singular vectors of the input matrix $\mathbf{A}$. Algorithm LABEL:alg:basic is a particularly simple version of the proto-algorithm that draws the test matrix according to the standard Gaussian distribution. The literature contains a wealth of information about these matrices, which allows us to perform a very precise error analysis.

We focus on the real case in this section. Analogous results hold in the complex case, where the algorithm even exhibits superior performance.

### Technical background

A *standard Gaussian matrix* is a random matrix whose entries are independent standard normal variables. The distribution of a standard Gaussian matrix is rotationally invariant: If $\mathbf{U}$ and $\mathbf{V}$ are orthonormal matrices, then ${\mathbf{U}}^{\ast}{\mathbf{G}}{\mathbf{V}}$ also has the standard Gaussian distribution.

Our analysis requires detailed information about the properties of Gaussian matrices. In particular, we must understand how the norm of a Gaussian matrix and its pseudoinverse vary. We summarize the relevant results and citations here, reserving the details for Appendix A.

### Proposition 14 (Expected norm of a scaled Gaussian matrix)

Fix matrices $\mathbf{S},\mathbf{T}$, and draw a standard Gaussian matrix $\mathbf{G}$. Then The identity (66. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions")) follows from a direct calculation. The second bound (67. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions")) relies on methods developed by Gordon. See Propositions 26 and 27.

### Proposition 15 (Expected norm of a pseudo-inverted Gaussian matrix)

Draw a $k \times {({k + p})}$ standard Gaussian matrix $\mathbf{G}$ with $k \geq 2$ and $p \geq 2$. Then The first identity is a standard result from multivariate statistics \[99, p. 96\]. The second follows from work of Chen and Dongarra. See Proposition 29 and 30.

To study the probability that Algorithm LABEL:alg:basic produces a large error, we rely on tail bounds for functions of Gaussian matrices. The next proposition rephrases a well-known result on concentration of measure \[14, Thm. 4.5.7\]. See also \[83, §1.1\] and \[82, §5.1\].

### Proposition 16 (Concentration for functions of a Gaussian matrix)

Suppose that $h$ is a Lipschitz function on matrices: Draw a standard Gaussian matrix $\mathbf{G}$. Then Finally, we state some large deviation bounds for the norm of a pseudo-inverted Gaussian matrix.

### Proposition 17 (Norm bounds for a pseudo-inverted Gaussian matrix)

Let $\mathbf{G}$ be a $k \times {({k + p})}$ Gaussian matrix where $p \geq 4$. For all $t \geq 1$, Compare these estimates with Proposition 15. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"). It seems that (70. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions")) is new; we were unable to find a comparable analysis in the random matrix literature. Although the form of (70. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions")) is not optimal, it allows us to produce more transparent results than a fully detailed estimate. The bound (71. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions")) essentially appears in the work of Chen and Dongarra. See Propositions 28 and Theorem 31 for more information.

### Average-case analysis of Algorithm LABEL:alg:basic

We separate our analysis into two pieces. First, we present information about expected values. In the next subsection, we describe bounds on the probability of a large deviation.

We begin with the simplest result, which provides an estimate for the expected approximation error in the Frobenius norm. All proofs are postponed to the end of the section.

### Theorem 18 (Average Frobenius error)

Suppose that $\mathbf{A}$ is a *real* $m \times n$ matrix with singular values $\sigma_{1} \geq \sigma_{2} \geq \sigma_{3} \geq \ldots$. Choose a target rank $k \geq 2$ and an oversampling parameter $p \geq 2$, where ${k + p} \leq {\min{\{ m,n\}}}$. Draw an $n \times {({k + p})}$ standard Gaussian matrix $\mathbf{\Omega}$, and construct the sample matrix $\mathbf{Y} = {\mathbf{A}\mathbf{\Omega}}$. Then the expected approximation error This theorem predicts several intriguing behaviors of Algorithm LABEL:alg:basic. The Eckart--Young theorem shows that ${({\sum_{j > k}\sigma_{j}^{2}})}^{1/2}$ is the minimal Frobenius-norm error when approximating $\mathbf{A}$ with a rank-$k$ matrix. This quantity is the appropriate benchmark for the performance of the algorithm. If the small singular values of $\mathbf{A}$ are very flat, the series may be as large as $\sigma_{k + 1}\sqrt{{\min{\{ m,n\}}} - k}$. On the other hand, when the singular values exhibit some decay, the error may be on the same order as $\sigma_{k + 1}$.

The error bound always exceeds this baseline error, but it may be polynomially larger, depending on the ratio between the target rank $k$ and the oversampling parameter $p$. For $p$ small (say, less than five), the error is somewhat variable because the small singular values of a nearly square Gaussian matrix are very unstable. As the oversampling increases, the performance improves quickly. When $p \sim k$, the error is already within a constant factor of the baseline.

The error bound for the spectral norm is somewhat more complicated, but it reveals some interesting new features.

### Theorem 19 (Average spectral error)

Under the hypotheses of Theorem 18. ‣ 10.2 Average-case analysis of Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"), Mirsky has shown that the quantity $\sigma_{k + 1}$ is the minimum spectral-norm error when approximating $\mathbf{A}$ with a rank-$k$ matrix, so the first term in Theorem 19. ‣ 10.2 Average-case analysis of Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") is analogous with the error bound in Theorem 18. ‣ 10.2 Average-case analysis of Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"). The second term represents a new phenomenon: we also pay for the Frobenius-norm error in approximating $\mathbf{A}$. Note that, as the amount $p$ of oversampling increases, the polynomial factor in the second term declines much more quickly than the factor in the first term. When $p \sim k$, the factor on the $\sigma_{k + 1}$ term is constant, while the factor on the series has order $k^{- {1/2}}$ We also note that the bound in Theorem 19. ‣ 10.2 Average-case analysis of Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") implies so the average spectral-norm error always lies within a small polynomial factor of the baseline $\sigma_{k + 1}$.

Let us continue with the proofs of these results.

### Theorem 18. ‣ 10.2 Average-case analysis of Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions")

Let $\mathbf{V}$ be the right unitary factor of $\mathbf{A}$. Partition ${\mathbf{V}} = {\lbrack\left. {\mathbf{V}}_{1} \middle| {\mathbf{V}}_{2} \right.\rbrack}$ into blocks containing, respectively, $k$ and $n - k$ columns. Recall that The Gaussian distribution is rotationally invariant, so ${\mathbf{V}}^{\ast}\mathbf{\Omega}$ is also a standard Gaussian matrix. Observe that $\mathbf{\Omega}_{1}$ and $\mathbf{\Omega}_{2}$ are *nonoverlapping* submatrices of ${\mathbf{V}}^{\ast}\mathbf{\Omega}$, so these two matrices are not only standard Gaussian but also stochastically independent. Furthermore, the rows of a (fat) Gaussian matrix are almost surely in general position, so the $k \times {({k + p})}$ matrix $\mathbf{\Omega}_{1}$ has full row rank with probability one.

Hölder's inequality and Theorem 11. ‣ 9.2 A deterministic error bound for the proto-algorithm ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") together imply that We compute this expectation by conditioning on the value of $\mathbf{\Omega}_{1}$ and applying Proposition 14. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") to the scaled Gaussian matrix $\mathbf{\Omega}_{2}$. Thus, where the last expectation follows from relation (68. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions")) of Proposition 15. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"). In summary, Observe that $\left\| \mathbf{\Sigma}_{2} \right\|_{F}^{2} = {\sum_{j > k}\sigma_{j}^{2}}$ to complete the proof. ∎

### Theorem 19. ‣ 10.2 Average-case analysis of Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions")

The argument is similar to the proof of Theorem 18. ‣ 10.2 Average-case analysis of Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"). First, Theorem 11. ‣ 9.2 A deterministic error bound for the proto-algorithm ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") implies that We condition on $\mathbf{\Omega}_{1}$ and apply Proposition 14. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") to bound the expectation with respect to $\mathbf{\Omega}_{2}$. Thus, where the second relation requires Hölder's inequality. Applying both parts of Proposition 15. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"), we obtain Note that $\left\| \mathbf{\Sigma}_{2} \right\| = \sigma_{k + 1}$ to wrap up. ∎

### Probabilistic error bounds for Algorithm LABEL:alg:basic

We can develop tail bounds for the approximation error, which demonstrate that the average performance of the algorithm is representative of the actual performance. We begin with the Frobenius norm because the result is somewhat simpler.

### Theorem 20 (Deviation bounds for the Frobenius error)

Frame the hypotheses of Theorem 18. ‣ 10.2 Average-case analysis of Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"). Assume further that $p \geq 4$. For all ${u,t} \geq 1$, with failure probability at most ${5t^{- p}} + {2e^{- {u^{2}/2}}}$.

To parse this theorem, observe that the first term in the error bound corresponds with the expected approximation error in Theorem 18. ‣ 10.2 Average-case analysis of Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"). The second term represents a deviation above the mean.

An analogous result holds for the spectral norm.

### Theorem 21 (Deviation bounds for the spectral error)

Frame the hypotheses of Theorem 18. ‣ 10.2 Average-case analysis of Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"). Assume further that $p \geq 4$. For all ${u,t} \geq 1$, with failure probability at most ${5t^{- p}} + e^{- {u^{2}/2}}$.

The bracket corresponds with the expected spectral-norm error while the remaining term represents a deviation above the mean. Neither the numerical constants nor the precise form of the bound are optimal because of the slackness in Proposition 17. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"). Nevertheless, the theorem gives a fairly good picture of what is actually happening.

We acknowledge that the current form of Theorem 21. ‣ 10.3 Probabilistic error bounds for Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") is complicated. To produce more transparent results, we make appropriate selections for the parameters $u,t$ and bound the numerical constants.

### Corollary 22 (Simplified deviation bounds for the spectral error)

Frame the hypotheses of Theorem 18. ‣ 10.2 Average-case analysis of Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"), and assume further that $p \geq 4$. Then with failure probability at most $6e^{- p}$. Moreover, with failure probability at most $6p^{- p}$.

### Proof

The first part of the result follows from the choices $t = e$ and $u = \sqrt{2p}$, and the second emerges when $t = p$ and $u = \sqrt{2p{\log p}}$. Another interesting parameter selection is $t = p^{c/p}$ and $u = \sqrt{2c{\log p}}$, which yields a failure probability $6p^{- c}$. ∎ Corollary 22. ‣ 10.3 Probabilistic error bounds for Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") should be compared with \[91, Obs. 4.4--4.5\]. Although our result contains sharper error estimates, the failure probabilities are usually worse. The error bound presented in §1.5 follows after further simplification of the second bound from Corollary 22. ‣ 10.3 Probabilistic error bounds for Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions").

We continue with a proof of Theorem 21. ‣ 10.3 Probabilistic error bounds for Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"). The same argument can be used to obtain a bound for the Frobenius-norm error, but we omit a detailed account.

### Theorem 21. ‣ 10.3 Probabilistic error bounds for Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions")

Since $\mathbf{\Omega}_{1}$ and $\mathbf{\Omega}_{2}$ are independent from each other, we can study how the error depends on the matrix $\mathbf{\Omega}_{2}$ by conditioning on the event that $\mathbf{\Omega}_{1}$ is not too irregular. To that end, we define a (parameterized) event on which the spectral and Frobenius norms of the matrix $\mathbf{\Omega}_{1}^{\dagger}$ are both controlled. For $t \geq 1$, let Invoking both parts of Proposition 17. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"), we find that Consider the function ${h{({\mathbf{X}})}} = {\parallel{\mathbf{\Sigma}_{2}{\mathbf{X}}\mathbf{\Omega}_{1}^{\dagger}}\parallel}$. We quickly compute its Lipschitz constant $L$ with the lower triangle inequality and some standard norm estimates: Therefore, $L \leq {\left\| \mathbf{\Sigma}_{2} \right\|{\parallel\mathbf{\Omega}_{1}^{\dagger}\parallel}}$. Relation (67. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions")) of Proposition 14. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") implies that Applying the concentration of measure inequality, Proposition 16. ‣ 10.1 Technical background ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"), conditionally to the random variable ${h{(\mathbf{\Omega}_{2})}} = {\parallel{\mathbf{\Sigma}_{2}\mathbf{\Omega}_{2}\mathbf{\Omega}_{1}^{\dagger}}\parallel}$ results in Under the event $E_{t}$, we have explicit bounds on the norms of $\mathbf{\Omega}_{1}^{\dagger}$, so Use the fact ${{\mathbb{P}}\left(E_{t}^{c} \right)} \leq {5t^{- p}}$ to remove the conditioning. Therefore, Insert the expressions for the norms of $\mathbf{\Sigma}_{2}$ into this result to complete the probability bound. Finally, introduce this estimate into the error bound from Theorem 11. ‣ 9.2 A deterministic error bound for the proto-algorithm ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"). ∎

### Analysis of the power scheme

Theorem 19. ‣ 10.2 Average-case analysis of Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") makes it clear that the performance of the randomized approximation scheme, Algorithm LABEL:alg:basic, depends heavily on the singular spectrum of the input matrix. The power scheme outlined in Algorithm LABEL:alg:poweriteration addresses this problem by enhancing the decay of spectrum. We can combine our analysis of Algorithm LABEL:alg:basic with Theorem 12. ‣ 9.3 Analysis of the power scheme ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") to obtain a detailed report on the behavior of the performance of the power scheme using a Gaussian matrix.

### Corollary 23 (Average spectral error for the power scheme)

Frame the hypotheses of Theorem 18. ‣ 10.2 Average-case analysis of Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"). Define $\mathbf{B} = {{({\mathbf{A}\mathbf{A}^{\ast}})}^{q}\mathbf{A}}$ for a nonnegative integer $q$, and construct the sample matrix $\mathbf{Z} = {\mathbf{B}\mathbf{\Omega}}$. Then

### Proof

By Hölder's inequality and Theorem 12. ‣ 9.3 Analysis of the power scheme ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"), Invoke Theorem 19. ‣ 10.2 Average-case analysis of Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") to bound the right-hand side, noting that ${\sigma_{j}{({\mathbf{B}})}} = \sigma_{j}^{{2q} + 1}$. ∎ The true message of Corollary 23. ‣ 10.4 Analysis of the power scheme ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") emerges if we bound the series using its largest term $\sigma_{k + 1}^{{4q} + 2}$ and draw the factor $\sigma_{k + 1}$ out of the bracket: In words, as we increase the exponent $q$, the power scheme drives the extra factor in the error to one exponentially fast. By the time $q \sim {\log\left({\min{\{ m,n\}}} \right)}$, which is the baseline for the spectral norm.

In most situations, the error bound given by Corollary 23. ‣ 10.4 Analysis of the power scheme ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") is substantially better than the estimates discussed in the last paragraph. For example, suppose that the tail singular values exhibit the decay profile Then the series in Corollary 23. ‣ 10.4 Analysis of the power scheme ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") is comparable with its largest term, which allows us to remove the dimensional factor $\min{\{ m,n\}}$ from the error bound.

To obtain large deviation bounds for the performance of the power scheme, simply combine Theorem 12. ‣ 9.3 Analysis of the power scheme ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") with Theorem 21. ‣ 10.3 Probabilistic error bounds for Algorithm ‣ 10 Gaussian test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions"). We omit a detailed statement.

### Remark 10.1

We lack an analogous theory for the Frobenius norm because Theorem 12. ‣ 9.3 Analysis of the power scheme ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") depends on Proposition 10, which is not true for the Frobenius norm. It is possible to obtain some results by estimating the Frobenius norm in terms of the spectral norm.

## SRFT test matrices

Another way to implement the proto-algorithm from §1.3 is to use a structured random matrix so that the matrix product in Step 2 can be performed quickly. One type of structured random matrix that has been proposed in the literature is the *subsampled random Fourier transform*, or SRFT, which we discussed in §4.6. In this section, we present bounds on the performance of the proto-algorithm when it is implemented with an SRFT test matrix. In contrast with the results for Gaussian test matrices, the results in this section hold for both real and complex input matrices.

### Construction and Properties

Recall from §4.6 that an SRFT is a tall $n \times \ell$ matrix of the form $\mathbf{\Omega} = {{\sqrt{n/\ell} \cdot {\mathbf{D}}}{\mathbf{F}}{\mathbf{R}}^{\ast}}$ where $\mathbf{D}$ is a random $n \times n$ diagonal matrix whose entries are independent and uniformly distributed on the complex unit circle; $\mathbf{F}$ is the $n \times n$ unitary discrete Fourier transform; and $\mathbf{R}$ is a random $\ell \times n$ matrix that restricts an $n$-dimensional vector to $\ell$ coordinates, chosen uniformly at random.

Up to scaling, an SRFT is just a section of a unitary matrix, so it satisfies the norm identity $\left\| \mathbf{\Omega} \right\| = \sqrt{n/\ell}$. The critical fact is that an appropriately designed SRFT approximately preserves the geometry of an *entire subspace of vectors*.

### Theorem 24 (The SRFT preserves geometry)

Fix an $n \times k$ orthonormal matrix $\mathbf{V}$, and draw an $n \times \ell$ SRFT matrix $\mathbf{\Omega}$ where the parameter $\ell$ satisfies with failure probability at most $O{(k^{- 1})}$.

In words, the kernel of an SRFT of dimension $\ell \sim {k{\log{(k)}}}$ is unlikely to intersect a fixed $k$-dimensional subspace. In contrast with the Gaussian case, the logarithmic factor $\log{(k)}$ in the lower bound on $\ell$ cannot generally be removed (Remark 11.2).

Theorem 24. ‣ 11.1 Construction and Properties ‣ 11 SRFT test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") follows from a straightforward variation of the argument , which establishes equivalent bounds for a real analog of the SRFT, called the *subsampled randomized Hadamard transform* (SRHT). We omit further details.

### Remark 11.1

For large problems, we can obtain better numerical constants \[134, Thm. 3.2\]. Fix a small, positive number $\iota$. If $k \gg {\log{(n)}}$, then sampling coordinates is sufficient to ensure that ${\sigma_{k}{({{\mathbf{V}}^{\ast}\mathbf{\Omega}})}} \geq \iota$ with failure probability at most $O{(k^{- {c\iota}})}$. This sampling bound is essentially optimal because ${{({1 - \iota})} \cdot k}{\log{(k)}}$ samples are not adequate in the worst case; see Remark 11.2.

### Remark 11.2

The logarithmic factor in Theorem 24. ‣ 11.1 Construction and Properties ‣ 11 SRFT test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") is *necessary* when the orthonormal matrix $\mathbf{V}$ is particularly evil. Let us describe an infinite family of worst-case examples. Fix an integer $k$, and let $n = k^{2}$. Form an $n \times k$ orthonormal matrix $\mathbf{V}$ by regular decimation of the $n \times n$ identity matrix. More precisely, $\mathbf{V}$ is the matrix whose $j$th row has a unit entry in column ${({j - 1})}/k$ when $j \equiv {1\mspace{17mu}{({\operatorname{mod}k})}}$ and is zero otherwise. To see why this type of matrix is nasty, it is helpful to consider the auxiliary matrix ${\mathbf{W}} = {{\mathbf{V}}^{\ast}{\mathbf{D}}{\mathbf{F}}}$. Observe that, up to scaling and modulation of columns, $\mathbf{W}$ consists of $k$ copies of a $k \times k$ DFT concatenated horizontally.

Suppose that we apply the SRFT $\mathbf{\Omega} = {{\mathbf{D}}{\mathbf{F}}{\mathbf{R}}^{\ast}}$ to the matrix ${\mathbf{V}}^{\ast}$. We obtain a matrix of the form ${\mathbf{X}} = {{\mathbf{V}}^{\ast}\mathbf{\Omega}} = {{\mathbf{W}}{\mathbf{R}}^{\ast}}$, which consists of $\ell$ random columns sampled from $\mathbf{W}$. Theorem 24. ‣ 11.1 Construction and Properties ‣ 11 SRFT test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") certainly cannot hold unless ${\sigma_{k}{({\mathbf{X}})}} > 0$. To ensure the latter event occurs, we must pick at least one copy each of the $k$ distinct columns of $\mathbf{W}$. This is the coupon collector's problem \[98, Sec. 3.6\] in disguise. To obtain a complete set of $k$ coupons (i.e., columns) with nonnegligible probability, we must draw at least $k{\log{(k)}}$ columns. The fact that we are sampling without replacement does not improve the analysis appreciably because the matrix has too many columns.

### Performance guarantees

We are now prepared to present detailed information on the performance of the proto-algorithm when the test matrix $\mathbf{\Omega}$ is an SRFT.

### Theorem 25 (Error bounds for SRFT)

Fix an $m \times n$ matrix $\mathbf{A}$ with singular values $\sigma_{1} \geq \sigma_{2} \geq \sigma_{3} \geq \ldots$. Draw an $n \times \ell$ SRFT matrix $\mathbf{\Omega}$, where Construct the sample matrix $\mathbf{Y} = {\mathbf{A}\mathbf{\Omega}}$. Then with failure probability at most $O{(k^{- 1})}$.

As we saw in §10.2, the quantity $\sigma_{k + 1}$ is the minimal spectral-norm error possible when approximating $\mathbf{A}$ with a rank-$k$ matrix. Similarly, the series in the second bound is the minimal Frobenius-norm error when approximating $\mathbf{A}$ with a rank-$k$ matrix. We see that both error bounds lie within a polynomial factor of the baseline, and this factor decreases with the number $\ell$ of samples we retain.

The likelihood of error with an SRFT test matrix is substantially worse than in the Gaussian case. The failure probability here is roughly $k^{- 1}$, while in the Gaussian case, the failure probability is roughly $e^{- {({\ell - k})}}$. This qualitative difference is not an artifact of the analysis; discrete sampling techniques inherently fail with higher probability.

Matrix approximation schemes based on SRFTs often perform much better in practice than the error analysis here would indicate. While it is not generally possible to guarantee accuracy with a sampling parameter less than $\ell \sim {k{\log{(k)}}}$, we have found empirically that the choice $\ell = {k + 20}$ is adequate in almost all applications. Indeed, SRFTs sometimes perform even better than Gaussian matrices (see, e.g., Figure 8).

We complete the section with the proof of Theorem 25. ‣ 11.2 Performance guarantees ‣ 11 SRFT test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions").

### Theorem 25. ‣ 11.2 Performance guarantees ‣ 11 SRFT test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions")

Let $\mathbf{V}$ be the right unitary factor of matrix $\mathbf{A}$, and partition ${\mathbf{V}} = {\lbrack\left. {\mathbf{V}}_{1} \middle| {\mathbf{V}}_{2} \right.\rbrack}$ into blocks containing, respectively, $k$ and $n - k$ columns. Recall that where $\mathbf{\Omega}$ is the conjugate transpose of an SRFT. Theorem 24. ‣ 11.1 Construction and Properties ‣ 11 SRFT test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") ensures that the submatrix $\mathbf{\Omega}_{1}$ has full row rank, with failure probability at most $O{(k^{- 1})}$. Therefore, Theorem 11. ‣ 9.2 A deterministic error bound for the proto-algorithm ‣ 9 Error bounds via linear algebra ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") implies that where $\left| \middle| \middle| \cdot \middle| \middle| \right|$ denotes either the spectral norm or the Frobenius norm. Our application of Theorem 24. ‣ 11.1 Construction and Properties ‣ 11 SRFT test matrices ‣ Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions") also ensures that the spectral norm of $\mathbf{\Omega}_{1}^{\dagger}$ is under control.

We may bound the spectral norm of $\mathbf{\Omega}_{2}$ deterministically. since ${\mathbf{V}}_{2}$ and $\sqrt{\ell/n} \cdot \mathbf{\Omega}$ are both orthonormal matrices. Combine these estimates to complete the proof. ∎
