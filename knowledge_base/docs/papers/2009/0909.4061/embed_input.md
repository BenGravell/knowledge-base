Finding Structure with Randomness: Probabilistic Algorithms for Constructing Approximate Matrix Decompositions

Topics include Randomized algorithms, Matrix decomposition, Low-rank approximation, Numerical linear algebra, Singular value decomposition, Matrix sketching.

Surveys and analyzes randomized algorithms for constructing approximate matrix decompositions such as low-rank SVDs. The paper helped popularize randomized numerical linear algebra as a practical tool for large data matrices.

Low-rank matrix approximations, such as the truncated singular value decomposition and the rank-revealing QR decomposition, play a central role in data analysis and scientific computing. This work surveys and extends recent research which demonstrates that randomization offers a powerful tool for performing low-rank matrix approximation. These techniques exploit modern computational architectures more fully than classical methods and open the possibility of dealing with truly massive data sets. This paper presents a modular framework for constructing randomized algorithms that compute partial matrix decompositions. These methods use random sampling to identify a subspace that captures most of the action of a matrix. The input matrix is then compressed - either explicitly or implicitly - to this subspace, and the reduced matrix is manipulated deterministically to obtain the desired low-rank factorization. In many cases, this approach beats its classical competitors in terms of accuracy, speed, and robustness. These claims are supported by extensive numerical experiments and a detailed error analysis.

## Abstract

Low-rank matrix approximations, such as the truncated singular value decomposition and the rank-revealing QR decomposition, play a central role in data analysis and scientific computing. This work surveys and extends recent research which demonstrates that *randomization* offers a powerful tool for performing low-rank matrix approximation. These techniques exploit modern computational architectures more fully than classical methods and open the possibility of dealing with truly massive data sets.

This paper presents a modular framework for constructing randomized algorithms that compute partial matrix decompositions. These methods use random sampling to identify a subspace that captures most of the action of a matrix. The input matrix is then compressed---either explicitly or implicitly---to this subspace, and the reduced matrix is manipulated deterministically to obtain the desired low-rank factorization. In many cases, this approach beats its classical competitors in terms of accuracy, speed, and robustness. These claims are supported by extensive numerical experiments and a detailed error analysis.

We may bound the spectral norm of $\mathbf{\Omega}_{2}$ deterministically.

since ${\mathbf{V}}_{2}$ and $\sqrt{\ell/n} \cdot \mathbf{\Omega}$ are both orthonormal matrices. Combine these estimates to complete the proof. ∎

Given a matrix $\mathbf{Q}$ such that holds, we can obtain a rank-$k$ factorization

There always exists an ID where the entries in the factor $\mathbf{X}$ have magnitude bounded by one. Known proofs of this fact are constructive, e.g., \[103, Lem. 3.3\], but they require us to find a collection of $k$ columns that has "maximum volume." It is NP-hard to identify a subset of columns with this type of extremal property. We find it remarkable that ID computations are possible as soon as the bound on $\mathbf{X}$ is relaxed.

Second, we investigate how the choice of random test matrix influences the error in approximating an input matrix. For these experiments, we return to the $200 \times 200$ matrix $\mathbf{A}$ defined in Section 7.1. Consider variations of Algorithm LABEL:alg:basic obtained when the random test matrix $\mathbf{\Omega}$ is drawn from the following four distributions:

The specific benefits of randomized techniques depend on the computational environment....
