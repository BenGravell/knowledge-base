Fitting a Linear Control Policy to Demonstrations with a Kalman Constraint

We consider the problem of learning a linear control policy for a linear dynamical system, from demonstrations of an expert regulating the system. The standard approach to this problem is policy fitting, which fits a linear policy by minimizing a loss function between the demonstrations and the policy's outputs plus a regularization function that encodes prior knowledge. Despite its simplicity, this method fails to learn policies with low or even finite cost when there are few demonstrations. We propose to add an additional constraint to policy fitting, that the policy is the solution to some LQR problem, i.e., optimal in the stochastic control sense for some choice of quadratic cost. We refer to this constraint as a Kalman constraint. Policy fitting with a Kalman constraint requires solving an optimization problem with convex cost and bilinear constraints. We propose a heuristic method, based on the alternating direction method of multipliers (ADMM), to approximately solve this problem. Numerical experiments demonstrate that adding the Kalman constraint allows us to learn good, i.e., low cost, policies even when very few data are available.

## Introduction

### Fitting a linear policy to demonstrations

Typically, we find a control policy for a task as follows. We first design a cost function that encodes the desired outcomes of the task, then find a control policy that minimizes that cost function, and finally we observe or simulate the behavior of this control policy on the true system. We repeat this process until we are content with the control policy's performance, either in simulation or in the real world.

## Conclusion

In this paper, we introduced a method for learning policies from demonstrations in linear systems and showed in numerical experiments that this method outperforms a widely-used baseline. Our method, which is based on convex optimization, is easy to implement and consistently produces reliable results, in contrast to gradient-based methods that are difficult to make work. We believe that this method and its extensions (see §5) have wide-ranging practical applications, especially in the domain of autonomous driving; indeed, a rigorous examination of this claim is the subject of future work....

### Interpretability

## Policy fitting with a Kalman constraint

## Examples

This procedure (optimization-based control) has been successfully applied to many tasks. However, for complex tasks, it is often difficult to find a cost function that precisely captures the desired task outcomes and can be optimized effectively. For example, in autonomous driving, it is difficult, if not impossible, to construct a cost function that reliably generates "comfortable" driving behavior. For such tasks, the established procedure mentioned above is very expensive, time-consuming, and tedious, if it works at all.

Returning to the autonomous driving example, while it may be difficult to choose a cost function that captures "comfortable" driving behavior, it is relatively straightforward for human operators to provide demonstrations of such behavior. Similarly, for many other tasks, it is easier to collect demonstrations of (nearly) optimal behavior than it is to define a good cost function. This line of thought has motivated a long line of research on learning from demonstrations.

Despite this, there has been comparatively little work on learning from demonstrations in linear systems. This is surprising, since there are many practical applications of linear systems....
