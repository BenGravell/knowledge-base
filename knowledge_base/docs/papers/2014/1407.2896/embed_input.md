Asymptotically Optimal Sampling-based Kinodynamic Planning

Topics include Kinodynamic planning, Asymptotic optimality, BVP-free, Sparse tree, SST.

SST is a kinodynamic planner that requires no 2-point BVP solver or steering function, instead relying solely on forward propagation of control actions while maintaining a sparse sample set for computational efficiency.

Sampling-based algorithms are viewed as practical solutions for high-dimensional motion planning. Recent progress has taken advantage of random geometric graph theory to show how asymptotic optimality can also be achieved with these methods. Achieving this desirable property for systems with dynamics requires solving a two-point boundary value problem (BVP) in the state space of the underlying dynamical system. It is difficult, however, if not impractical, to generate a BVP solver for a variety of important dynamical models of robots or physically simulated ones. Thus, an open challenge was whether it was even possible to achieve optimality guarantees when planning for systems without access to a BVP solver. This work resolves the above question and describes how to achieve asymptotic optimality for kinodynamic planning using incremental sampling-based planners by introducing a new rigorous framework. Two new methods, STABLE_SPARSE_RRT (SST) and SST*, result from this analysis, which are asymptotically near-optimal and optimal, respectively.

## Introduction

Kinodynamic Planning: For many interesting robots it is difficult to adapt a collision-free path into a feasible one given the underlying dynamics. This class of robots includes ground vehicles at high-velocities (Likhachev & Ferguson ), unmanned aerial vehicles, such as fixed-wing airplanes (Richter et al. ), or articulated robots with dynamics, including balancing and locomotion systems (Kuindersma et al. ).

Summary of Contribution: This paper introduces a new way to analyze the properties of incremental sampling-based algorithms that construct a tree data structure for a wide class of kinodynamic planning challenges. This analysis provides the conditions under which asymptotic optimality can be achieved when a planner has access only to a forward propagation model of the system's dynamics.

Includes All Collision-Free Samples
Includes All Collision-Free Samples
Sparse Data Structure / Converges to All Collision-Free Samples

## Discussion and Conclusion

Recently, the focus in sampling-based motion planning has moved to providing optimality guarantees, while balancing the computational efficiency of the related methods. Achieving this objective for systems with dynamics has generally required the generation of specialized steering functions. This work shows that a fully-random selection/propagation procedure can achieve asymptotic optimality under reasonable assumptions for kinodynamic systems.

To address these issues, this work proposed a new framework for asymptotically optimal sampling-based motion planning. The departure from previous work is the utilization of best-first selection strategy and a pruning process, which allow for fast convergence to high-quality solutions and a sparse data structure. Experiments and analytical results show the running time and space requirements of a concrete implementation of this framework, i.e., the SST approach, are better even than that of the efficient but suboptimal RRT, while SST can still improve path quality over time.
