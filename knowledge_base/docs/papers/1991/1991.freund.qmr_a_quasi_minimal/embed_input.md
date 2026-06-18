<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

QMR: A Quasi-minimal Residual Method for Non-Hermitian Linear Systems

Topics include Krylov methods, QMR, Non-hermitian linear systems, Biconjugate gradient, Lanczos method, Iterative solvers, Numerical linear algebra.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the Quasi-Minimal Residual (QMR) method, a BCG-like Krylov solver for non-Hermitian linear systems designed to avoid the instability and breakdown behavior of classical biconjugate gradients. The paper combines a look-ahead nonsymmetric Lanczos implementation with error analysis and numerical evidence, making QMR a standard reference point for robust nonsymmetric iterative solvers.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The biconjugate gradient (BCG) method is the "natural" generalization of the classical conjugate gradient algorithm for Hermitian positive definite matrices to general non-Hermitian linear systems. Unfortunately, the original BCG algorithm is susceptible to possible breakdowns and numerical instabilities. In this paper, we present a novel BCG-like approach, the quasi-minimal residual (QMR) method, which overcomes the problems of BCG. An implementation of QMR based on a look-ahead version of the nonsymmetric Lanczos algorithm is proposed. It is shown how BCG iterates can be recovered stably from the QMR process. Some further properties of the QMR approach are given and an error bound is presented. Finally, numerical experiments are reported.
