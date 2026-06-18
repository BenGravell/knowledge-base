A High-Performant Multi-Parametric Quadratic Programming Solver

We propose a combinatorial method for computing explicit solutions to multi-parametric quadratic programs, which can be used to compute explicit control laws for linear model predictive control. In contrast to classical methods, which are based on geometrical adjacency, the proposed method is based on combinatorial adjacency. After introducing the notion of combinatorial adjacency, we show that the explicit solution forms a connected graph in terms of it. We then leverage this connectedness to propose an algorithm that computes the explicit solution. The purely combinatorial nature of the algorithm leads to computational advantages since it enables demanding geometrical operations (such as computing facets of polytopes) to be avoided. Compared with classical combinatorial methods, the proposed method requires fewer combinations to be considered by exploiting combinatorial connectedness. We show that an implementation of the proposed method can yield a speedup of about two orders of magnitude compared with state-of-the-art software packages such as MPT and POP.

## Introduction

In Model Predictive Control (MPC), a control action is determined at each time step by solving an optimization problem. When the dynamics of the system to be controlled is linear, the optimization problems in question can be cast as instances of a multi-parametric quadratic program (mpQP) of the form

where the decision variable $x \in {\mathbb{R}}^{n}$ is related to the control action, and the parameter $\theta \in \Theta_{0} \subseteq {\mathbb{R}}^{p}$ is related to setpoints and the system state. The parameter set $\Theta_{0}$ is assumed to be a polyhedron. For a given linear (and time-invariant) MPC application, the Hessian $H \succ 0$ and the constraint matrix $A \in {\mathbb{R}}^{m \times n}$ are constant. Moreover, both the linear cost $f:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}^{n}}$ and the constraint offset $b:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}^{m}}$ are affine functions of $\theta$....

We have proposed a combinatorial method for computing explicit solutions to multi-parametric quadratic programs. The method builds on optimal active sets being "combinatorially connected", which makes the explicit solution form a combinatorially connected graph. We show that an implementation of the proposed method can yield a speedup of two orders of magnitude compared to state-of-the-art software packages such as MPT and POP.

Future work include presenting details of how to implement Algorithm 1 efficiently, and to develop a parallelized version of it.

## A combinatorial connected-graph algorithm

To form an explicit solution to, we are interested in parameters for which a given active set $\mathcal{A}$ leads to a solvable system. The set of all such parameters for a given active set is known as a critical region:

Note that two active sets being geometrically adjacent does not generally imply that they are combinatorially adjacent, but it does imply that they are combinatorially connected. An illustrative example of this distinction is given in Example 1 in. Geometrical adjacency does, however, imply combinatorial adjacency when no degeneracies occur, which follows directly from Theorem 2 in.

Albeit straightforward to theoretically derive the explicit solution, it is not as straightforward to compute the corresponding polyhedral regions efficiently and reliably....
