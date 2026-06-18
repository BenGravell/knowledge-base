Globally Convergent Policy Search over Dynamic Filters for Output Estimation

Topics include Gradient descent, Reinforcement learning, Lyapunov methods, Learning, Linear dynamical system, Dynamical systems.

We introduce the first direct policy search algorithm which provably converges to the globally optimal dynamic filter for the classical problem of predicting the outputs of a linear dynamical system, given noisy, partial observations. Despite the ubiquity of partial observability in practice, theoretical guarantees for direct policy search algorithms, one of the backbones of modern reinforcement learning, have proven difficult to achieve. This is primarily due to the degeneracies which arise when optimizing over filters that maintain internal state. In this paper, we provide a new perspective on this challenging problem based on the notion of informativity, which intuitively requires that all components of a filter's internal state are representative of the true state of the underlying dynamical system. We show that informativity overcomes the aforementioned degeneracy. Specifically, we propose a regularizer which explicitly enforces informativity, and establish that gradient descent on this regularized objective - combined with a ``reconditioning step'' - converges to the globally optimal cost a O(1/T) rate.

## Introduction

Data used for prediction and control of real world dynamical systems is almost always noisy and incomplete (partially observed). Sensors and other measurement procedures inevitably introduce errors into the datasets, so designing reliable learning algorithms for these noisy or partially observed domains requires confronting fundamental questions of disturbance filtering and state estimation. Despite the ubiquity of partial observation in practice, these concerns are often underexplored in modern analyses of learning for control that assume perfect observations of the underlying dynamics.

In this work, we study the output estimation (OE) problem or learning to predict in partially observed linear dynamical systems. The output estimation problem is one of the most fundamental problems in theoretical statistics and learning theory. Both in theory and in practice, advances in predicting partially observed linear systems have led to successes in a variety of areas from controls to biology and economics, (c.f. e.g. Athans; Lillacci and Khammash; Gautier and Poignet ).

## Limitations of direct policy search

Through simulations and counterexamples, we show that gradient descent on the prediction loss $\mathcal{L}_{\mathtt{O}\mathtt{E}}{( \cdot )}$ can fail to recover the optimal filter for OE problem. While consistent with prior work, the failure of gradient descent remains puzzling, as the OE problem admits a convex reformulation, a fact which at first glance seems to rule out suboptimal stationary points.

## Conclusion

The work introduces the first policy search algorithm which converges to the globally optimal *dynamic* filter for the output estimation problem. We hope that our analysis serves as a valuable starting point to study direct policy search for reinforcement learning and control problems with partial observations, in which the relevant class of policies are dynamic and maintain internal state. We also hope that both our proposed principle of informativity, and our technical contributions around convex reformulations, continue to prove useful in future work.
