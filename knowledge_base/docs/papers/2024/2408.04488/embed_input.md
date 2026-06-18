Multi-Objective LQR with Linear Scalarization

The framework of decision-making, modeled as a Markov Decision Process (MDP), typically assumes a single objective. However, practical scenarios often involve tradeoffs between multiple objectives. We address this in the Linear Quadratic Regulator (LQR), a canonical continuous, infinite horizon MDP. First, we establish that the Pareto front for LQR is characterized by linear scalarization: a convex combination of objectives recovers all tradeoff points, making multi-objective LQR reducible to single-objective problems. This highlights an important instance where linear scalarization suffices for a non-convex problem. Second, we show the Pareto front is smooth, in that an epsilon perturbation of a scalarization parameter yields an epsilon approximation to the objective. These results inspire a simple algorithm to approximate the Pareto front via grid search over scalarization parameters, where each optimization problem retains the computational efficiency of single-objective LQR. Lastly, we extend the analysis to certainty equivalence, where unknown dynamics are replaced with estimates.

## Introduction

Modern techniques in control theory and optimization have significantly shaped the landscape of our physical and digital infrastructure, encompassing data centers, power grids, and supply chains. However, many of these systems involve a range of objective functions dictated by stakeholder input. For example, control methods have recently been employed to manage power distribution in plug-in electric vehicles. By optimizing a handcrafted objective function, Lu et al. demonstrated that their control policy enhanced system efficiency and improved vehicle response.

Traditional approaches to settings with competing objectives often rely on ad-hoc rules of thumb, heuristics, or stakeholder input to craft a single objective function. However, this method obscures the intricate relationship between different metrics, making it challenging to navigate tradeoffs without a clear understanding of each objective's relative performance. Furthermore, there typically is no single best "ranking" or a clear scalar objective function to determine which tradeoffs are preferable.

How can we characterize and approximate the Pareto front of solutions in multi-objective control? What is the computational complexity? How do these algorithms extend when the system dynamics are unknown and the certainty equivalence control is used?

## Our Contributions

Approximation of the Pareto front in an inverted pendulum problem. The x-axis denotes performance on the first objective minimizing the distance to the upright position, and the y-axis performance on the second objective of the cumulative acceleration. Performance is normalized to fall in where lower values correspond to better performance. Each point corresponds to a control in the Pareto front, where we used the algorithm in Section 4 with known dynamics matrices and ϵ = 10−1.5.

## Conclusion

In this paper, we discussed the Linear Quadratic Regulator (LQR), a prevalent model in control theory with applications spanning fields such as energy management and robotics. Traditional LQR methodologies focus on optimizing a predefined combination of objectives, which can obscure the relationship between individual metrics and complicate the identification of optimal tradeoffs. Addressing this limitation, we demonstrated the sufficiency of linear scalarization in enumerating the Pareto front in multi-objective LQR.
