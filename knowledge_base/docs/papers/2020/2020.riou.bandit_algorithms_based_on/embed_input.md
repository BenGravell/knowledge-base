<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Bandit Algorithms Based on Thompson Sampling for Bounded Reward Distributions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We focus on a classic reinforcement learning problem, called a multi-armed bandit, and more specifically in the stochastic setting with reward distributions bounded . For this model, an optimal problem-dependent asymptotic regret lower bound has been derived. However, the existing algorithms achieving this regret lower bound all require to solve an optimization problem at each step, inducing a large complexity. In this paper, we propose two new algorithms, which we prove to achieve the problem-dependent asymptotic regret lower bound. The first one, which we call Multinomial TS, is an adaptation of Thompson Sampling for Bernoulli rewards to multinomial reward distributions whose support is included in 0, 1/M, …, 1. This algorithm achieves the regret lower bound in the case of multinomial distributions with the aforementioned support, and it can be easily generalized to bounded reward distributions in by randomly rounding the observed rewards. The second algorithm we introduce, which we call Non-parametric TS, is a randomized algorithm but not based on the posterior sampling in the strict sense. At each step, it computes an average of the observed rewards with random weight.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Not only is it asymptotically optimal, but also it performs very well even for small horizons.
