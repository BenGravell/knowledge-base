Exponentially Weighted Moving Models

An exponentially weighted moving model (EWMM) for a vector time series fits a new data model each time period, based on an exponentially fading loss function on past observed data. The well known and widely used exponentially weighted moving average (EWMA) is a special case that estimates the mean using a square loss function. For quadratic loss functions EWMMs can be fit using a simple recursion that updates the parameters of a quadratic function. For other loss functions, the entire past history must be stored, and the fitting problem grows in size as time increases. We propose a general method for computing an approximation of EWMM, which requires storing only a window of a fixed number of past samples, and uses an additional quadratic term to approximate the loss associated with the data before the window. This approximate EWMM relies on convex optimization, and solves problems that do not grow with time. We compare the estimates produced by our approximation with the estimates from the exact EWMM method.

## Introduction

We consider the problem of fitting a time-varying model to a vector time series, updating it each time period as new data is observed. Assuming that recent data is more relevant than data from many periods in the past, the model is fit giving more weight to recent past values and lower weight to values far in the past.

## Rolling window model

One simple method to do this is to fit the model at time period $t$ using a rolling window of $R$ previous values of the time series. The choice of $R$ involves a trade-off. When it is small, we have fewer data to fit our model; when it is large, the model takes longer to adapt to changes in the underlying data. We can think of a rolling window model (RWM) with window length $R$ as one that puts weight one on the last $R$ data values, and weight zero on any values more than $R$ periods in the past. One advantage of such an RWM is that the optimization problem we solve to carry out the fitting has the same size in each time period.

## Exponentially weighted moving model

Another method for fitting a time-varying model uses all past data to create the model, but puts a time-varying weight on past values that decays smoothly as we move farther back in time. A natural choice for the weights is an exponential decay. We refer to such a model as an exponentially weighted moving model (EWMM). The parameter in EWMM analogous to $R$ in an RWM is the half-life, the number of periods in the past where the weight decays to one-half.

## Exponentially weight moving average

EWMMs generalize the well known and widely used exponentially weighted moving average (EWMA). When we fit the data with a constant model using a square loss function, i.e., we attempt to estimate the mean, EWMM reduces to EWMA. But EWMM includes many other interesting data models beyond EWMA, such as exponentially weighted quantile estimation, exponentially weighted covariance estimation, and various exponentially weighted regression models, possibly with regularization.
