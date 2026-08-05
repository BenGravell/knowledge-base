<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Randomized Algorithms for Low-rank Matrix Approximation: Design, Analysis, and Applications

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This survey explores modern approaches for computing low-rank approximations of high-dimensional matrices by means of the randomized SVD, randomized subspace iteration, and randomized block Krylov iteration. The paper compares the procedures via theoretical analyses and numerical studies to highlight how the best choice of algorithm depends on spectral properties of the matrix and the computational resources available. Despite superior performance for many problems, randomized block Krylov iteration has not been widely adopted in computational science. The paper strengthens the case for this method in three ways. First, it presents new pseudocode that can significantly reduce computational costs. Second, it provides a new analysis that yields simple, precise, and informative error bounds. Last, it showcases applications to challenging scientific problems, including principal component analysis for genetic data and spectral clustering for molecular dynamics data.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

This survey explores modern approaches for computing low-rank approximations of high-dimensional matrices by means of the randomized SVD, randomized subspace iteration, and randomized block Krylov iteration. The paper compares the procedures via theoretical analyses and numerical studies to highlight how the best choice of algorithm depends on spectral properties of the matrix and the computational resources available.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Abstract", "weight": 1.5} -->

Despite superior performance for many problems, randomized block Krylov iteration has not been widely adopted in computational science. This paper strengthens the case for the method in three ways. First, it presents new pseudocode that can significantly reduce computational costs. Second, it provides a new analysis that yields simple, precise, and informative error bounds. Last, it showcases applications to challenging scientific problems, including principal component analysis for genetic data and spectral clustering for molecular dynamics data.

<!-- chunk {"id": "body-0005", "role": "body", "section": "keywords", "weight": 1.0} -->

Low-rank matrix approximation, randomized numerical linear algebra, Krylov subspace methods

<!-- chunk {"id": "body-0006", "role": "body", "section": "Motivation", "weight": 1.0} -->

A core problem in numerical linear algebra is to produce a low-rank, factorized approximation of a high-dimensional input matrix ${\mathbf{A}} \in {\mathbb{R}}^{L \times N}$: We think of the inner dimension $k$ as much smaller than the outer dimensions $L$ and $N$. In this case, the factorized approximation ${\mathbf{B}}{\mathbf{C}}$ has fewer degrees of freedom than the input matrix $\mathbf{A}$, so the factorization is easier to store and manipulate. Furthermore, to attain a small error, the approximation must expose structure in the input matrix. Particular examples of "structure" include the range of the input matrix (rank-revealing QR factorization), principal components (truncated singular value decomposition), or salient columns (CUR or interpolative decomposition).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Motivation", "weight": 1.0} -->

Low-rank approximation serves as a fundamental tool for computational science. Application areas include fluid dynamics, uncertainty quantification, genetics, climate science, geophysics, astronomical imaging, and beyond. Indeed, low-rank approximation is helpful whenever we need to extract dominant patterns in data, remove unwanted noise, or perform compression.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Motivation", "weight": 1.0} -->

For high-dimensional matrices, the computational difficulty of low-rank approximation depends on the singular value spectrum of the input matrix; see Fig. 1 for a schematic. While we can apply simple algorithms to approximate a matrix with a rapidly decaying spectrum, we need more powerful algorithms to approximate a matrix with a slowly decaying spectrum. This challenge arises in many modern applications. For example, consider this quotation from the genetics literature: > "\[I\]n large datasets, eigenvalues may be highly significant (reflecting real population structure in the data) but only slightly larger than background noise eigenvalues..."

<!-- chunk {"id": "body-0009", "role": "body", "section": "Motivation", "weight": 1.0} -->

In this setting, we require scalable techniques that can filter out the noise components, while accurately approximating the signal components. So what algorithms should we use?

<!-- chunk {"id": "body-0010", "role": "body", "section": "Motivation", "weight": 1.0} -->

This survey explores a family of powerful methods for low-rank approximation: the randomized singular value decomposition (RSVD), randomized subspace iteration (RSI), and randomized block Krylov iteration (RBKI). We will introduce these techniques in Sections 2.1 and 2.2. They are related because each one collects information about the input matrix using matrix--vector products with random vectors. We will develop a systematic comparison of the three approaches by examining their mathematical structure, providing new implementations, refining theoretical analyses, and presenting numerical studies.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Motivation", "weight": 1.0} -->

As compared with classic methods, the randomized algorithms are more scalable, reliable, and robust. Our investigation shows that the simplest method, RSVD, returns accurate approximations for matrices with rapid singular value decay, but we must use the more sophisticated RBKI method for challenging problems. In case storage is the limiting factor, RSI may offer a reasonable compromise. These conclusions will be familiar to experts.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Motivation", "weight": 1.0} -->

Nevertheless, the RBKI method still has not reached a wide audience in computational science. (For example, see the recent genetics review.) Therefore, the second goal of this survey is to establish firm foundations for the RBKI method to speed its adoption. We develop a new formulation of the algorithm that is significantly faster than previous implementations. We prove new theoretical guarantees that demonstrate exactly how RBKI improves over RSVD and RSI. Finally, we show applications to benchmark problems in computational science that confirm the benefits of RBKI in these settings.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Remark 1.1 (Finding structure with randomness)", "weight": 1.0} -->

The paper of Halko et al. made a comprehensive case for RSVD and RSI, which led to broader usage of these methods. The goal of this survey is to perform the same mission for RBKI.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Randomized matrix approximation: Overview", "weight": 1.0} -->

This section offers an introduction to the randomized algorithms that we study in this paper. It provides a first look at the numerical behavior of these methods, and it presents simple theoretical bounds that allow us to compare their performance.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Framework", "weight": 1.0} -->

In 2009, Halko et al. developed a framework for designing randomized algorithms for low-rank matrix approximation. In this section, we outline the key concepts from their approach.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Framework", "weight": 1.0} -->

Consider the problem of approximating a high-dimensional matrix ${\mathbf{A}} \in {\mathbb{R}}^{L \times N}$. The matrix can be an array of data stored on a computer, or it can be an abstract linear operator defined by its action on test vectors. Regardless, we only access $\mathbf{A}$ by performing multiplications ${\mathbf{x}}\mapsto{{\mathbf{A}}{\mathbf{x}}}$ and ${\mathbf{y}}\mapsto{{\mathbf{A}}^{\ast}{\mathbf{y}}}$ with input vectors ${\mathbf{x}} \in {\mathbb{R}}^{N}$ and ${\mathbf{y}} \in {\mathbb{R}}^{L}$. As usual, ${\mathbf{A}}^{\ast}$ is the (conjugate) transpose.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Framework", "weight": 1.0} -->

The first idea underlying low-rank approximation is that we can find important directions in the range of $\mathbf{A}$ by applying the matrix to a *random* vector. Suppose that $\mathbf{A}$ has the singular value decomposition (SVD) The "leading" left singular vectors ${\mathbf{u}}_{i}$, associated with the largest singular values $\sigma_{i}$, are significant directions in the range. Draw a random vector ${\mathbf{ω}} \in {\mathbb{R}}^{N}$ from the standard normal distribution $\mathcal{N}{(\mathbf{0},\mathbf{I}_{N})}$. By rotational invariance, we can express $\mathbf{ω}$ in the basis of right singular vectors: With probability one, all of the random coefficients $Z_{i}$ are nonzero, and they are on the same scale because each coefficient $Z_{i}$ has mean zero and variance one.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Framework", "weight": 1.0} -->

The matrix--vector product takes the form We see that the image ${\mathbf{A}}{\mathbf{ω}}$ is strongly correlated with the leading left singular vectors, while it is weakly correlated with the trailing left singular vectors.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Framework", "weight": 1.0} -->

Now, observe that *repeated* multiplication with the input matrix $\mathbf{A}$ and its transpose ${\mathbf{A}}^{\ast}$ amplify the coefficients associated with large singular values, while attenuating coefficients with small singular values. More precisely, As we increase the depth $q = {1,2,3,\ldots}$, the small singular values are suppressed exponentially fast. Therefore, the output vector is more and more likely to be aligned with the leading left singular vectors. In fact, we can achieve this goal even when the depth is a moderate constant, say, $q \leq 5$. There is no need to take a limit.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Framework", "weight": 1.0} -->

Next, we double down on this insight by multiplying the input matrix with a *block* of $k \gg 1$ vectors to find many important directions in the range. To express this operation, we introduce a standard normal matrix $\mathbf{\Omega} = \begin{bmatrix} {\mathbf{ω}}_{1} & \ldots & {\mathbf{ω}}_{k} \end{bmatrix} \in {\mathbb{R}}^{N \times k}$ with independent columns. By sequential multiplication, we obtain the matrices As the powers increase, the ranges of these matrices align better with the $k$ leading left singular vectors ${\mathbf{u}}_{1},\ldots,{\mathbf{u}}_{k}$ of the input matrix. We will quantify the extent of the overlap in Sections 8 and 9.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Framework", "weight": 1.0} -->

Finally, suppose we have constructed a matrix ${\mathbf{M}} \in {\mathbb{R}}^{L \times k}$ whose range aligns with the leading left singular vectors of the input matrix $\mathbf{A}$. We can build the desired low-rank approximation of $\mathbf{A}$ by *compressing* $\mathbf{A}$ into the range of $\mathbf{M}$. To that end, we orthogonalize the columns of $\mathbf{M}$ to obtain a matrix ${\mathbf{X}} = {\text{orth}{({\mathbf{M}})}}$, and we construct the orthogonal projection $\mathbf{\Pi}_{\mathbf{M}} = {{\mathbf{X}}{\mathbf{X}}^{\ast}}$ onto the range of $\mathbf{M}$. Then we form the approximation Since $\mathbf{X}$ has at most $k$ columns, so does the matrix $\mathbf{Y}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Framework", "weight": 1.0} -->

At this point, the approximation $\hat{\mathbf{A}}$ can be manipulated into alternative forms by standard transformations. For example, we can easily produce an SVD, a QR factorization, or a CUR decomposition. See \[54, Sec. 5\] for details.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Matrix approximations and matrix computations", "weight": 1.0} -->

Combining these basic ideas, we obtain several fundamental approaches to low-rank matrix approximation.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Matrix approximations and matrix computations", "weight": 1.0} -->

In the first approach, called "randomized singular value decomposition" or RSVD, we generate the low-rank approximation This procedure requires a first multiplication with $\mathbf{A}$ and a second multiplication with ${\mathbf{A}}^{\ast}$, while storage is limited to two blocks of $k$ vectors. See Algorithm 1 for pseudocode.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Matrix approximations and matrix computations", "weight": 1.0} -->

In the second approach, called "randomized subspace iteration" or RSI, we generate This procedure requires $2q$ multiplications, alternating between $\mathbf{A}$ and ${\mathbf{A}}^{\ast}$, while storage is limited to two blocks of $k$ vectors. We think about the depth parameter $q$ as a *fixed* number, rather than treating the algorithm as a limiting process. See Algorithm 2 for pseudocode.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Matrix approximations and matrix computations", "weight": 1.0} -->

The third approach, called "randomized block Krylov iteration" or RBKI, forms the approximation In this case, we project onto the range of the block matrix $\begin{bmatrix} {{\mathbf{A}}\mathbf{\Omega}} & \cdots & {{({{\mathbf{A}}{\mathbf{A}}^{\ast}})}^{q - 1}{\mathbf{A}}\mathbf{\Omega}} \end{bmatrix}$. Section 5.3 shows how to carry out this construction using $2q$ multiplications. The storage cost is higher than the other algorithms, typically $2q$ blocks of $k$ vectors. As before, the depth parameter $q$ is viewed as a fixed number. See Algorithm 4 for pseudocode, which reduces the number of matrix--vector products by 33% compared to previous RBKI implementations.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Matrix approximations and matrix computations", "weight": 1.0} -->

