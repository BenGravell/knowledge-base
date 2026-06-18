<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Randomized Numerical Linear Algebra: Foundations & Algorithms

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This survey describes probabilistic algorithms for linear algebra computations, such as factorizing matrices and solving linear systems. It focuses on techniques that have a proven track record for real-world problem instances. The paper treats both the theoretical foundations of the subject and the practical computational issues. Topics covered include norm estimation; matrix approximation by sampling; structured and unstructured random embeddings; linear regression problems; low-rank approximation; subspace iteration and Krylov methods; error estimation and adaptivity; interpolatory and CUR factorizations; Nyström approximation of positive-semidefinite matrices; single view ("streaming") algorithms; full rank-revealing factorizations; solvers for linear systems; and approximation of kernel matrices that arise in machine learning and in scientific computing.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Numerical linear algebra (NLA) is one of the great achievements of scientific computing. On most computational platforms, we can now routinely and automatically solve small- and medium-scale linear algebra problems to high precision. The purpose of this survey is to describe a set of probabilistic techniques that have joined the mainstream of NLA over the last decade. These new techniques have accelerated everyday computations for small- and medium-size problems, and they have enabled large-scale computations that were beyond the reach of classical methods.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Classical numerical linear algebra", "weight": 1.0} -->

NLA definitively treats several major classes of problems, including

<!-- chunk {"id": "body-0005", "role": "body", "section": "Classical numerical linear algebra", "weight": 1.0} -->

solution of dense and sparse linear systems;

<!-- chunk {"id": "body-0006", "role": "body", "section": "Classical numerical linear algebra", "weight": 1.0} -->

orthogonalization, least-squares, and Tikhonov regularization;

<!-- chunk {"id": "body-0007", "role": "body", "section": "Classical numerical linear algebra", "weight": 1.0} -->

determination of eigenvalues, eigenvectors, and invariant subspaces;

<!-- chunk {"id": "body-0008", "role": "body", "section": "Classical numerical linear algebra", "weight": 1.0} -->

singular value decomposition (SVD) and total least-squares.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Classical numerical linear algebra", "weight": 1.0} -->

In spite of this catalog of successes, important challenges remain. The sheer scale of certain datasets (terabytes and beyond) makes them impervious to classical NLA algorithms. Modern computing architectures (GPUs, multi-core CPUs, massively distributed systems) are powerful, but this power can only be unleashed by algorithms that minimize data movement and that are designed ab initio with parallel computation in mind. New ways to organize and present data (out-of-core, distributed, streaming) also demand alternative techniques.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Classical numerical linear algebra", "weight": 1.0} -->

Randomization offers novel tools for addressing all of these challenges. This paper surveys these new ideas, provides detailed descriptions of algorithms with a proven track record, and outlines the mathematical techniques used to analyze these methods.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Randomized algorithms emerge", "weight": 1.0} -->

Probabilistic algorithms have held a central place in scientific computing ever since Ulam and von Neumann's groundbreaking work on Monte Carlo methods in the 1940s. For instance, Monte Carlo algorithms are essential for high-dimensional integration and for solving PDEs set in high-dimensional spaces. They also play a major role in modern machine learning and uncertainty quantification.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Randomized algorithms emerge", "weight": 1.0} -->

For many decades, however, numerical analysts regarded randomized algorithms as a method of last resort---to be invoked only in the absence of an effective deterministic alternative. Indeed, probabilistic techniques have several undesirable features. First, Monte Carlo methods often produce output with low accuracy. This is a consequence of the central limit theorem, and in many situations it cannot be avoided. Second, many computational scientists have a strong attachment to the engineering principle that two successive runs of the same algorithm should produce identical results. This requirement aids with debugging, and it can be critical for applications where safety is paramount, for example simulation of infrastructure or control of aircraft. Randomized methods do not generally offer this guarantee. (Controlling the seed of the random number generator can provide a partial work-around, but this necessarily involves additional complexity.)

