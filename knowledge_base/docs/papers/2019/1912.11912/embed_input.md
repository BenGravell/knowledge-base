Quasi-Newton Trust Region Policy Optimization

Topics include Reinforcement learning, Policy optimization, Trust region methods, Quasi-Newton methods.

Applies a quasi-Newton Hessian approximation within the TRPO trust region framework, achieving better sample efficiency and faster convergence than standard TRPO by making more informed second-order parameter updates.

We propose a trust region method for policy optimization that employs Quasi-Newton approximation for the Hessian, called Quasi-Newton Trust Region Policy Optimization QNTRPO. Gradient descent is the de facto algorithm for reinforcement learning tasks with continuous controls. The algorithm has achieved state-of-the-art performance when used in reinforcement learning across a wide range of tasks. However, the algorithm suffers from a number of drawbacks including: lack of stepsize selection criterion, and slow convergence. We investigate the use of a trust region method using dogleg step and a Quasi-Newton approximation for the Hessian for policy optimization. We demonstrate through numerical experiments over a wide range of challenging continuous control tasks that our particular choice is efficient in terms of number of samples and improves performance

## Introduction

Reinforcement Learning (RL) is a learning framework that handles sequential decision-making problems, wherein an 'agent' or decision maker learns a policy to optimize a long-term reward by interacting with the (unknown) environment. At each step, an RL agent obtains evaluative feedback (called reward or cost) about the performance of its action, allowing it to improve (maximize or minimize) the performance of subsequent actions. Recent research has resulted in remarkable success of these algorithms in various domains like computer games, robotics, etc.

Notably, the Trust Region Policy Optimization (TRPO) has been proposed to provide monotonic improvement of policy performance. TRPO relies on a linear model of the objective function and quadratic model of the constraints to determine a candidate search direction. Even though a theoretically justified trust region radius is derived such a radius cannot be computed and hence, linesearch is employed for obtaining a stepsize that ensures progress to a solution. Consequently, TRPO is a scaled gradient descent algorithm and is not a trust region algorithm as the name suggests.

Our objective in this work is to show that a *classical trust region method* in conjunction with *quadratic model* of the objective addresses the drawbacks of TRPO. It is well known that incorporating curvature information of the objective function (i.e. quadratic approximation) allows for rapid convergence in the neighborhood of a solution. Far from a solution, the curvature information should be incorporated in a manner that ensures the search direction improves on the reduction obtained by a linear model.

accelerate the convergence to an optimal policy, and
