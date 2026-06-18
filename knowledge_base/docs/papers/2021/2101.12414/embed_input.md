Low Rank Forecasting

We consider the problem of forecasting multiple values of the future of a vector time series, using some past values. This problem, and related ones such as one-step-ahead prediction, have a very long history, and there are a number of well-known methods for it, including vector auto-regressive models, state-space methods, multi-task regression, and others. Our focus is on low rank forecasters, which break forecasting up into two steps: estimating a vector that can be interpreted as a latent state, given the past, and then estimating the future values of the time series, given the latent state estimate. We introduce the concept of forecast consistency, which means that the estimates of the same value made at different times are consistent. We formulate the forecasting problem in general form, and focus on linear forecasters, for which we propose a formulation that can be solved via convex optimization. We describe a number of extensions and variations, including nonlinear forecasters, data weighting, the inclusion of auxiliary data, and additional objective terms. We illustrate our methods with several examples.

## Introduction

### Forecasting

We consider the problem of forecasting future values of a vector time series $x_{t} \in \text{R}^{n}$, $t = {1,2,\ldots}$, given previously observed values. At each time $t$ we form an estimate of the future values $x_{t + 1},\ldots,x_{t + H}$, where $H$ is our prediction horizon. We denote these as ${\hat{x}}_{t + {1|t}},{\hat{x}}_{t + {2|t}},\ldots,{\hat{x}}_{t + {H|t}}$, where ${\hat{x}}_{\tau|t}$ is our prediction of $x_{\tau}$ made at time $t$. These estimates are based on the $M$ current and past values, $x_{t},x_{t - 1},\ldots,x_{{t - M} + 1}$, where $M$ is the memory of our forecaster....

### Nonlinear forecasters

There also exist many nonlinear forecasting methods. These methods are often based on neural networks, e.g., recurrent neural networks, convolutional neural networks, and autoencoders. Other nonlinear forecasting methods include regime switching models and NARMAX models. Recently, there have also been methods proposed that perform vector time series forecasting through matrix completion, where the vector time series are assumed share some common structures.

### Convergence

This shows that $\theta$ has rank (at most) $r$, the dimension of the latent time series. This is hardly surprising, since under this model the past and future are independent, given the current state $z_{t}$.

### Latent state dynamics

We introduce some notation to denote these windows of past and future values. We define the *past* at time $t$ as

We make the observation that $p_{t}$ and $p_{t + 1}$ are related by a block shift, since

where $a_{i:j}$ denotes the subvector of $a$ with entries $i,\ldots,j$. A similar shift structure holds for $f_{t}$.

We use ${\hat{f}}_{t}$ to denote our estimate or forecast of the future at time $t$, i.e.,

We observe that the forecasts do not necessarily have the shift structure that the past and future vectors do. While ${(f_{t + 1})}_{1:n}$ and ${(f_{t})}_{{n + 1}:{2n}}$ are both equal to $x_{t + 2}$, ${({\hat{f}}_{t + 1})}_{1:n}$ and ${({\hat{f}}_{t})}_{{n + 1}:{2n}}$ can be different. The first is ${\hat{x}}_{t + {2|{t + 1}}}$, our estimate of $x_{t + 2}$ made at time $t + 1$, whereas the second is ${\hat{x}}_{t + {2|t}}$, our estimate of $x_{t + 2}$ made at time $t$. These two estimates need not be the same. (We will come back to this soon with the concept of forecasting consistency.)
