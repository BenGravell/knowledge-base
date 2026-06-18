<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Variable Metric Method for Minimization

Topics include Quasi-Newton methods, DFP, Optimization, Variable metric, Unconstrained optimization, Numerical optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

The foundational Davidon-Fletcher-Powell (DFP) quasi-Newton method, originally circulated as an Argonne National Laboratory technical report in 1959 and published formally in SIAM Journal on Optimization in 1991. DFP was the first practical quasi-Newton update formula, building a positive-definite Hessian approximation from gradient differences; it was later superseded by the closely related BFGS update.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This is a method for determining numerically local minima of differentiable functions of several variables. In the process of locating each minimum, a matrix which characterizes the behavior of the function about the minimum is determined.
