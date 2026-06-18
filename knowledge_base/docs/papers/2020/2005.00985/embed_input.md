Constrained Differential Dynamic Programming Revisited

Topics include Differential dynamic programming, Constrained optimization, Augmented Lagrangian, Trajectory optimization.

Revisits constrained DDP with augmented Lagrangian methods, improving constraint handling within the DDP backward-forward pass framework. Contemporary with ALTRO, but from a different group with a different perspective on convergence.

Differential Dynamic Programming (DDP) has become a well established method for unconstrained trajectory optimization. Despite its several applications in robotics and controls, however, a widely successful constrained version of the algorithm has yet to be developed. This paper builds upon penalty methods and active-set approaches towards designing a Dynamic Programming-based methodology for constrained optimal control. Regarding the former, our derivation employs a constrained version of Bellman's principle of optimality, by introducing a set of auxiliary slack variables in the backward pass. In parallel, we show how Augmented Lagrangian methods can be naturally incorporated within DDP, by utilizing a particular set of penalty-Lagrangian functions that preserve second-order differentiability. We demonstrate experimentally that our extensions (individually and combinations thereof) enhance significantly the convergence properties of the algorithm, and outperform previous approaches on a large number of simulated scenarios.

## Introduction

Trajectory optimization problems arise very frequently in robotics and controls applications. Examples include finding suitable motions for robotic grasping and manipulation tasks, or minimizing fuel for orbital transfers. Mathematically speaking, such problems require computing a state/control sequence that minimizes a specified cost function, while satisfying the dynamics constraints of the agent. Common methodologies for trajectory optimization rely on optimal control and/or optimization theory.

In this paper we build upon the works in to develop a state- and control-constrained version of DDP in discrete time. Specifically, we extend by introducing a slack variable formulation into Bellman's principle, and thus avoid assumptions regarding the active constraints of the problem. Moreover, we propose an Augmented Lagrangian-inspired algorithm, by considering a set of penalty functions that preserves smoothness of the transformed objective function. This property was not satisfied , but is required to establish the convergence properties of DDP.

We will save the in-depth discussion about technical differences between our methods and previous papers for subsequent sections. Nevertheless, we note that a comparison among different constrained optimization methods on various simulated scenarios will be provided, which will highlight the efficiency and generalizability of our approach; something which has been lacking from previous DDP-related schemes. To the best of the authors' knowledge, such an extensive experimental study on constrained trajectory optimization has not been conducted in the past.

## Conclusion

In this paper we have introduced novel constrained trajectory optimization methods that outperform previous versions of constrained DDP. Some key ideas in this paper rely on the combination of slack variables together with augmented Lagrangian method and the KKT conditions. In particular,

Slack variables are an effective way to get lower cost with respect to alternative algorithms relying on the active set method.
