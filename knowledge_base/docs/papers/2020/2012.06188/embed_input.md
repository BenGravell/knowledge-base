Recent Theoretical Advances in Non-Convex Optimization

Topics include Convex optimization, Neural networks, Optimization, Stationary point, Optimization problem, Convex function.

Motivated by recent increased interest in optimization algorithms for non-convex optimization in application to training deep neural networks and other optimization problems in data analysis, we give an overview of recent theoretical results on global performance guarantees of optimization algorithms for non-convex optimization. We start with classical arguments showing that general non-convex problems could not be solved efficiently in a reasonable time. Then we give a list of problems that can be solved efficiently to find the global minimizer by exploiting the structure of the problem as much as it is possible. Another way to deal with non-convexity is to relax the goal from finding the global minimum to finding a stationary point or a local minimum. For this setting, we first present known results for the convergence rates of deterministic first-order methods, which are then followed by a general theoretical analysis of optimal stochastic and randomized gradient schemes, and an overview of the stochastic first-order methods.

## Introduction

In this survey, we consider non-convex optimization problems in different settings, including stochastic optimization. We are mainly motivated by an increased interest in such problems in connection to applications in machine learning and data analysis, and our main focus is on the methods which possess theoretical guarantees for their global convergence rate or complexity. As we explain first by providing classical examples murty1987some; nesterov2018lectures, there is no hope to have any theoretical guarantees for finding a global minimizer in a general non-convex optimization problem in a reasonable time.

In the last 20 years, theoretical analysis of the global convergence rate or global complexity guarantees has become de facto a standard in the area of numerical optimization. Since the convexity of the problem allows for such an analysis, many global complexity and convergence results have been obtained in convex optimization ben-tal2001lectures; bubeck2015convex; nesterov2018lectures; lan2020first; dvurechensky2020advances; dvurechensky2021first-order.

Since, in general, non-convex optimization problems cannot be made efficiently solved, we consider several ways to relax this challenging goal. The first relaxation consists of finding problems with hidden convexity or in a convex reformulation of the problem. This requires exploitation of the problem structure as much as it is possible, which limits the generality of the approach, yet leading to a possibility to find a global solution. Another way is to change the goal from finding the global solution to finding a stationary point or a local extremum.

## Global Optimization is NP-hard

Following murty1987some, we consider an example which illustrates that the problem of finding the exact global solution of a non-convex problem is NP-hard. To that end, we consider the minimization problem
