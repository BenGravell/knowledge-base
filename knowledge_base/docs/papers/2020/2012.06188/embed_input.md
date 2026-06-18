Recent Theoretical Advances in Non-Convex Optimization

Topics include Convex optimization, Neural networks, Optimization, Stationary point, Optimization problem, Convex function.

Motivated by recent increased interest in optimization algorithms for non-convex optimization in application to training deep neural networks and other optimization problems in data analysis, we give an overview of recent theoretical results on global performance guarantees of optimization algorithms for non-convex optimization. We start with classical arguments showing that general non-convex problems could not be solved efficiently in a reasonable time. Then we give a list of problems that can be solved efficiently to find the global minimizer by exploiting the structure of the problem as much as it is possible. Another way to deal with non-convexity is to relax the goal from finding the global minimum to finding a stationary point or a local minimum. For this setting, we first present known results for the convergence rates of deterministic first-order methods, which are then followed by a general theoretical analysis of optimal stochastic and randomized gradient schemes, and an overview of the stochastic first-order methods....

## Introduction

In this survey, we consider non-convex optimization problems in different settings, including stochastic optimization. We are mainly motivated by an increased interest in such problems in connection to applications in machine learning and data analysis, and our main focus is on the methods which possess theoretical guarantees for their global convergence rate or complexity. As we explain first by providing classical examples murty1987some; nesterov2018lectures, there is no hope to have any theoretical guarantees for finding a global minimizer in a general non-convex optimization problem in a reasonable time....

In the last 20 years, theoretical analysis of the global convergence rate or global complexity guarantees has become de facto a standard in the area of numerical optimization. Since the convexity of the problem allows for such an analysis, many global complexity and convergence results have been obtained in convex optimization ben-tal2001lectures; bubeck2015convex; nesterov2018lectures; lan2020first; dvurechensky2020advances; dvurechensky2021first-order....

where $h > 0$ is the stepsize and $\epsilon_{k}$ is standard gaussian random variable. Non-asymptotic results demonstrating the convergence of this method to an approximate global minimum were presented in the work xu2018global. In this paper, the temperature parameter $T$ was assumed to be constant. However, other strategies are sometimes used in practice, for example,

which ensures $T_{k}\rightarrow{0 +}$ as $k\rightarrow\infty$.

In this section, we discuss variance reduction for non-convex optimization -- a special technique aimed at improving the convergence speed of SGD for finite-sum optimization problems +. The typical behaviour of SGD with constant stepsize $h$ and batch size $r < m$ is as following: during the first iterations the method converges rapidly to some neighbourhood of the solution or local minimum and then it starts to oscillate in this neighbourhood. Such oscillations of SGD are common even for strongly convex problems meaning that it is not a drawback of the problem....

### Stochastic Case: Finite Sum Minimization

where $\partial{f{(x)}}$ is a subgradient of $f{(x)}$ and $N,M$ are some constants. This class of functions was first defined in shor1967generalized and discussed in polyak1987introduction.
