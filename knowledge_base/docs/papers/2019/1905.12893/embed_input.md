A General Optimization Framework for Dynamic Time Warping

The goal of dynamic time warping is to transform or warp time in order to approximately align two signals together. We pose the choice of warping function as an optimization problem with several terms in the objective. The first term measures the misalignment of the time-warped signals. Two additional regularization terms penalize the cumulative warping and the instantaneous rate of time warping; constraints on the warping can be imposed by assigning the value +inf to the regularization terms. Different choices of the three objective terms yield different time warping functions that trade off signal fit or alignment and properties of the warping function. The optimization problem we formulate is a classical optimal control problem, with initial and terminal constraints, and a state dimension of one. We describe an effective general method that minimizes the objective by discretizing the values of the original and warped time, and using standard dynamic programming to compute the (globally) optimal warping function with the discretized values. Iterated refinement of this scheme yields a high accuracy warping function in just a few iterations.

## Abstract

The goal of *dynamic time warping* is to transform or warp time in order to approximately align two signals together. We pose the choice of warping function as an optimization problem with several terms in the objective. The first term measures the misalignment of the time-warped signals. Two additional regularization terms penalize the cumulative warping and the instantaneous rate of time warping; constraints on the warping can be imposed by assigning the value $+ \infty$ to the regularization terms.

## Signals

A (vector-valued) signal $f$ is a function $f:{{\lbrack a,b\rbrack}\rightarrow\text{R}^{d}}$, with argument time. A signal can be specified or described in many ways, for example a formula, or via a sequence of samples along with a method for interpolating the signal values in between samples.

## Time warp function

Suppose $\phi:{{\lbrack 0,1\rbrack}\rightarrow{\lbrack 0,1\rbrack}}$ is increasing, with ${\phi{}} = 0$ and ${\phi{}} = 1$. We refer to $\phi$ as the *time warp function*, and $\tau = {\phi{(t)}}$ as the warped time associated with real or original time $t$. When ${\phi{(t)}} = t$ for all $t$, the warped time is the same as the original time. In general we can think of

as the amount of cumulative warping at time $t$, and

## Conclusion

We claim three main contributions. We propose a full reformulation of DTW in continuous time that eliminates singularities without the need for preprocessing or step functions. Because our formulation allows for non-uniformly sampled signals, we are the first to demonstrate how validation can be used for DTW model selection. Finally, we offer an implementation that runs 50x faster than state-of-the-art methods on typical problem sizes, and distribute our C++ code (as well as all of our example data) as an open-source Python package called GDTW.