Our primary objective in this work is to address the following question: > What is the most appropriate algorithm for low-rank approximation of a given matrix: RSVD, RSI, or RBKI?

<!-- chunk {"id": "body-0028", "role": "body", "section": "Matrix approximations and matrix computations", "weight": 1.0} -->

The answer depends on the singular value spectrum of the matrix, the required accuracy, and limitations on computational resources (such as storage).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Matrix approximations and matrix computations", "weight": 1.0} -->

We focus on the high-dimensional setting in which $L$ or $N$ is large (say, $\geq 10^{5}$). In this case, the predominant operating cost for each approximation method is the repeated application of $\mathbf{A}$ and ${\mathbf{A}}^{\ast}$ to a block of $k$ vectors. Therefore, we measure the operating cost in terms of the number $m$ of matrix--matrix multiplications, together with the block size $k$. The number of matrix--vector products is $km$ for all the algorithms we consider.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Matrix approximations and matrix computations", "weight": 1.0} -->

Our goal is to reduce the parameters $m$ and $k$ as much as possible, while ensuring a robust and accurate low-rank approximation. We accept certain tradeoffs between $m$ and $k$, but we focus mainly on decreasing the number $m$ of multiplications. Reducing $m$ gives a linear improvement in the runtime because the repeated matrix multiplications are inherently serial.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 2.1 (Matrix multiplication)", "weight": 1.0} -->

On modern computers, matrix multiplications with a large block size $k$ are optimized to take advantage of architectural features, including multithreading, caching, parallelization, and single-instruction multiple data processing. By designing multiplication-rich algorithms, we harness the full power of modern computing platforms. This is one of the main advantages of block Krylov methods over Krylov methods with a single starting vector ($k = 1$). See Section 6.1 for runtime comparisons.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Illustrative comparison", "weight": 1.0} -->

In this section, we present an illustrative comparison of RSVD, RSI, and RBKI. Section 7 presents a more comprehensive series of experiments, including real-world applications.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Illustrative comparison", "weight": 1.0} -->

We consider approximating two matrices with dimensions $L = N = 10^{4}$: The first matrix $\mathbf{A}$ has exponentially decaying singular values; see the "fast decay" profile in Fig. 1. The second matrix $\mathbf{B}$ is a noisy version of $\mathbf{A}$ that has been perturbed by adding an independent Gaussian random variable to each entry. For a particular realization of the noise, the upper left submatrices are The matrix entries are similar, up to variations on the scale $\pm 0.002$. However, the Gaussian noise transforms the structure of the singular values. The matrix $\mathbf{B}$ has a long tail of singular values with magnitudes $0.0$ to $0.4$; see the "slow decay" profile in Fig. 1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Illustrative comparison", "weight": 1.0} -->

First, we exhibit the output of RSVD (Algorithm 1) with a block size $k = 100$ when applied to the original matrix $\mathbf{A}$: The upper left submatrix coincides with $\mathbf{A}$ up to three decimal places. RSVD performs ideally for this example, and there is no reason to increase the block size or use a more elaborate approximation.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Illustrative comparison", "weight": 1.0} -->

In contrast, RSVD with a block size $k = 100$ produces an appalling approximation of the noisy matrix $\mathbf{B}$, with major discrepancies in the first four rows and columns: We can improve the approximation quality by using a larger block size $k = {1,000}$, but the errors remains large: The off-diagonal entries are too large in magnitude, and the diagonal entries are too small.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Illustrative comparison", "weight": 1.0} -->

As an alternative to RSVD, we can approximate the noisy matrix $\mathbf{B}$ using RSI (Algorithm 3) or RBKI (Algorithm 5) with a block size $k = 100$. After $m = 5$ multiplications, RSI improves on RSVD, but it still produces an underestimate of the diagonal: In contrast, after $m = 5$ multiplications, RBKI yields the superior approximation In fact, the approximation ${\hat{\mathbf{B}}}_{\text{RBKI}}$ agrees with the best rank-$100$ approximation of $\mathbf{B}$ up to three decimal places. The remaining error is a consequence of the low-rank approximation, rather than a deficiency in the RBKI algorithm.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Illustrative comparison", "weight": 1.0} -->

The takeaway from these simple experiments is that it can be difficult to approximate a matrix such as $\mathbf{B}$ that has been corrupted by noise. For approximation problems with noisy matrices, RBKI typically offers the best combination of speed and accuracy, and it outperforms the other randomized low-rank approximation algorithms.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

In this section, we introduce our main error bounds for randomized low-rank matrix approximation, which help to explain the outcomes of the experiments in Section 2.3. Detailed derivations and additional bounds can be found in Sections 8 and 9.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

Return to the setting where ${\mathbf{A}} \in {\mathbb{R}}^{L \times N}$ is an arbitrary matrix. We measure the quality of a computed approximation by comparison with an optimal rank-$r$ approximation. For a parameter $r \geq 1$, the minimal rank-$r$ approximation error in the spectral norm is given by the $({r + 1})$st singular value: Here, $\parallel \cdot \parallel$ is the spectral norm, and $\sigma_{j}{(\cdot)}$ returns the $j$th largest singular value. Equality holds for any $r$-truncated SVD of the matrix $\mathbf{A}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

A randomized low-rank approximation algorithm produces a random approximation $\hat{\mathbf{A}}$ of the input matrix $\mathbf{A}$. We evaluate the computed approximation $\hat{\mathbf{A}}$ using the mean-square relative error: The expectation $\mathbb{E}$ averages over the randomness in the algorithm, which comes from the choice of the random initialization matrix $\mathbf{\Omega}$. When we compare an approximation with rank $k$ to a best approximation with rank $r < k$, the relative error could be smaller than one.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

Here is the core technical question: > For a given target rank $r$, what block size $k$ and number $m$ of matrix multiplications suffice to make the mean-square relative error small?

<!-- chunk {"id": "body-0042", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

Our theoretical analysis elucidates how the parameters $k,m$ and the choice of approximation subspace affect the quality of the approximation. Let us emphasize that the user of the algorithm specifies $k$ and $m$, while the comparison rank $r$ only appears in the theoretical analysis.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

As a first result, we present an error bound for RSVD with $k$ Gaussian vectors. For each block size $k \geq {r + 2}$, we have the estimate As the block size $k$ increases, the polynomial factor $r/{({k - r - 1})}$ decreases. Typical choices for the block size are $k = {r + 2}$ and $k = {{2r} + 1}$. Once $k$ and $r$ are fixed, the bound depends only on the tail singular values ${\sigma_{r + 1}{({\mathbf{A}})}},{\sigma_{r + 2}{({\mathbf{A}})}},\ldots$. When these tail singular values decay quickly, the error is proportional to the optimal rank-$r$ error.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

The next result shows that randomized subspace iteration, RSI, is a better alternative for matrices with slowly decaying singular values. Consider the approximation $\hat{\mathbf{A}}$ produced by the RSI algorithm with $k$ Gaussian vectors and $m$ matrix multiplications. For each block size $k \geq {r + 2}$, The *logarithm* of the mean-square relative error decreases in proportion to the number $m$ of multiplications. The logarithm ensures that the error cannot depend too strongly on the singular value decay.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

Now, consider the approximation $\hat{\mathbf{A}}$ produced by the RBKI algorithm with $k$ Gaussian initialization vectors and $m$ matrix multiplications. For each block size $k \geq {r + 2}$, This bound shows that RBKI reduces the logarithm of the relative error proportionally to the *square* $m^{2}$ of the number $m$ of multiplications, which suggests that RBKI can provide a far more accurate approximation than RSI. For example, we might require $m = 100$ multiplications to obtain an accurate approximation using RSI but only $m = 10$ multiplications using RBKI.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

As stated, these error bounds are new, but they build on prior work. The results for RSVD and RSI are patterned on arguments from Halko et al. \[54, Thm. 10.6, Cor. 10.10\]. Musco and Musco \[74, Thm. 1\] obtained a qualitative result for RBKI that identifies the $\mathcal{O}{(m^{- 2})}$ scaling, but our detailed analysis of RBKI does not have a precedent in the literature. For mathematical derivations and a more comprehensive discussion, see Sections 8 and 9.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Positive-semidefinite matrices", "weight": 1.0} -->

A special priority of this survey is to develop methods for approximating *positive-semidefinite* (psd) matrices. Of course, we can approximate a psd matrix using the general-purpose algorithms RSVD, RSI, and RBKI, but this strategy is wasteful. A more accurate alternative that also preserves the psd property is to employ algorithms based on Nyström approximation (discussed in Section 5.4).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Positive-semidefinite matrices", "weight": 1.0} -->

We discuss three methods: NysSVD, NysSI, and NysBKI, which are the Nyström-based extensions of RSVD, RSI, or RBKI. We address the following question: > What is the most appropriate algorithm for low-rank approximation of a given psd matrix: NysSVD, NysSI, or NysBKI?

<!-- chunk {"id": "body-0049", "role": "body", "section": "Positive-semidefinite matrices", "weight": 1.0} -->

Our results show that NysSVD is the most efficient algorithm for rapidly decaying eigenvalues, while NysBKI is the most efficient algorithm for slowly decaying eigenvalues. Additionally, our theory and experiments suggest that NysBKI improves on RBKI by a factor of $\sqrt{2}$ matrix--matrix multiplications, demonstrating the potential for speedups in the psd setting.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Positive-semidefinite matrices", "weight": 1.0} -->

The NysRBKI algorithm is new, as is most of the theory for the Nyström methods. For a real-world application, see the spectral clustering problem in Section 7.3.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Plan for the paper", "weight": 1.0} -->

The rest of the paper is organized as follows. Section 3 presents historical background, Section 4 defines goals of low-rank matrix approximation, Section 5 presents pseudocode, Section 6 discusses parameter choices, Section 7 showcases numerical experiments, Sections 8 and 9 derive error bounds, and Section 10 offers conclusions.

<!-- chunk {"id": "body-0052", "role": "body", "section": "History", "weight": 1.0} -->

In this section, we provide a concise history of randomized low-rank matrix approximation.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Numerical methods for spectral computation", "weight": 1.0} -->

Computational tools for low-rank approximation have their roots in numerical methods for spectral computation. We focus on methods that extract a few eigenvalues and eigenvectors, rather than returning a full spectral decomposition.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Numerical methods for spectral computation", "weight": 1.0} -->

In the early 20th century, the power method and variants, such as inverse iteration, emerged as popular techniques for computing a few eigenvalues and eigenvectors of a square matrix (see \[96, Sec. 2.1.3\]). Around 1950, Lanczos introduced an improvement of the power method for Hermitian matrices that fully exploits Krylov information (matrix powers applied to vectors).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Numerical methods for spectral computation", "weight": 1.0} -->

Both the power method and the Lanczos algorithm employ just a single starting vector (i.e., block size $k = 1$), making them inadequate for resolving eigenvalues with multiplicity higher than one. To address this shortcoming, between the 1950s and 1970s, computational mathematicians developed versions of the power method and the Lanczos algorithm that use multiple starting vectors, called "subspace iteration" and "block Krylov iteration" (see \[96, Secs. 5.3.4, 6.1.4\]).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Numerical methods for spectral computation", "weight": 1.0} -->

These classic iterative methods have been extensively discussed in the literature; see Golub and van der Vorst for an historical overview. For modern accounts of the power method and the Lanczos algorithm, refer to the textbooks of Partlett and Saad. For analyses of subspace iteration and block Krylov iteration, see Stewart and Li and Zhang.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Numerical methods for spectral computation", "weight": 1.0} -->

All the traditional iterative methods for calculating the dominant eigenvalues and eigenvectors of a Hermitian matrix can be adapted to calculate the dominant singular values and singular vectors of a rectangular matrix ${\mathbf{A}} \in {\mathbb{R}}^{L \times N}$ by applying them to the Jordan--Wielandt matrix $\begin{bmatrix} {\mathbf{A}}^{\ast} & \mathbf{0} \end{bmatrix}$; see. When initialized with ${\mathbf{A}}\mathbf{\Omega}$ where $\mathbf{\Omega}$ is a random matrix, this approach matches the approximate singular value decomposition $\hat{\mathbf{A}} = {{\mathbf{U}}\mathbf{\Sigma}{\mathbf{V}}^{\ast}}$ from RSI or RBKI. However, the iterative approach to singular value decomposition was historically used to calculate a few (say, 1--4) leading singular values and singular vectors.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Numerical methods for spectral computation", "weight": 1.0} -->

The potential for converting these schemes into algorithms for low-rank approximation apparently went unrecognized until the 21st century.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Numerical methods for spectral computation", "weight": 1.0} -->

Early iterative algorithms for eigenvalue or singular vector computations used relatively few starting vectors (say, 3 or 4), which were often generated randomly, e.g., by random Gaussians. The random initialization was viewed as undesirable but necessary to ensure nonzero overlap with the leading singular vectors. To obtain accurate results, the algorithms employed a large number of matrix multiplications (10s or 100s). Numerical analysts emphasized the benefit of these repeated multiplications, since they viewed these computations as limiting processes, rather than finite algorithms \[83, Sec. 13.2\].

<!-- chunk {"id": "body-0060", "role": "body", "section": "The benefits of random sampling", "weight": 1.0} -->

The idea to calculate a singular value decomposition using just a few matrix multiplications was not seriously considered in the literature on classical iterative algorithm. Computational scientists needed a new probabilistic perspective to bring this computational strategy to light.

<!-- chunk {"id": "body-0061", "role": "body", "section": "The benefits of random sampling", "weight": 1.0} -->

Dixon and Kuczyński and Woźniakowski introduced a fresh analysis by applying probability theory to analyze the power method and the Lanczos algorithm. When the starting vector is Gaussian, these authors proved that the iterative algorithms can approximate the largest eigenvalue of a psd matrix after a *fixed* number of steps that depends logarithmically on the matrix dimension. They also demonstrated that the algorithms succeed even when the maximum eigenvalue is not separated from the remaining eigenvalues.

<!-- chunk {"id": "body-0062", "role": "body", "section": "The benefits of random sampling", "weight": 1.0} -->

In the late 1990s and early 2000s, theoretical computer scientists began to analyze a different type of randomized low-rank approximation, through an approach called column sampling. The simplest column sampling approximation takes the form $\hat{\mathbf{A}} = {\mathbf{\Pi}_{\mathbf{C}}{\mathbf{A}}}$, where $\mathbf{C}$ is a random subset of the columns of $\mathbf{A}$, chosen from an appropriate probability distribution. The probabilities can be defined proportionally to the square column norms, or using a more complicated distribution based on adaptive sampling or subspace sampling. Additionally as a post-processing procedure, many column sampling algorithms apply an $r$-truncated singular value decomposition to produce the rank-$r$ approximation $\hat{\mathbf{A}} = {\lfloor{\mathbf{\Pi}_{\mathbf{C}}{\mathbf{A}}}\rfloor}_{r}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "The benefits of random sampling", "weight": 1.0} -->

