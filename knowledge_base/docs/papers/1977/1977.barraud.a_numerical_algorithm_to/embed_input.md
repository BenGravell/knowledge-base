<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Numerical Algorithm to Solve AT X A - X = Q

Topics include Discrete Lyapunov equation, Matrix equations, Numerical algorithms, Control theory, Stability analysis, Linear systems.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Barraud proposes an algorithm for the discrete Lyapunov equation A^T X A - X = Q that avoids both large dense linear-system formulations and stability assumptions on A. The method targets lower storage and cubic arithmetic cost, making Lyapunov-equation solution more practical for larger control problems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Two kinds of algorithm are usually resorted to in order to solve the well-known Lyapounov discrete equation AT X A - X = Q: transformation of the original linear system in a classical one with n(n+1)/2 unknowns, and iterative scheme. The first requires n4/4 storage words and a cost of n6/3 multiplications, which is impractical with a large system, and the second applies only if A is a stable matrix. The solution proposed requires no stability assumption and operates in only some n2 words and n3 multiplications.
