Automatic Differentiation in Machine Learning: A Survey

Topics include Graphs, Optimization, Learning, Automatic differentiation, Differentiable programming, Machine learning, CLARITY.

Derivatives, mostly in the form of gradients and Hessians, are ubiquitous in machine learning. Automatic differentiation (AD), also called algorithmic differentiation or simply "autodiff", is a family of techniques similar to but more general than backpropagation for efficiently and accurately evaluating derivatives of numeric functions expressed as computer programs. AD is a small but established field with applications in areas including computational fluid dynamics, atmospheric sciences, and engineering design optimization. Until very recently, the fields of machine learning and AD have largely been unaware of each other and, in some cases, have independently discovered each other's results. Despite its relevance, general-purpose AD has been missing from the machine learning toolbox, a situation slowly changing with its ongoing adoption under the names "dynamic computational graphs" and "differentiable programming". We survey the intersection of AD and machine learning, cover applications where AD has direct relevance, and address the main implementation techniques....

## Introduction

Methods for the computation of derivatives in computer programs can be classified into four categories: manually working out derivatives and coding them; *numerical differentiation*using finite difference approximations; *symbolic differentiation*using expression manipulation in computer algebra systems such as Mathematica, Maxima, and Maple; and *automatic differentiation*, also called *algorithmic differentiation*, which is the subject matter of this paper.

Conventionally, many methods in machine learning have required the evaluation of derivatives and most of the traditional learning algorithms have relied on the computation of gradients and Hessians of an objective function. When introducing new models, machine learning researchers have spent considerable effort on the manual derivation of analytical derivatives to subsequently plug these into standard optimization procedures such as L-BFGS or stochastic gradient descent. Manual differentiation is time consuming and prone to error....

It is an exciting time for working at the intersection of AD and machine learning, and there are many opportunities for bringing advanced techniques and expertise from AD literature to bear on machine learning problems. Techniques that have been developed by the AD community such as tape reduction and elimination, fixed-point iterations, utilizing sparsity by matrix coloring, and reverse AD checkpointing are just a few examples that can find potential use in machine learning for increasing performance, improving convergence of optimization, using hardware more efficiently, and even enabling new types of machine learning models to be...

An important direction for future work is to make use of nested AD techniques in machine learning, allowing differentiation to be nested arbitrarily deep with referential transparency. Nested AD is highly relevant in hyperparameter optimization as it can effortlessly provide exact hypergradients, that is, derivatives of a training objective with respect to the hyperparameters of an optimization routine. Potential applications include Bayesian model selection and gradient-based tuning of Hamiltonian Monte Carlo step sizes and mass matrices....

### Gradient-Based Optimization

and using dual numbers as data structures for carrying the tangent value together with the primal.^1111^11Just as the complex number written $x...