Various analyses demonstrate that column sampling can lead to a more accurate low-rank approximation than deterministic algorithms based on rank-revealing QR. For a more detailed history of column-sampling approaches, see the survey \[54, Sec. 2.1.2\].

<!-- chunk {"id": "body-0064", "role": "body", "section": "The benefits of random sampling", "weight": 1.0} -->

Around the same time, researchers began investigating randomized low-rank approximations similar to RSVD and RSI. Papadimitriou et al. introduced a low-rank approximation $\hat{\mathbf{A}} = {\mathbf{\Pi}_{{\lfloor{{\mathbf{A}}\mathbf{\Omega}}\rfloor}_{r}}{\mathbf{A}}}$, where $\mathbf{\Omega} \in {\mathbb{R}}^{N \times k}$ is a random orthogonal matrix and ${\lfloor{{\mathbf{A}}\mathbf{\Omega}}\rfloor}_{r}$ is a $r$-truncated singular value decomposition of ${\mathbf{A}}\mathbf{\Omega}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "The benefits of random sampling", "weight": 1.0} -->

Rokhlin et al. acknowledged the difficulty of approximating a matrix with slowly decaying singular values, and they proposed a more accurate low-rank approximation $\mathbf{\Pi}_{{\lfloor{{({{\mathbf{A}}{\mathbf{A}}^{\ast}})}^{q - 1}{\mathbf{A}}\mathbf{\Omega}}\rfloor}_{r}}{\mathbf{A}}$, where $\mathbf{\Omega} \in {\mathbb{R}}^{N \times k}$ is a Gaussian matrix and $q \geq 1$ is a depth parameter; see also the 1997 paper of Roweis. These early works argue that a small number of multiplications with a large block of random vectors (typically, ${10 \leq k \leq 1},000$) is sufficient to approximate a matrix with rapidly decaying singular values, and they provide preliminary theory to support their argument.

<!-- chunk {"id": "body-0066", "role": "body", "section": "The benefits of random sampling", "weight": 1.0} -->

In 2008 and 2009, Halko, Martinsson, and Tropp developed a framework for designing randomized low-rank approximation algorithms, which leads to the standard versions of RSVD and RSI that treat the the rank-$r$ truncation as an optional last step. Halko et al. also obtained the first theoretical analysis for these algorithms that is precise enough to predict their empirical behavior. They showed that RSI yields provable guarantees after a fixed number of matrix multiplications, even when the input matrix does not have gaps between the singular values. Following the publication of, researchers from various fields have applied randomized low-rank approximation to large-scale matrix computations in spectral clustering, genetics, uncertainty quantification, and image processing, among other areas.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Proposals for more efficient methods", "weight": 1.0} -->

In the next stage of inquiry, researchers proposed ways to improve the efficiency of randomized low-rank approximation, going beyond the basic RSVD and RSI. First, they introduced new approaches for the low-rank approximation of psd matrices based on *Nyström approximation*. For a mathematical description of Nyström approximation, see Section 5.4 or \[70, Sec. 14\]. Nyström approximation can be applied with any choice of test vectors, including random Gaussian vectors or random coordinate vectors. The approximation is always psd, and it always yields more accurate results than the simpler approximation based on orthogonal projection (see Lemma 5.3. ‣ 5.4 Positive-semidefinite matrices ‣ 5 Pseudocode ‣ Randomized algorithms for low-rank matrix approximation: Design, analysis, and applicationsFunding: JAT and RJW acknowledge partial support from the Office of Naval Research through BRC Award N00014-18-1-2363, from the National Science Foundation through FRG Award 1952777, and from Caltech through the Carver Mead New Adventures Fund.")).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Proposals for more efficient methods", "weight": 1.0} -->

In another development, researchers improved the theoretical understanding of structured random matrices $\mathbf{\Omega} \in {\mathbb{R}}^{N \times k}$. Random matrices constructed using sparse sign vectors or subsampled trigonometric transforms can be used for initializing randomized low-rank approximation, and they ensure a high quality of approximation. Due to fast matrix multiplications, these structured initialization matrices significantly improve runtimes for algorithms that require just a single matrix--matrix multiplication, such as NysSVD (Algorithm 6) or one-pass RSVD algorithms. However, when low-rank matrix approximation requires repeatedly multiplying the iterates with $\mathbf{A}$ and ${\mathbf{A}}^{\ast}$, as in RSVD or RBKI, the computational benefits of a structured random initialization are limited due to loss of structure after the first multiplication.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Proposals for more efficient methods", "weight": 1.0} -->

Last, one of the most significant advances in low-rank matrix approximation has been the introduction and analysis of randomized block Krylov methods. In 2015, Musco and Musco proved that RBKI can be substantially more accurate than RSI, and their insight has spurred a variety of follow-up works. In spite of this progress, the literature still lacks a crisp treatment of RBKI that parallels the earlier work on RSVD and RBKI. As a consequence, while RBKI is well-known among experts in randomized numerical linear algebra, it remains under-utilized in computational science (for instance, see the recent survey article in genetics). Therefore, our objective in this work is to increase the use of RBKI by providing efficient pseudocode, detailed theory, and numerical experiments that highlight the benefits of this algorithm.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Goals and consequences", "weight": 1.0} -->

In this section, we identify the goals and consequences of randomized low-rank matrix approximation. We answer the questions, "What is the purpose of randomized low-rank approximation?" and "What would an ideal low-rank approximation algorithm accomplish?"

<!-- chunk {"id": "body-0071", "role": "body", "section": "Goals", "weight": 1.0} -->

Ideally, a low-rank approximation algorithm should satisfy three main criteria: speed, accuracy, and utility for downstream matrix computations.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Goals", "weight": 1.0} -->

The first design criterion is speed. Randomized low-rank approximation is intended to quickly extract structure from a high-dimensional matrix ${\mathbf{A}} \in {\mathbb{R}}^{L \times N}$. To that end, we develop multiplication-rich algorithms, which harness the efficiency of matrix multiplications on modern computing platforms. We perform most of the computations in a sequence of $m$ matrix multiplications between $\mathbf{A}$ or ${\mathbf{A}}^{\ast}$ and a block of $k$ vectors. Even with dense matrix--matrix multiplication, this approach costs only $\mathcal{O}{({kmLN})}$ arithmetic operations, so it can be much faster than a traditional (full) singular value decomposition or eigendecomposition, which expends $\mathcal{O}{({LN{\min{\{ L,N\}}}})}$ operations. See Section 7 for examples of computational speedups spanning 1 to 3 orders of magnitude.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Goals", "weight": 1.0} -->

The second design criterion is accuracy. Our goal is to produce an approximation $\hat{\mathbf{A}}$ that is competitive with the best rank-$r$ approximation in spectral norm: We allow the rank of the approximation $\hat{\mathbf{A}}$ to be slightly larger than the comparison rank $r$. Our experiments (Section 7) and theory (Sections 8 and 9) show how randomized low-rank approximation achieves the goal Eq. 2.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Goals", "weight": 1.0} -->

The third design criterion is utility for downstream matrix calculations. We focus on algorithms that return a factorized approximation, which can be stored and manipulated efficiently. In the general setting, we seek a singular value decomposition $\hat{\mathbf{A}} = {{\mathbf{U}}\mathbf{\Sigma}{\mathbf{V}}^{\ast}}$. In the psd setting, we instead seek an eigenvalue decomposition $\hat{\mathbf{A}} = {{\mathbf{U}}\mathbf{\Lambda}{\mathbf{U}}^{\ast}}$. The output of these algorithms identifies the singular vectors or eigenvectors of the approximation $\hat{\mathbf{A}}$, which serve as proxies for the singular vectors or eigenvectors of the input matrix $\mathbf{A}$. Additionally, the factorized output leads to accelerated routines for computing matrix--vector products or solving regularized linear systems.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Consequences", "weight": 1.0} -->

As we have noted, our goal is to produce an approximation that is close to the input matrix in spectral norm, say, ${\parallel{{\mathbf{A}} - \hat{\mathbf{A}}}\parallel} \leq \varepsilon$. This type of bound allows us to substitute the approximation in place of the input matrix in many different contexts.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Consequences", "weight": 1.0} -->

