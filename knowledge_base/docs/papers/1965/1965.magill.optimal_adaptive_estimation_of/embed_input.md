<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimal Adaptive Estimation of Sampled Stochastic Processes

Topics include Adaptive estimation, Multiple-model estimation, Sampled stochastic processes, Conditional mean estimation, Gauss-Markov processes, Bayesian filtering, State estimation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Magill derives an optimal adaptive estimator for stochastic processes whose unknown parameter vector belongs to a finite set of possibilities. The estimator combines elemental estimators with evolving weights, anticipating multiple-model adaptive estimation and mixture-style filtering approaches for systems with uncertain dynamics.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This work presents an adaptive approach to the problem of estimating a sampled, stochastic process described by an initially unknown parameter vector. Knowledge of this quantity completely specifies the statistics of the process, and consequently the optimal estimator must "learn" the value of the parameter vector. In order that construction of the optimal estimator be feasible it is necessary to consider only those processes whose parameter vector comes from a finite set of a priori known values. Fortunately, many practical problems may be represented or adequately approximated by such a model. The optimal estimator is found to be composed of a set of elemental estimators and a corresponding set of weighting coefficients, one pair for each possible value of the parameter vector. This structure is derived using properties of the conditional mean operator. For Gauss-Markov processes the elemental estimators are linear, dynamic systems, and evaluation of the weighting coefficients involves relatively simple, nonlinear calculations. The resulting system is optimum in the sense that it minimizes the expected value of a positive-definite, quadratic form in terms of the error (a generalized mean-square-error criterion).

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Because the system described in this work is optimal, it differs from previous attempts at adaptive estimation, all of which have used approximation techniques or sub-optimal, sequential, optimization procedures and.
