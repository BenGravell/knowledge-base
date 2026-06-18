Revisiting the Asymptotic Optimality of RRT*

Topics include Motion planning, Asymptotically optimal, Probabilistically complete, Rapidly-exploring random tree star.

This paper, from the original authors and friends, corrects some small mistakes in the theory of the asymptotic optimality results and offers new proof techniques.

RRT* is one of the most widely used sampling-based algorithms for asymptotically-optimal motion planning. RRT* laid the foundations for optimality in motion planning as a whole, and inspired the development of numerous new algorithms in the field, many of which build upon RRT* itself. In this paper, we first identify a logical gap in the optimality proof of RRT*, which was developed by Karaman and Frazzoli. Then, we present an alternative and mathematically-rigorous proof for asymptotic optimality. Our proof suggests that the connection radius used by RRT* should be increased from γ (log n/n)1/d to γ' (log n/n)1/(d+1) in order to account n n for the additional dimension of time that dictates the samples' ordering. Here γ, γ' are constants, and n, d are the number of samples and the dimension of the problem, respectively.

## Introduction

For many robot motion-planning applications, feasibility is not enough---we further desire path plans that are of high quality, reflecting a need for robots that can achieve their goals with efficiency, alacrity, and economy of motion. To this end we seek planning algorithms that can be trusted, whatever obstacle environment a robot faces, to produce optimal or near-optimal plans with minimal scenario-specific tuning. The advent of the asymptotically-optimal rapidly-exploring random tree (RRT^∗^) algorithm has ushered in a decade of theoretical and practical successes in the development of optimal sampling-based motion-planning algorithms.

Although proposed in its initial form for the case of minimum-length path planning for robots without dynamic constraints, RRT^∗^ has been extended to handle kinodynamic planning problems including robotic systems governed by non-holonomic constraints, more expressive costs accounting for robot energy expenditure, and even to plan paths that minimize violation of safety rules or that otherwise balance performance considerations with safety constraints. Heuristic modifications to the core algorithm have also been demonstrated that improve practical RRT^∗^ implementations.

## Conclusion

In this paper we revisited the original asymptotic-optimality proof of RRT^∗^ in, and discussed an apparent logical gap within it. We then introduced an alternative proof that amends this logical gap. Our new proof suggests that the connection radius of RRT^∗^ should be slightly larger than the original bound on the radius that was developed in. We leave the question of whether our bound is tight, i.e., whether the exponent of $1/{({d + 1})}$ in Equation can be lowered to $1/d$, to future research. The practical successes of the algorithm and its extensions, using the exponent $1/d$, provide some evidence that this might be the case.

### Theorem 1

Figure 1: Illustration of the components in the original proof. (a) The robustly-optimal path σε is drawn as a black curve. (b) Discs represent the balls Bn, 1, …, Bn, Mn, whose centers are denoted as red bullets along σε. The path σn connecting samples between adjacent balls in an increasing order is illustrated as a blue curve. (c) A problematic scenario (Section III-B), where the RRT∗ tree G yields a suboptimal solution, is depicted in green.