Matrix--vector multiplications. We can use the low-rank approximation $\hat{\mathbf{A}}$ for matrix--vector products, and the error is controlled as Regularized linear systems. If $\mathbf{A}$ is psd and we generate a psd Nyström approximation $\hat{\mathbf{A}}$, we can use the approximation to solve the regularized linear system ${{({{\mathbf{A}} + {\mu\mathbf{I}}})}{\mathbf{x}}} = {\mathbf{y}}$ with $\mu > 0$. By the resolvent identity, the error is controlled by Hence, the linear solve is guaranteed to be accurate as long as ${\parallel{{\mathbf{A}} - \hat{\mathbf{A}}}\parallel} \ll \mu^{2}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Consequences", "weight": 1.0} -->

Singular values. We can use the low-rank approximation $\hat{\mathbf{A}}$ to compute singular values. Weyl's inequality \[56, Thm. 4.3.1\] guarantees that the error is controlled by for each $1 \leq i \leq {\min{\{ L,N\}}}$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Consequences", "weight": 1.0} -->

In summary, randomized low-rank approximation can be a helpful tool for performing many fast, approximate matrix computations.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Pseudocode", "weight": 1.0} -->

In this section, we present pseudocode for all of the algorithms we study. Efficient versions of RSVD, RSI, NysSVD and NysSI have already appeared, but we have developed a faster implementation of RBKI. Our RBKI pseudocode stores and reuses matrix multiplications, which reduces the number of matrix--vector products by roughly $33\%$. Additionally, to the best of our knowledge, the NysBKI algorithm is new, and it provides an additional factor-of-$\sqrt{2}$ savings in the number of matrix--vector products needed to achieve a fixed accuracy.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Pseudocode", "weight": 1.0} -->

The section is structured as follows: Sections 5.1, 5.2, and 5.3 provide pseudocode for RSVD, RSI, and RBKI; Section 5.4 discusses Nyström approximation algorithms. and Section 5.5 discusses modifications to the pseudocode that reduce or eliminate orthogonalization steps.

<!-- chunk {"id": "body-0081", "role": "body", "section": "RSVD", "weight": 1.0} -->

The simplest approach for randomized low-rank matrix approximation is the *randomized singular value decomposition*, which was introduced in and refined. RSVD has been applied to thousands of problems in spectral clustering, biology, uncertainty quantification, and image processing. The algorithm is now implemented in scikit-learn using the command "randomized_svd" with parameter "n_iter" set to 0 and in Matlab using the command "svdsketch" with parameter "NumPowerIterations" set to 0.

<!-- chunk {"id": "body-0082", "role": "body", "section": "RSVD", "weight": 1.0} -->

1:Matrix A ∈ ℝL × N; block size k 2:Orthogonal U ∈ ℝL × k, orthogonal V ∈ ℝN × k, and diagonal Σ ∈ ℝk × k such that A ≈ U Σ V* 3:Generate a random matrix Ω ∈ ℝN × k 5:[X, ∼] = qr_econ (X) ⊳ economy-sized QR or stabilized QR Eq. 4 7:${\lbrack\hat{\mathbf{U}},\mathbf{\Sigma},{\mathbf{V}}\rbrack} = {\text{svd_econ}{({\mathbf{Y}}^{\ast})}}$ ⊳ economy-sized SVD factorization 8:${\mathbf{U}} = {{\mathbf{X}}\hat{\mathbf{U}}}$ RSVD generates a low-rank approximation where $\mathbf{\Omega} \in {\mathbb{R}}^{N \times k}$ is a random matrix, typically Gaussian, and $k$ is a block size

<!-- chunk {"id": "body-0083", "role": "body", "section": "RSVD", "weight": 1.0} -->

parameter chosen by the user, typically ${10 \leq k \leq 1},000$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "RSVD", "weight": 1.0} -->

Algorithm 1 provides RSVD pseudocode, which is optimized for efficiency in three ways: The low-rank approximation is generated without forming the pseudoinverse ${({{\mathbf{A}}\mathbf{\Omega}})}^{\dagger}$. As a cheaper and stabler approach, the columns of ${\mathbf{A}}\mathbf{\Omega}$ are orthogonalized to produce a matrix ${\mathbf{X}} = {\text{orth}{({{\mathbf{A}}\mathbf{\Omega}})}}$ and the low-rank approximation is generated using The orthogonalization step ${\mathbf{X}} = {\text{orth}{({{\mathbf{A}}\mathbf{\Omega}})}}$ can be performed by taking the $\mathbf{Q}$ matrix from a standard economy-sized QR factorization. However, this leads to numerical issues when the requested rank of $\hat{\mathbf{A}}$ exceeds the true rank of $\mathbf{A}$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "RSVD", "weight": 1.0} -->

For such problems, we advocate a stabler approach in which we first calculate the SVD Then, we identify all the indices $i = {s_{1},\ldots,s_{r}}$ for which the diagonal entry $\sigma_{ii}$ exceeds a threshold proportional to the machine precision $\varepsilon_{\text{mach}}$ and return the approximate factorization This is not a traditional QR factorization since $\mathbf{R}$ is not upper triangular, but it is a stabilized QR factorization since it reliably exposes the range of ${\mathbf{A}}\mathbf{\Omega}$ \[46, Sec. 5.5.8\]. We can take $\text{orth}{({{\mathbf{A}}\mathbf{\Omega}})}$ to be the $\mathbf{Q}$ factor from the stabilized QR factorization, as usual.

<!-- chunk {"id": "body-0086", "role": "body", "section": "RSVD", "weight": 1.0} -->

The SVD of ${\mathbf{X}}{({{\mathbf{X}}^{\ast}{\mathbf{A}}})}$ is evaluated by first computing the SVD of the wide matrix and then applying the rotation These implementation techniques, which are mostly standard \[54, Sec. 1.5\], lead to the fast and stable pseudocode that is presented in Algorithm 1.

<!-- chunk {"id": "body-0087", "role": "body", "section": "RSVD", "weight": 1.0} -->

Next, we comment on the main user choice when implementing RSVD: choosing the block size $k$. As a general rule, increasing the block size $k$ increases the cost of RSVD, but it also improves the approximation quality.

<!-- chunk {"id": "body-0088", "role": "body", "section": "RSI", "weight": 1.0} -->

The early developers of RSVD acknowledged that the algorithm leads to large random errors when applied to a matrix with slowly decaying singular values. When targeting a matrix with slow singular value decay, they proposed an alternative strategy called *randomized subspace iteration*. RSI is based on the randomized low-rank approximation where $\mathbf{\Omega} \in {\mathbb{R}}^{N \times k}$ is a random matrix, typically Gaussian, and $q$ is a depth parameter, typically $2 \leq q \leq 5$. RSI is implemented in scikit-learn using the command "randomized_svd" and in Matlab using the command "svdsketch".

<!-- chunk {"id": "body-0089", "role": "body", "section": "RSI", "weight": 1.0} -->

RSI requires $q$ matrix multiplications with $\mathbf{A}$ and $q$ multiplications with ${\mathbf{A}}^{\ast}$. The algorithm with $q = 1$ is identical to RSVD. Increasing the depth $q$ systematically improves the approximation quality, but the cost grows linearly with $q$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "RSI", "weight": 1.0} -->

1:Matrix A ∈ ℝL × N; block size k; iteration count q 2:Orthogonal U ∈ ℝL × k, orthogonal V ∈ ℝN × k, and diagonal Σ ∈ ℝk × k such that A ≈ U Σ V* 3:Generate a random matrix Y ∈ ℝN × k 6: [X, ∼] = qr_econ (X) ⊳ Optional: stabilized QR Eq. 4 9:${\lbrack\hat{\mathbf{U}},\mathbf{\Sigma},{\mathbf{V}}\rbrack} = {\text{svd_econ}{({\mathbf{Y}}^{\ast})}}$ 10:${\mathbf{U}} = {{\mathbf{X}}\hat{\mathbf{U}}}$ Algorithm 2 RSI, simple version We provide simple, stable pseudocode for RSI in Algorithm 2. However, note that the pseudocode has the slightly awkward requirement of performing an *even* number of matrix multiplications ($q$ multiplications with $\mathbf{A}$ and

<!-- chunk {"id": "body-0091", "role": "body", "section": "RSI", "weight": 1.0} -->

Therefore we ask, "Is there any way to perform RSI with an *odd* number of multiplications?" Bjarkason answered this question in the affirmative (also see earlier work of \[87, Sec. 4.3\]), by replacing the approximation $\hat{\mathbf{A}} = {\mathbf{\Pi}_{{({{\mathbf{A}}{\mathbf{A}}^{\ast}})}^{q - 1}{\mathbf{A}}\mathbf{\Omega}}{\mathbf{A}}}$ with the closely related approximation The approach requires $q + 1$ matrix-matrix multiplications with $\mathbf{A}$ and only $q$ matrix--matrix multiplications with ${\mathbf{A}}^{\ast}$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "RSI", "weight": 1.0} -->

When multiplications with $\mathbf{A}$ are much cheaper than multiplications with ${\mathbf{A}}^{\ast}$ (as in some PDE models), we essentially get the final matrix multiplication for free, and we obtain an improved approximation.

<!-- chunk {"id": "body-0093", "role": "body", "section": "RSI", "weight": 1.0} -->

1:Matrix A ∈ ℝL × N; block size k; stopping criterion 2:Orthogonal U ∈ ℝL × k, orthogonal V ∈ ℝN × k, and diagonal Σ ∈ ℝk × k such that A ≈ U Σ V* 3:Generate a random matrix Y ∈ ℝN × k 4:i = 1 ⊳ i counts the number of multiplications 7:while stopping criterion is not met do 11: [Y, R] = qr_econ (Y) ⊳ Optional: stabilized QR Eq. 4 15: [X, S] = qr_econ (X) ⊳ Optional: stabilized QR Eq. 4 19:${\lbrack\hat{\mathbf{U}},\mathbf{\Sigma},\hat{\mathbf{V}}\rbrack} = {\text{svd_econ}{({\mathbf{T}})}}$ 20:${\mathbf{U}} = {{\mathbf{X}}\hat{\mathbf{U}}}$ 21:${\mathbf{V}} =

<!-- chunk {"id": "body-0094", "role": "body", "section": "RSI", "weight": 1.0} -->

{{\mathbf{Y}}\hat{\mathbf{V}}}$ Algorithm 3 RSI, extended version Bjarkason's insight leads to an extended version of RSI that uses either an odd or an even number of matrix multiplications.

<!-- chunk {"id": "body-0095", "role": "body", "section": "RSI", "weight": 1.0} -->

We provide an implementation in Algorithm 3, which incorporates the following features: The algorithm generates orthonormal matrices ${\mathbf{X}} \in {\mathbb{R}}^{L \times k}$ and ${\mathbf{Y}} \in {\mathbb{R}}^{N \times k}$, representing the range and co-range of the low-rank approximation. The low-rank approximation takes the form $\hat{\mathbf{A}} = {{\mathbf{X}}{\mathbf{T}}{\mathbf{Y}}^{\ast}}$ for a core matrix ${\mathbf{T}} \in {\mathbb{R}}^{k \times k}$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "RSI", "weight": 1.0} -->

At odd iterations, the algorithm updates $\mathbf{X}$ and $\mathbf{T}$. At even iterations, the algorithm updates $\mathbf{Y}$ and $\mathbf{T}$.

<!-- chunk {"id": "body-0097", "role": "body", "section": "RSI", "weight": 1.0} -->

The algorithm uses the fact that to efficiently compute an SVD for the low-rank approximation $\hat{\mathbf{A}}$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "RSI", "weight": 1.0} -->

To optimize the number of multiplications, we can run Algorithm 3 with an adaptive stopping criterion. For example, we can stop the algorithm as soon as the square Frobenius--norm error ${\parallel{{\mathbf{A}} - \hat{\mathbf{A}}}\parallel}_{F}^{2} = {{\parallel{\mathbf{A}}\parallel}_{F}^{2} - {\parallel\hat{\mathbf{A}}\parallel}_{F}^{2}}$ falls below a target precision $\varepsilon^{2} \cdot {\parallel{\mathbf{A}}\parallel}_{F}^{2}$. See Section 6 for a discussion.

