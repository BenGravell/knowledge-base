<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Implementation of the Simultaneous Perturbation Algorithm for Stochastic Optimization

Topics include SPSA, Stochastic optimization, Simultaneous perturbation, Gradient-free optimization, Finite differences, Engineering optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Provides a practical implementation guide for simultaneous perturbation stochastic approximation, whose two-measurement gradient estimate is independent of parameter dimension. The paper is a useful companion to SPSA theory because it focuses on coefficient choices and engineering deployment details.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The need for solving multivariate optimization problems is pervasive in engineering and the physical and social sciences. The simultaneous perturbation stochastic approximation (SPSA) algorithm has recently attracted considerable attention for challenging optimization problems where it is difficult or impossible to directly obtain a gradient of the objective function with respect to the parameters being optimized. SPSA is based on an easily implemented and highly efficient gradient approximation that relies on measurements of the objective function, not on measurements of the gradient of the objective function. The gradient approximation is based on only two function measurements (regardless of the dimension of the gradient vector). This contrasts with standard finite-difference approaches, which require a number of function measurements proportional to the dimension of the gradient vector. This paper presents a simple step-by-step guide to implementation of SPSA in generic optimization problems and offers some practical suggestions for choosing certain algorithm coefficients.
