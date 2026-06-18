From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs

In this paper we present a review of the connections between classical algorithms for solving Markov Decision Processes (MDPs) and classical gradient-based algorithms in convex optimization. Some of these connections date as far back as the 1980s, but they have gained momentum in recent years and have lead to faster algorithms for solving MDPs. In particular, two of the most popular methods for solving MDPs, Value Iteration and Policy Iteration, can be linked to first-order and second-order methods in convex optimization. In addition, recent results in quasi-Newton methods lead to novel algorithms for MDPs, such as Anderson acceleration. By explicitly classifying algorithms for MDPs as first-order, second-order, and quasi-Newton methods, we hope to provide a better understanding of these algorithms, and, further expanding this analogy, to help to develop novel algorithms for MDPs, based on recent advances in convex optimization.

## Introduction

Markov Decision Process (MDP) is a common framework modeling dynamic optimization problems, with applications ranging from reinforcement learning to healthcare and wireless sensor networks. Most of the algorithms for computing an optimal control policy are variants of two algorithms: Value Iteration (VI) and Policy Iteration (PI). Over the last 40 years, a number of works have highlighted the strong connections between these algorithms and methods from convex optimization, even though computing an optimal policy is a non-convex problem....

### Outline

tackle the potential singularity of the matrices $\left( {\mathbf{J}}_{t} \right)_{t \geq 0}$ (with restart checking),

Zhang et al. present a stabilized version of the vanilla Anderson algorithm AndVI-I. This results in ${\lim_{t\rightarrow{+ \infty}}{\mathbf{v}}_{t}} = {\mathbf{v}}^{\ast}$, but the convergence rate is not known (Theorem 3.1 in Zhang et al. ), even though the algorithm enjoys good empirical performances, typically outperforming VI ‣ From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs"). Note that this is the first result on the convergence of Anderson Acceleration, without differentiability of the operator $T$ (and with fixed-memory, i.e., with $m$ fixed)....

### Properties for non-affine operators

Clearly, VI ‣ From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs") is a first-order method for MDP. However, Policy Iteration is not, since it relies on the update ${\mathbf{v}}_{t} = {\mathbf{v}}^{\pi_{t}}$ (Policy Evaluation step).

### Mirror Descent

We introduce the MDP framework as well as the classical Value Iteration and Policy Iteration algorithms in Section 2 ‣ From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs"). We highlight the recent connections between Value Iteration and first-order methods (Gradient Descent) in Section 3. The relations between Policy Iteration and second-order methods (Newton's method) are presented in Section 4. We review Anderson Value Iteration, a quasi-Newton methods for MDPs, in Section 5....

### Notations

In this paper, $n$ and $A$ denote integers in $\mathbb{N}$. The notation $\Delta{(A)}$ refers to the simplex of size $A$....
