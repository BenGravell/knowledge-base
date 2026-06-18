Convex Co-Design of Control Barrier Functions and State Feedback Controllers for Linear Systems with Input Constraints

Topics include Control barrier functions, Safety, Sum-of-squares programming, Semidefinite programming, Input constraints, Linear systems.

Formulates joint CBF and linear feedback-controller synthesis for linear systems as a semidefinite program, including input constraints and mixed-relative-degree safe sets. The useful idea is treating safe-set certificate design and controller design as one convex co-design problem.

We study the problem of co-designing control barrier functions (CBF) and linear state feedback controllers for continuous-time linear systems. We achieve this by means of a single semi-definite optimization program. Our formulation can handle mixed-relative degree problems without requiring an explicit safe controller. Different L-norm based input limitations can be introduced as convex constraints in the proposed program. We demonstrate our results on an omni-directional car numerical example.

## Introduction

Safety is essential for feedback control systems. As a system is steered from an initial set to a target set, safety requires that the trajectory of the system avoids entering an unexpected region, or to remain inside a safe set. On the state space, safety is always formulated by means of constraints imposed on states. Based on these descriptions, two questions are raised: given a dynamical system $\overset{˙}{x} = {f{(x,u)}}$, a set of initial sets $\mathcal{I}$, and a set of safe states $\mathcal{S}$, (i) verify whether there exists a control input $u{( \cdot )}$, so that the trajectories starting from $\mathcal{I}$ stay inside...

A CBF aims to separate the safe and unsafe regions by its zero super- and sub-level sets; the initial set also belongs to the level set. In addition, there exists a control law, such that the vector field points towards the safe side on its zero sub-level set \[\]. This property is also known as *invariance*, characterized by Nagumo's theorem \[\]. It is therefore guaranteed that if the system starts from a point inside the zero super-level set, the system can always stay inside. Given a CBF, the controller that guarantees safety can be designed according to the direction requirement of vector field....

## Conclusion

In this paper we proposed a method to synthesize a control barrier function and a state feedback controller by solving a single convex program. Our approach considers quadratic control barrier functions and affine state feedback controllers. Different types of control input limits can be handled as additional convex constraints to the synthesis program. We demonstrate the efficacy of our approach on an omni-directional car collision avoidance problem. Future work concentrates towards generalizing the obtained results to allow using higher-relative degree polynomials for the CBF and the controller....

We follow the construction in Theorem. The vector $c \in {\mathbb{R}}^{2}$ that satisfies rank($\lbrack{BAc}\rbrack$) = rank($B$) is any vector such that $\underset{¯}{c} = 0$. We also fix $\overline{c} = 0$. Consequently $d = 0$.

where ${x{(t)}} \in {\mathbb{R}}^{n}$, ${u{(t)}} \in \mathcal{U} \subseteq {\mathbb{R}}^{m}$ are the state and control input, and $A \in {\mathbb{R}}^{n \times n}$, $B \in {\mathbb{R}}^{n \times m}$. We assume that the system is stabilizable....
