A Smoother Way to Train Structured Prediction Models

We present a framework to train a structured prediction model by performing smoothing on the inference algorithm it builds upon. Smoothing overcomes the non-smoothness inherent to the maximum margin structured prediction objective, and paves the way for the use of fast primal gradient-based optimization algorithms. We illustrate the proposed framework by developing a novel primal incremental optimization algorithm for the structural support vector machine. The proposed algorithm blends an extrapolation scheme for acceleration and an adaptive smoothing scheme and builds upon the stochastic variance-reduced gradient algorithm. We establish its worst-case global complexity bound and study several practical variants, including extensions to deep structured prediction. We present experimental results on two real-world problems, namely named entity recognition and visual object localization. The experimental results show that the proposed framework allows us to build upon efficient inference algorithms to develop large-scale optimization algorithms for structured prediction which can achieve competitive performance on the two real-world problems.

## Introduction

Consider the optimization problem arising when training maximum margin structured prediction models:

where each $f^{(i)}$ is the structural hinge loss. Max-margin structured prediction was designed to forecast discrete data structures such as sequences and trees.

We introduced a general notion of smooth inference oracles in the context of black-box first-order optimization. This allows us to set the scene to extend the scope of fast incremental optimization algorithms to structured prediction problems owing to a careful blend of a smoothing strategy and an acceleration scheme. We illustrated the potential of our framework by proposing a new incremental optimization algorithm to train structural support vector machines both enjoying worst-case complexity bounds and demonstrating competitive performance on two real-world problems....

There are several potential venues for future work. When there is no discrete structure that admits efficient inference algorithms, it could be beneficial to not treat inference as a black-box numerical procedure. Instance-level improved algorithms along the lines of Hazan et al. could also be interesting to explore.

Eq. follows from plugging in in for $k \geq 1$, while for $k = 0$, it is true by definition. Eq. follows from plugging in. Eq. follows from and. Lastly, to show, we shall show instead that is equivalent to the update for ${\mathbf{z}}_{k}$. We have,

The max-marginal of $\psi$ relative to a variable $y_{v}$ is defined, for $j \in \mathcal{Y}_{v}$ as

### Convergence Guarantee

Batch non-smooth optimization algorithms such as cutting plane methods are appropriate for problems with small or moderate sample sizes. Stochastic non-smooth optimization algorithms such as stochastic subgradient methods can tackle problems with large sample sizes. However, both families of methods achieve the typical worst-case complexity bounds of non-smooth optimization algorithms and cannot easily leverage a possible hidden smoothness of the objective.

Furthermore, as significant progress is being made on incremental smooth optimization algorithms for training unstructured prediction models, we would like to transfer such advances and design faster optimization algorithms to train structured prediction models....