<!-- chunk {"id": "body-0013", "role": "body", "section": "Randomized algorithms emerge", "weight": 1.0} -->

Nevertheless, in the 1980s, randomized algorithms started to make inroads into NLA. Some of the early work concerns spectral computations, where it was already traditional to use random initialization. ? recognized that (a variant of) the power method with a random start *provably* approximates the largest eigenvalue of a positive semidefinite (PSD) matrix, even without a gap between the first and second eigenvalue. ? provided a sharp analysis of this phenomenon for both the power method and the Lanczos algorithm. Around the same time, ? and ? proposed Monte Carlo methods for estimating the trace of a large psd matrix. Soon after, ? demonstrated that randomized transformations can be used to avoid pivoting steps in Gaussian elimination.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Randomized algorithms emerge", "weight": 1.0} -->

Starting in the late 1990s, researchers in theoretical computer science identified other ways to apply probabilistic algorithms in NLA. ? and ? showed that randomized embeddings allow for computations on streaming data with limited storage. (?) and (?) proposed Monte Carlo methods for low-rank matrix approximation. (?), (?), and (?) wrote the first statement of theoretical principles for randomized NLA. ? showed how subspace embeddings support linear algebra computations.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Randomized algorithms emerge", "weight": 1.0} -->

In the mid-2000s, numerical analysts introduced practical randomized algorithms for low-rank matrix approximation and least-squares problems. This work includes the first computational evidence that randomized algorithms outperform classical NLA algorithms for particular classes of problems. Early contributions include (?, ?, ?, ?). These papers inspired later work, such as (?, ?, ?), that has made a direct impact in applications

<!-- chunk {"id": "body-0016", "role": "body", "section": "Randomized algorithms emerge", "weight": 1.0} -->

Parallel with the advances in numerical analysis, a tide of enthusiasm for randomized algorithms has flooded into cognate fields. In particular, stochastic gradient descent (?) has become a standard algorithm for solving large optimization problems in machine learning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Randomized algorithms emerge", "weight": 1.0} -->

At the time of writing, in late 2019, randomized algorithms have joined the mainstream of NLA. They now appear in major reference works and textbooks (?, ?). Key methods are being incorporated into standard software libraries (?, ?, ?).

<!-- chunk {"id": "body-0018", "role": "body", "section": "What does randomness accomplish?", "weight": 1.0} -->

Over the course of this survey we will explore a number of different ways that randomization can be used to design effective NLA algorithms. For the moment, let us just summarize the most important benefits.

<!-- chunk {"id": "body-0019", "role": "body", "section": "What does randomness accomplish?", "weight": 1.0} -->

Randomized methods can handle certain NLA problems faster than any classical algorithm. In Section 10, we describe a randomized algorithm that can solve a dense $m \times n$ least-squares problem with $m \gg n$ using about $O{({{mn} + n^{3}})}$ arithmetic operations (?). Meanwhile, classical methods require $O{({mn^{2}})}$ operations. In Section 18, we present an algorithm called SparseCholesky that can solve the Poisson problem on a dense undirected graph in time that is roughly *quadratic* in the number of vertices (?). Standard methods have cost that is *cubic* in the number of vertices. The improvements can be even larger for sparse graphs.

<!-- chunk {"id": "body-0020", "role": "body", "section": "What does randomness accomplish?", "weight": 1.0} -->

Randomization allows us to tackle problems that otherwise seem impossible. Section 15 contains an algorithm that can compute a rank-$r$ truncated SVD of an $m \times n$ matrix in a single pass over the data using working storage $O{({r{({m + n})}})}$. The first reference for this kind of algorithm is ?. We know of no classical method with this computational profile.

<!-- chunk {"id": "body-0021", "role": "body", "section": "What does randomness accomplish?", "weight": 1.0} -->

