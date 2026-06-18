Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error

Topics include Reinforcement learning, Imitation learning, Control, Learning.

Compounding error, where small prediction mistakes accumulate over time, presents a major challenge in learning-based control. For example, this issue often limits the performance of model-based reinforcement learning and imitation learning. One common approach to mitigate compounding error is to train multi-step predictors directly, rather than relying on autoregressive rollout of a single-step model. However, it is not well understood when the benefits of multi-step prediction outweigh the added complexity of learning a more complicated model. In this work, we provide a rigorous analysis of this trade-off in the context of linear dynamical systems. We show that when the model class is well-specified and accurately captures the system dynamics, single-step models achieve lower asymptotic prediction error. On the other hand, when the model class is misspecified due to partial observability, direct multi-step predictors can significantly reduce bias and thus outperform single-step approaches....

## Introduction

A typical approach to time series forecasting is to fit a one-step ahead prediction model and apply it recursively to obtain predictions over multiple time steps. In doing so, small errors may compound over time, leading to poor long-horizon prediction. This issue hinders the application of such single-step models in e.g., controller design.

By directly training multi-step models to predict longer horizons, the issue of compounding error can be mitigated. The main drawback of doing so is that the number of parameters for a direct multi-step predictor scales with the prediction horizon, thus potentially requiring more data to achieve a desired prediction performance. While this tradeoff between prediction horizon accuracy and data requirements is broadly known to exist, it is primarily studied from an empirical perspective. We therefore lack principled guidance for exactly when direct multi-step prediction should be preferred over autoregressive rollout of single-step models....

In this work, we present a novel theoretical comparison of the asymptotic prediction error associated with autoregressive rollouts of single-step predictors and direct multi-step predictors. Our analysis offers insight into when each modeling approach is preferable. Specifically, we show that for well-specified model classes, autoregressive rollouts of single-step predictors achieve lower asymptotic prediction error. However, in the presence of model misspecification due to an incorrect Markovian assumption, multi-step predictors can significantly outperform their single-step counterparts.

These findings provide a foundation for more informed model design in learning-based control and forecasting. Promising directions for future work include: developing a rigorous analysis of intermediate approaches, such as the single-step model trained with a multi-step loss, which we investigate only empirically in this work; and extending our analysis beyond the white-noise input assumption to study how each of these prediction approaches performs in a closed-loop control setting.

### Proposition III.1

As past predictions become part of the regressor for future predictions, this approach often suffers from compounding error.

Under these definitions, and exploiting that innovations are independent across time, the error is given by

### I-A Related Work
