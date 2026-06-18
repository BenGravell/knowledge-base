<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CVXGEN: A Code Generator for Embedded Convex Optimization

Topics include CVXGEN, Code generation, Embedded optimization, Convex optimization, Quadratic programming, Interior-point methods, Real-time optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Describes CVXGEN, a tool that compiles a high-level convex optimization problem family into flat, dependency-free C code for a custom solver. The paper is useful because it explains the transformations, regularization, iterative refinement, and branch-light implementation choices that make generated embedded QP solvers both fast and predictable.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

CVXGEN is a software tool that takes a high level description of a convex optimization problem family, and automatically generates custom C code that compiles into a reliable, high speed solver for the problem family. The current implementation targets problem families that can be transformed, using disciplined convex programming techniques, to convex quadratic programs of modest size. CVXGEN generates simple, flat, library-free code suitable for embedding in real-time applications. The generated code is almost branch free, and so has highly predictable run-time behavior. The combination of regularization (both static and dynamic) and iterative refinement in the search direction computation yields reliable performance, even with poor quality data. In this paper we describe how CVXGEN is implemented, and give some results on the speed and reliability of the automatically generated solvers.