<!-- chunk {"id": "body-0099", "role": "body", "section": "RBKI", "weight": 1.0} -->

In light of Lemma 5.1. ‣ 5.1 RSVD ‣ 5 Pseudocode ‣ Randomized algorithms for low-rank matrix approximation: Design, analysis, and applicationsFunding: JAT and RJW acknowledge partial support from the Office of Naval Research through BRC Award N00014-18-1-2363, from the National Science Foundation through FRG Award 1952777, and from Caltech through the Carver Mead New Adventures Fund."), it is always better to project onto a bigger subspace, and *randomized block Krylov iteration* projects onto the biggest subspace generated by the sequential matrix products. We define the Krylov subspace by In this expression, $\phi$ varies over polynomials with degree not exceeding $q - 1$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "RBKI", "weight": 1.0} -->

The RBKI method compresses the input matrix to the Krylov subspace: The Krylov subspace is much larger than the projection space used in RSI, which only contains the range of the final power ${({{\mathbf{A}}{\mathbf{A}}^{\ast}})}^{q - 1}{\mathbf{A}}\mathbf{\Omega}$. As a consequence, the RBKI approximation has the potential to be much more accurate.

<!-- chunk {"id": "body-0101", "role": "body", "section": "RBKI", "weight": 1.0} -->

RBKI was first introduced by Rokhlin, Szlam, and Tygert. The paper contains a numerical study in the context of principal component analysis. The first theoretical analysis is due to Musco and Musco. Over the past decade, RBKI has been applied to problems in genetics, meteorology, and geophysical imaging, leading to reported higher accuracy than RSI. Nonetheless, RBKI has remained under-utilized in applications (as reflected in the computational genetics review ).

<!-- chunk {"id": "body-0102", "role": "body", "section": "RBKI", "weight": 1.0} -->

1:Matrix A ∈ ℝL × N; block size k; iteration count q 2:Orthogonal U ∈ ℝL × q k, orthogonal V ∈ ℝN × q k, and diagonal Σ ∈ ℝq k × q k such that A ≈ U Σ V* 3:Generate a random matrix Y0 ∈ ℝN × K. 6: Xi = Xi − ∑j < iXj (Xj* Xi) ⊳ Orthogonalize w.r.t.

<!-- chunk {"id": "body-0103", "role": "body", "section": "RBKI", "weight": 1.0} -->

past iterates 7: Xi = Xi − ∑j < iXj (Xj* Xi) ⊳ The repetition ensures stability 8: [Xi, ∼] = qr_econ (Xi) ⊳ Optional: stabilized QR Eq. 4 11:${\lbrack\hat{\mathbf{U}},\mathbf{\Sigma},{\mathbf{V}}\rbrack} = {\text{svd_econ}\left(\begin{bmatrix} {\mathbf{Y}}_{1} & \cdots & {\mathbf{Y}}_{q} \end{bmatrix}^{\ast} \right)}$ 12:${\mathbf{U}} = {\begin{bmatrix} {\mathbf{X}}_{1} & \cdots & {\mathbf{X}}_{q} \end{bmatrix}\hat{\mathbf{U}}}$ Algorithm 4 RBKI, simple version 1:Matrix A ∈ ℝL × N; block size k; stopping criterion 2:Orthogonal

<!-- chunk {"id": "body-0104", "role": "body", "section": "RBKI", "weight": 1.0} -->

U, orthogonal V, and diagonal Σ such that A ≈ U Σ V* 3:Generate a random matrix Y0 ∈ ℝN × k 4:i = 1 ⊳ i counts the number of multiplications 8:while stopping criterion is not met do 12: ${\mathbf{R}}_{\bullet i} = {\begin{bmatrix} {\mathbf{Y}}_{2} & {\mathbf{Y}}_{4} & \cdots & {\mathbf{Y}}_{i - 2} \end{bmatrix}^{\ast}{\mathbf{Y}}_{i}}$ 13: Yi = Yi − ∑even j < iYj (Yj* Yi) ⊳ Orthog.

<!-- chunk {"id": "body-0105", "role": "body", "section": "RBKI", "weight": 1.0} -->

{\mathbf{Y}}_{4} & \cdots \end{bmatrix}\hat{\mathbf{V}}}$ Algorithm 5 RBKI, extended version Algorithm 4 presents pseudocode for a simple version of RBKI, while Algorithm 5 displays pseudocode for an extended version of RBKI that uses an even or odd number of multiplications.

<!-- chunk {"id": "body-0106", "role": "body", "section": "RBKI", "weight": 1.0} -->

Note that the block Gram--Schmidt step (lines 4 and 5 in Algorithm 4) must be performed twice for numerical stability. In subsequent algorithm displays, we indicate this repetition with the label (2$\times$) rather than writing out the formula twice.

<!-- chunk {"id": "body-0107", "role": "body", "section": "RBKI", "weight": 1.0} -->

Our RBKI pseudocode is more efficient than existing RBKI implementations. Indeed, the existing procedures all require the following series of multiplications: $q$ times: multiply $\mathbf{A}$ with a matrix of size $N \times k$; $q - 1$ times: multiply ${\mathbf{A}}^{\ast}$ with a matrix of size $L \times k$; and $1$ time: multiply ${\mathbf{A}}^{\ast}$ with a block matrix of size ${L \times k}q$.

<!-- chunk {"id": "body-0108", "role": "body", "section": "RBKI", "weight": 1.0} -->

In contrast, Algorithm 4 uses a reduced set of multiplications: $q$ times: multiply $\mathbf{A}$ with a matrix of size $N \times k$; and $q$ times: multiply ${\mathbf{A}}^{\ast}$ with a matrix of size $L \times k$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "RBKI", "weight": 1.0} -->

Our new procedure removes step (c), which involves an expensive multiplication of ${\mathbf{A}}^{\ast}$ with a block matrix of size ${L \times k}q$. We have substituted a single multiplication with a smaller matrix of size $L \times k$.

<!-- chunk {"id": "body-0110", "role": "body", "section": "RBKI", "weight": 1.0} -->

If we measure computational cost in the simplest way, by counting matrix--vector products, our new pseudocode results in cost savings of roughly $33\%$. The savings are even higher when matrix--vector multiplications are more expensive with ${\mathbf{A}}^{\ast}$ than with $\mathbf{A}$ (as in some PDE models ). Our new pseudocode does not change the asymptotic arithmetic cost of RBKI, which is still $\mathcal{O}{({kmLN})}$ for dense matrices, yet it makes a noticeable difference in applications. There are also potential reductions in communication costs.

<!-- chunk {"id": "body-0111", "role": "body", "section": "RBKI", "weight": 1.0} -->

Our new pseudocode enables a clean comparison between RSI and RBKI because the two algorithms now perform matrix multiplications with precisely the same block size. Although RBKI performs more arithmetic than RSI outside the matrix products, this arithmetic is rarely the predominant cost of the algorithm. We acknowledge that RBKI requires $\mathcal{O}{({km{({L + N})}})}$ storage whereas RSI only requires $\mathcal{O}{({k{({L + N})}})}$ storage. However, in typical applications involving data matrices (see Section 7), this is not an issue because storing the low-rank approximation $\hat{\mathbf{A}}$ is much cheaper than storing the original matrix $\mathbf{A}$.

<!-- chunk {"id": "body-0112", "role": "body", "section": "RBKI", "weight": 1.0} -->

As the main distinction, RBKI makes better use of the matrix products than RSI, resulting in a far more accurate approximation. Overall, we suspect that RSI is preferable to RBKI only if $\mathbf{A}$ is an abstract linear operator and working storage is the limiting factor for the computation.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Positive-semidefinite matrices", "weight": 1.0} -->

Suppose that ${\mathbf{A}} \in {\mathbb{R}}^{N \times N}$ is psd and we have generated a matrix ${\mathbf{M}} \in {\mathbb{R}}^{N \times k}$ whose range is aligned with leading eigenvectors of $\mathbf{A}$. Then, the simplest approximation for $\mathbf{A}$, which is used in RSVD, RSI, and RBKI, is based on compressing the range or co-range of $\mathbf{A}$ as follows: Since $\mathbf{A}$ is psd, we can employ the same data more effectively using the *Nyström approximation* \[70, Sec. 14\]: The Nyström approximation always improves over the simpler approximations.

<!-- chunk {"id": "body-0114", "role": "body", "section": "NysSVD", "weight": 1.0} -->

In *randomized Nyström approximation*, we generate a low-rank approximation: where $\mathbf{\Omega} \in {\mathbb{R}}^{N \times k}$ is a random matrix. In this work, $\mathbf{\Omega}$ is always a Gaussian matrix, mimicking the strategy used in RSVD. For parallelism, we call the resulting algorithm NysSVD even though it produces an eigenvalue decomposition.

<!-- chunk {"id": "body-0115", "role": "body", "section": "NysSVD", "weight": 1.0} -->

1:Psd matrix A ∈ ℝN × N; block size k; shift ε > 0 2:Orthogonal U ∈ ℝN × k and diagonal Λ ∈ ℝk × k such that A ≈ U Λ U* 3:Generate a random matrix Ω ∈ ℝN × k 8:Λ = max {0, Σ2 − ε I} ⊳ Remove ε shift Algorithm 6 presents NysSVD pseudocode, which is optimized for efficiency in the following ways: The low-rank approximation is generated without ever forming the pseudoinverse ${({\mathbf{\Omega}^{\ast}{\mathbf{A}}\mathbf{\Omega}})}^{\dagger}$ explicitly.

<!-- chunk {"id": "body-0116", "role": "body", "section": "NysSVD", "weight": 1.0} -->

Instead, we compute an upper-triangular Cholesky factor ${\mathbf{C}} \in {\mathbb{R}}^{k \times k}$ so that ${\mathbf{\Omega}^{\ast}{({{\mathbf{A}}\mathbf{\Omega}})}} = {{\mathbf{C}}^{\ast}{\mathbf{C}}}$. The low-rank approximation is generated as To ensure numerical stability, the Nyström approximation is applied to a shifted operator ${\mathbf{A}}_{\varepsilon} = {{\mathbf{A}} + {\varepsilon\mathbf{I}}}$, where the shift parameter $\varepsilon = {\varepsilon_{\text{mach}}\text{tr}{({\mathbf{A}})}}$ depends on the machine precision.

<!-- chunk {"id": "body-0117", "role": "body", "section": "NysSVD", "weight": 1.0} -->

To approximately counteract the shift, the eigenvalues of the approximation ${\hat{\mathbf{A}}}_{\varepsilon}$ are all reduced by $\varepsilon$.

<!-- chunk {"id": "body-0118", "role": "body", "section": "NysSVD", "weight": 1.0} -->

These improvements, previously recommended, lead to the fast and robust NysSVD implementation in Algorithm 6.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Remark 5.5 (Column Nyström approximation)", "weight": 1.0} -->

When evaluating each entry of the input matrix $\mathbf{A}$ is expensive, we might prefer to construct a Nyström approximation with the range determined from just a few columns of $\mathbf{A}$. Equivalently, the test matrix $\mathbf{\Omega}$ contains (random) coordinate vectors. To find an informative set of columns, we need additional ideas; see the paper and its background references.

<!-- chunk {"id": "body-0120", "role": "body", "section": "NysSI", "weight": 1.0} -->

