A General Optimization Framework for Dynamic Time Warping

The goal of dynamic time warping is to transform or warp time in order to approximately align two signals together. We pose the choice of warping function as an optimization problem with several terms in the objective. The first term measures the misalignment of the time-warped signals. Two additional regularization terms penalize the cumulative warping and the instantaneous rate of time warping; constraints on the warping can be imposed by assigning the value +inf to the regularization terms. Different choices of the three objective terms yield different time warping functions that trade off signal fit or alignment and properties of the warping function. The optimization problem we formulate is a classical optimal control problem, with initial and terminal constraints, and a state dimension of one. We describe an effective general method that minimizes the objective by discretizing the values of the original and warped time, and using standard dynamic programming to compute the (globally) optimal warping function with the discretized values. Iterated refinement of this scheme yields a high accuracy warping function in just a few iterations....

## Abstract

The goal of *dynamic time warping* is to transform or warp time in order to approximately align two signals together. We pose the choice of warping function as an optimization problem with several terms in the objective. The first term measures the misalignment of the time-warped signals. Two additional regularization terms penalize the cumulative warping and the instantaneous rate of time warping; constraints on the warping can be imposed by assigning the value $+ \infty$ to the regularization terms....

## Background

## Conclusion

We claim three main contributions. We propose a full reformulation of DTW in continuous time that eliminates singularities without the need for preprocessing or step functions. Because our formulation allows for non-uniformly sampled signals, we are the first to demonstrate how validation can be used for DTW model selection. Finally, we offer an implementation that runs 50x faster than state-of-the-art methods on typical problem sizes, and distribute our C++ code (as well as all of our example data) as an open-source Python package called GDTW.

With these node and edge costs, the objective $\hat{f}{(\tau)}$ is the total cost of a path starting at node $\tau_{11} = 0$ and ending at $\tau_{NM} = 1$. (Infeasible paths, for examples ones for which $\tau_{{i + 1},k} < \tau_{i,j}$, have cost $+ \infty$.) Our problem is therefore to find the shortest weighted path through a graph, which is readily done by dynamic programming.

It can be formulated as a classical continuous-time optimal control problem, with scalar state $\phi{(t)}$ and action or input ${u{(t)}} = {\phi^{\prime}{(t)}}$:

We will show how to extend our formulation to address complex scenarios, such as aligning a portion of a signal to the target, regularization of higher-order derivatives, and symmetric time warping, where both signals align to each other.

The goal of dynamic time warping (DTW) is to find a time warping function that transforms, or warps, time in order to approximately align two signals together. At the same time, we prefer that the time warping be as gentle as possible, in some sense, or we require that it satisfy some requirements.

DTW is a versatile tool used in many scientific fields, including biology, economics, signal processing, finance, and robotics....
