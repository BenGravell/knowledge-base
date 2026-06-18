Distributionally Robust Covariance Steering with Optimal Risk Allocation

This article extends the optimal covariance steering (CS) problem for discrete time linear stochastic systems modeled using moment-based ambiguity sets. To hedge against the uncertainty in the state distributions while performing covariance steering, distributionally robust risk constraints are employed during the optimal allocation of the risk. Specifically, a distributionally robust iterative risk allocation (DR-IRA) formalism is used to solve the optimal risk allocation problem for the CS problem using a two-stage approach. The upper-stage of DR-IRA is a convex problem that optimizes the risk, while the lower-stage optimizes the controller with the new distributionally robust risk constraints. The proposed framework results in solutions that are robust against arbitrary distributions in the considered ambiguity set. Finally, we demonstrate our proposed approach using numerical simulations. Addressing the covariance steering problem through the lens of distributional robustness marks the novel contribution of this article.

## Introduction

Intelligent and adaptive systems of the "smart world" that work under operational constraints seek to solve some instance of a constrained optimal control problem for optimizing their performance. Such constrained optimal control problems can now be increasingly solved efficiently using several numerical optimization techniques. For instance, robot path planning in uncertain environments has gained the attention of researchers worldwide as robots are being increasingly deployed to solve many real-world problems....

Control of stochastic systems can be best formulated as a problem of controlling the distribution of trajectories over time subject to constraints. Recently, the finite horizon covariance steering (CS) problem, namely, the problem of steering an initial distribution to a final distribution at a specific final time step subject to linear time varying dynamics has been explored. Specifically, the control problem in the CS problem setting involves steering the mean and the covariance to the desired terminal values....

## Conclusion and Future Directions

In this article we have incorporated an DR-IRA strategy to optimize the worst case probability of violating the state constraints at every time step within the CS problem of a linear stochastic system subject to distributionally robust risk constraints. The use of DR-IRA in the context of CS with distributionally robust risk constraints results in optimal solutions that have a true risk much closer to the intended design requirements, compared to the use of a uniform risk allocation. We also extended the approach to quadratic chance constraints in the form of convex cones....

### III-C2 Distributionally Robust Iterative Risk Allocation (DR-IRA) Algorithm

### III-B Distributionally Robust Polytopic Joint Risk Constraints

The proof uses the same arguments as in and hence is omitted. ∎

Control of stochastic systems often involves optimizing the system's objective subject to chance constraints, where one assumes that the system uncertainties follow a known distribution and enforces that the system constraints hold with high probability as a function of the decision variables. The number of constraint violations, called the total risk budget, is usually a user-defined a priori specification and is a natural metric to assess risk....
