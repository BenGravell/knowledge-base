<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Randomized Algorithms for Low-rank Matrix Approximation: Design, Analysis, and Applications

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This survey explores modern approaches for computing low-rank approximations of high-dimensional matrices by means of the randomized SVD, randomized subspace iteration, and randomized block Krylov iteration. The paper compares the procedures via theoretical analyses and numerical studies to highlight how the best choice of algorithm depends on spectral properties of the matrix and the computational resources available. Despite superior performance for many problems, randomized block Krylov iteration has not been widely adopted in computational science. The paper strengthens the case for this method in three ways. First, it presents new pseudocode that can significantly reduce computational costs. Second, it provides a new analysis that yields simple, precise, and informative error bounds. Last, it showcases applications to challenging scientific problems, including principal component analysis for genetic data and spectral clustering for molecular dynamics data.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To the editorial board of SIAM Review,

<!-- chunk {"id": "body-0004", "role": "body", "section": "Paper Body", "weight": 1.0} -->

I am writing on behalf of my coauthor Joel A. Tropp and myself to submit our manuscript titled "Randomized algorithms for low-rank matrix approximation: Design, analysis, and applications" for consideration by the "Survey and Review" section of SIAM Review.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The main goal of our work is to offer a comprehensive, authoritative, and up-to-date perspective on randomized low-rank approximation, focusing specifically on randomized block Krylov iteration. The manuscript starts out with an expository mathematical argument, explaining why randomized low-rank approximation is helpful for exposing structure in large matrices and for speeding up matrix computations. Then we highlight the main challenge in low-rank approximation, which concerns the difficulty of approximating matrices with slowly decaying singular values. This problem is most satisfactorily addressed with randomized block Krylov methods.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Twelve years ago, SIAM Review published the paper "Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions", by Nathan Halko, Per-Gunnar Martinsson, and Joel Tropp. played a major role in the subsequent development of randomized numerical linear algebra: the paper presented comprehensible theory and user-friendly algorithms that spurred the widespread interest in randomized low-rank approximation, leading to 4,000+ citations. Yet did not satisfactorily address the problem of approximating a matrix with slowly decaying singular values. The omission of randomized block Krylov methods has confused practitioners, who sometimes experience (and complain about) long runtimes and inaccurate approximations when using the standard methods.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Randomized block Krylov iteration is by far the most accurate randomized low-rank approximation method for a matrix with slowly decaying singular values. The method has become visible within the small community of experts in randomized numerical linear algebra, but it would benefit from being broadcast more widely. Judging by a recent computational genetics survey, randomized block Krylov iteration is hardly used in applications, which is a major missed opportunity.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our manuscript is an integrative paper that combines mathematical motivation, history, thoroughly tested pseudocode, and a consolidation of theoretical results. We focus especially on the last decade of developments, including the development of Nyström methods for positive semidefinite matrix approximation and the development and theoretical analysis of Krylov methods.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Algorithmically, we can reduce number of matrix--vector multiplications in randomized block Krylov iteration by $33\%$ through efficiently storing and reusing matvecs. We can achieve an additional $\sqrt{2}$-factor reduction in the number of matvecs by incorporating Nyström approximation for positive semidefinite matrices.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Mathematically, we can identify the advantage of randomized block Krylov iteration using an explicit spectral-norm error bound, which holds even without any gaps in the singular value spectrum. Our main error bound is new, but it is patterned on the error bounds derived for the randomized singular value decomposition and randomized subspace iteration in past work.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Paper Body", "weight": 1.0} -->

These new contributions serve to unify our understanding of block Krylov methods and illustrate their importance.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We recommend Alex Townsend as the associate editor to handle the manuscript. He has personal expertise in randomized matrix computations, and he has written papers extending randomized SVD algorithms to infinite-dimensional settings.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We also request that our paper should be reviewed by scientific computing researchers, since our goal is to advocate for the greater use of randomized block Krylov iteration in scientific computing applications. Examples of researchers working in scientific computing that have relevant background include Mikhail Belkin (UCSD), Tyler Chen (NYU), Matthew Colbrook (Cambridge), Benjamin Erichson (ICSI), Felix Herrmann (Georgia Tech), Riley Murray (LBNL), and Georg Stadler (NYU). Other potential reviewers cited in the manuscript include Elvar Bjarkason (Akita), Cameron Musco (Amherst), Christopher Musco (NYU Tandon), and Mark Tygert (Meta). None of these individuals has a conflict of interest with the authors.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We believe our work will be of considerable interest to the applied mathematics and scientific computing communities. We would be honored if you would consider our manuscript for publication in SIAM Review.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Thank you for your time and consideration.
