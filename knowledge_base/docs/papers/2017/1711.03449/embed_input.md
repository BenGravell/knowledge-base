Optimization-Based Collision Avoidance

Topics include Collision avoidance, Trajectory optimization, Autonomous vehicles, Nonlinear optimization, Augmented Lagrangian.

Presents an optimization-based collision avoidance formulation using differentiable signed distance functions. Optimization problems are solved with general nonlinear solver IPOPT. Proposes using A* for warm-starting.

This paper presents a novel method for reformulating non-differentiable collision avoidance constraints into smooth nonlinear constraints using strong duality of convex optimization. We focus on a controlled object whose goal is to avoid obstacles while moving in an n-dimensional space. The proposed reformulation does not introduce approximations, and applies to general obstacles and controlled objects that can be represented in an n-dimensional space as the finite union of convex sets. Furthermore, we connect our results with the notion of signed distance, which is widely used in traditional trajectory generation algorithms. Our method can be used in generic navigation and trajectory planning tasks, and the smoothness property allows the use of general-purpose gradient- and Hessian-based optimization algorithms. Finally, in case a collision cannot be avoided, our framework allows us to find "least-intrusive" trajectories, measured in terms of penetration.

## Introduction

Maneuvering autonomous systems in an environment with obstacles is a challenging problem that arises in a number of practical applications including robotic manipulators and trajectory planning for autonomous systems such as self-driving cars and quadcopters. In almost all of those applications, a fundamental feature is the system's ability to avoid collision with obstacles which are, for example, humans operating in the same area, other autonomous systems, or static objects such as walls.

In this paper, we focus on a *controlled object* that moves in a general $n$-dimensional space while avoiding obstacles, and propose a novel approach for modeling obstacle avoidance constraints that overcomes the aforementioned limitations.

We show that if the controlled object and the obstacles are described by convex sets such as polytopes or ellipsoids (or can be decomposed into a finite union of such convex sets), then the collision avoidance constraints can be exactly and non-conservatively reformulated as a set of smooth non-convex constraints. This is achieved by appropriately reformulating the *distance*-function between two convex sets using strong duality of convex optimization.

## Conclusion

In this paper, we presented smooth reformulations for collision avoidance constraints for problems where the controlled object and the obstacle can be represented as the finite union of convex sets. We have shown that non-differentiable polytopic obstacle constraints can be dealt with via dualization techniques to preserve differentiability, allowing the use of gradient- and Hessian-based optimization methods. The presented reformulation techniques are exact and non-conservative, and apply equally to point-mass and full-dimensional controlled vehicles.

Our numerical studies, performed on a quadcopter trajectory planning and autonomous car parking example, indicate that, when appropriately initialized, the proposed framework is robust, real-time feasible, and able to generate dynamically feasible trajectories. Furthermore, we have seen that the initialization method is problem-dependent, and should be chosen depending on the system at hand. Current research focuses on appropriately warm starting the discretization time $T_{\text{opt}}$, as well as on methods for further speeding up computation times.