From an engineering point of view, randomization has another crucial advantage: it allows us to restructure NLA computations in a fundamentally different way. In Section 11, we will introduce the randomized SVD algorithm (?, ?). Essentially all the arithmetic in this procedure takes place in a short sequence of matrix--matrix multiplications. Matrix multiplication is a highly optimized primitive on most computer systems; it parallelizes easily; and it performs particularly well on modern hardware such as GPUs. In contrast, classical SVD algorithms require either random access to the data or sequential matrix--vector multiplications. As a consequence, the randomized SVD can process matrices that are beyond the reach of classical SVD algorithms.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Algorithm design considerations", "weight": 1.0} -->

Before we decide what algorithm to use for a linear algebra computation, we must ask how we are permitted to interact with the data. A recurring theme of this survey is that randomization allows us to reorganize algorithms so that they control whichever computational resource is the most scarce (flops, communication, matrix entry evaluation, etc.).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Algorithm design considerations", "weight": 1.0} -->

Streaming computations ("single-view"): There is rising demand for algorithms that can treat matrices that are so large that they cannot be stored at all; other applications involve matrices that are presented dynamically.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Algorithm design considerations", "weight": 1.0} -->

We must discard each innovation ${\mathbf{H}}_{i}$ after it has been processed. As it happens, the *only* type of algorithm that can handle the model (1.1) is one based on randomized linear dimension reduction (?). Our survey describes a number of algorithms that can operate in the streaming setting; see Sections 4, 5, 14, and 15.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Algorithm design considerations", "weight": 1.0} -->

Dense matrices stored in RAM: One traditional computational model for NLA assumes that the input matrix is stored in fast memory, so that any entry can quickly be read and/or overwritten as needed. The ability of CPUs to perform arithmetic operations keeps growing rapidly, but memory latency has not kept up. Thus, it has become essential to formulate blocked algorithms that operate on submatrices. Section 16 shows how randomization can help.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Algorithm design considerations", "weight": 1.0} -->

Large sparse matrices: For sparse matrices, it is natural to search for techniques that interact with a matrix only through its application to vectors, such as Krylov methods or subspace iteration. Randomization expands the design space for these methods. When the iteration is initialized with a random matrix, we can reach provably correct and highly accurate results after a few iterations; see Sections 11.6 and 11.7.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Algorithm design considerations", "weight": 1.0} -->

Another idea is to apply randomized sampling to control sparsity levels. This technique arises in Section 18, which contains a randomized algorithm that accelerates incomplete Cholesky preconditioning for sparse graph Laplacians.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Algorithm design considerations", "weight": 1.0} -->

Matrices for which entry evaluation is expensive: In machine learning and computational physics, it is often desirable to solve linear systems where it is too expensive to evaluate the full coefficient matrix. Randomization offers a systematic way to extract data from the matrix and to compute approximations that serve for the downstream applications. See Sections 19 and 20.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Overview", "weight": 1.0} -->

This paper covers fundamental mathematical ideas, as well as algorithms that have proved to be effective in practice. The balance shifts from theory at the beginning toward computational practice at the end. With the practitioner in mind, we have attempted to make the algorithmic sections self-contained, so that they can be read with a minimum of references to other parts of the paper.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Overview", "weight": 1.0} -->

After introducing notation and covering preliminaries from linear algebra and probability in Sections 2--3, the survey covers the following topics.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Overview", "weight": 1.0} -->

Sections 4--5 discuss algorithms for trace estimation and Schatten $p$-norm estimation based on randomized sampling (i.e., Monte Carlo methods). Section 6 shows how iteration can improve the quality of estimates for maximum eigenvalues, maximum singular values, and trace functions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Overview", "weight": 1.0} -->

Section 7 develops randomized sampling methods for approximating matrices, including applications to matrix multiplication and approximation of combinatorial graphs.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Overview", "weight": 1.0} -->

Sections 8--9 introduce the notion of a randomized linear embedding. These maps are frequently used to reduce the dimension of a set of vectors, while preserving their geometry. In Section 10, we explore several ways to use randomized embeddings in the context of an overdetermined least-squares problem.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Overview", "weight": 1.0} -->

