<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Structured Semidefinite Programs and Semialgebraic Geometry Methods in Robustness and Optimization

Topics include Sum-of-squares optimization, Semidefinite programming, Semialgebraic geometry, Positivstellensatz, Linear matrix inequalities, Robustness analysis, Polynomial optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops semidefinite tests based on sums-of-squares decompositions and the Positivstellensatz for polynomial feasibility and optimization. The thesis also exploits cone-invariant and frequency-dependent LMI structure, with applications to robustness, copositivity, and Lyapunov analysis.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In the first part of this thesis, we introduce a specific class of Linear Matrix Inequalities (LMI) whose optimal solution can be characterized exactly. This family corresponds to the case where the associated linear operator maps the cone of positive semidefinite matrices onto itself. In this case, the optimal value equals the spectral radius of the operator. It is shown that some rank minimization problems, as well as generalizations of the structured singular value (µ) LMIs, have exactly this property. In the same spirit of exploiting structure to achieve computational efficiency, an algorithm for the numerical solution of a special class of frequency-dependent LMIs is presented. These optimization problems arise from robustness analysis questions, via the Kalman-Yakubovich-Popov lemma. The procedure is an outer approximation method based on the algorithms used in the computation of H∞ norms for linear, time invariant systems. The result is especially useful for systems with large state dimension. The other main contribution in this thesis is the formulation of a convex optimization framework for semialgebraic problems, i.e., those that can be expressed by polynomial equalities and inequalities.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The key element is the interaction of concepts in real algebraic geometry (Positivstellensatz) and semidefinite programming. To this end, an LMI formulation for the sums of squares decomposition for multivariable polynomials is presented. Based on this, it is shown how to construct sufficient Positivstellensatz-based convex tests to prove that certain sets are empty. Among other applications, this leads to a nonlinear extension of many LMI based results in uncertain linear system analysis. Within the same framework, we develop stronger criteria for matrix copositivity, and generalizations of the well-known standard semidefinite relaxations for quadratic programming. Some applications to new and previously studied problems are presented. A few examples are Lyapunov function computation, robust bifurcation analysis, structured singular values, etc. It is shown that the proposed methods allow for improved solutions for very diverse questions in continuous and combinatorial optimization.
