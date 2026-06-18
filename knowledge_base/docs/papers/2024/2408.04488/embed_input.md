Multi-Objective LQR with Linear Scalarization

The framework of decision-making, modeled as a Markov Decision Process (MDP), typically assumes a single objective. However, practical scenarios often involve tradeoffs between multiple objectives. We address this in the Linear Quadratic Regulator (LQR), a canonical continuous, infinite horizon MDP. First, we establish that the Pareto front for LQR is characterized by linear scalarization: a convex combination of objectives recovers all tradeoff points, making multi-objective LQR reducible to single-objective problems. This highlights an important instance where linear scalarization suffices for a non-convex problem. Second, we show the Pareto front is smooth, in that an epsilon perturbation of a scalarization parameter yields an epsilon approximation to the objective. These results inspire a simple algorithm to approximate the Pareto front via grid search over scalarization parameters, where each optimization problem retains the computational efficiency of single-objective LQR. Lastly, we extend the analysis to certainty equivalence, where unknown dynamics are replaced with estimates.

## Introduction

Modern techniques in control theory and optimization have significantly shaped the landscape of our physical and digital infrastructure, encompassing data centers, power grids, and supply chains. However, many of these systems involve a range of objective functions dictated by stakeholder input. For example, control methods have recently been employed to manage power distribution in plug-in electric vehicles. By optimizing a handcrafted objective function, Lu et al. demonstrated that their control policy enhanced system efficiency and improved vehicle response....

Traditional approaches to settings with competing objectives often rely on ad-hoc rules of thumb, heuristics, or stakeholder input to craft a single objective function. However, this method obscures the intricate relationship between different metrics, making it challenging to navigate tradeoffs without a clear understanding of each objective's relative performance. Furthermore, there typically is no single best "ranking" or a clear scalar objective function to determine which tradeoffs are preferable....

## Conclusion

In this paper, we discussed the Linear Quadratic Regulator (LQR), a prevalent model in control theory with applications spanning fields such as energy management and robotics. Traditional LQR methodologies focus on optimizing a predefined combination of objectives, which can obscure the relationship between individual metrics and complicate the identification of optimal tradeoffs. Addressing this limitation, we demonstrated the sufficiency of linear scalarization in enumerating the Pareto front in multi-objective LQR....

## Perturbation Theory for the Discrete Riccati Equation

In fact, Theorem 3.3 ‣ 3 Sufficiency of Linear Scalarization for MObjLQR") immediately implies that restricting to linear controls is without loss of generality for MObjLQR. Indeed, it is well known that the LQR objective is convex in the (potentially non-linear) control inputs $u = {(u_{t})}_{t \in {\mathbb{N}}} \in \mathcal{U}$. Combined with the fact that $\mathcal{U}$ is convex, we immediately have that ${\text{PF}{(\mathcal{U})}} = {\text{CCS}{(\mathcal{U})}}$. However, ${\text{CCS}{(\mathcal{U})}} = {\text{CCS}{(\mathcal{S})}}$ due to the optimality of linear controls for any fixed LQR problem....

By again using Lemma 10.1 ‣ 10.1 Matrix Properties ‣ 10 Auxilary Lemmas"),