Sections 11--12 demonstrate how randomized methods can be used to find a subspace that is aligned with the range of a matrix and to assess the quality of this subspace. Sections 13, 14, and 15 show how to use this subspace to compute a variety of low-rank matrix approximations.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Overview", "weight": 1.0} -->

Section 16 develops randomized algorithms for computing a factorization of a full-rank matrix, such as a pivoted QR decomposition or a URV decomposition.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Overview", "weight": 1.0} -->

Section 17 describes some general approaches to solving linear systems using randomized techniques. Section 18 presents the SparseCholesky algorithm for solving the Poisson problem on an undirected graph (i.e., a linear system in a graph Laplacian).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Overview", "weight": 1.0} -->

Last, Sections 19 and 20 show how to use randomized methods to approximate kernel matrices that arise in machine learning, computational physics, and scientific computing.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Omissions", "weight": 1.0} -->

While randomized NLA was a niche topic 15 years ago, we have seen an explosion of research over the last decade. This survey can only cover a small subset of the many important and interesting ideas that have emerged.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Omissions", "weight": 1.0} -->

Among many other omissions, we do not discuss spectral computations in detail. There have been interesting and very recent developments, especially for the challenging problem of computing a spectral decomposition of a nonnormal matrix (?). We also had to leave out a treatment of tensors and the rapidly developing field of randomized multilinear algebra.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Omissions", "weight": 1.0} -->

There is no better way to demonstrate the value of a numerical method than careful numerical experiments that measure its speed and accuracy against state-of-the-art implementations of competing methods. Our selection of topics to cover is heavily influenced by such comparisons; for reasons of space, we have often had to settle for citations to the literature, instead of including the numerical evidence.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Omissions", "weight": 1.0} -->

The intersection between optimization and linear algebra is of crucial importance in applications, and it remains a fertile ground for theoretical work. Randomized algorithms are invaluable in this context, but we realized early on that the paper would double in length if we included just the essential facts about randomized optimization algorithms.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Omissions", "weight": 1.0} -->

There is a complementary perspective on randomized numerical analysis algorithms, called *probabilistic numerics*. See the website (?) for a comprehensive bibliography.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Omissions", "weight": 1.0} -->

For the topics that we do cover, we have made every effort to include all essential citations. Nevertheless, the literature is vast, and we are sure to have overlooked important work; we apologize in advance for these oversights.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Other surveys", "weight": 1.0} -->

There are a number of other survey papers on randomized algorithms for randomized NLA and related topics.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Other surveys", "weight": 1.0} -->

? develop and analyse computational methods for low-rank matrix approximation (including the "randomized SVD" algorithm) from the point of view of a numerical analyst. The main idea is that randomization can furnish a subspace that captures the action of a matrix, and this subspace can be used to build structured low-rank matrix approximations.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Other surveys", "weight": 1.0} -->

? treats randomized methods for least-squares computations and for low-rank matrix approximation. He emphasizes the useful principle that we can often decouple the linear algebra and the probability when analyzing randomized NLA algorithms.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Other surveys", "weight": 1.0} -->

? describes how to use subspace embeddings as a primitive for developing randomized linear algebra algorithms. A distinctive feature is the development of lower bounds.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Other surveys", "weight": 1.0} -->

? gives an introduction to matrix concentration inequalities, and includes some applications to randomized NLA algorithms.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Other surveys", "weight": 1.0} -->

The survey of ? appeared in a previous volume of *Acta Numerica*. A unique aspect is the discussion of randomized tensor computations.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Other surveys", "weight": 1.0} -->

? have updated the presentation in ?, and include an introduction to linear algebra and probability that is directed toward NLA applications.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Other surveys", "weight": 1.0} -->

? focuses on computational aspects of randomized NLA. A distinctive feature is the discussion of efficient algorithms for factorizing matrices of full, or nearly full, rank.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Other surveys", "weight": 1.0} -->

? gives a mathematical treatment of how matrix concentration supports a few randomized NLA algorithms, and includes a complete proof of correctness for the SparseCholesky algorithm described in Section 18.