In *randomized subspace iteration with Nyström approximation* \[54, Alg. 5.5\], we approximate a psd matrix ${\mathbf{A}} \in {\mathbb{R}}^{N \times N}$ as: Algorithm 7 presents NysSI pseudocode, which can be implemented with any adaptive stopping criterion. For example, we can stop the algorithm as soon as the trace--norm error ${\parallel{{\mathbf{A}} - \hat{\mathbf{A}}}\parallel}_{\ast} = {{\parallel{\mathbf{A}}\parallel}_{\ast} - {\parallel\hat{\mathbf{A}}\parallel}_{\ast}}$ falls below a target precision $\varepsilon \cdot {\parallel{\mathbf{A}}\parallel}_{\ast}$. NysSI achieves a target precision more quickly than RSI by one-half of a matrix--matrix multiplication, as reflected in our experiments (Figs.

<!-- chunk {"id": "body-0121", "role": "body", "section": "NysSI", "weight": 1.0} -->

1:Psd matrix A ∈ ℝN × N; block size k; stopping criterion; shift ε > 0 2:Orthogonal U ∈ ℝN × k and diagonal Λ ∈ ℝk × k such that A ≈ U Λ U* 3:Generate a random matrix Y ∈ ℝN × k 5:while stopping criterion is not met do 7: [X, ∼] = qr_econ (Y) ⊳ Optional: stabilized QR Eq. 4 11:C = chol (X* Y) ⊳ Cholesky decomposition 14:Λ = max {0, Σ2 − ε I} ⊳ Remove ε shift

<!-- chunk {"id": "body-0122", "role": "body", "section": "NysBKI", "weight": 1.0} -->

In *randomized block Krylov iteration with Nyström approximation*, we approximate a psd matrix ${\mathbf{A}} \in {\mathbb{R}}^{N \times N}$ as NysBKI uses the output of *every* matrix multiplication, not just every second matrix multiplication, to build an enriched approximation space. As a result, NysBKI is more efficient than RBKI by a factor of $\sqrt{2}$ matrix--matrix multiplications (Figs. 5, 6, and 9). To the best of our knowledge, NysBKI has not appeared in the matrix approximation literature before now. NysBKI pseudocode appears in Algorithm 8.

<!-- chunk {"id": "body-0123", "role": "body", "section": "NysBKI", "weight": 1.0} -->

1:Psd matrix A ∈ ℝN × N; block size k; stopping criterion; shift ε > 0 2:Orthogonal U and diagonal Λ such that A ≈ U Λ U* 3:Generate a random matrix Y0 ∈ ℝN × k 5:while stopping criterion is not met do 7: Xi = Xi − ∑j < iXj (Xj* Xi) ⊳ Orthog. w.r.t.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Additional opportunities for speedups", "weight": 1.0} -->

So far, we have presented simple, stable pseudocode that requires the minimal number of matrix multiplications with $\mathbf{A}$ and ${\mathbf{A}}^{\ast}$. However, we have not necessarily optimized the operations involving smaller matrices, and the algorithms use a large number of QR and SVD factorizations. Here we discuss some possibilities for computational speedups by removing or replacing these factorizations. This section is intended for numerical linear algebra experts, and most readers can skip it with impunity.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Additional opportunities for speedups", "weight": 1.0} -->

As the first speedup opportunity, we can remove all the SVD steps in our pseudocode. We can redesign RSVD to return a factorization $\hat{\mathbf{A}} = {{\mathbf{X}}{\mathbf{Y}}^{\ast}}$, without ever calculating the singular values and vectors. We can make similar adjustments to the pseudocode for other randomized low-rank approximation algorithms. After making these changes, the algorithms return the same low-rank approximation (in exact precision arithmetic), but the singular values and singular vectors of $\hat{\mathbf{A}}$ are no longer easily accessible as before.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Additional opportunities for speedups", "weight": 1.0} -->

As the second speedup opportunity, we can replace all the QR factorizations in the Nyström-based algorithms and all but the last QR factorization in RSI with cheaper matrix decompositions. Indeed, the sole purpose of the QR factorizations is to prevent the iterates from becoming ill-conditioned, but we can also avoid ill-conditioning using an LU factorization or a randomized QR decomposition. These alternatives use roughly $50\%$ of the arithmetic of the standard pivoted QR factorization.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Additional opportunities for speedups", "weight": 1.0} -->

For RBKI and NysBKI, we can also replace the block orthogonalization steps (such as lines 4--5 in Algorithm 4) by a shorter Lanczos-type recurrence: This reduces the total orthogonalization cost from $\mathcal{O}{({k^{2}q^{2}{({L + N})}})}$ to $\mathcal{O}{({k^{2}q{({L + N})}})}$ arithmetic operations. On the other hand, in finite precision arithmetic it may result in a basis ${\mathbf{M}} = \begin{bmatrix} {\mathbf{X}}_{1} & \cdots & {\mathbf{X}}_{q} \end{bmatrix}$ that is not orthogonal.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Additional opportunities for speedups", "weight": 1.0} -->

Last, orthogonalization is used in RSVD, RSI, and RBKI to compute a low-rank approximation $\hat{\mathbf{A}} = {\mathbf{\Pi}_{\mathbf{M}}{\mathbf{A}}}$ from a nonorthogonal basis matrix $\mathbf{M}$. However, if we are willing to accept some additional error, Nakatsukasa \[75, Eq. 3\] has proposed replacing ${\mathbf{\Pi}_{\mathbf{M}}{\mathbf{A}}} = {{\mathbf{M}}{\mathbf{M}}^{\dagger}{\mathbf{A}}}$ with a cheaper approximation where $\mathbf{S}$ is a randomized embedding matrix that reduces the dimensionality of $\mathbf{M}$ and $\mathbf{A}$. Nakatsukasa finds the additional error to be small in numerical tests.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Parameter choices", "weight": 1.0} -->

In this section, we discuss strategies for choosing the block size $k$ and the number of matrix--matrix multiplications $m$ in low-rank approximation algorithms. In RSVD and NysSVD, there is no choice but to increase $k$ to handle more difficult problems. However, in the other algorithms, a major question concerns the relative advantages of using a large depth ($m \gg 1$) versus a large block size ($k \gg 1$). Section 6.1 considers the tradeoff between $k$ and $m$, while Section 6.2 discusses adaptive strategies for choosing $k$ and $m$ that ensure a high-quality approximation.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Tradeoff between the block size and depth", "weight": 1.0} -->

A recent analysis of Meyer, Musco, and Musco gives evidence that $k = 1$ often leads to the highest accuracy in RBKI, assuming a fixed number of matrix--vector products $km$. Setting $k = 1$ leads to the classical Lanczos iteration. However, Meyer and coauthors also acknowledge two problems with setting $k = 1$. First, the approximation quality can be poor if any singular values have multiplicity greater than one (or have exponentially small singular value gaps), limiting the applicability to eigenvalue problems in physics and chemistry with high multiplicities (e.g., \[42, Sec. 14\]). Second, the Lanczos method is intrinsically serial, making it slow to run on modern computers.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Tradeoff between the block size and depth", "weight": 1.0} -->

We have performed a runtime analysis for NysBKI applied to the $250,{000 \times 250},000$ kernel matrix that will be introduced later in Section 7.3, leading to the results pictured in Fig. 2.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Tradeoff between the block size and depth", "weight": 1.0} -->

The figure presents the eigenvector approximation error where $\mathbf{\Pi}_{3}{(\cdot)}$ denotes the orthogonal projection onto the leadings three eigenvectors, and $\hat{\mathbf{A}}$ is the stochastic approximation of the kernel matrix $\mathbf{A}$ from a single run of NysBKI. We vary the block size to be either $k = 1$, $2$, $5$, $10$, or $100$ (different color lines). The results in the left panel of Fig. 2 support the conclusion of Meyer et al. that the smallest block size $k = 1$ leads to the highest accuracy, given a fixed number of matrix--vector products.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Tradeoff between the block size and depth", "weight": 1.0} -->

However, the number of matrix--vector multiplications is not a good indicator of the runtime cost, as shown in the right panel of Fig. 2. To reach a tolerance of $\varepsilon = 10^{- 5}$, NysBKI with a block size $k = 1$ takes $167$ minutes on a laptop computer, whereas NysBKI with a block size $k = 100$ takes $11$ minutes, making it $15 \times$ faster. We often anticipate an order-of-magnitude speedup by switching to a much larger block size.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Tradeoff between the block size and depth", "weight": 1.0} -->

In earlier work, Li and coauthors performed similar speed tests comparing a Matlab implementation of RSI against Lanczos implementations in ARPACK and PROPACK. Their results reinforce the practical advantages of using a large block size, both for reducing runtimes and for reducing errors: > On strictly serial processors with no complicated caching (such as the processors of many decades ago), the most careful implementations of Lanczos iterations... could likely attain performance nearing the randomized methods'... The randomized methods can attain much higher performance on parallel and distributed processors and generally are easier to use---setting their parameters properly is trivial (defaults perform well).

<!-- chunk {"id": "body-0135", "role": "body", "section": "Tradeoff between the block size and depth", "weight": 1.0} -->

The conclusions of Li et al. are based on hundreds of tests with dense matrices as large as $100,{000 \times 100},000$ and sparse matrices as large as $3,000,{000 \times 3},000,000$.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Tradeoff between the block size and depth", "weight": 1.0} -->

In light of the computational evidence, we advocate using a block size of at least $k = 10$ and potentially $k = 100$--$1,000$ for large-scale problems ($N \geq 10^{5}$). After choosing the block size, we recommend running RBKI or NysBKI with an adaptive stopping rule to determine the minimal number of multiplications. See Section 6.2 for a discussion of stopping rules that ensure the quality of the low-rank approximation.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Quality assurance", "weight": 1.0} -->

Here we evaluate two strategies for controlling the quality of a randomized low-rank approximation $\hat{\mathbf{A}}$. The first strategy is based on measuring and controlling the global approximation error. In this strategy, we increase the block size $k$ or depth parameter $m$ until achieving an error tolerance ${\parallel{{\mathbf{A}} - \hat{\mathbf{A}}}\parallel}_{F} < {\varepsilon \cdot {\parallel{\mathbf{A}}\parallel}_{F}}$ or ${\parallel{{\mathbf{A}} - \hat{\mathbf{A}}}\parallel}_{\ast} < {\varepsilon \cdot {\parallel{\mathbf{A}}\parallel}_{\ast}}$. These error bounds imply that $\hat{\mathbf{A}}$ can be reliably used in place of $\mathbf{A}$ in various matrix computations (Section 4.2).

<!-- chunk {"id": "body-0138", "role": "body", "section": "Quality assurance", "weight": 1.0} -->

An RSI implementation that controls the global approximation error is provided in the "svdsketch" function for Matlab, based on pseudocode: As the first step, this function evaluates the square Frobenius norm ${\parallel{\mathbf{A}}\parallel}_{F}^{2}$ using a single pass through the entries of $\mathbf{A}$.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Quality assurance", "weight": 1.0} -->

At each subsequent step, the function adds new columns to the initialization matrix $\mathbf{\Omega}$, updates the low-rank approximation $\hat{\mathbf{A}}$, and updates the Frobenius norm ${\parallel\hat{\mathbf{A}}\parallel}_{F}$.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Quality assurance", "weight": 1.0} -->

The procedure terminates as soon as "Svdsketch" always returns a low-rank approximation which accounts for a $1 - \varepsilon^{2}$ proportion of the square Frobenius norm of the target matrix.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Quality assurance", "weight": 1.0} -->

Two improvements to "svdsketch" could make the procedure even more powerful. First, "svdsketch" adaptively chooses the block size $k$, but our numerical experiments (Section 7) suggest that adaptively choosing the number of multiplications $m$ would lead to even greater efficiency. When computations are serial, adding to the depth more quickly reduces the errors than adding to the block size (Fig. 2 left panel). Second, "svdsketch" can only be applied to matrices stored entry-wise on a computer, because of the way it calculates the Frobenius-norm error. The recent paper \[37, Sec. 2\] describes a different strategy for approximating the Frobenius norm error based on matrix multiplications, which remains valid even when $\mathbf{A}$ is an abstract linear operator.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Quality assurance", "weight": 1.0} -->

Next we consider a different adaptive strategy, in which we increase $k$ or $m$ until each one of the leading singular vector triplets $({\hat{\mathbf{u}}}_{i},{\hat{\sigma}}_{i},{\hat{\mathbf{v}}}_{i})$ achieves the residual accuracy As soon as $r_{i} < \varepsilon$, the $i$th singular vector triplet is stable in the sense of backward error.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Quality assurance", "weight": 1.0} -->

Namely, there is a perturbation matrix ${\mathbf{E}} \in {\mathbb{R}}^{L \times N}$ with ${\parallel{\mathbf{E}}\parallel}_{F} < \varepsilon$ such that ${\mathbf{A}} + {\mathbf{E}}$ has exactly the singular vector triplet $({\hat{\mathbf{u}}}_{i},{\hat{\sigma}}_{i},{\hat{\mathbf{v}}}_{i})$. With assistance from Maksim Melnichenko and Riley Murray, we have developed adaptive versions of RBKI and NysBKI implementing this strategy, with the pseudocode appearing in Algorithms 9 and 10.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Quality assurance", "weight": 1.0} -->

Both adaptive strategies presented here would lead to a more reliable approximation than the earlier approach of applying an $r$-truncated singular value decomposition to the low-rank approximation with a default value $r = {k - 2}$ or $r = {\lfloor{k/2}\rfloor}$. A sufficiently small truncation parameter $r$ can in principle eliminate inaccurate singular vector estimates, but selecting $r$ is notoriously difficult in practice. For example, Fig. 3 evaluates the error for the estimated singular vectors of the clean matrix $\mathbf{A}$ and noisy matrix $\mathbf{B}$ described in Section 2.3.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Quality assurance", "weight": 1.0} -->

Here, $\mathbf{\Pi}_{{\mathbf{v}}_{i}{( \cdot )}}$ denotes the orthogonal projection onto the $i$th right singular vector, and the expectation is evaluated over 100 runs of RBKI with $k = 100$ and $m = 5$. From the results in Fig. 3, we would need to apply truncation with $r \leq 4$ for the noisy matrix but we could take $r$ as high as $186$ for the clean matrix, in order to achieve an error tolerance $\varepsilon =.1$. Unfortunately, there is no default truncation parameter $r$ which performs well for both matrices.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Applications", "weight": 1.0} -->

In this section, we present experiments comparing different randomized low-rank approximation algorithms (Section 7.1), and we apply the algorithms to scientific problems that require principal component analysis (Section 7.2) or kernel spectral clustering (Section 7.3).

<!-- chunk {"id": "body-0147", "role": "body", "section": "Comparison", "weight": 1.0} -->

As a simple, direct comparison, we apply RSVD, RSI, RBKI, and their Nyström-based variants to approximate two psd matrices $\mathbf{A}$ and $\mathbf{B}$ with singular values Matrix $\mathbf{B}$ models a noisy version of $\mathbf{A}$, with noise affecting the singular values $\sigma_{i}{({\mathbf{B}})}$ for $i \geq 81$ (see Fig. 4). The noise singular values are small, ranging from $0.00$ to $0.04$ in magnitude, but given the high-dimensionality ($L = N = 10^{5}$), they threaten to drown out the signal. We construct $\mathbf{A}$ and $\mathbf{B}$ as diagonal matrices, as the choice of singular vectors does not affect the performance of our algorithms in exact arithmetic (Lemma 8.3.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Comparison", "weight": 1.0} -->

‣ 8.1 Diagonal, psd reduction ‣ 8 Analysis of RSVD and NysSVD ‣ Randomized algorithms for low-rank matrix approximation: Design, analysis, and applicationsFunding: JAT and RJW acknowledge partial support from the Office of Naval Research through BRC Award N00014-18-1-2363, from the National Science Foundation through FRG Award 1952777, and from Caltech through the Carver Mead New Adventures Fund.")).

<!-- chunk {"id": "body-0149", "role": "body", "section": "Comparison", "weight": 1.0} -->

The results in Fig. 5 show that various randomized low-rank approximation algorithms, including NysSVD and RSVD, can produce a high-quality approximation of the matrix $\mathbf{A}$ with fast singular value decay. Since NysSVD and RSVD use fewer matrix--matrix multiplications ($m = 1$ for NysSVD, $m = 2$ for RSVD), these strategies are more cost-efficient when approximating such a matrix. NysSVD is more efficient than RSVD since it achieves the same approximation accuracy using half as many matrix--matrix multiplications.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Comparison", "weight": 1.0} -->

In contrast, the Krylov methods yield the highest accuracy approximations for the matrix $\mathbf{B}$ with slowly decaying singular values. The NysBKI method is the top performer, since it achieves this high approximation accuracy using a factor of $\sqrt{2}$ fewer matrix--matrix multiplications than RBKI.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Comparison", "weight": 1.0} -->

Next, Fig. 6 compares the singular vector approximations from several low-rank approximation algorithms. The singular vectors are vital for principal component analysis and kernel spectral clustering, as we will show through examples in Sections 7.2 and 7.3. We evaluate the error in the estimated singular vectors as where $\mathbf{\Pi}_{75}{(\cdot)}$ denotes the orthogonal projection onto the dominant $75$ right singular vectors. We find that RSVD and NysSVD lead to accurate singular vector approximations for the matrix $\mathbf{A}$ with rapid singular value decay. However, RBKI and NysBKI produce 10$\times$ to 300$\times$ more accurate singular vector approximations for the matrix $\mathbf{B}$ than the other low-rank approximation methods.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Human genetic diversity data", "weight": 1.0} -->

Principal component analysis is frequently applied to large matrices containing single-nucleotide polymorphism (SNP) data, encoding the variations in DNA at specific locations in the genome. The principal components of the SNP data can be used to cluster individuals that share similar genomes.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Human genetic diversity data", "weight": 1.0} -->

Here, we apply principal component analysis to the HapMap3 data set, one of the earliest data sets measuring human genetic diversity, which we downloaded. The data is organized into a matrix ${\mathbf{A}} \in {\mathbb{R}}^{{957 \times 14},079}$ containing counts of SNPs for 957 individuals in 14,079 chromosomal locations. The entries of $\mathbf{A}$ are 0, 1, or 2, corresponding to the number of affected chromosomes. To normalize the matrix entries, we apply the transformation Our goal is to extract the principal components, which are defined as the right singular vectors of $\mathbf{B}$. Once we have identified the principal components, we can cluster individuals by genetic ancestry as depicted in Fig. 7.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Human genetic diversity data", "weight": 1.0} -->

HapMap3 is a small data set by today's standards, and we can obtain the principal components using a full singular value decomposition on a laptop. Yet modern genetic data sets may contain millions of individuals and genetic markers, making a full singular value decomposition infeasible. Therefore, we consider a more scalable approach to principal component analysis based on randomized low-rank approximation.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Human genetic diversity data", "weight": 1.0} -->

The randomized approach to principal component analysis has been questioned in the past. In 2013, Chen et al. wrote, > "In theory, randomized eigenvector approximations \[RSVD\] can reduce the running time.... However, a colleague of ours reports that efforts to apply this approach to genetic data have not yet been successful, as in large datasets, eigenvalues may be highly significant (reflecting real population structure in the data) but only slightly larger than background noise eigenvalues, and thus sometimes missed by randomized methods (N. Patterson, personal communication)."

<!-- chunk {"id": "body-0156", "role": "body", "section": "Human genetic diversity data", "weight": 1.0} -->

The authors are concerned that randomized algorithms cannot accurately identify principal components when the singular values are close together. This would present a major limitation, since genetic data sets often have small singular value gaps, as shown for the HapMap3 data in Fig. 8.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Human genetic diversity data", "weight": 1.0} -->

RBKI also performs well at separating individuals into clusters. With just ${km} = 40$ matrix--vector products, the algorithm identifies the top $i = 5$ principal components well enough to match the ideal clustering results in Fig. 7. In contrast, we would need to perform RSVD with 20$\times$ as many matvecs (${km} = 800$) to achieve the same clustering accuracy.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Human genetic diversity data", "weight": 1.0} -->

These investigations show that RBKI is both fast and accurate when performing principal component analysis with genetic data. RBKI is faster than traditional singular value decomposition, since we can take $km$ to be a small fraction of the number of rows. Moreover RBKI is highly accurate, even when the signal barely rises above the noise.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Spectral clustering", "weight": 1.0} -->

Kernel spectral clustering is a powerful approach for analyzing the dynamics of proteins using data from molecular dynamics simulations. Spectral clustering is useful for identifying metastable states that the protein occupies for a long time, with rare transitions between states (e.g., folded and unfolded states). However in the past, kernel spectral clustering has mainly been limited to data sets with $N \leq 10^{4}$ data points, because it requires calculating the dominant eigenvectors of an $N \times N$ matrix.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Spectral clustering", "weight": 1.0} -->

Here, we use NysBKI to extend kernel spectral clustering to a large data set with $N = {250,000}$ points. The data comes from a 250 ns simulation of alanine dipeptide (\\ceCH_3-CO-NH-C_αHCH_3-CO-NH-CH_3), which we downloaded. The data points ${\mathbf{x}}^{(i)} \in {\mathbb{R}}^{30}$ identify the spatial $(x,y,z)$-positions of the 10 non-hydrogen atoms at 1 ps intervals. We will perform kernel spectral clustering as follows.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Spectral clustering", "weight": 1.0} -->

Form the psd Gaussian kernel matrix ${\mathbf{A}} \in {\mathbb{R}}^{N \times N}$ with entries where $\sigma > 0$ is a tunable bandwidth.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Spectral clustering", "weight": 1.0} -->

Form the diagonal matrix ${\mathbf{D}} \in {\mathbb{R}}^{N \times N}$ containing the row sums of $\mathbf{A}$.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Spectral clustering", "weight": 1.0} -->

Apply $k$-means clustering to the rows of $\mathbf{V}$.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Spectral clustering", "weight": 1.0} -->

The spectral clustering algorithm identifies three clusters in the 30-dimensional alanine dipeptide data space. These clusters are highly correlated with the dihedral angle $\phi$ between \\ceC, \\ceN, \\ceC_α, and \\ceC and $\psi$ between \\ceN, \\ceC_α, \\ceC, and \\ceN, as shown in Fig. 10. Yet we emphasize that the algorithm does not have access to the dihedral angles: it discovers the clusters organically, reproducing the past work.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Spectral clustering", "weight": 1.0} -->

It is computationally challenging to complete the third step of kernel spectral clustering, which requires calculating the dominant eigenvectors of an $N \times N$ psd matrix. For the alanine dipeptide problem, the matrix ${\mathbf{B}} = {{\mathbf{D}}^{- {1/2}}{\mathbf{A}}{\mathbf{D}}^{- {1/2}}}$ requires 222GB storage and is therefore too large to fit in working memory on a 64GB laptop. Therefore, to produce the results in Fig. 10, we store the matrix on disk and use NysBKI to approximate the leading eigenvectors. With parameter settings $k = 100$ and $m = 2$, NysBKI runs in just $11$ minutes and $99.9\%$ of the time is spent loading blocks of the matrix and performing blockwise matrix multiplications.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Spectral clustering", "weight": 1.0} -->

To provide additional insight into the difficulties of kernel spectral clustering, we take a subset of $N = {25,000}$ equally spaced data points (so we can perform a full eigendecomposition as a reference) and consider the impact of varying the bandwidth $\sigma$. A small bandwidth $\sigma$ is needed to obtain physically relevant clusters with sharp boundaries between clusters. Unfortunately, however, the eigenvalues decay more slowly when $\sigma$ is small (Fig. 11), leading to a difficult approximation problem.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Spectral clustering", "weight": 1.0} -->

In summary, we find that kernel spectral clustering leads to challenging, high-dimensional eigenvalue problems, especially when the bandwidth $\sigma$ is small. To solve these eigenvalue problems with high accuracy and scalability, we recommend the NysBKI algorithm. NysBKI works robustly across different bandwidth settings, and it leads to dramatic computational speedups. With $N = {250,000}$ data points and an approximation rank of ${km} = 200$, the difference between the traditional $\mathcal{O}{(N^{3})}$ operation count and NysBKI's $\mathcal{O}{({kmN^{2}})}$ operation count is over 3 orders of magnitude.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Analysis of RSVD and NysSVD", "weight": 1.0} -->

In this section, we derive error bounds for RSVD (Algorithm 1) and NysSVD (Algorithm 6), which are the simplest randomized low-rank approximation algorithms. These results provide the foundation for studying the more sophisticated methods (RSI, RBKI, NysSI, NysBKI). Although related results are already well-established, we have found opportunities for simplification and improvement.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Analysis of RSVD and NysSVD", "weight": 1.0} -->

We compare the RSVD approximation to an optimal rank-$r$ approximation ${\lfloor{\mathbf{A}}\rfloor}_{r}$, which arises from an $r$-truncated singular value decomposition, and we establish the following main result. The proof appears below in Section 8.3.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Diagonal, psd reduction", "weight": 1.0} -->

As the first step in our analysis, we show that the error of many randomized low-rank approximation algorithms depends only on the singular values of the target matrix, regardless of the singular vectors. This reduction is standard.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Deterministic analysis using parallel sums", "weight": 1.0} -->

In this section, we develop a simple formula for the error of RSVD when approximating a diagonal, psd matrix. We fix the target matrix ${\mathbf{A}} \in {\mathbb{R}}^{N \times N}$, fix the initialization matrix $\mathbf{\Omega} \in {\mathbb{R}}^{N \times k}$, and analyze the $p$-norm error ${\parallel{{\mathbf{A}} - {\mathbf{\Pi}_{{\mathbf{A}}\mathbf{\Omega}}{\mathbf{A}}}}\parallel}_{p}$. For this section, it does not matter whether the test matrix $\mathbf{\Omega}$ is deterministic or random.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Deterministic analysis using parallel sums", "weight": 1.0} -->

Our analysis is based on *parallel sums* of psd matrices. Parallel sums were introduced by Anderson & Duffin to give a mathematical framework for analyzing electric networks of capacitors and resistors. Parallel sums have become a favorite topic in linear algebra textbooks (e.g., \[13, Ch.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Calculations using random matrix theory", "weight": 1.0} -->

To complete the proof of our main result, we apply the following error bounds for Gaussian matrices, which are derived in Section B.1.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Additional expectation bounds", "weight": 1.0} -->

The analysis of RSVD using parallel sums of psd matrices leads to a family of expectation bounds with respect to various Schatten $p$-norms. We give a collection of these bounds in Theorem 8.11. ‣ 8.4 Additional expectation bounds ‣ 8 Analysis of RSVD and NysSVD ‣ Randomized algorithms for low-rank matrix approximation: Design, analysis, and applicationsFunding: JAT and RJW acknowledge partial support from the Office of Naval Research through BRC Award N00014-18-1-2363, from the National Science Foundation through FRG Award 1952777, and from Caltech through the Carver Mead New Adventures Fund."), with the proof appearing in Section B.2. The bounds underscore the potential for high errors when $k - r$ is small.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Analysis of Krylov algorithms", "weight": 1.0} -->

In this section, we analyze RBKI and NysBKI and provide a matching analysis of RSI and NysSI for comparison. We develop both *gapless* error bounds that do not require any distance between the singular values and *gapped* error bounds that grow increasingly strong with the size of singular value gaps.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Analysis of Krylov algorithms", "weight": 1.0} -->

The gapless error bounds are given in Theorem 9.1. ‣ 9 Analysis of Krylov algorithms ‣ Randomized algorithms for low-rank matrix approximation: Design, analysis, and applicationsFunding: JAT and RJW acknowledge partial support from the Office of Naval Research through BRC Award N00014-18-1-2363, from the National Science Foundation through FRG Award 1952777, and from Caltech through the Carver Mead New Adventures Fund."), and the proof appears in Section 9.3. Instead of bounding the error ratio which is ideally close to one, these bounds apply to the log-error ratio which is ideally close to zero. We demonstrate that the log-error ratio decreases at a rate $\mathcal{O}{({1/m})}$ for RSI or NysSI and a faster rate $\mathcal{O}{({1/m^{2}})}$ for RBKI or NysBKI. In each case, $m$ is the total number of multiplications with $\mathbf{A}$ or ${\mathbf{A}}^{\ast}$.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Overview of technical approach", "weight": 1.0} -->

To prove the gapped and gapless error bounds, our main approach is to apply a polynomial filter $\phi{({\mathbf{A}})}$ that increases the top singular values and decreases the bottom singular values. As we choose a filter, we need to ensure that $\phi{({\mathbf{A}})}\mathbf{\Omega}$ lies inside the approximation space. Therefore, we use power function filters to analyze subspace iteration methods, and we use Chebyshev polynomial filters to analyze Krylov methods. The enhanced ability of Chebyshev polynomials to separate the top singular values from the bottom singular values is why we obtain such powerful Krylov bounds. Chebyshev polynomials have long been used in this context; for example, see Kuczyński and Woźniakowski.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Overview of technical approach", "weight": 1.0} -->

Our filtering analysis relies on the fact that is the error of RSVD applied to a matrix $\phi{({\mathbf{A}})}$, and the RSVD error is bounded by Theorem 8.1. ‣ 8 Analysis of RSVD and NysSVD ‣ Randomized algorithms for low-rank matrix approximation: Design, analysis, and applicationsFunding: JAT and RJW acknowledge partial support from the Office of Naval Research through BRC Award N00014-18-1-2363, from the National Science Foundation through FRG Award 1952777, and from Caltech through the Carver Mead New Adventures Fund."). The main difficulty is relating the RSVD error Eq. 20 to the quantity the error actually attained by RSI and RBKI algorithms.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Overview of technical approach", "weight": 1.0} -->

‣ 9.3 Gapless error bounds ‣ 9 Analysis of Krylov algorithms ‣ Randomized algorithms for low-rank matrix approximation: Design, analysis, and applicationsFunding: JAT and RJW acknowledge partial support from the Office of Naval Research through BRC Award N00014-18-1-2363, from the National Science Foundation through FRG Award 1952777, and from Caltech through the Carver Mead New Adventures Fund."), which allows us to prove the gapless bounds. For RSI, the convexity argument is already visible in \[54, Prop. 8.6\]. For RBKI, the crucial new observation is that Chebyshev polynomials are not globally convex, yet they admit supporting lines on the range $x \geq 1$. The supporting lines are all that we need to extend the convexity-based arguments. See Fig. 14 for an illustration. Second, as a more standard mathematical result, we use matrix submultiplicativity to establish Lemma 9.8.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Overview of technical approach", "weight": 1.0} -->

