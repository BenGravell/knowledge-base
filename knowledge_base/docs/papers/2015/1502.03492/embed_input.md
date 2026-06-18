Gradient-based Hyperparameter Optimization through Reversible Learning

Topics include Gradient descent, Stochastic gradients, Neural networks, Optimization, Learning, Reversible learning, Hyperparameter optimization, Stochastic gradient descent.

Tuning hyperparameters of learning algorithms is hard because gradients are usually unavailable. We compute exact gradients of cross-validation performance with respect to all hyperparameters by chaining derivatives backwards through the entire training procedure. These gradients allow us to optimize thousands of hyperparameters, including step-size and momentum schedules, weight initialization distributions, richly parameterized regularization schemes, and neural network architectures. We compute hyperparameter gradients by exactly reversing the dynamics of stochastic gradient descent with momentum.

## Introduction

^†††^The order of these two authors is random. See [github.com/hips/author-roulette](github.com/hips/author-roulette)

Machine learning systems abound with hyperparameters. These can be parameters that control model complexity, such as $L_{1}$ and $L_{2}$ penalties, or parameters that specify the learning procedure itself -- step sizes, momentum decay parameters and initialization conditions. Choosing the best hyperparameters is both crucial and frustratingly difficult.

The current gold standard for hyperparameter selection is gradient-free model-based optimization Snoek et al.; Bergstra et al.; Hutter et al.. Hyperparameters are chosen to optimize the validation loss after complete training of the model parameters. These approaches have demonstrated that automatic tuning of hyperparameters can yield state-of-the-art performance. However, in general they are not able to effectively optimize more than 10 to 20 hyperparameters.

Why not use gradients? Reverse-mode differentiation allows gradients to be computed with a similar time cost to the original objective function. This approach is taken almost universally for optimization of elementary^11^1Since this paper is about hyperparameters, we use "elementary" to unambiguously denote the other sort of parameter, the "parameter-that-is-just-a-parameter-and-not-a-hyperparameter". parameters.

## Limitations

Back-propagation for training neural networks has several pitfalls that were later addressed by analysis and engineering. Likewise, the use of hypergradients also has several apparent difficulties that need to be addressed before it becomes practical. This section explores several issues with this technique that became apparent in our experiments.

## Conclusion

In this paper, we derived a computationally efficient procedure for computing gradients through stochastic gradient descent with momentum. We showed how the approximate reversibility of learning dynamics can be used to drastically reduce the memory requirement for exactly back-propagating gradients through hundreds of training iterations.
