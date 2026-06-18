Second-Order Constrained Dynamic Optimization

Topics include Differential dynamic programming, Second-order methods, Constrained optimization, Trajectory optimization.

Comparative study over the variations of differential dynamic programming for constrained trajectory optimization problems, including interior-point, augmented Lagrangian, primal-dual, and sequential quadratic programming techniques.

This paper provides an overview, analysis, and comparison of second-order dynamic optimization algorithms, i.e., constrained Differential Dynamic Programming (DDP) and Sequential Quadratic Programming (SQP). Although a variety of these algorithms have been proposed and used successfully, there exists a gap in understanding the key differences and advantages, which we aim to provide in this work. For constrained DDP, we choose methods that incorporate nonlinear programming techniques to handle state and control constraints, including Augmented Lagrangian (AL), Interior Point, Primal-Dual Augmented Lagrangian (PDAL), and Alternating Direction Method of Multipliers (ADMM). Both DDP and SQP are provided in single- and multiple-shooting formulations, where constraints that arise from dynamics are encoded implicitly and explicitly, respectively. As a byproduct of the review, we propose a single-shooting PDAL DDP that has more favorable properties than the standard AL variant, such as the robustness to the growth of penalty parameters....

## Introduction

Second-order dynamic optimization methods are powerful optimization techniques used for optimal control of systems with nonlinear dynamics and non-quadratic cost functions. Dynamic systems with these characteristics can be found in robotics, aerospace and transportation systems, economics, biology and computational neuroscience, etc. There exist two main families of methods for dynamic optimization, namely Differential Dynamic Programming (DDP) and Sequential Quadratic Programming (SQP)....

### Differential Dynamic Programming

### Consent for publication

Not applicable. {dci} The author(s) declared no potential conflicts of interest with respect to the research, authorship, and/or publication of this article. {funding} The author(s) disclosed receipt of the following financial support for the research, authorship, and/or publication of this article: Augustinos D. Saravanos and Evangelos A. Theodorou were supported by ARO Award \[grant number W911NF2010151\]; Augustinos D. Saravanos was supported by the A. Onassis Foundation Scholarship.

The constraint term in ${\hat{Q}}_{yy}$ can be excluded for better conditioning, that is, ${\hat{Q}}_{uu} \approx Q_{uu}$. In order to derive the backward pass, the optimality condition for $\hat{Q}$ under constraints is considered. Partial derivative of quadratic approximation of $\hat{Q}$ with respect to $\deltau_{k}$, first order expansion of complementary slackness, and that of slack variable give

Mapping the terms of both sides of the expanded gives

Consider the constrained optimal control problem. Here, we have the sequence of state and control as long vectors as in and a deviated trajectory as in a similar manner as in section, i.e., ${X = {\overline{X} + {\deltaX}}},{U = {\overline{U} + {\deltaU}}}$. Both single- and multiple-shooting SQP have linearized dynamics as constraints. The difference is whether the constraints are implicit or explicit. The constraints from the dynamics are linearized as below.

Using Bellman's principle of optimality, dynamic programming (DP) divides the original optimization problem into a sequence of smaller subproblems at each time step. Nevertheless, DP is known to suffer from "curse of dimensionality" because its computational and memory demands explode as the dimension of the problem increases....
