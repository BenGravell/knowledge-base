Fitting a Kalman Smoother to Data

Topics include Kalman filtering, Datasets.

This paper considers the problem of fitting the parameters of a Kalman smoother to data. We formulate the Kalman smoothing problem with missing measurements as a constrained least squares problem and provide an efficient method to solve it based on sparse linear algebra. We then introduce the Kalman smoother tuning problem, which seeks to find parameters that achieve low prediction error on held out measurements. We derive a Kalman smoother auto-tuning algorithm, which is based on the proximal gradient method, that finds good, if not the best, parameters for a given dataset. Central to our method is the computation of the gradient of the prediction error with respect to the parameters of the Kalman smoother; we describe how to compute this at little to no additional cost. We demonstrate the method on population migration within the United States as well as data collected from an IMU+GPS system while driving. The paper is accompanied by an open-source implementation.

## Introduction

Kalman smoothers are widely used to estimate the state of a linear dynamical system from noisy measurements. In the traditional formulation, the dynamics and output matrices are considered fixed attributes of the system; the covariance matrices of the process and sensor noise are tuned by the designer, within some limits, to obtain good performance in simulation or on the actual system. For example, it is common to use noise levels in the Kalman smoother well in excess of the actual noise, to obtain practical robustness \[3, §8\].

In this paper we take a machine learning approach to the problem of tuning a Kalman smoother. We start with the observation that (by our definition) only the output is observed. This implies that the only way we can verify that a Kalman smoother is working well is to compare the outputs we predict with those that actually occur, on new or unseen test data, i.e., data that was not used by the Kalman smoother. In machine learning terms, we would consider this output prediction error to be our error, with the goal of minimizing it....

The prediction error decreased from 13.23 to 2.97. The test error decreased from 16.57 to 1.37. The algorithm took 135 seconds to run. The diagonals of the final state and output covariance matrices were

(Note that these matrices can be scaled and the smoothing result is the same, so only relative magnitude matters.) We observe that there is more state noise in north and east dimensions than up, which makes sense. Also, there is less state noise in velocity than in position. We also observe that there is much higher measurement noise for $z$ direction in GPS, which is true with GPS. In Fig. 2 we show the position estimates before and after tuning. Visually, we see significant improvement from tuning.

for some nominal guess $A_{nom}$ and hyper-parameter $\rho > 0$.

given initial hyper-parameter vector θ1 ∈ Θ, initial step size t1, number of iterations niter,

In this section, we describe our implementation of Kalman smoother auto-tuning, as well as the results of some numerical experiments that illustrate the method. All experiments were performed on a single core of an unloaded Intel i7-8770K CPU.

To do this we formulate the Kalman smoothing problem, with missing observations, as a simple least squares problem, with a coefficient matrix that depends on the parameters, i.e.,...
