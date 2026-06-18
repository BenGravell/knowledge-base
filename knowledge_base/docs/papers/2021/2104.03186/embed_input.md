Temporal Parallelization of Dynamic Programming and Linear Quadratic Control

This article proposes a general formulation for temporal parallelization of dynamic programming for optimal control problems. We derive the elements and associative operators to be able to use parallel scans to solve these problems with logarithmic time complexity rather than linear time complexity. We apply this methodology to problems with finite state and control spaces, linear quadratic tracking control problems, and to a class of nonlinear control problems. The computational benefits of the parallel methods are demonstrated via numerical simulations run on a graphics processing unit.

## Introduction

Optimal control theory (see, e.g., ) is concerned with designing control signals to steer a system such that a given cost function is minimised, or equivalently, a performance measure is maximised. The system can be, for example, an airplane or autonomous vehicle which is steered to follow a given trajectory, an inventory system, a chemical reaction, or a mobile robot.

The main contribution of this paper is to present a parallel formulation of dynamic programming that is exact and has a time complexity $O{({\log T})}$. None of the previous works achieve these two aspects simultaneously. The central idea is to reformulate dynamic programming in terms of associative operators, which enable the use of parallel scan algorithms to parallelise the algorithm. The resulting algorithm has a span-complexity of $O{({\log T})}$, which translates into a time-complexity of $O{({\log T})}$ with a large enough number of computational cores.

In this paper, we first provide the general formulation to parallelise dynamic programming by defining conditional value functions between two different time steps and combining them via the rule . We also show how to obtain the optimal control laws and resulting trajectories making use of parallel computation. Then, we explain how this general methodology can be directly applied to problems with finite state and control spaces. The second contribution of this paper is to specialise the methodology to linear quadratic optimal control problems, that is, to linear quadratic trackers (LQTs).

## Conclusion

In this paper, we have shown how dynamic programming solutions to optimal control problems and their linear quadratic special case, the linear quadratic tracker (LQT), can be parallelised in the temporal domain by defining the corresponding associative operators and making use of parallel scans. The parallel methods have logarithmic complexity with respect to the number of time steps, which significantly reduces the linear complexity of standard (sequential) methods for long time horizon control problems. These benefits are shown via numerical experiments run on a GPU.
