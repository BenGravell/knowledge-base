<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Inexact Kleinman-Newton Method for Riccati Equations

Topics include Riccati equation, Kleinman-Newton method, Inexact solves, Optimal control, Numerical linear algebra, Large-scale systems.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes Kleinman-Newton iterations for algebraic Riccati equations when the internal linear solves are performed inexactly. This is important for large-scale control problems where exact Lyapunov or linear equation solves are computationally unrealistic.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we consider the numerical solution of the algebraic Riccati equation using Newton's method. We propose an inexact variant which allows one control the number of the inner iterates used in an iterative solver for each Newton step. Conditions are given under which the monotonicity and global convergence result of Kleinman also hold for the inexact Newton iterates. Numerical results illustrate the efficiency of this method.
