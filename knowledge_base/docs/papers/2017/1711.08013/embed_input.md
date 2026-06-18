<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

OSQP: An Operator Splitting Solver for Quadratic Programs

Topics include Quadratic programming, Convex optimization, Operator splitting, Alternating-direction method of multipliers, First-order optimization, Embedded optimization, Model predictive control, Warm-starting, Factorization caching, Infeasibility detection, Sparse linear algebra.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces OSQP, a general-purpose convex quadratic programming solver built around an ADMM-style operator splitting that repeatedly solves a quasi-definite linear system with reusable structure. The paper is especially useful for embedded and repeated-solve settings because it combines robustness to semidefinite objectives and dependent constraints with warm starts, factorization caching, optional division-free iterations, infeasibility detection, and a compact open-source C implementation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a general-purpose solver for convex quadratic programs based on the alternating direction method of multipliers, employing a novel operator splitting technique that requires the solution of a quasi-definite linear system with the same coefficient matrix at almost every iteration. Our algorithm is very robust, placing no requirements on the problem data such as positive definiteness of the objective function or linear independence of the constraint functions. It can be configured to be division-free once an initial matrix factorization is carried out, making it suitable for real-time applications in embedded systems. In addition, our technique is the first operator splitting method for quadratic programs able to reliably detect primal and dual infeasible problems from the algorithm iterates. The method also supports factorization caching and warm starting, making it particularly efficient when solving parametrized problems arising in finance, control, and machine learning. Our open-source C implementation OSQP has a small footprint, is library-free, and has been extensively tested on many problem instances from a wide variety of application areas. It is typically ten times faster than competing interior-point methods, and sometimes much more when factorization caching or warm start is used.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

OSQP has already shown a large impact with tens of thousands of users both in academia and in large corporations.
