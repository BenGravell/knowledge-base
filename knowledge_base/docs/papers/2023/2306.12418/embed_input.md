Randomized Algorithms for Low-rank Matrix Approximation: Design, Analysis, and Applications

This survey explores modern approaches for computing low-rank approximations of high-dimensional matrices by means of the randomized SVD, randomized subspace iteration, and randomized block Krylov iteration. The paper compares the procedures via theoretical analyses and numerical studies to highlight how the best choice of algorithm depends on spectral properties of the matrix and the computational resources available. Despite superior performance for many problems, randomized block Krylov iteration has not been widely adopted in computational science. The paper strengthens the case for this method in three ways. First, it presents new pseudocode that can significantly reduce computational costs. Second, it provides a new analysis that yields simple, precise, and informative error bounds. Last, it showcases applications to challenging scientific problems, including principal component analysis for genetic data and spectral clustering for molecular dynamics data.

## Paper Body

To the editorial board of SIAM Review,

I am writing on behalf of my coauthor Joel A. Tropp and myself to submit our manuscript titled "Randomized algorithms for low-rank matrix approximation: Design, analysis, and applications" for consideration by the "Survey and Review" section of SIAM Review.

We believe our work will be of considerable interest to the applied mathematics and scientific computing communities. We would be honored if you would consider our manuscript for publication in SIAM Review.

Thank you for your time and consideration.

Algorithmically, we can reduce number of matrix--vector multiplications in randomized block Krylov iteration by $33\%$ through efficiently storing and reusing matvecs. We can achieve an additional $\sqrt{2}$-factor reduction in the number of matvecs by incorporating Nyström approximation for positive semidefinite matrices.

Twelve years ago, SIAM Review published the paper "Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions", by Nathan Halko, Per-Gunnar Martinsson, and Joel Tropp. played a major role in the subsequent development of randomized numerical linear algebra: the paper presented comprehensible theory and user-friendly algorithms that spurred the widespread interest in randomized low-rank approximation, leading to 4,000+ citations. Yet did not satisfactorily address the problem of approximating a matrix with slowly decaying singular values....

These new contributions serve to unify our understanding of block Krylov methods and illustrate their importance.

The main goal of our work is to offer a comprehensive, authoritative, and up-to-date perspective on randomized low-rank approximation, focusing specifically on randomized block Krylov iteration. The manuscript starts out with an expository mathematical argument, explaining why randomized low-rank approximation is helpful for exposing structure in large matrices and for speeding up matrix computations. Then we highlight the main challenge in low-rank approximation, which concerns the difficulty of approximating matrices with slowly decaying singular values. This problem is most satisfactorily addressed with randomized block Krylov methods.

Randomized block Krylov iteration is by far the most accurate randomized low-rank approximation method for a matrix with slowly decaying...
