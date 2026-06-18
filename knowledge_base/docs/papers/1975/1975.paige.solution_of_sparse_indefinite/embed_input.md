<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Solution of Sparse Indefinite Systems of Linear Equations

Topics include SYMMLQ, MINRES, Symmetric indefinite systems, Lanczos algorithm, Sparse linear systems, Numerical linear algebra, Krylov subspace methods.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Paige and Saunders extend Lanczos and conjugate-gradient ideas to large sparse symmetric indefinite linear systems. The paper is the source of methods such as SYMMLQ and closely related MINRES-style reasoning, showing how tridiagonal Lanczos reductions can produce practical solvers beyond positive-definite systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The method of conjugate gradients for solving systems of linear equations with a symmetric positive definite matrix A is given as a logical development of the Lanczos algorithm for tridiagonalizing A. This approach suggests numerical algorithms for solving such systems when A is symmetric but indefinite. These methods have advantages when A is large and sparse.
