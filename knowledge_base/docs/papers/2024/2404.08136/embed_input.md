Exponentially Weighted Moving Models

An exponentially weighted moving model (EWMM) for a vector time series fits a new data model each time period, based on an exponentially fading loss function on past observed data. The well known and widely used exponentially weighted moving average (EWMA) is a special case that estimates the mean using a square loss function. For quadratic loss functions EWMMs can be fit using a simple recursion that updates the parameters of a quadratic function. For other loss functions, the entire past history must be stored, and the fitting problem grows in size as time increases. We propose a general method for computing an approximation of EWMM, which requires storing only a window of a fixed number of past samples, and uses an additional quadratic term to approximate the loss associated with the data before the window. This approximate EWMM relies on convex optimization, and solves problems that do not grow with time. We compare the estimates produced by our approximation with the estimates from the exact EWMM method.

## Introduction

We consider the problem of fitting a time-varying model to a vector time series, updating it each time period as new data is observed. Assuming that recent data is more relevant than data from many periods in the past, the model is fit giving more weight to recent past values and lower weight to values far in the past.

### Rolling window model

When the loss is not quadratic, a simple recursion cannot be used. Instead we propose an approximate method that stores a fixed window of data and carries out computation that does not grow with time.

In this paper we do not suggest or recommend EWMMs for applications; we simply address the question of how to compute it, or an approximation of it, efficiently.

### Probability mass estimator

We use loss ${\ell{(x,\theta)}} = {L{({y_{t} - {\hat{y}}_{t}})}}$, where $L$ is a convex loss function. With ${L{(u)}} = {\| u\|}_{2}^{2}$, we get the exponentially weighted ordinary least squares regression model. We can use other losses such as pinball or Huber. We can add any convex regularization. With regularizer ${r{(\theta)}} = {\lambda{\|\theta\|}_{2}^{2}}$, where $\lambda > 0$ is a hyper-parameter, we obtain exponentially weighted ridge regression \[golub2013matrix, page 564\] With ${r{(\theta)}} = {\lambda{\|\theta\|}_{1}}$, we obtain the exponentially weighted LASSO regression model \[tibshirani1996regression\]....

It remains to specify the quadratic approximation of $\ell{(x_{t - M - 1};\theta)}$. We seek a convex quadratic approximation that is accurate near ${\hat{\theta}}_{t - 1}$, the previously computed parameter estimate. When $\ell$ is twice differentiable with respect to $\theta$, an obvious approximation is its second-order Taylor expansion about the previous estimate,

One simple method to do this is to fit the model at time period $t$ using a rolling window of $R$ previous values of the time series. The choice of $R$ involves a trade-off. When it is small, we have fewer data to fit our model; when it is large, the model takes longer to adapt to changes in the underlying data. We can think of a rolling window model (RWM) with window length $R$ as one that puts weight one on the last $R$ data values, and weight zero on any values more than $R$ periods in the past....
