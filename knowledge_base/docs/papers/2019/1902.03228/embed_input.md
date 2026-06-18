A Smoother Way to Train Structured Prediction Models

We present a framework to train a structured prediction model by performing smoothing on the inference algorithm it builds upon. Smoothing overcomes the non-smoothness inherent to the maximum margin structured prediction objective, and paves the way for the use of fast primal gradient-based optimization algorithms. We illustrate the proposed framework by developing a novel primal incremental optimization algorithm for the structural support vector machine. The proposed algorithm blends an extrapolation scheme for acceleration and an adaptive smoothing scheme and builds upon the stochastic variance-reduced gradient algorithm. We establish its worst-case global complexity bound and study several practical variants, including extensions to deep structured prediction. We present experimental results on two real-world problems, namely named entity recognition and visual object localization. The experimental results show that the proposed framework allows us to build upon efficient inference algorithms to develop large-scale optimization algorithms for structured prediction which can achieve competitive performance on the two real-world problems.

## Introduction

Consider

where each $f^{(i)}$ is the structural hinge loss. Max-margin structured prediction was designed to forecast discrete data structures such as sequences and trees.

Batch non-smooth optimization algorithms such as cutting plane methods are appropriate for problems with small or moderate sample sizes. Stochastic non-smooth optimization algorithms such as stochastic subgradient methods can tackle problems with large sample sizes. However, both families of methods achieve the typical worst-case complexity bounds of non-smooth optimization algorithms and cannot easily leverage a possible hidden smoothness of the objective.

We introduce a general framework that allows us to bring the power of accelerated incremental optimization algorithms to the realm of structured prediction problems. To illustrate our framework, we focus on the problem of training a structural support vector machine (SSVM), and extend the developed algorithms to deep structured prediction models with nonlinear mappings.

We seek primal optimization algorithms, as opposed to saddle-point or primal-dual optimization algorithms, in order to be able to tackle structured prediction models with affine mappings such as SSVM as well as deep structured prediction models with nonlinear mappings. We show how to shade off the inherent non-smoothness of the objective while still being able to rely on efficient inference algorithms.

: We introduce a notion of smooth inference oracles that gracefully fits the framework of black-box first-order optimization. While the exp inference oracle reveals the relationship between max-margin and probabilistic structured prediction models, the top-$K$ inference oracle can be efficiently computed using simple modifications of efficient inference algorithms in many cases of interest.

: We present a new algorithm built on top of SVRG, blending an extrapolation scheme for acceleration and an adaptive smoothing scheme. We establish the worst-case complexity bounds of the proposed algorithm and extend it to the case of non-linear mappings. Finally, we demonstrate its effectiveness compared to competing algorithms on two tasks, namely named entity recognition and visual object localization.