‣ 9.4 Gapped error bounds ‣ 9 Analysis of Krylov algorithms ‣ Randomized algorithms for low-rank matrix approximation: Design, analysis, and applicationsFunding: JAT and RJW acknowledge partial support from the Office of Naval Research through BRC Award N00014-18-1-2363, from the National Science Foundation through FRG Award 1952777, and from Caltech through the Carver Mead New Adventures Fund."), which allows us to prove the gapped bounds.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Overview of technical approach", "weight": 1.0} -->

The gapless and gapped error bounds apply to the *untruncated* approximation $\hat{\mathbf{A}}$, which is the approximation returned by our pseudocode and recommended for most practical applications. However, similar bounds extend to the approximation ${\lfloor\hat{\mathbf{A}}\rfloor}_{r}$, which comes from applying an $r$-truncated singular value decomposition to $\hat{\mathbf{A}}$. The gapped error bounds (Theorem 9.2.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Overview of technical approach", "weight": 1.0} -->

‣ 9 Analysis of Krylov algorithms ‣ Randomized algorithms for low-rank matrix approximation: Design, analysis, and applicationsFunding: JAT and RJW acknowledge partial support from the Office of Naval Research through BRC Award N00014-18-1-2363, from the National Science Foundation through FRG Award 1952777, and from Caltech through the Carver Mead New Adventures Fund.")) remain valid even when we replace $\hat{\mathbf{A}}$ with ${\lfloor\hat{\mathbf{A}}\rfloor}_{r}$, due to the reverse Eckart--Young inequality \[50, Thm. 3.4\]. Likewise, we can prove gapless error bounds for ${\lfloor\hat{\mathbf{A}}\rfloor}_{r}$ by pursuing Musco and Musco's observation that either there is a singular value gap and the gapped error bounds apply or else there is no gap and the approximation is close to optimal. We omit a detailed treatment.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Chebyshev polynomials", "weight": 1.0} -->

