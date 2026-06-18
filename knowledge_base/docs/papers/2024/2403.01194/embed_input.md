A Comparative Study of Rapidly-exploring Random Tree Algorithms Applied to Ship Trajectory Planning and Behavior Generation

Topics include Rapidly-exploring random tree, Comparison study, Ship trajectory planning, Scenario generation, Electronic navigational charts, R-trees, Constrained Delaunay triangulation.

Compares variations of RRT in an application domain for marine ship navigation. The dynamic model is basically the same as for car-like vehicles.

Rapidly Exploring Random Tree (RRT) algorithms, notably used for nonholonomic vehicle navigation in complex environments, are often not thoroughly evaluated for their specific challenges. This paper presents a first such comparison study of the variants Potential-Quick RRT* (PQ-RRT*), Informed RRT* (IRRT*), RRT*, and RRT, in maritime single-query nonholonomic motion planning. Additionally, the practicalities of using these algorithms in maritime environments are discussed and outlined. We also contend that these algorithms are beneficial not only for trajectory planning in Collision Avoidance Systems (CAS) but also for CAS verification when used as vessel behavior generators. Optimal RRT variants tend to produce more distance-optimal paths but require more computational time due to complex tree wiring and nearest neighbor searches. Our findings, supported by Welch`s t-test at a significance level of Alpha = 0.05, indicate that PQ-RRT* slightly outperform IRRT* and RRT* in achieving shorter trajectory length but at the expense of higher tuning complexity and longer run-times....

## Introduction

### Background

Trajectory planning is an important aspect of ship autonomy, not only in Collision Avoidance Systems (CAS) for safe and efficient voyage, but also for the safety assurance of the former. To verify CAS safety and compliance with the International Regulations for Preventing Collision at Sea (COLREG), it will be necessary to conduct simulation-based testing in a diverse set of scenarios. The scenarios must cover varying difficulties with respect to grounding hazards or static obstacles, ships with uncertain kinematics and intentions, and environmental disturbances....

From Monte Carlo simulations on selected cases, we see that PQ-RRT\* attains more distance optimal trajectories, also verified through pair-wise hypothesis testing with Welch's $t$-test when using a significance level $\alpha = 0.05$. Here, IRRT\* and RRT\* follow close behind. This distance optimality comes naturally at the cost of increased run-time due to nearest neighbor searches and parent consideration in both tree wiring and rewiring. IRRT\* struggles with cases where obstacles cover a large part of the configuration space....

From the results and through tuning of the algorithm, it was found that the PQ-RRT\* involves much higher complexity in tuning than the other variants, because of the sample adjustment procedure and ancestor consideration. On the other hand, the IRRT\* algorithm here attains a good balance between simpler tuning and obtainable performance. It's informed sampling heuristic should, however, be improved to reduce its sample rejection rate. In the maritime domain, this can be achieved by an iterative pruning or update of a safe sea triangulation used to sample new collision-free configurations.

### Algorithm Pros and Cons

To incorporate dynamic obstacle collision avoidance, one can employ a joint simulator as in Chiang and Tapia in the steering together with adding virtual obstacles for striving towards COLREG compliance, or utilize biased sampling methods as in e.g.. However, this will not be considered in the present work.

The grounding hazards in the environment are buffered with a horizontal clearance parameter $d_{safe}$ of $0\ m$ in the first two cases, and $5\ m$ in the last case. This will in general be dependent on the map accuracy, ship type, and application....
