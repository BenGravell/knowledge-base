Fast Efficient Hyperparameter Tuning for Policy Gradient Methods

Topics include HOOF, Hyperparameter optimization, Policy gradients, Reinforcement learning, Sample efficiency, Meta-learning, Importance sampling, Automatic tuning.

Presents HOOF, a one-run hyperparameter tuning method for policy-gradient reinforcement learning. The method uses trajectories already collected by the learner to rank candidate policy updates via importance-weighted one-step improvement estimates, reducing the extra sampling burden of grid search or population-based tuning.

The performance of policy gradient methods is sensitive to hyperparameter settings that must be tuned for any new application. Widely used grid search methods for tuning hyperparameters are sample inefficient and computationally expensive. More advanced methods like Population Based Training that learn optimal schedules for hyperparameters instead of fixed settings can yield better results, but are also sample inefficient and computationally expensive. In this paper, we propose Hyperparameter Optimisation on the Fly (HOOF), a gradient-free algorithm that requires no more than one training run to automatically adapt the hyperparameter that affect the policy update directly through the gradient. The main idea is to use existing trajectories sampled by the policy gradient method to optimise a one-step improvement objective, yielding a sample and computationally efficient algorithm that is easy to implement. Our experimental results across multiple domains and algorithms show that using HOOF to learn these hyperparameter schedules leads to faster learning with improved performance.

## Introduction

Policy gradient methods optimise reinforcement learning policies by performing gradient ascent on the policy parameters and have shown considerable success in environments characterised by large or continuous action spaces. However, like other gradient-based optimisation methods, their performance can be sensitive to a number of key hyperparameters.

For example, the performance of first order policy gradient methods can depend critically on the learning rate, the choice of which in turn often depends on the task, the particular policy gradient method in use, and even the optimiser, e.g., RMSProp and ADAM have narrow ranges for good learning rates which may not be known a priori. Even for second order methods like Natural Policy Gradients (NPG) or Trust Region Policy Optimisation (TRPO), which are more robust to the KL divergence constraint (which can be interpreted as a learning rate), significant performance gains can often be obtained by tuning this parameter.

Table 2: Comparison of sample efficiency of HOOF over grid search.

Finally, to ascertain the sample efficiency of HOOF relative to grid search, we perform a benchmarking exercise. We used HOOF to learn both the learning rate and the entropy coefficient ($c_{2}$ in ). We split the search bounds for these across a grid with 11x11 points and ran A2C for each setting on the grid. For computational reasons we set the budget for each training run to 1 million timesteps. Given a budget of $n$ training runs, we randomly subsample $n$ points from the grid (without replacement) and note the best return....

### Robustness to HOOF Hyperparameters and Computational Costs

The main idea behind HOOF is to automatically adapt the hyperparameters during training by greedily maximising the value of the updated policy, i.e., starting with policy $\pi_{n}$ at iteration $n$, HOOF sets

PBT is a hybrid of random and sequential search, with the added benefit of adapting hyperparameters during training. It starts by training a population of hyperparameters which are then updated periodically to further explore promising hyperparameter settings. However, by requiring multiple training runs, it inherits the sample inefficiency of random search.

Similarly, variance reduction techniques such as Generalised Advantage Estimators (GAE), which trade variance for bias in policy gradient estimates,...
