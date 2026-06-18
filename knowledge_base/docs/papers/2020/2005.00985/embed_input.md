Constrained Differential Dynamic Programming Revisited

Topics include Differential dynamic programming, Constrained optimization, Augmented Lagrangian, Trajectory optimization.

Revisits constrained DDP with augmented Lagrangian methods, improving constraint handling within the DDP backward-forward pass framework. Contemporary with ALTRO, but from a different group with a different perspective on convergence.

Differential Dynamic Programming (DDP) has become a well established method for unconstrained trajectory optimization. Despite its several applications in robotics and controls, however, a widely successful constrained version of the algorithm has yet to be developed. This paper builds upon penalty methods and active-set approaches towards designing a Dynamic Programming-based methodology for constrained optimal control. Regarding the former, our derivation employs a constrained version of Bellman's principle of optimality, by introducing a set of auxiliary slack variables in the backward pass. In parallel, we show how Augmented Lagrangian methods can be naturally incorporated within DDP, by utilizing a particular set of penalty-Lagrangian functions that preserve second-order differentiability. We demonstrate experimentally that our extensions (individually and combinations thereof) enhance significantly the convergence properties of the algorithm, and outperform previous approaches on a large number of simulated scenarios.

## Introduction

Trajectory optimization problems arise very frequently in robotics and controls applications. Examples include finding suitable motions for robotic grasping and manipulation tasks, or minimizing fuel for orbital transfers. Mathematically speaking, such problems require computing a state/control sequence that minimizes a specified cost function, while satisfying the dynamics constraints of the agent. Common methodologies for trajectory optimization rely on optimal control and/or optimization theory....

One of the most successful trajectory optimization algorithms is Differential Dynamic Programming (DDP), originally developed by Jacobson and Mayne. DDP is an indirect method which utilizes Bellman's principle of optimality to split the problem into "smaller" optimization subproblems at each time step. Under mild assumptions on the cost and dynamics, it can be shown that DDP achieves locally quadratic convergence rates....

AL is very fast for first few iterations but get slow when it comes close to constraints and sometimes violate constraints. Whereas S-KKT takes time in one iteration, but can keep feasibility in a few iterations. By combining them we may be able to compensate for weakness of both and have a better algorithm.

Future directions will include mechanisms for uncertainty representations and learning, and development of chance constrained trajectory optimization algorithms that have the benefits of the fast convergence of the proposed algorithms.

### IV-A AL-DDP and penalty function

It is known that if we use the pure Newton direction obtained by $\mu = 0$, we can take only a small step $\alpha$ before violating ${{\mathbf{s}}^{\mathsf{T}}{\mathbf{λ}}} \geq 0$. To make the direction less aggressive, and the optimization process more effective we reduce $s_{i}\lambda_{i}$ to a certain value based on the average value of elementwise product $s_{i}\lambda_{i}$, instead of zero. Note that $\mu$ is an average value of $s_{i}\lambda_{i}$ and $\mu$ must converge to zero over the optimization process. We satisfy this requirement by multiplying $\sigma$ ($0 < \sigma < 1$) \[17, Chapter 19\].\

Figure 3: Cost and max. inequality constraint of 2D car starting from several initial points.

While unconstrained DDP has been widely tested and used over the past decades, its constrained counterpart has yet to be properly established....
