Gradient-Based Optimization of Hyperparameters

Topics include Hyperparameter optimization, Gradient-based optimization, Hypergradients, Model selection, Implicit differentiation, Cholesky differentiation, Machine learning.

Develops gradient-based hyperparameter optimization by differentiating a model-selection criterion with respect to hyperparameters. The paper shows how to compute hypergradients through Cholesky decompositions for quadratic criteria and through implicit differentiation more generally, anticipating later bilevel and differentiable hyperparameter-optimization methods.

Many machine learning algorithms can be formulated as the minimization of a training criterion that involves a hyperparameter. This hyperparameter is usually chosen by trial and error with a model selection criterion. In this article we present a methodology to optimize several hyper-parameters, based on the computation of the gradient of a model selection criterion with respect to the hyperparameters. In the case of a quadratic training criterion, the gradient of the selection criterion with respect to the hyperparameters is efficiently computed by backpropagating through a Cholesky decomposition. In the more general case, we show that the implicit function theorem can be used to derive a formula for the hyper-parameter gradient involving second derivatives of the training criterion.
