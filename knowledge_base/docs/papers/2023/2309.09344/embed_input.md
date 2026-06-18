Efficient Belief Road Map for Planning under Uncertainty

Topics include Belief-space planning, Motion planning under uncertainty, Covariance control, Roadmap, Output feedback, Robotics.

Builds a graph-based belief-space planner using covariance-control edges and road-map nodes with controlled uncertainty. The paper targets practical planning in narrow or uncertain environments where paths must manage both geometry and state-estimation quality.

Robotic systems, particularly in demanding environments like narrow corridors or disaster zones, often grapple with imperfect state estimation. Addressing this challenge requires a trajectory plan that not only navigates these restrictive spaces but also manages the inherent uncertainty of the system. We present a novel approach for graph-based belief space planning via the use of an efficient covariance control algorithm. By adaptively steering state statistics via output state feedback, we efficiently craft a belief roadmap characterized by nodes with controlled uncertainty and edges representing collision-free mean trajectories. The roadmap's structured design then paves the way for precise path searches that balance control costs and uncertainty considerations. Our numerical experiments affirm the efficacy and advantage of our method in different motion planning tasks. Our open-source implementation can be found at

## Introduction

In the challenging realm of robotic motion planning, uncertainty presents a critical hurdle for effective operation in dynamic and complex real-world environments. Historically, motion planning under uncertainty evolved from deterministic motion planning foundations, adopting one of two primary trajectories: the optimization-based approach and the sampling-based strategy.

The trajectory optimization paradigm, extensively studied in works like and, transforms planning challenges into optimal control problems. This transformation necessitates the resolution of the Hamilton--Jacobi--Bellman equation through dynamic programming techniques. However, while this method promises precision, it faces significant scalability issues, often at the cost of local solutions or even infeasibility.

Building upon these advances, our research introduces a nuanced covariance steering approach for graph-based motion planning. We tackle the BRM's existing challenges by proficiently crafting probabilistic graph edges. Incorporating state estimation further aligns our methodology with the broader belief space planning framework, drawing parallels to chance-constrained strategies like CC-RRT\*. Empirical evidence, as we will present, accentuates the advantages of our approach over existing methods, showcasing both its effectiveness and efficiency in managing uncertainties.

## Conclusion and future work

This work presents an efficient belief space roadmap (PGCS-BRM) for planning under uncertainty. The proposed method models the belief as state distributions and leverages nonlinear covariance steering with safety constraints for edge construction. We also include an entropy cost in the edge costs to account for robustness under uncertainty. Experiments show that the proposed method effectively constructs BRMs in different dimensions and outperforms state-of-the-art sampling-based belief space planning methods.
