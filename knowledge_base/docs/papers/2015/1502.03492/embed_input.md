Gradient-based Hyperparameter Optimization through Reversible Learning

Topics include Gradient descent, Stochastic gradients, Neural networks, Optimization, Learning, Reversible learning, Hyperparameter optimization, Stochastic gradient descent.

Tuning hyperparameters of learning algorithms is hard because gradients are usually unavailable. We compute exact gradients of cross-validation performance with respect to all hyperparameters by chaining derivatives backwards through the entire training procedure. These gradients allow us to optimize thousands of hyperparameters, including step-size and momentum schedules, weight initialization distributions, richly parameterized regularization schemes, and neural network architectures. We compute hyperparameter gradients by exactly reversing the dynamics of stochastic gradient descent with momentum.

## Introduction

^†††^The order of these two authors is random. See [github.com/hips/author-roulette](github.com/hips/author-roulette)

Machine learning systems abound with hyperparameters. These can be parameters that control model complexity, such as $L_{1}$ and $L_{2}$ penalties, or parameters that specify the learning procedure itself -- step sizes, momentum decay parameters and initialization conditions. Choosing the best hyperparameters is both crucial and frustratingly difficult.

In this paper, we derived a computationally efficient procedure for computing gradients through stochastic gradient descent with momentum. We showed how the approximate reversibility of learning dynamics can be used to drastically reduce the memory requirement for exactly back-propagating gradients through hundreds of training iterations.

We showed how these gradients allow the optimization of validation loss with respect to thousands of hyperparameters, something which was previously infeasible. This new ability allows the automatic tuning of most details of training neural networks. We demonstrated the tuning of detailed training schedules, regularization schedules, and neural network architectures.

### Optimizing regularization parameters

In typical machine learning applications, only a few hyperparameters (less than 20) are optimized. Since each experiment only yields a single number (the validation loss), the search rapidly becomes more difficult as the dimension of the hyperparameter vector increases. In contrast, when hypergradients are available, the amount of information gained from each training run grows along with the number of hyperparameters, allowing us to optimize thousands of hyperparameters. How can we take advantage of this new ability?

Figure 9 shows the learned penalties (normalized by row and column to have ones on the diagonal, akin to a correlation matrix). We see that the lowest layer has been partially shared, across all alphabets equally, with the upper layers much less shared. Interestingly, the top layer penalty learns to share weights between the rotated alphabets.

The current gold standard for hyperparameter selection is gradient-free model-based optimization Snoek et al.; Bergstra et al.; Hutter et al.. Hyperparameters are chosen to optimize the validation loss after complete training of the model parameters....
