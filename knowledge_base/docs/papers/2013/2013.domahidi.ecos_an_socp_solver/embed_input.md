<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

ECOS: An SOCP Solver for Embedded Systems

Topics include ECOS, Second-order cone programming, Interior-point methods, Embedded optimization, Conic optimization, Sparse LDL.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces ECOS, a compact embedded SOCP solver built around a fixed-order sparse LDL factorization and primal-dual interior-point method. It is influential because it made conic optimization more viable on small and real-time systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we describe the embedded conic solver (ECOS), an interior-point solver for second-order cone programming (SOCP) designed specifically for embedded applications. ECOS is written in low footprint, single-threaded, library-free ANSI-C and so runs on most embedded platforms. The main interior-point algorithm is a standard primal-dual Mehrotra predictor-corrector method with Nesterov-Todd scaling and self-dual embedding, with search directions found via a symmetric indefinite KKT system, chosen to allow stable factorization with a fixed pivoting order. The indefinite system is solved using Davis SparseLDL package, which we modify by adding dynamic regularization and iterative refinement for stability and reliability, as is done in the CVXGEN code generation system, allowing us to avoid all numerical pivoting; the elimination ordering is found entirely symbolically. This keeps the solver simple, only 750 lines of code, with virtually no variation in run time. For small problems, ECOS is faster than most existing SOCP solvers; it is still competitive for medium-sized problems up to tens of thousands of variables.
