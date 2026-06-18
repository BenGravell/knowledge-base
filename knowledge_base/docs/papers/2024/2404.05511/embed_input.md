A High-Performant Multi-Parametric Quadratic Programming Solver

We propose a combinatorial method for computing explicit solutions to multi-parametric quadratic programs, which can be used to compute explicit control laws for linear model predictive control. In contrast to classical methods, which are based on geometrical adjacency, the proposed method is based on combinatorial adjacency. After introducing the notion of combinatorial adjacency, we show that the explicit solution forms a connected graph in terms of it. We then leverage this connectedness to propose an algorithm that computes the explicit solution. The purely combinatorial nature of the algorithm leads to computational advantages since it enables demanding geometrical operations (such as computing facets of polytopes) to be avoided. Compared with classical combinatorial methods, the proposed method requires fewer combinations to be considered by exploiting combinatorial connectedness. We show that an implementation of the proposed method can yield a speedup of about two orders of magnitude compared with state-of-the-art software packages such as MPT and POP.

## Introduction

In Model Predictive Control (MPC), a control action is determined at each time step by solving an optimization problem. When the dynamics of the system to be controlled is linear, the optimization problems in question can be cast as instances of a multi-parametric quadratic program (mpQP) of the form

The main contribution of this paper is a combinatorial method that efficiently computes the explicit solution of (LABEL:eq:rmpc-mpqp). The method is based on exploring a connected graph, similar to and, to tame the combinatorial nature of computing the explicit solution. In contrast to, the method does not rely on any geometrical operations such as computing the facets of polytopes, which makes the resulting method more efficient and reliable. In contrast to, the proposed method handles degeneracies in a more straightforward manner; the proposed method does not, for example, need to explicitly check if constraints are weakly active/inactive.

The rest of the paper is organized as follows: In Section II we describe how a multi-parametric least-distance problem (mpLDP) can be consider instead of the mpQP in (LABEL:eq:rmpc-mpqp). We then derive the explicit solution to this mpLDP and formalize a combinatorial problem for computing it. The section ends with a brief review of existing methods for computing the explicit solution. In Section III we introduce the concept of geometrical and combinatorial adjacency of active sets, and show that any pair of optimal active sets are connected by a sequence combinatorially adjacent acitve sets.

## Conclusion

We have proposed a combinatorial method for computing explicit solutions to multi-parametric quadratic programs. The method builds on optimal active sets being "combinatorially connected", which makes the explicit solution form a combinatorially connected graph. We show that an implementation of the proposed method can yield a speedup of two orders of magnitude compared to state-of-the-art software packages such as MPT and POP.

Future work include presenting details of how to implement Algorithm 1 efficiently, and to develop a parallelized version of it.
