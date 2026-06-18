Low Rank Forecasting

We consider the problem of forecasting multiple values of the future of a vector time series, using some past values. This problem, and related ones such as one-step-ahead prediction, have a very long history, and there are a number of well-known methods for it, including vector auto-regressive models, state-space methods, multi-task regression, and others. Our focus is on low rank forecasters, which break forecasting up into two steps: estimating a vector that can be interpreted as a latent state, given the past, and then estimating the future values of the time series, given the latent state estimate. We introduce the concept of forecast consistency, which means that the estimates of the same value made at different times are consistent. We formulate the forecasting problem in general form, and focus on linear forecasters, for which we propose a formulation that can be solved via convex optimization. We describe a number of extensions and variations, including nonlinear forecasters, data weighting, the inclusion of auxiliary data, and additional objective terms. We illustrate our methods with several examples.

## Forecasting

We consider the problem of forecasting future values of a vector time series $x_{t} \in \text{R}^{n}$, $t = {1,2,\ldots}$, given previously observed values. At each time $t$ we form an estimate of the future values $x_{t + 1},\ldots,x_{t + H}$, where $H$ is our prediction horizon. We denote these as ${\hat{x}}_{t + {1|t}},{\hat{x}}_{t + {2|t}},\ldots,{\hat{x}}_{t + {H|t}}$, where ${\hat{x}}_{\tau|t}$ is our prediction of $x_{\tau}$ made at time $t$. These estimates are based on the $M$ current and past values, $x_{t},x_{t - 1},\ldots,x_{{t - M} + 1}$, where $M$ is the memory of our forecaster.

We introduce some notation to denote these windows of past and future values. We define the *past* at time $t$ as

We make the observation that $p_{t}$ and $p_{t + 1}$ are related by a block shift, since

where $a_{i:j}$ denotes the subvector of $a$ with entries $i,\ldots,j$. A similar shift structure holds for $f_{t}$.
