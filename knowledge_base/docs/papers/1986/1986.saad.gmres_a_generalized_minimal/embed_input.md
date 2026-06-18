<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

GMRES: A Generalized Minimal Residual Algorithm for Solving Nonsymmetric Linear Systems

Topics include GMRES, Krylov subspace methods, Nonsymmetric linear systems, Arnoldi process, Minimal residual methods, Iterative solvers, Numerical linear algebra.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Saad and Schultz introduce GMRES, a Krylov-subspace method for nonsymmetric linear systems that minimizes the residual norm over the Arnoldi basis at each iteration. The paper is foundational for modern iterative linear solvers, especially large sparse nonsymmetric systems where conjugate gradients does not apply.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present an iterative method for solving linear systems, which has the property of minimizing at every step the norm of the residual vector over a Krylov subspace. The algorithm is derived from the Arnoldi process for constructing an l2-orthogonal basis of Krylov subspaces. It can be considered as a generalization of Paige and Saunders' MINRES algorithm and is theoretically equivalent to the Generalized Conjugate Residual (GCR) method and to ORTHODIR. The new algorithm presents several advantages over GCR and ORTHODIR.
