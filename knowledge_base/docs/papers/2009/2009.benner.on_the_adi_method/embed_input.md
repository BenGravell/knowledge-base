<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the ADI Method for Sylvester Equations

Topics include ADI method, Sylvester equations, Numerical linear algebra, Matrix equations, Model reduction, Riccati equation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Studies ADI iterations for Sylvester equations, including convergence behavior and practical shift choices. The paper is useful for large-scale control and model-reduction computations where matrix equations are too large for dense solvers.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper is concerned with the numerical solution of large scale Sylvester equations AX - XB = C, Lyapunov equations as a special case in particular included, with C having very small rank. For stable Lyapunov equations, Penzl and Li and White demonstrated that the so-called Cholesky factor ADI method with decent shift parameters can be very effective. In this paper we present a generalization of the Cholesky factor ADI method for Sylvester equations. An easily implementable extension of Penzl's shift strategy for the Lyapunov equation is presented for the current case. It is demonstrated that Galerkin projection via ADI subspaces often produces much more accurate solutions than ADI solutions.
