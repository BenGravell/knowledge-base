Differentiable Collision Avoidance Using Collision Primitives

Topics include Trajectory optimization, Motion planning, Robotics, Optimization, Planning, Collision primitives, Collision avoidance.

A central aspect of robotic motion planning is collision avoidance, where a multitude of different approaches are currently in use. Optimization-based motion planning is one method, that often heavily relies on distance computations between robots and obstacles. These computations can easily become a bottleneck, as they do not scale well with the complexity of the robots or the environment. To improve performance, many different methods suggested to use collision primitives, i.e. simple shapes that approximate the more complex rigid bodies, and that are simpler to compute distances to and from. However, each pair of primitives requires its own specialized code, and certain pairs are known to suffer from numerical issues. In this paper, we propose an easy-to-use, unified treatment of a wide variety of primitives. We formulate distance computation as a minimization problem, which we solve iteratively. We show how to take derivatives of this minimization problem, allowing it to be seamlessly integrated into a trajectory optimization method. Our experiments show that our method performs favourably, both in terms of timing and the quality of the trajectory....

## Introduction

Collision avoidance is an integral part of robotic motion planning. Cluttered environments like construction sites, where many potential collisions may occur, are burdened with great computational load. Planning paths for multiple robots requires *dynamic* and flexible collision avoidance, making the problem more difficult. Furthermore, where human collaborators are involved, robots need to plan ahead while treating the humans as unpredictable, moving obstacles. Indeed, the increasing complexity of tasks that robots are expected to perform certainly requires an equal increase in the efficiency of motion planning algorithms.

Our goal in this paper is to derive a simple, yet robust and *customizable* approach for collision avoiding trajectory optimization. A common practice with this approach is to utilize distance functions between obstacles and define motion planning as a constrained optimization problem. In that sense, the distance functions are used to penalize proximity of the robot to obstacles. Computing the true distance to an obstacle, however, can be computationally demanding. Instead, previous approaches opted to use approximations in the form of collision primitives....

## Discussion

To summarize, our approach provides a unified, straight-forward framework that can be applied to various collision primitives, and safely handles numerical issues that can arise when computing distances and its derivatives. Therefore, our distance computation scheme can seamlessly be integrated into other path planners that profit from these properties. In terms of limitations, our overall trajectory optimization framework suffers from the same drawbacks as other gradient-based methods: it can only find a local minimum....

### III-E Extension to Robot Motion Planning

where $\mathbf{p}{(\mathbf{x})}$ is a point on the primitive, and $\mathbf{v}_{l}{(\mathbf{x})}$ denote a varying number $L$ of vectors, depending on the type of primitive. All primitive shapes used in this work are visualized in Table I. We find that this set of simple primitives is sufficient for our application. Nevertheless, we note that more constraints can be added to create different shapes, e.g. ${\sum_{l = 1}^{L}t_{l}} \leq 1$ for a simplex....
