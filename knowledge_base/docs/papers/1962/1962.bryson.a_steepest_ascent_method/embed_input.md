<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Steepest-Ascent Method for Solving Optimum Programming Problems

Topics include Trajectory optimization, Optimal control, Gradient descent, Adjoint equations, Numerical methods, Variational calculus.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

One of the foundational papers on gradient-based trajectory optimization, introducing the use of adjoint-equation integration to compute the steepest-ascent direction for optimal control problems with terminal constraints. The adjoint (co-state) approach is the direct predecessor of modern shooting methods and continuous-time policy gradient algorithms.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A systematic and rapid steepest-ascent numerical procedure is described for determining optimum programs for nonlinear systems with terminal constraints. The procedure uses the concept of local linearization around a nominal (nonoptimum) path. The effect on the terminal conditions of a small change in the control variable program is determined by numerical integration of the adjoint differential equations for small perturbations about the nominal path.