The $q$th Chebyshev polynomial $x\mapsto{T_{q}{(x)}}$ is a polynomial of degree $q$ that shares some properties with the $q$th power function $x\mapsto x^{q}$. The values of both polynomials lie inside $\lbrack{- 1},1\rbrack$ for $0 \leq x \leq 1$, and both polynomials exhibit a sharp rate of increase for $x \geq 1$. Lemma 9.3. ‣ 9.2 Chebyshev polynomials ‣ 9 Analysis of Krylov algorithms ‣ Randomized algorithms for low-rank matrix approximation: Design, analysis, and applicationsFunding: JAT and RJW acknowledge partial support from the Office of Naval Research through BRC Award N00014-18-1-2363, from the National Science Foundation through FRG Award 1952777, and from Caltech through the Carver Mead New Adventures Fund.") provides more fine-grained estimates that will be used in the analysis.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Gapless error bounds", "weight": 1.0} -->

To prove the gapless error bounds, we will need the following version of Jensen's inequality. Compare this result with \[54, Prop. 8.6\].

<!-- chunk {"id": "body-0185", "role": "body", "section": "Gapped error bounds", "weight": 1.0} -->

To establish the gapped error bounds, we will need to apply a polynomial $\phi$ that enhances the singular value gap. To that end, we establish the following filtering lemma.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we have described randomized low-rank approximation algorithms and provided user recommendations regarding which algorithms are the most efficient. We have focused on computations involving high-dimensional matrices, in which matrix multiplications are the main computational bottleneck. We have established simple, explicit bounds which allow for precise descriptions of the differences between algorithms. Our results demonstrate that RSVD and NysSVD are fast and accurate when the singular values of the target matrix decay quickly. However, in settings of slow singular value decay, RBKI and NysBKI are the available algorithms with the greatest speed and robustness. We have presented numerical tests demonstrating the utility of these Krylov methods for principal component analysis and kernel spectral clustering.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The widespread adoption of RBKI and NysBKI will require changes in software, since RSI is currently the default randomized low-rank matrix approximation algorithm in Matlab and sci-kit learn. Yet, RBKI and NysBKI are of great benefit to computational scientists who have found RSI to be expensive while resulting in large random errors. RBKI and NysBKI are more accurate and scalable algorithms. To support the broader use of these Krylov methods, we have provided simple and stable pseudocode that cuts down on the cost of RBKI by roughly $33\%$ of the number of matrix--vector products, and we have provided the first pseudocode for NysBKI, which is faster than RBKI by a factor of $\sqrt{2}$ matrix--vector products.
